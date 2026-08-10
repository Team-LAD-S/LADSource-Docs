---
title: "ENT:CustomThink"
status: realm-server-client
---

[Back to Shared](index.md)

<a id="ent-customthink-1641"></a>
# `ENT:CustomThink` { .api-method-title }

=== "Server"

    <div class="api-badges"><span class="api-badge api-badge--server">server</span><span class="api-badge api-badge--internal">internal</span></div>

    <div class="api-signature" markdown>

    ```lua
    function ENT:CustomThink()
    ```

    </div>

    Belongs to DrGBase, called every tick by the engine. Handles AI, HUD, and other internal logic.
    Use ENT:CustomFighterThink() to add custom logic for your fighter.

    ## Parameters { #server-parameters data-toc-label="Parameters" }

    This method takes no explicit arguments.

    ## Returns { #server-returns data-toc-label="Returns" }

    No return values are documented.

    <p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:856</code>.</p>

=== "Client"

    <div class="api-badges"><span class="api-badge api-badge--client">client</span></div>

    <div class="api-signature" markdown>

    ```lua
    function ENT:CustomThink()
    ```

    </div>

    Only calls self:_InitDebugText().
    Called internally only.

    ## Parameters { #client-parameters data-toc-label="Parameters" }

    This method takes no explicit arguments.

    ## Returns { #client-returns data-toc-label="Returns" }

    No return values are documented.

    <p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:1641</code>.</p>
