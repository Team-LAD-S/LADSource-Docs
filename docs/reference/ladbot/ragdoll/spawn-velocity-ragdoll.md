---
title: "ENT:_SpawnVelocityRagdoll"
---

[Back to Ragdoll](index.md)

<a id="ent-spawnvelocityragdoll"></a>
# `ENT:_SpawnVelocityRagdoll` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_SpawnVelocityRagdoll()
```

</div>

Spawns a prop_ragdoll that exactly matches the NPC's current pose and applies
per-bone animation velocities so limbs carry momentum rather than freezing.
Returns the ragdoll entity (or nil on failure).

## Parameters

This method takes no explicit arguments.

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ragdoll.lua:83</code>.</p>
