# LADSource developer wiki

LADSource is a Garry's Mod addon for building fighters and combat inspired by
the Like a Dragon series. This wiki documents how to create a LADBot and how to
work with the systems exposed by `lad_framework_base`.

## Where to begin

<div class="grid cards" markdown>

-   **Getting started**

    ---

    Install the required addons and learn where LADSource content belongs.

    [Get started](guides/getting-started.md)

-   **Create a LADBot**

    ---

    Build a minimal fighter entity derived from `lad_framework_base`.

    [Create a LADBot](guides/creating-a-ladbot.md)

-   **Framework reference**

    ---

    Browse generated methods grouped by the Lua file that defines them.

    [Browse the API](reference/index.md)

-   **Document the API**

    ---

    Add descriptions, parameter types, realm information, and examples beside
    the source function.

    [Annotation format](guides/documenting-the-api.md)

</div>

!!! note "Reference pages are generated"

    Files under `docs/reference` are generated from the private LADSource source
    checkout and committed to this repository for publication. Edit the Lua
    documentation comments rather than generated Markdown.
