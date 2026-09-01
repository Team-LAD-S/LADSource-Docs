---
title: "ENT:CICO"
status: realm-server-client
---

[Back to Shared](index.md)

<a id="ent-cico"></a>
# `ENT:CICO` { .api-method-title }

=== "Server"

    <div class="api-badges"><span class="api-badge api-badge--server">server</span></div>

    <div class="api-signature" markdown>

    ```lua
    function ENT:CICO(callback)
    ```

    </div>

    Call In Coroutine Override (CICO), originally created by NextBot developer Roach.
    Temporarily replaces LADBot's normal behavior coroutine with a callback.
    The callback may use yielding helpers such as PlaySequenceAndWait, allowing code
    to run sequentially before and after animations or other waits. Normal behavior
    remains paused until the callback returns, after which the previous behavior
    coroutine is restored if another system has not already replaced it.

    !!! warning "Warning"

        If not properly terminated, CICO calls can stack on top of one another and resume execution in reverse order.

    ## Example { #server-example data-toc-label="Example" }

    ```lua
    self:CICO(function(self)
        self._isWaving = true
        self:PlaySequenceAndWait("waving_animation")
        self._isWaving = false
    end)
    ```

    ## Parameters { #server-parameters data-toc-label="Parameters" }

    <div class="api-parameter-table" markdown>

    | Name | Type | Required | Description |
    | --- | --- | :---: | --- |
    | `callback` | `function` | Yes | Code to run inside the temporary behavior coroutine. Receives this LADBot as its only argument. |

    </div>

    ## Returns { #server-returns data-toc-label="Returns" }

    No return values are documented.

    <p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:628</code>.</p>

=== "Client"

    <div class="api-badges"><span class="api-badge api-badge--client">client</span></div>

    <div class="api-signature" markdown>

    ```lua
    function ENT:CICO(callback)
    ```

    </div>

    Client-side counterpart to Call In Coroutine Override (CICO).
    Runs a callback inside a temporary client behavior coroutine and restores
    the previous behavior coroutine after the callback returns. Most addon code
    should use the server implementation; this version exists for clientside
    coroutine sequences.

    Not recommended to use, will probably be deprecated in the future.

    ## Parameters { #client-parameters data-toc-label="Parameters" }

    <div class="api-parameter-table" markdown>

    | Name | Type | Required | Description |
    | --- | --- | :---: | --- |
    | `callback` | `function` | Yes | Code to run inside the temporary client behavior coroutine. Receives this LADBot as its only argument. |

    </div>

    ## Returns { #client-returns data-toc-label="Returns" }

    No return values are documented.

    <p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:1569</code>.</p>
