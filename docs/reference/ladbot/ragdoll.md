# Ragdoll

Methods defined in `lua/entities/lad_framework_base/ragdoll.lua`.

!!! info "Generated reference"

    This page is generated from the current Lua source. Add API annotations
    above a method in the source file to improve its documentation.

## Methods

<div class="api-method-list" markdown>

| Method | Summary |
| --- | --- |
| [`ENT:DeathRagdoll`](#ent-deathragdoll) | Death ragdoll — spawns a permanent physics ragdoll with per-bone animation velocities so every limb carries the momentum it had at the moment of death. Only active when lad_ragdollmode == 1 (checked at call-site in OnDeath). |
| [`ENT:DowningRagdoll`](#ent-downingragdoll) | Ragdoll triggered by a downing hit-reaction at a specific animation cycle. The NPC is hidden behind a physics ragdoll for ragdoll_time seconds; it then lerps its limbs toward the first frame of the appropriate get-up animation and seamlessly transitions back to the NPC standing-up sequence. Only active when lad_ragdollmode == 1. Call this from inside your hit-reaction cycle callback — orientation flags (DownedFront / DownedBack) must already be set by the time you call it. |
| [`ENT:_GetRootAnimVelocity`](#ent-getrootanimvelocity) | Returns the root-motion velocity of the current animation sequence in world space. Source model space: +X = forward, +Y = LEFT, +Z = up. ang:Right() points to the RIGHT (-Y in model space), so the Y component must be negated; otherwise lateral root-motion is applied in the opposite direction. |
| [`ENT:_RagdollApplyHitImpulse`](#ent-ragdollapplyhitimpulse) | Applies a physics impulse to the active ragdoll at the nearest bone to hitPos. Used by ApplyAttackDamage to make the ragdoll react to incoming hits. |
| [`ENT:_SpawnVelocityRagdoll`](#ent-spawnvelocityragdoll) | Spawns a prop_ragdoll that exactly matches the NPC's current pose and applies per-bone animation velocities so limbs carry momentum rather than freezing. Returns the ragdoll entity (or nil on failure). |
| [`ENT:_TrackBoneVelocities`](#ent-trackbonevelocities) | Tracks per-bone world velocities every think tick by differencing positions. Called automatically from the main think loop.  Only active while the NPC is alive and not in an active ragdoll phase so we don't waste cycles. |

</div>

<a id="ent-deathragdoll"></a>
## `ENT:DeathRagdoll`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:DeathRagdoll()
```

</div>

Death ragdoll — spawns a permanent physics ragdoll with per-bone animation
velocities so every limb carries the momentum it had at the moment of death.
Only active when lad_ragdollmode == 1 (checked at call-site in OnDeath).

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ragdoll.lua:586</code>.</p>

<a id="ent-downingragdoll"></a>
## `ENT:DowningRagdoll`

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

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `ragdoll_time` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ragdoll.lua:292</code>.</p>

<a id="ent-getrootanimvelocity"></a>
## `ENT:_GetRootAnimVelocity`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_GetRootAnimVelocity()
```

</div>

Returns the root-motion velocity of the current animation sequence in world space.
Source model space: +X = forward, +Y = LEFT, +Z = up.
ang:Right() points to the RIGHT (-Y in model space), so the Y component must be
negated; otherwise lateral root-motion is applied in the opposite direction.

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ragdoll.lua:74</code>.</p>

<a id="ent-ragdollapplyhitimpulse"></a>
## `ENT:_RagdollApplyHitImpulse`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_RagdollApplyHitImpulse(hitPos, impulse)
```

</div>

Applies a physics impulse to the active ragdoll at the nearest bone to hitPos.
Used by ApplyAttackDamage to make the ragdoll react to incoming hits.

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `hitPos` | `any` | Not documented. |
| `impulse` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ragdoll.lua:559</code>.</p>

<a id="ent-spawnvelocityragdoll"></a>
## `ENT:_SpawnVelocityRagdoll`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_SpawnVelocityRagdoll()
```

</div>

Spawns a prop_ragdoll that exactly matches the NPC's current pose and applies
per-bone animation velocities so limbs carry momentum rather than freezing.
Returns the ragdoll entity (or nil on failure).

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ragdoll.lua:83</code>.</p>

<a id="ent-trackbonevelocities"></a>
## `ENT:_TrackBoneVelocities`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_TrackBoneVelocities()
```

</div>

Tracks per-bone world velocities every think tick by differencing positions.
Called automatically from the main think loop.  Only active while the NPC is
alive and not in an active ragdoll phase so we don't waste cycles.

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ragdoll.lua:26</code>.</p>
