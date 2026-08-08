# Fighter Command

Methods defined in `lua/entities/lad_framework_base/fighter_command.lua`.

!!! info "Generated reference"

    This page is generated from the current Lua source. Add API annotations
    above a method in the source file to improve its documentation.

## Methods

<div class="api-method-list" markdown>

| Method | Summary |
| --- | --- |
| [`ENT:ActivateCombat`](activate-combat.md) | Activates combat of a LADBot that this function is ran on. |
| [`ENT:ActivatePerk`](activate-perk.md) | Documentation pending. |
| [`ENT:BecomeConfused`](become-confused.md) | Documentation pending. |
| [`ENT:BecomePissed`](become-pissed.md) | Documentation pending. |
| [`ENT:BecomeScared`](become-scared.md) | Documentation pending. |
| [`ENT:CancelGuard`](cancel-guard.md) | Documentation pending. |
| [`ENT:CeaseMovementRates`](cease-movement-rates.md) | Documentation pending. |
| [`ENT:CycleToNextStyle`](cycle-to-next-style.md) | Documentation pending. |
| [`ENT:DeactivateCombat`](deactivate-combat.md) | Documentation pending. |
| [`ENT:DeductAreaWideBravery`](deduct-area-wide-bravery.md) | Documentation pending. |
| [`ENT:GetDoorState`](get-door-state.md) | Documentation pending. |
| [`ENT:GetLockedInDirectionalTarget`](get-locked-in-directional-target.md) | Returns the best enemy candidate in the direction the possessor is pressing (WASD, 8-way), or nil if no suitable candidate passes all three filters: 1. Edge-triggered: caller only invokes this on a direction change (see PossessionThink). 2. Angular separation: candidate must be >20 degrees away from current target (avoids switching between enemies that are essentially overlapping from our POV). 3. Hysteresis: candidate must outscore the current target by a margin of 0.15 (avoids switching to a marginally better-aligned enemy in a tight cluster). |
| [`ENT:GetLockInDirSnapshot`](get-lock-in-dir-snapshot.md) | Used for edge-detection: a switch is only evaluated when this string changes. |
| [`ENT:GetMovementDirection`](get-movement-direction.md) | Documentation pending. |
| [`ENT:GetNearestEnemy`](get-nearest-enemy.md) | Documentation pending. |
| [`ENT:Guard`](guard.md) | Documentation pending. |
| [`ENT:Interact`](interact.md) | Documentation pending. |
| [`ENT:IsDoorLocked`](is-door-locked.md) | Documentation pending. |
| [`ENT:IsInLockOnCone`](is-in-lock-on-cone.md) | Returns true if ent is within the lock-on cone (default ±65° from the nextbot's own forward vector). |
| [`ENT:LAD_DoScreenShake`](lad-do-screen-shake.md) | Documentation pending. |
| [`ENT:OnIdleEnemy`](on-idle-enemy.md) | Documentation pending. |
| [`ENT:OnMeleeAttack`](on-melee-attack.md) | Documentation pending. |
| [`ENT:OnPossessed`](on-possessed.md) | Documentation pending. |
| [`ENT:OnRangeAttack`](on-range-attack.md) | Documentation pending. |
| [`ENT:OnWaterLevelChange`](on-water-level-change.md) | Documentation pending. |
| [`ENT:PossessionR`](possession-r.md) | Grabbing/weapon pick up related |
| [`ENT:PossessionThink`](possession-think.md) | Documentation pending. |
| [`ENT:PossessionX`](possession-x.md) | Guarding related |
| [`ENT:PredictNextPosition`](predict-next-position.md) | Documentation pending. |
| [`ENT:RegenerateHealth`](regenerate-health.md) | Documentation pending. |
| [`ENT:RemovePerk`](remove-perk.md) | Documentation pending. |
| [`ENT:ResetDownedState`](reset-downed-state.md) | Documentation pending. |
| [`ENT:ResetMovementAnimations`](reset-movement-animations.md) | Documentation pending. |
| [`ENT:ResetRates`](reset-rates.md) | Documentation pending. |
| [`ENT:SetCommonFighterMoveset`](set-common-fighter-moveset.md) | Documentation pending. |
| [`ENT:SetHyperArmor`](set-hyper-armor.md) | Documentation pending. |
| [`ENT:SetMovementAnimations`](set-movement-animations.md) | Documentation pending. |
| [`ENT:SetupKeybinds`](setup-keybinds.md) | Documentation pending. |
| [`ENT:ShouldRun`](should-run.md) | Documentation pending. |
| [`ENT:SootheAnger`](soothe-anger.md) | Documentation pending. |
| [`ENT:SwitchStyle`](switch-style.md) | Documentation pending. |
| [`ENT:SwitchStyleUntilReady`](switch-style-until-ready.md) | Documentation pending. |
| [`ENT:TempHyperArmor`](temp-hyper-armor.md) | for use in CICO |

</div>
