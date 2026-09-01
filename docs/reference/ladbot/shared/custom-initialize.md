---
title: "ENT:CustomInitialize"
status: realm-server-client
---

[Back to Shared](index.md)

<a id="ent-custominitialize"></a>
# `ENT:CustomInitialize` { .api-method-title }

=== "Server"

    <div class="api-badges"><span class="api-badge api-badge--server">server</span><span class="api-badge api-badge--internal">internal</span></div>

    <div class="api-signature" markdown>

    ```lua
    function ENT:CustomInitialize()
    ```

    </div>

    Sets up the LADBot. Use ENT:CustomFighterInitialize() to set up custom variables and other stuff for your fighter.

    ## Parameters { #server-parameters data-toc-label="Parameters" }

    This method takes no explicit arguments.

    ## Returns { #server-returns data-toc-label="Returns" }

    No return values are documented.

    <p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:245</code>.</p>

=== "Client"

    <div class="api-badges"><span class="api-badge api-badge--client">client</span><span class="api-badge api-badge--internal">internal</span></div>

    <div class="api-signature" markdown>

    ```lua
    function ENT:CustomInitialize()
    ```

    </div>

    Initializes the LADBot colors.
    Called internally only.

    ## Parameters { #client-parameters data-toc-label="Parameters" }

    This method takes no explicit arguments.

    ## Returns { #client-returns data-toc-label="Returns" }

    No return values are documented.

    <p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:1629</code>.</p>
