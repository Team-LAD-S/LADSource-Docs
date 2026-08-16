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
function ENT:EnableLimbFlash(enable, AttachmentBone, radius, material, additive)
```

</div>

Serverside caller for the Aura effect around specific limbs. Used internally by many functions in `moveset.lua` but can also be used externally where required.

!!! warning "Warning"

    This function is not garbage collected. You must set `enable` to false in order to properly destroy it, otherwise it'll persist until entity deletion.

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `enable` | `bool` | Yes | Sets the effect active. This calls the clientside function of the same name that sets up a render hook with the invisible limbflash material. |
| `AttachmentBone` | `int` | Yes | The ID of the attachment you want to attach the controller (point_flesh_effect_target) to. Linked to the Var of the same name in `moveset.lua`. |
| `radius` | `float` | Yes | The radius of the controller. Linked to the Var of the same name in `moveset.lua`, parsed to string because we are dealing with a keyvalue. |
| `material` | `string` | Yes | The path to the material you want to use in place of the default one in a limbflash call. Linked to the Var of the same name in `moveset.lua`. |
| `additive` | `bool` | No | True by default. Set to false and the interior of the limbflash effect will be made pitch black. |

</div>

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/vfx.lua:170</code>.</p>
