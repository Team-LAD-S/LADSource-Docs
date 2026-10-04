---
title: "ENT:HactAttackVortex"
status: realm-server
---

[Back to VFX](index.md)

<a id="ent-hactattackvortex"></a>
# `ENT:HactAttackVortex` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span></div>

<div class="api-signature" markdown>

```lua
function ENT:HactAttackVortex(enable, boneName, ang, pos, destroyInstant)
```

</div>

Serverside caller for the HactAttackVortex effect, creates "flowdust" around the specified limb.

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `enable` | `bool` | Yes | Enables or disables the vortex effect |
| `boneName` | `string` | Yes | The bone to attach the effect to |
| `ang` | `Angle` | Yes | The local angle offset for the particle container |
| `pos` | `Vector` | Yes | The local position offset for the particle container |
| `destroyInstant` | `bool` | Yes | Immediately kills the particles and prevents them from lingering. |

</div>

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/vfx.lua:765</code>.</p>
