---
title: "ENT:ChargeAura"
status: realm-server
---

[Back to VFX](index.md)

<a id="ent-chargeaura"></a>
# `ENT:ChargeAura` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:ChargeAura(enable, SDRCleanupTime, SDRColor, SDRMaterial, destroyInstant)
```

</div>

Serverside caller for the Aura effect used when charging attacks.

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `enable` | `bool` | Yes | Sets the effect active. |
| `SDRCleanupTime` | `float` | Yes | The base amount of time before the SlowDownRate is forced to reset to 0. Linked to the Var of the same name in `moveset.lua`. |
| `SDRColor` | `color` | Yes | The actual color of the Charge Aura. Linked to the Var of the same name in `moveset.lua`. |
| `SDRMaterial` | `string` | Yes | The path to the material you want to use in place of the default one in a Charge Aura call. Linked to the Var of the same name in `moveset.lua`. |
| `destroyInstant` | `bool` | No | Immediately cut off the Charge Aura effect instead of doing a fade out. Not mapped to anything but can be called from the function if need be. |

</div>

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/vfx.lua:123</code>.</p>
