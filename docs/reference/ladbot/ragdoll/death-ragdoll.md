---
title: "ENT:DeathRagdoll"
---

[Back to Ragdoll](index.md)

<a id="ent-deathragdoll"></a>
# `ENT:DeathRagdoll` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:DeathRagdoll()
```

</div>

Death ragdoll — spawns a permanent physics ragdoll with per-bone animation
velocities so every limb carries the momentum it had at the moment of death.
Only active when lad_ragdollmode == 1 (checked at call-site in OnDeath).

## Parameters

This method takes no explicit arguments.

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ragdoll.lua:586</code>.</p>
