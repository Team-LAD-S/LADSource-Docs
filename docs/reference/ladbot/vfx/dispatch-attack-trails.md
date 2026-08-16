---
title: "ENT:DispatchAttackTrails"
status: realm-server
---

[Back to VFX](index.md)

<a id="ent-dispatchattacktrails"></a>
# `ENT:DispatchAttackTrails` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:DispatchAttackTrails(p, moveName, animSeq)
```

</div>

Serverside tracker that dispatches active MeshTrails to their intended entities and bones.

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `p` | `table` | Yes | The MeshTrail that is to be constructed. This uses the same table referenced by VFX_MeshTrail, however this function retrieves it from the current attack's properties in `moveset.lua`. |
| `moveName` | `string` | Yes | The name of the current move that this AttackTrail/MeshTrail is to be dispatched to. |
| `animSeq` | `string` | Yes | The ID of the animation sequence that is playing right now, used to retrieve the cycle when the AttackTrail should be instanced. |

</div>

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/vfx.lua:452</code>.</p>
