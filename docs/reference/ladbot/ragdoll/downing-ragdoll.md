---
title: "ENT:DowningRagdoll"
---

[Back to Ragdoll](index.md)

<a id="ent-downingragdoll"></a>
# `ENT:DowningRagdoll` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:DowningRagdoll(ragdoll_time)
```

</div>

Ragdoll triggered by a downing hit-reaction at a specific animation cycle.
The NPC is hidden behind a physics ragdoll for ragdoll_time seconds; it then
lerps its limbs toward the first frame of the appropriate get-up animation
and seamlessly transitions back to the NPC standing-up sequence.
Only active when lad_ragdollmode == 1.
Call this from inside your hit-reaction cycle callback — orientation flags
(DownedFront / DownedBack) must already be set by the time you call it.

## Parameters

| Name | Type | Description |
| --- | --- | --- |
| `ragdoll_time` | `any` | Not documented. |

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ragdoll.lua:292</code>.</p>
