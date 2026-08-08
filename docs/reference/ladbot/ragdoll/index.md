# Ragdoll

Methods defined in `lua/entities/lad_framework_base/ragdoll.lua`.

!!! info "Generated reference"

    This page is generated from the current Lua source. Add API annotations
    above a method in the source file to improve its documentation.

## Methods

<div class="api-method-list" markdown>

| Method | Summary |
| --- | --- |
| [`ENT:DeathRagdoll`](death-ragdoll.md) | Death ragdoll — spawns a permanent physics ragdoll with per-bone animation velocities so every limb carries the momentum it had at the moment of death. Only active when lad_ragdollmode == 1 (checked at call-site in OnDeath). |
| [`ENT:DowningRagdoll`](downing-ragdoll.md) | Ragdoll triggered by a downing hit-reaction at a specific animation cycle. The NPC is hidden behind a physics ragdoll for ragdoll_time seconds; it then lerps its limbs toward the first frame of the appropriate get-up animation and seamlessly transitions back to the NPC standing-up sequence. Only active when lad_ragdollmode == 1. Call this from inside your hit-reaction cycle callback — orientation flags (DownedFront / DownedBack) must already be set by the time you call it. |
| [`ENT:_GetRootAnimVelocity`](get-root-anim-velocity.md) | Returns the root-motion velocity of the current animation sequence in world space. Source model space: +X = forward, +Y = LEFT, +Z = up. ang:Right() points to the RIGHT (-Y in model space), so the Y component must be negated; otherwise lateral root-motion is applied in the opposite direction. |
| [`ENT:_RagdollApplyHitImpulse`](ragdoll-apply-hit-impulse.md) | Applies a physics impulse to the active ragdoll at the nearest bone to hitPos. Used by ApplyAttackDamage to make the ragdoll react to incoming hits. |
| [`ENT:_SpawnVelocityRagdoll`](spawn-velocity-ragdoll.md) | Spawns a prop_ragdoll that exactly matches the NPC's current pose and applies per-bone animation velocities so limbs carry momentum rather than freezing. Returns the ragdoll entity (or nil on failure). |
| [`ENT:_TrackBoneVelocities`](track-bone-velocities.md) | Tracks per-bone world velocities every think tick by differencing positions. Called automatically from the main think loop.  Only active while the NPC is alive and not in an active ragdoll phase so we don't waste cycles. |

</div>
