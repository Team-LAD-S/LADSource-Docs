"""Generate LADSource API references from the private framework source."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass, field
from pathlib import Path
from urllib.parse import quote


INCLUDE_RE = re.compile(r'DrGBase\.IncludeFile\(["\']([^"\']+\.lua)["\']\)')
DOC_LINE_RE = re.compile(r"^\s*---(?!-)(.*)$")
COMMENT_LINE_RE = re.compile(r"^\s*--(?!-|\[\[)(.*)$")
TAG_RE = re.compile(r"^@(?P<name>[A-Za-z_]\w*)(?:\s+(?P<value>.*))?$")
PARAM_RE = re.compile(r"^(?P<name>[A-Za-z_]\w*|\.\.\.)\s+(?P<type>\S+)(?:\s+(?P<description>.*))?$")
FIELD_RE = re.compile(
    r"^(?P<parameter>[A-Za-z_]\w*)\."
    r"(?P<name>[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*)(?P<optional>\?)?\s+"
    r"(?P<type>\S+)(?:\s+(?P<description>.*))?$"
)
RETURN_RE = re.compile(r"^(?P<type>\S+)(?:\s+(?P<description>.*))?$")


@dataclass
class TableField:
    name: str
    type: str = "any"
    description: str = ""
    optional: bool = False


@dataclass
class Parameter:
    name: str
    type: str = "any"
    description: str = ""
    fields: list[TableField] = field(default_factory=list)


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
    page_slug: str = ""
    navigation_title: str = ""


def module_title(path: Path) -> str:
    initialisms = {"ai": "AI", "hact": "HACT", "hud": "HUD", "vfx": "VFX"}
    words = path.stem.replace("_", " ").replace("-", " ").split()
    return " ".join(initialisms.get(word.lower(), word.title()) for word in words)


def markdown_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()


def split_arguments(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def read_lua_source(path: Path) -> str:
    data = path.read_bytes()
    try:
        return data.decode("utf-8-sig")
    except UnicodeDecodeError:
        return data.decode("cp1252")


def extract_doc_block(lines: list[str], method_index: int) -> list[str]:
    block: list[str] = []
    index = method_index - 1
    while index >= 0:
        match = DOC_LINE_RE.match(lines[index]) or COMMENT_LINE_RE.match(lines[index])
        if not match:
            break
        block.append(match.group(1).lstrip())
        index -= 1
    block.reverse()
    return block


def parse_documentation(method: Method, doc_lines: list[str]) -> None:
    descriptions: list[str] = []
    documented_parameters: dict[str, Parameter] = {}
    documented_fields: dict[str, list[TableField]] = defaultdict(list)

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
        elif tag == "field" and (match := FIELD_RE.match(value)):
            documented_fields[match.group("parameter")].append(
                TableField(
                    match.group("name"),
                    match.group("type"),
                    match.group("description") or "",
                    bool(match.group("optional")),
                )
            )
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
    method.parameters = []
    for argument in method.arguments:
        parameter = documented_parameters.get(argument, Parameter(argument))
        parameter.fields.extend(documented_fields.get(argument, []))
        method.parameters.append(parameter)


def method_patterns(receiver: str) -> tuple[re.Pattern[str], re.Pattern[str]]:
    escaped = re.escape(receiver)
    direct = re.compile(
        rf"^\s*function\s+{escaped}(?P<separator>[:.])"
        rf"(?P<name>[A-Za-z_]\w*)\s*\((?P<arguments>[^)]*)\)"
    )
    assigned = re.compile(
        rf"^\s*{escaped}\.(?P<name>[A-Za-z_]\w*)\s*=\s*function\s*"
        rf"\((?P<arguments>[^)]*)\)"
    )
    return direct, assigned


def parse_methods(
    path: Path,
    repository_root: Path,
    receiver: str = "ENT",
    display_receiver: str | None = None,
    default_realm: str = "not documented",
) -> list[Method]:
    lines = read_lua_source(path).splitlines()
    direct_pattern, assigned_pattern = method_patterns(receiver)
    display_receiver = display_receiver or receiver
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

        match = direct_pattern.match(line)
        separator = match.group("separator") if match else "."
        if not match:
            match = assigned_pattern.match(line)
        if not match:
            continue

        name = match.group("name")
        raw_arguments = match.group("arguments").strip()
        display_name = f"{display_receiver}{separator}{name}"
        method = Method(
            name=name,
            display_name=display_name,
            signature=f"function {display_name}({raw_arguments})",
            arguments=split_arguments(raw_arguments),
            source_file=path.relative_to(repository_root).as_posix(),
            source_line=index + 1,
            realm=default_realm,
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
    badges = [method.realm]
    if method.callback:
        badges.append("callback")
    if method.internal:
        badges.append("internal")
    if method.deprecated:
        badges.append("deprecated")

    content = "".join(
        f'<span class="api-badge api-badge--{badge_slug(label)}">{label}</span>'
        for label in badges
    )
    return f'<div class="api-badges">{content}</div>'


def badge_slug(label: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", label.casefold()).strip("-") or "unknown"


def method_sort_key(method: Method) -> tuple[bool, str, int]:
    return method.internal, method.name.casefold(), method.source_line


def method_page_slug(name: str) -> str:
    separated = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1-\2", name)
    separated = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "-", separated)
    return re.sub(r"[^a-z0-9]+", "-", separated.casefold()).strip("-") or "method"


def assign_method_pages(methods: list[Method]) -> None:
    base_slugs = [method_page_slug(method.name) for method in methods]
    duplicate_slugs = Counter(base_slugs)
    for method, base_slug in zip(methods, base_slugs):
        duplicate = duplicate_slugs[base_slug] > 1
        method.page_slug = f"{base_slug}-{method.source_line}" if duplicate else base_slug
        method.navigation_title = (
            f"{method.display_name} (line {method.source_line})"
            if duplicate
            else method.display_name
        )


def render_method(method: Method, repository_url: str, branch: str) -> list[str]:
    output = [
        f'<a id="{method.anchor}"></a>',
        f"# `{method.display_name}` {{ .api-method-title }}",
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

    output.extend(["## Parameters", ""])
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

    for parameter in method.parameters:
        if not parameter.fields:
            continue
        output.extend(
            [
                f"### `{parameter.name}` table fields",
                "",
                "| Key | Type | Required | Description |",
                "| --- | --- | :---: | --- |",
            ]
        )
        for table_field in parameter.fields:
            output.append(
                f"| `{markdown_cell(table_field.name)}` | "
                f"`{markdown_cell(table_field.type)}` | "
                f"{'No' if table_field.optional else 'Yes'} | "
                f"{markdown_cell(table_field.description) or 'Not documented.'} |"
            )
        output.append("")

    output.extend(["## Returns", ""])
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


def render_method_page(
    method: Method,
    module_name: str,
    repository_url: str,
    branch: str,
) -> str:
    output = [
        "---",
        f"title: {json.dumps(method.navigation_title, ensure_ascii=False)}",
        "---",
        "",
        f"[Back to {module_name}](index.md)",
        "",
    ]
    output.extend(render_method(method, repository_url, branch))
    return "\n".join(output)


def render_module_index(
    path: Path,
    methods: list[Method],
    repository_url: str,
    branch: str,
    title: str | None = None,
    introduction: str | None = None,
) -> str:
    relative_path = (
        methods[0].source_file
        if methods
        else f"lua/entities/lad_framework_base/{path.name}"
    )
    output = [
        f"# {title or module_title(path)}",
        "",
    ]
    if introduction:
        output.extend([introduction, ""])
    output.extend(
        [
        f"Methods defined in `{relative_path}`.",
        "",
        ]
    )
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
        return "\n".join(output + ["No matching API methods were detected in this file.", ""])

    output.extend(
        [
            "## Methods",
            "",
            '<div class="api-method-list" markdown>',
            "",
            "| Method | Summary |",
            "| --- | --- |",
        ]
    )
    for method in methods:
        summary = markdown_cell(method.description) or "Documentation pending."
        output.append(
            f"| [`{method.display_name}`]({method.page_slug}.md) | {summary} |"
        )
    output.extend(["", "</div>", ""])
    return "\n".join(output)


def write_method_section(
    output_directory: Path,
    source_path: Path,
    methods: list[Method],
    repository_url: str,
    branch: str,
    title: str | None = None,
    introduction: str | None = None,
) -> None:
    output_directory.mkdir(parents=True, exist_ok=True)
    assign_method_pages(methods)
    section_title = title or module_title(source_path)
    (output_directory / "index.md").write_text(
        render_module_index(
            source_path,
            methods,
            repository_url,
            branch,
            title=section_title,
            introduction=introduction,
        ),
        encoding="utf-8",
        newline="\n",
    )
    for method in methods:
        (output_directory / f"{method.page_slug}.md").write_text(
            render_method_page(method, section_title, repository_url, branch),
            encoding="utf-8",
            newline="\n",
        )


def ordered_source_files(source_directory: Path) -> list[Path]:
    shared = source_directory / "shared.lua"
    ordered_names = ["shared.lua"]
    if shared.exists():
        text = read_lua_source(shared)
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
    ladbot_source_directory = source_root / "lua" / "entities" / "lad_framework_base"
    entity_source = source_root / "lua" / "lad_framework" / "meta.lua"
    battle_manager_source = (
        source_root / "lua" / "lad_framework" / "battle_manager.lua"
    )
    docs_directory = (docs_root / "docs").resolve()
    output_directory = (docs_directory / "reference").resolve()
    if output_directory.parent != docs_directory:
        raise RuntimeError(f"Refusing to replace unexpected directory: {output_directory}")
    required_sources = [
        ladbot_source_directory,
        entity_source,
        battle_manager_source,
    ]
    for required_source in required_sources:
        if not required_source.exists():
            raise FileNotFoundError(f"Framework source not found: {required_source}")
    if output_directory.exists():
        shutil.rmtree(output_directory)
    output_directory.mkdir(parents=True)
    ladbot_output_directory = output_directory / "ladbot"
    ladbot_output_directory.mkdir()

    manifest: list[dict[str, object]] = []
    ladbot_modules: list[tuple[Path, list[Method]]] = []
    for path in ordered_source_files(ladbot_source_directory):
        methods = parse_methods(path, source_root)
        methods.sort(key=method_sort_key)
        ladbot_modules.append((path, methods))
        write_method_section(
            ladbot_output_directory / path.stem,
            path,
            methods,
            repository_url,
            branch,
        )
        for method in methods:
            record = asdict(method)
            record["api_group"] = "ladbot"
            record["reference_path"] = (
                f"reference/ladbot/{path.stem}/{method.page_slug}.md"
            )
            manifest.append(record)

    entity_methods = parse_methods(
        entity_source,
        source_root,
        receiver="ladMeta",
        display_receiver="Entity",
        default_realm="shared",
    )
    entity_methods.sort(key=method_sort_key)
    write_method_section(
        output_directory / "entity",
        entity_source,
        entity_methods,
        repository_url,
        branch,
        title="Entity extensions",
        introduction=(
            "These methods extend Garry's Mod's `Entity` metatable, so they can be "
            "called on any entity and are not limited to LADBots."
        ),
    )
    for method in entity_methods:
        record = asdict(method)
        record["api_group"] = "entity"
        record["reference_path"] = f"reference/entity/{method.page_slug}.md"
        manifest.append(record)

    battle_manager_methods = parse_methods(
        battle_manager_source,
        source_root,
        receiver="BM",
        display_receiver="BattleManager",
        default_realm="server",
    )
    battle_manager_methods.sort(key=method_sort_key)
    write_method_section(
        output_directory / "battle_manager",
        battle_manager_source,
        battle_manager_methods,
        repository_url,
        branch,
        title="Battle Manager",
        introduction=(
            "Server-side battle lifecycle methods exposed through "
            "`LADSource.BattleManager`."
        ),
    )
    for method in battle_manager_methods:
        record = asdict(method)
        record["api_group"] = "battle_manager"
        record["reference_path"] = (
            f"reference/battle_manager/{method.page_slug}.md"
        )
        manifest.append(record)

    ladbot_count = sum(len(methods) for _, methods in ladbot_modules)
    ladbot_index = [
        "# LADBot modules",
        "",
        "Methods inherited from `lad_framework_base`, grouped by the Lua module",
        "that defines them.",
        "",
        f"**{ladbot_count} methods** were detected across "
        f"**{len(ladbot_modules)} modules**.",
        "",
        '<div class="api-module-list" markdown>',
        "",
        "| Module | Methods | Source file |",
        "| --- | ---: | --- |",
    ]
    sorted_ladbot_modules = sorted(
        ladbot_modules, key=lambda item: module_title(item[0]).casefold()
    )
    for path, methods in sorted_ladbot_modules:
        relative = path.relative_to(source_root).as_posix()
        ladbot_index.append(
            f"| [{module_title(path)}]({path.stem}/index.md) | {len(methods)} | `{relative}` |"
        )
    ladbot_index.extend(["", "</div>", ""])
    (ladbot_output_directory / "index.md").write_text(
        "\n".join(ladbot_index), encoding="utf-8", newline="\n"
    )

    documented_count = sum(bool(item["description"]) for item in manifest)
    source_file_count = len(ladbot_modules) + 2
    index = [
        "# API reference",
        "",
        "The reference covers LADBot methods, shared Entity extensions, and the",
        "server-side Battle Manager API.",
        "",
        f"**{len(manifest)} methods** were detected across **{source_file_count} files**.",
        f"**{documented_count} methods** currently have descriptions.",
        "",
        "| API group | Methods | Description |",
        "| --- | ---: | --- |",
        f"| [LADBot modules](ladbot/index.md) | {ladbot_count} | Methods inherited from `lad_framework_base`. |",
        f"| [Entity extensions](entity/index.md) | {len(entity_methods)} | Shared helpers available on all entities. |",
        f"| [Battle Manager](battle_manager/index.md) | {len(battle_manager_methods)} | Server-side battle lifecycle management. |",
    ]
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
    return source_file_count, len(manifest)


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
    print(f"Generated {methods} methods from {modules} source files.")


if __name__ == "__main__":
    main()
