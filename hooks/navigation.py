"""Adjust generated navigation labels without changing stable page URLs."""

import json
from pathlib import Path

from mkdocs.structure.nav import Section


INITIALISMS = {
    "ai": "AI",
    "api": "API",
    "hact": "HACT",
    "hud": "HUD",
    "ladbot": "LADBot",
    "vfx": "VFX",
}

SECTION_TITLES = {
    "entity": "Entity extensions",
}


def on_nav(nav, config, files):
    method_order = load_method_order(config)
    for item in nav.items:
        format_navigation(item, method_order)
    return nav


def load_method_order(config):
    manifest_path = Path(config.docs_dir) / "reference" / "api-index.json"
    if not manifest_path.is_file():
        return {}

    records = json.loads(manifest_path.read_text(encoding="utf-8"))
    return {
        record["reference_path"].replace("\\", "/"): (
            bool(record["internal"]),
            record["name"].casefold(),
            int(record["source_line"]),
        )
        for record in records
        if record.get("reference_path")
    }


def source_path(item):
    file = getattr(item, "file", None)
    path = getattr(file, "src_uri", None) or getattr(file, "src_path", None)
    return str(path).replace("\\", "/") if path else ""


def format_navigation(item, method_order):
    if isinstance(item, Section):
        normalized = item.title.casefold()
        if normalized in SECTION_TITLES:
            item.title = SECTION_TITLES[normalized]
        else:
            item.title = " ".join(
                INITIALISMS.get(word.casefold(), word.title())
                for word in item.title.replace("_", " ").split()
            )

    children = getattr(item, "children", None) or []
    for child in children:
        format_navigation(child, method_order)

    method_pages = [child for child in children if source_path(child) in method_order]
    if not method_pages:
        return

    other_pages = [child for child in children if source_path(child) not in method_order]
    method_pages.sort(key=lambda child: method_order[source_path(child)])
    children[:] = other_pages + method_pages
