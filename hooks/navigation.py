"""Adjust generated navigation labels without changing stable page URLs."""

from mkdocs.structure.nav import Section


def on_nav(nav, config, files):
    for item in nav.items:
        rename_ladbot_section(item)
    return nav


def rename_ladbot_section(item):
    if isinstance(item, Section) and item.title.casefold() == "ladbot":
        item.title = "LADBot"

    for child in getattr(item, "children", None) or []:
        rename_ladbot_section(child)
