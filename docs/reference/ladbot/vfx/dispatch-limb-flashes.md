---
title: "ENT:DispatchLimbFlashes"
status: realm-server
---

[Back to VFX](index.md)

<a id="ent-dispatchlimbflashes"></a>
# `ENT:DispatchLimbFlashes` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:DispatchLimbFlashes(move, moveName, animSeq)
```

</div>

Serverside tracker that dispatches active LimbFlashes to their intended entities and bones.

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `move` | `table` | Yes | The current move that is being played inside a Node. The function uses this to assert the properties of the LimbFlash. |
| `moveName` | `string` | Yes | The name of the current move that this LimbFlash is to be dispatched to. |
| `animSeq` | `int` | Yes | ID of the animation sequence that this LimbFlash is tied to. Used to assert its start and end cycles. |

</div>

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/vfx.lua:628</code>.</p>
