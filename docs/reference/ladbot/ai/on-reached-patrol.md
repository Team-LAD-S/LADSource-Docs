---
title: "ENT:OnReachedPatrol"
status: realm-server
---

[Back to AI](index.md)

<a id="ent-onreachedpatrol"></a>
# `ENT:OnReachedPatrol` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span></div>

<div class="api-signature" markdown>

```lua
function ENT:OnReachedPatrol(pos)
```

</div>

Belongs to DrGBase, called after the LADBot successfully reaches its current patrol destination. (inside the coroutine).
Can be overriden to implement custom behavior.
By default currently waits for 1 second before setting self._patrolling to false.

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `pos` | `Vector` | Yes | The destination returned by the active patrol task and used for pathfinding. This is the intended patrol destination, not necessarily the LADBot's exact current position. |

</div>

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:1679</code>.</p>
