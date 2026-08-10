---
title: "ENT:OnRemove"
status: realm-server-client
---

[Back to Shared](index.md)

<a id="ent-onremove"></a>
# `ENT:OnRemove` { .api-method-title }

=== "Server"

    <div class="api-badges"><span class="api-badge api-badge--server">server</span><span class="api-badge api-badge--internal">internal</span></div>

    <div class="api-signature" markdown>

    ```lua
    function ENT:OnRemove()
    ```

    </div>

    Serverside clean up function. Called automatically by DrGBase, cleans up LADBot related stuff,
    use ENT:CustomOnRemove() to clean up any additional things you may need.

    ## Parameters { #server-parameters data-toc-label="Parameters" }

    This method takes no explicit arguments.

    ## Returns { #server-returns data-toc-label="Returns" }

    No return values are documented.

    <p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:1224</code>.</p>

=== "Client"

    <div class="api-badges"><span class="api-badge api-badge--client">client</span><span class="api-badge api-badge--internal">internal</span></div>

    <div class="api-signature" markdown>

    ```lua
    function ENT:OnRemove()
    ```

    </div>

    Clientside clean up function. Called automatically by DrGBase.

    ## Parameters { #client-parameters data-toc-label="Parameters" }

    This method takes no explicit arguments.

    ## Returns { #client-returns data-toc-label="Returns" }

    No return values are documented.

    <p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:1649</code>.</p>
