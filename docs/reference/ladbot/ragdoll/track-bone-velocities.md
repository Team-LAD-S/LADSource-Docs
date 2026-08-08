---
title: "ENT:_TrackBoneVelocities"
---

[Back to Ragdoll](index.md)

<a id="ent-trackbonevelocities"></a>
# `ENT:_TrackBoneVelocities` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_TrackBoneVelocities()
```

</div>

Tracks per-bone world velocities every think tick by differencing positions.
Called automatically from the main think loop.  Only active while the NPC is
alive and not in an active ragdoll phase so we don't waste cycles.

## Parameters

This method takes no explicit arguments.

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ragdoll.lua:26</code>.</p>
