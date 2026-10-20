---
title: "ENT:EnableLimbFlash"
status: realm-server
---

[Back to VFX](index.md)

<a id="ent-enablelimbflash"></a>
# `ENT:EnableLimbFlash` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span></div>

<div class="api-signature" markdown>

```lua
function ENT:EnableLimbFlash(enable, AttachmentBone, radius, material, additive, colorBlend)
```

</div>

Serverside caller for the LimbFlash effect around a specific bone. Used internally by moveset properties and can also be called externally.

!!! warning "Warning"

    This function is not garbage collected. You must set `enable` to false in order to properly destroy it, otherwise it'll persist until entity deletion.

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `enable` | `bool` | Yes | Enables or updates the sphere for the bone. Set to `false` to free its sphere slot. |
| `AttachmentBone` | `string`/`int` | Yes | The bone name or ID to center the sphere on. |
| `radius` | `float` | Yes | The sphere radius in model units. |
| `material` | `string` | Yes | The path to the material you want to use in place of the default one in a limbflash call. Linked to the Var of the same name in `moveset.lua`. |
| `additive` | `bool` | No | True by default. Set to false and the interior of the limbflash effect will be made pitch black. |
| `colorBlend` | `number` | No | Blend from black to the material's `$LFColor`, from `0` to `1`. Defaults to `1`. |

</div>

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/vfx.lua:183</code>.</p>
