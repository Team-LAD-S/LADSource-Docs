# AI

Methods defined in `lua/entities/lad_framework_base/ai.lua`.

!!! info "Generated reference"

    This page is generated from the current Lua source. Add API annotations
    above a method in the source file to improve its documentation.

## Methods

<div class="api-method-list" markdown>

| Method | Summary |
| --- | --- |
| [`ENT:AIAttemptReload`](ai-attempt-reload.md) | Documentation pending. |
| [`ENT:AICheckEnemyWeaponClass`](ai-check-enemy-weapon-class.md) | Documentation pending. |
| [`ENT:AICheckObstacles`](ai-check-obstacles.md) | Documentation pending. |
| [`ENT:AIDefaultAttackRoutine`](ai-default-attack-routine.md) | Documentation pending. |
| [`ENT:AIDefaultFlinchAttack`](ai-default-flinch-attack.md) | Documentation pending. |
| [`ENT:AIDefaultGuardAction`](ai-default-guard-action.md) | Documentation pending. |
| [`ENT:AIDefaultGuardAttack`](ai-default-guard-attack.md) | Documentation pending. |
| [`ENT:AIDefaultRangeAttackRoutine`](ai-default-range-attack-routine.md) | Documentation pending. |
| [`ENT:AIDefaultRecoverFast`](ai-default-recover-fast.md) | Documentation pending. |
| [`ENT:AIDefaultStrafingRoutine`](ai-default-strafing-routine.md) | Documentation pending. |
| [`ENT:AIDefaultSwayGuardRoutine`](ai-default-sway-guard-routine.md) | Documentation pending. |
| [`ENT:AIFaceEnemy`](ai-face-enemy.md) | Documentation pending. |
| [`ENT:AIFlinchReGuard`](ai-flinch-re-guard.md) | Documentation pending. |
| [`ENT:AIForceEnemyMovesetActivation`](ai-force-enemy-moveset-activation.md) | Documentation pending. |
| [`ENT:AIGrabAttackRoutine`](ai-grab-attack-routine.md) | Documentation pending. |
| [`ENT:AIGrabMovementRoutine`](ai-grab-movement-routine.md) | Documentation pending. |
| [`ENT:AIHactBBoxAvoidance`](ai-hact-b-box-avoidance.md) | Documentation pending. |
| [`ENT:AILoopFar`](ai-loop-far.md) | Documentation pending. |
| [`ENT:AILoopNear`](ai-loop-near.md) | Documentation pending. |
| [`ENT:AIManageAnger`](ai-manage-anger.md) | Documentation pending. |
| [`ENT:AIManageBravery`](ai-manage-bravery.md) | Documentation pending. |
| [`ENT:AIManageTauntAnger`](ai-manage-taunt-anger.md) | Documentation pending. |
| [`ENT:AINodedComboThink`](ai-noded-combo-think.md) | Documentation pending. |
| [`ENT:AINodeExecute`](ai-node-execute.md) | Documentation pending. |
| [`ENT:AIOpenDoors`](ai-open-doors.md) | Documentation pending. |
| [`ENT:AIRunAttackRoutine`](ai-run-attack-routine.md) | Documentation pending. |
| [`ENT:AIScanAndExecuteHacts`](ai-scan-and-execute-hacts.md) | Documentation pending. |
| [`ENT:AIWeaponThrowRoutine`](ai-weapon-throw-routine.md) | Documentation pending. |
| [`ENT:BattleAILoopFar`](battle-ai-loop-far.md) | override this function in your ladbot to make custom battle AI (when farther away from enemy) |
| [`ENT:BattleAILoopNear`](battle-ai-loop-near.md) | override this function in your ladbot to make custom battle AI (when close to the enemy) |
| [`ENT:FindNearbyAlliesInCombat`](find-nearby-allies-in-combat.md) | find nearby Nextbots of the same type |
| [`ENT:GetEncirclementStrafeBias`](get-encirclement-strafe-bias.md) | Documentation pending. |
| [`ENT:GetSwayFrequency`](get-sway-frequency.md) | Documentation pending. |
| [`ENT:GetSwayNextAttack`](get-sway-next-attack.md) | Documentation pending. |
| [`ENT:GoToWall`](go-to-wall.md) | Documentation pending. |
| [`ENT:GoToWeapon`](go-to-weapon.md) | Documentation pending. |
| [`ENT:OnAvoidEnemy`](on-avoid-enemy.md) | Belongs to DrGBase, whether the LADBot should avoid entity. Can be overriden to implement custom behavior. |
| [`ENT:OnChaseEnemy`](on-chase-enemy.md) | Belongs to DrGBase, called when the LADBot is chasing an enemy (inside the coroutine). Can be overriden to implement custom behavior when the LADBot is chasing an enemy. By default currently checks if the LADBot IsOverworldStationary() and returns true to stop chasing any other enemies. |
| [`ENT:OnIdle`](on-idle.md) | Belongs to DrGBase, called after the LADBot successfully reaches its current patrol destination. (inside the coroutine). Can be overriden to implement custom behavior. By default currently waits for 1 second before setting self._patrolling to false. |
| [`ENT:OnLastEnemy`](on-last-enemy.md) | Documentation pending. |
| [`ENT:OnPatrolling`](on-patrolling.md) | Documentation pending. |
| [`ENT:OnPatrolUnreachable`](on-patrol-unreachable.md) | Documentation pending. |
| [`ENT:OnReachedPatrol`](on-reached-patrol.md) | Belongs to DrGBase, called after the LADBot successfully reaches its current patrol destination. (inside the coroutine). Can be overriden to implement custom behavior. By default currently waits for 1 second before setting self._patrolling to false. |
| [`ENT:ScanForNearestWallAndJump`](scan-for-nearest-wall-and-jump.md) | Documentation pending. |
| [`ENT:ScanForNearestWeaponAndMove`](scan-for-nearest-weapon-and-move.md) | Documentation pending. |
| [`ENT:SetNextAttack`](set-next-attack.md) | Documentation pending. |
| [`ENT:ShouldIgnore`](should-ignore.md) | Belongs to DrGBase, whether the LADBot should ignore an entity. Can be overriden to implement custom behavior. By default currently checks if the LADBot should ignore other LADBots which are IsOverworldStationary(). |

</div>
