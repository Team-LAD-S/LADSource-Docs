---
title: "ENT:SetGreyscaleEffect"
status: realm-server
---

[Back to VFX](index.md)

<a id="ent-setgreyscaleeffect"></a>
# `ENT:SetGreyscaleEffect` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span></div>

<div class="api-signature" markdown>

```lua
function ENT:SetGreyscaleEffect(enable)
```

</div>

Serverside caller that makes everything, excluding the Player's current fighter, black and white.

!!! warning "Warning"

    This function has no safeguards that disable it automatically. You must, under all circumstances, make a call that disables the greyscale effect after you're done using it. Otherwise, everything will stay black and white unless you dispossess the fighter or remove it.

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `enable` | `bool` | Yes | Trigger this effect. Setting it to false disables it. |

</div>

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/vfx.lua:749</code>.</p>
