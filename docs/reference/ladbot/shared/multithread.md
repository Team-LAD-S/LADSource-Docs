---
title: "ENT:Multithread"
status: realm-server
---

[Back to Shared](index.md)

<a id="ent-multithread"></a>
# `ENT:Multithread` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span></div>

<div class="api-signature" markdown>

```lua
function ENT:Multithread(funcs)
```

</div>

Cooperatively runs multiple callbacks as child coroutines and waits for all of them to finish.
Each suspended callback is resumed once per update, allowing callbacks which yield to make progress
alongside one another. This is not true parallel execution: a callback which never yields runs to
completion before the next callback is resumed. Call this from a yieldable coroutine, such as a CICO
callback. Return values are discarded, and errors raised by callbacks are not propagated by the current
implementation.

## Example

```lua
self:CICO(function(self)
    self:Multithread({
        function()
            self:PlaySequenceAndWait("animation_a")
        end,
        function()
            self:Wait(0.5)
            self:EmitSound("buttons/button15.wav")
        end,
    })

    -- Both callbacks have finished here.
end)
```

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `funcs` | `function[]` | Yes | An array of zero-argument callbacks to run cooperatively. |

</div>

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:823</code>.</p>
