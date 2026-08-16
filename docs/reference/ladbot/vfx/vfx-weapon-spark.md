---
title: "ENT:VFX_WeaponSpark"
status: realm-server
---

[Back to VFX](index.md)

<a id="ent-vfx-weaponspark"></a>
# `ENT:VFX_WeaponSpark` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:VFX_WeaponSpark(slot)
```

</div>

Same as `VFX_SparkOnce`, but this confines it to a weapon slot.

!!! warning "Warning"

    Will fail silently if there's no active weapon in the slot.

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `slot` | `any` | Yes | Not documented. |

</div>

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/vfx.lua:270</code>.</p>
