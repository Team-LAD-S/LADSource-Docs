# Overrides

Methods defined in `lua/entities/lad_framework_base/overrides.lua`.

!!! info "Generated reference"

    This page is generated from the current Lua source. Add API annotations
    above a method in the source file to improve its documentation.

## Methods

<div class="api-method-list" markdown>

| Method | Summary |
| --- | --- |
| [`ENT:ApplyAttackDamage`](apply-attack-damage.md) | Documentation pending. |
| [`ENT:Approach`](approach.md) | Documentation pending. |
| [`ENT:Attack`](attack.md) | filters downed people |
| [`ENT:AttackEntity`](attack-entity.md) | Documentation pending. |
| [`ENT:BehaveStart`](behave-start.md) | Documentation pending. |
| [`ENT:BehaveUpdate`](behave-update.md) | Documentation pending. |
| [`ENT:ClearPSAWPrediction`](clear-psaw-prediction.md) | Documentation pending. |
| [`ENT:CustomInitialize`](custom-initialize.md) | Documentation pending. |
| [`ENT:Draw`](draw.md) | Documentation pending. |
| [`ENT:EntitiesInCone`](entities-in-cone.md) | Documentation pending. |
| [`ENT:FaceEnemy`](face-enemy.md) | Documentation pending. |
| [`ENT:FaceTowards`](face-towards.md) | Documentation pending. |
| [`ENT:FixCollisions`](fix-collisions.md) | Documentation pending. |
| [`ENT:GetConfiguredCollisionBounds`](get-configured-collision-bounds.md) | Documentation pending. |
| [`ENT:GetRenderAngles`](get-render-angles.md) | Documentation pending. |
| [`ENT:GetRenderOrigin`](get-render-origin.md) | Return our client-predicted position for rendering instead of the network-interpolated origin.  GetPos() (hitboxes/physics) is never touched — only the visual draw position is overridden.  During non-PSAW states _LAD_predictedPos is nil so it falls back to the normal GetPos() path. |
| [`ENT:HandleEnemy`](handle-enemy.md) | Documentation pending. |
| [`ENT:Initialize`](initialize.md) | Documentation pending. |
| [`ENT:MoveBackward`](move-backward.md) | Documentation pending. |
| [`ENT:MoveForward`](move-forward.md) | Documentation pending. |
| [`ENT:MoveLeft`](move-left.md) | Documentation pending. |
| [`ENT:MoveRight`](move-right.md) | Documentation pending. |
| [`ENT:OnFallDamage`](on-fall-damage.md) | Documentation pending. |
| [`ENT:OnInjured`](on-injured.md) | Documentation pending. |
| [`ENT:OnKilled`](on-killed.md) | Documentation pending. |
| [`ENT:OnRemove`](on-remove.md) | Weak keys handle GC cleanup, but CallOnRemove fires before GC so explicit nil is cleaner. |
| [`ENT:OnUpdateAnimation`](on-update-animation.md) | Documentation pending. |
| [`ENT:Patrol`](patrol.md) | Documentation pending. |
| [`ENT:PlaySequence`](play-sequence.md) | Documentation pending. |
| [`ENT:PlaySequenceAndMove`](play-sequence-and-move.md) | Documentation pending. |
| [`ENT:PlaySequenceAndWait`](play-sequence-and-wait.md) | Documentation pending. |
| [`ENT:PossessorView`](possessor-view.md) | Documentation pending. |
| [`ENT:PushAwayFromEntity`](push-away-from-entity.md) | Unlike DrGBase's PushEntity(), this moves the fighter calling the function away from ent. PushEntity() applies velocity/force to ent instead. |
| [`ENT:SetGameplayCollisionBounds`](set-gameplay-collision-bounds.md) | SetCollisionBounds is affected by ModelScale on anim/NextBot entities. Keep fighter navigation bounds in gameplay units so a larger visual model does not grow an OBB corner into nearby map geometry when the AI turns in place. |
| [`ENT:SetupDataTables`](setup-data-tables.md) | Documentation pending. |
| [`ENT:Think`](think.md) | ENT:Think() override (source: drgbase_nextbot/shared.lua) Eliminates 10-12 redundant CurTime() C calls per tick by caching one value at the top. In the medium-delay block, reuses self._DrGBaseWaterLevel (already maintained at 20Hz by the short-delay block) instead of calling WaterLevel() a second time per 0.1s interval. |
| [`ENT:UpdateAnimation`](update-animation.md) | Documentation pending. |
| [`ENT:UpdateEnemy`](update-enemy.md) | Documentation pending. |
| [`ENT:_BaseInitialize`](base-initialize-152.md) | Documentation pending. |
| [`ENT:_BaseInitialize`](base-initialize-1979.md) | _BaseInitialize is an empty stub in DRGBase called after _InitModules() completes, so all internal fields (_DrGBaseSequenceEvents etc.) are already set up by the time this runs.  Overriding Initialize() directly would skip _InitModules() entirely. |
| [`ENT:_HandleLandOnGround`](handle-land-on-ground.md) | Documentation pending. |
| [`ENT:_HandleLeaveGround`](handle-leave-ground.md) | Documentation pending. |
| [`ENT:_InitModules`](init-modules.md) | Documentation pending. |
| [`ENT:_LADDrawBonemergedChild`](lad-draw-bonemerged-child.md) | Documentation pending. |

</div>
