"""Generate the LADBot API reference from lad_framework_base."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from dataclasses import asdict, dataclass, field
from pathlib import Path
from urllib.parse import quote


METHOD_RE = re.compile(
    r"^\s*function\s+ENT(?P<separator>[:.])(?P<name>[A-Za-z_]\w*)"
    r"\s*\((?P<arguments>[^)]*)\)"
)
ASSIGNED_METHOD_RE = re.compile(
    r"^\s*ENT\.(?P<name>[A-Za-z_]\w*)\s*=\s*function\s*"
    r"\((?P<arguments>[^)]*)\)"
)
INCLUDE_RE = re.compile(r'DrGBase\.IncludeFile\(["\']([^"\']+\.lua)["\']\)')
DOC_LINE_RE = re.compile(r"^\s*---(?!-)(.*)$")
TAG_RE = re.compile(r"^@(?P<name>[A-Za-z_]\w*)(?:\s+(?P<value>.*))?$")
PARAM_RE = re.compile(r"^(?P<name>[A-Za-z_]\w*|\.\.\.)\s+(?P<type>\S+)(?:\s+(?P<description>.*))?$")
RETURN_RE = re.compile(r"^(?P<type>\S+)(?:\s+(?P<description>.*))?$")


@dataclass
class Parameter:
    name: str
    type: str = "any"
    description: str = ""


@dataclass
class ReturnValue:
    type: str
    description: str = ""


@dataclass
class Method:
    name: str
    display_name: str
    signature: str
    arguments: list[str]
    source_file: str
    source_line: int
    description: str = ""
    realm: str = "not documented"
    parameters: list[Parameter] = field(default_factory=list)
    returns: list[ReturnValue] = field(default_factory=list)
    internal: bool = False
    callback: bool = False
    deprecated: str = ""
    anchor: str = ""


def module_title(path: Path) -> str:
    initialisms = {"ai": "AI", "hact": "HACT", "hud": "HUD", "vfx": "VFX"}
    words = path.stem.replace("_", " ").replace("-", " ").split()
    return " ".join(initialisms.get(word.lower(), word.title()) for word in words)


def markdown_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()


def split_arguments(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def extract_doc_block(lines: list[str], method_index: int) -> list[str]:
    block: list[str] = []
    index = method_index - 1
    while index >= 0:
        match = DOC_LINE_RE.match(lines[index])
        if not match:
            break
        block.append(match.group(1).lstrip())
        index -= 1
    block.reverse()
    return block


def parse_documentation(method: Method, doc_lines: list[str]) -> None:
    descriptions: list[str] = []
    documented_parameters: dict[str, Parameter] = {}

    for line in doc_lines:
        tag_match = TAG_RE.match(line)
        if not tag_match:
            descriptions.append(line)
            continue
        tag = tag_match.group("name").lower()
        value = (tag_match.group("value") or "").strip()
        if tag == "realm" and value:
            method.realm = value.lower()
        elif tag == "param" and (match := PARAM_RE.match(value)):
            parameter = Parameter(
                match.group("name"),
                match.group("type"),
                match.group("description") or "",
            )
            documented_parameters[parameter.name] = parameter
        elif tag == "return" and (match := RETURN_RE.match(value)):
            method.returns.append(
                ReturnValue(match.group("type"), match.group("description") or "")
            )
        elif tag == "internal":
            method.internal = True
        elif tag == "callback":
            method.callback = True
        elif tag == "deprecated":
            method.deprecated = value or "This method is deprecated."

    method.description = "\n".join(descriptions).strip()
    method.parameters = [
        documented_parameters.get(argument, Parameter(argument))
        for argument in method.arguments
    ]


def parse_methods(path: Path, repository_root: Path) -> list[Method]:
    lines = path.read_text(encoding="utf-8-sig", errors="replace").splitlines()
    methods: list[Method] = []
    used_anchors: set[str] = set()
    in_c_block_comment = False
    in_lua_block_comment = False
    for index, line in enumerate(lines):
        stripped = line.lstrip()
        if in_c_block_comment:
            if "*/" in line:
                in_c_block_comment = False
            continue
        if in_lua_block_comment:
            if "]]" in line:
                in_lua_block_comment = False
            continue
        if stripped.startswith("/*"):
            in_c_block_comment = "*/" not in stripped[2:]
            continue
        if stripped.startswith("--[["):
            in_lua_block_comment = "]]" not in stripped[4:]
            continue

        match = METHOD_RE.match(line)
        separator = match.group("separator") if match else "."
        if not match:
            match = ASSIGNED_METHOD_RE.match(line)
        if not match:
            continue

        name = match.group("name")
        raw_arguments = match.group("arguments").strip()
        display_name = f"ENT{separator}{name}"
        method = Method(
            name=name,
            display_name=display_name,
            signature=f"function {display_name}({raw_arguments})",
            arguments=split_arguments(raw_arguments),
            source_file=path.relative_to(repository_root).as_posix(),
            source_line=index + 1,
            internal=name.startswith("_"),
        )
        parse_documentation(method, extract_doc_block(lines, index))
        if not method.description:
            inline = re.search(r"(?:--|//)\s*(.+)$", line[match.end():])
            method.description = inline.group(1).strip() if inline else ""
        base_anchor = re.sub(r"[^a-z0-9]+", "-", display_name.lower()).strip("-")
        method.anchor = (
            f"{base_anchor}-{method.source_line}" if base_anchor in used_anchors else base_anchor
        )
        used_anchors.add(method.anchor)
        methods.append(method)
    return methods


def source_url(repository_url: str, branch: str, method: Method) -> str | None:
    if not repository_url:
        return None
    source_path = quote(method.source_file, safe="/")
    return f"{repository_url}/blob/{quote(branch, safe='')}/{source_path}#L{method.source_line}"


def render_badges(method: Method) -> str:
    badges = [(method.realm, "")]
    if method.callback:
        badges.append(("callback", ""))
    if method.internal:
        badges.append(("internal", "api-badge--internal"))
    if method.deprecated:
        badges.append(("deprecated", "api-badge--deprecated"))
    content = "".join(
        f'<span class="api-badge {css_class}">{label}</span>'
        for label, css_class in badges
    )
    return f'<div class="api-badges">{content}</div>'


def render_method(method: Method, repository_url: str, branch: str) -> list[str]:
    output = [
        f'<a id="{method.anchor}"></a>',
        f"## `{method.display_name}`",
        "",
        render_badges(method),
        "",
        '<div class="api-signature" markdown>',
        "",
        "```lua",
        method.signature,
        "```",
        "",
        "</div>",
        "",
        method.description
        or "*Documentation pending. The signature and source location were generated automatically.*",
        "",
    ]
    if method.deprecated:
        output.extend(["!!! warning \"Deprecated\"", "", f"    {method.deprecated}", ""])

    output.extend(["### Parameters", ""])
    if method.parameters:
        output.extend(["| Name | Type | Description |", "| --- | --- | --- |"])
        for parameter in method.parameters:
            output.append(
                f"| `{markdown_cell(parameter.name)}` | `{markdown_cell(parameter.type)}` | "
                f"{markdown_cell(parameter.description) or 'Not documented.'} |"
            )
        output.append("")
    else:
        output.extend(["This method takes no explicit arguments.", ""])

    output.extend(["### Returns", ""])
    if method.returns:
        output.extend(["| Type | Description |", "| --- | --- |"])
        for return_value in method.returns:
            output.append(
                f"| `{markdown_cell(return_value.type)}` | "
                f"{markdown_cell(return_value.description) or 'Not documented.'} |"
            )
        output.append("")
    else:
        output.extend(["No return values are documented.", ""])

    link = source_url(repository_url, branch, method)
    location = f"{method.source_file}:{method.source_line}"
    if link:
        source = f'<a href="{link}"><code>{location}</code></a>'
    else:
        source = f"<code>{location}</code>"
    output.extend([f'<p class="api-source">Defined in {source}.</p>', ""])
    return output


def render_module(
    path: Path, methods: list[Method], repository_url: str, branch: str
) -> str:
    relative_path = (
        methods[0].source_file
        if methods
        else f"lua/entities/lad_framework_base/{path.name}"
    )
    output = [
        f"# {module_title(path)}",
        "",
        f"Methods defined in `{relative_path}`.",
        "",
    ]
    if repository_url:
        encoded_path = quote(relative_path, safe="/")
        encoded_branch = quote(branch, safe="")
        view_url = f"{repository_url}/blob/{encoded_branch}/{encoded_path}"
        edit_url = f"{repository_url}/edit/{encoded_branch}/{encoded_path}"
        history_url = f"{repository_url}/commits/{encoded_branch}/{encoded_path}"
        output.extend(
            [
                f"[View source]({view_url}) &middot; "
                f"[Edit API comments]({edit_url}) &middot; [History]({history_url})",
                "",
            ]
        )
    output.extend(
        [
            "!!! info \"Generated reference\"",
            "",
            "    This page is generated from the current Lua source. Add API annotations",
            "    above a method in the source file to improve its documentation.",
            "",
        ]
    )
    if not methods:
        return "\n".join(output + ["No `ENT` methods were detected in this file.", ""])

    output.extend(["## Methods", "", "| Method | Summary |", "| --- | --- |"])
    for method in methods:
        summary = markdown_cell(method.description) or "Documentation pending."
        output.append(f"| [`{method.display_name}`](#{method.anchor}) | {summary} |")
    output.append("")
    for method in methods:
        output.extend(render_method(method, repository_url, branch))
    return "\n".join(output)


def ordered_source_files(source_directory: Path) -> list[Path]:
    shared = source_directory / "shared.lua"
    ordered_names = ["shared.lua"]
    if shared.exists():
        text = shared.read_text(encoding="utf-8-sig", errors="replace")
        ordered_names.extend(INCLUDE_RE.findall(text))

    files: list[Path] = []
    seen: set[str] = set()
    for name in ordered_names:
        path = source_directory / name
        if path.exists() and name.lower() not in seen:
            files.append(path)
            seen.add(name.lower())
    for path in sorted(source_directory.glob("*.lua")):
        if path.name.lower() not in seen:
            files.append(path)
            seen.add(path.name.lower())
    return files


def generate(
    source_root: Path,
    docs_root: Path,
    repository_url: str,
    branch: str,
) -> tuple[int, int]:
    source_directory = source_root / "lua" / "entities" / "lad_framework_base"
    docs_directory = (docs_root / "docs").resolve()
    output_directory = (docs_directory / "reference").resolve()
    if output_directory.parent != docs_directory:
        raise RuntimeError(f"Refusing to replace unexpected directory: {output_directory}")
    if not source_directory.is_dir():
        raise FileNotFoundError(f"Framework source not found: {source_directory}")
    if output_directory.exists():
        shutil.rmtree(output_directory)
    output_directory.mkdir(parents=True)

    manifest: list[dict[str, object]] = []
    modules: list[tuple[Path, list[Method]]] = []
    for path in ordered_source_files(source_directory):
        methods = parse_methods(path, source_root)
        methods.sort(key=lambda method: (method.name.casefold(), method.source_line))
        modules.append((path, methods))
        manifest.extend(asdict(method) for method in methods)
        (output_directory / f"{path.stem}.md").write_text(
            render_module(path, methods, repository_url, branch),
            encoding="utf-8",
            newline="\n",
        )

    documented_count = sum(bool(item["description"]) for item in manifest)
    index = [
        "# Framework reference",
        "",
        "This reference is generated from `lua/entities/lad_framework_base` and",
        "grouped by the Lua file that defines each method.",
        "",
        f"**{len(manifest)} methods** were detected across **{len(modules)} files**.",
        f"**{documented_count} methods** currently have descriptions.",
        "",
        "| Module | Methods | Source file |",
        "| --- | ---: | --- |",
    ]
    for path, methods in modules:
        relative = path.relative_to(source_root).as_posix()
        index.append(
            f"| [{module_title(path)}]({path.stem}.md) | {len(methods)} | `{relative}` |"
        )
    index.extend(
        [
            "",
            "!!! tip \"Improve a reference entry\"",
            "",
            "    Add a structured documentation comment immediately above the method in",
            "    its Lua source file. See [Documenting the API](../guides/documenting-the-api.md).",
            "",
        ]
    )
    (output_directory / "index.md").write_text(
        "\n".join(index), encoding="utf-8", newline="\n"
    )
    (output_directory / "api-index.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    return len(modules), len(manifest)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source-root",
        type=Path,
        help="LADSource checkout to scan. Defaults to the sibling ../LADSource directory.",
    )
    parser.add_argument(
        "--source-repository-url",
        "--repository-url",
        default="",
        help="Optional public source repository URL used for source links.",
    )
    parser.add_argument("--branch", default="main")
    arguments = parser.parse_args()
    docs_root = Path(__file__).resolve().parents[2]
    source_root = (arguments.source_root or docs_root.parent / "LADSource").resolve()
    modules, methods = generate(
        source_root,
        docs_root,
        arguments.source_repository_url.rstrip("/"),
        arguments.branch,
    )
    print(f"Generated {methods} methods from {modules} framework files.")


if __name__ == "__main__":
    main()
