---
title: "ENT:HeatAura"
status: realm-server
---

[Back to VFX](index.md)

<a id="ent-heataura"></a>
# `ENT:HeatAura` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:HeatAura(enable, color, destroyInstant)
```

</div>

Serverside caller for the HeatAura system. Relies on the provided moveset in order to create a particle instance of the heat aura.

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `enable` | `bool` | Yes | Trigger this effect. Setting it to false disables it. |
| `color` | `Color(R,G,B)` | Yes | The color of the heat aura. If the heat aura particle has a controlpoint remapped for coloring, this will apply to it to the particle as well. |
| `destroyInstant` | `bool` | Yes | Immediately delete the heat aura particles without letting them linger. |

</div>

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/vfx.lua:763</code>.</p>
