# Fighter Command

Methods defined in `lua/entities/lad_framework_base/fighter_command.lua`.

!!! info "Generated reference"

    This page is generated from the current Lua source. Add API annotations
    above a method in the source file to improve its documentation.

## Methods

<div class="api-method-list" markdown>

| Method | Summary |
| --- | --- |
| [`ENT:ActivateCombat`](#ent-activatecombat) | Activates combat of a LADBot that this function is ran on. |
| [`ENT:ActivatePerk`](#ent-activateperk) | Documentation pending. |
| [`ENT:BecomeConfused`](#ent-becomeconfused) | Documentation pending. |
| [`ENT:BecomePissed`](#ent-becomepissed) | Documentation pending. |
| [`ENT:BecomeScared`](#ent-becomescared) | Documentation pending. |
| [`ENT:CancelGuard`](#ent-cancelguard) | Documentation pending. |
| [`ENT:CeaseMovementRates`](#ent-ceasemovementrates) | Documentation pending. |
| [`ENT:CycleToNextStyle`](#ent-cycletonextstyle) | Documentation pending. |
| [`ENT:DeactivateCombat`](#ent-deactivatecombat) | Documentation pending. |
| [`ENT:DeductAreaWideBravery`](#ent-deductareawidebravery) | Documentation pending. |
| [`ENT:GetDoorState`](#ent-getdoorstate) | Documentation pending. |
| [`ENT:GetLockedInDirectionalTarget`](#ent-getlockedindirectionaltarget) | Returns the best enemy candidate in the direction the possessor is pressing (WASD, 8-way), or nil if no suitable candidate passes all three filters: 1. Edge-triggered: caller only invokes this on a direction change (see PossessionThink). 2. Angular separation: candidate must be >20 degrees away from current target (avoids switching between enemies that are essentially overlapping from our POV). 3. Hysteresis: candidate must outscore the current target by a margin of 0.15 (avoids switching to a marginally better-aligned enemy in a tight cluster). |
| [`ENT:GetLockInDirSnapshot`](#ent-getlockindirsnapshot) | Used for edge-detection: a switch is only evaluated when this string changes. |
| [`ENT:GetMovementDirection`](#ent-getmovementdirection) | Documentation pending. |
| [`ENT:GetNearestEnemy`](#ent-getnearestenemy) | Documentation pending. |
| [`ENT:Guard`](#ent-guard) | Documentation pending. |
| [`ENT:Interact`](#ent-interact) | Documentation pending. |
| [`ENT:IsDoorLocked`](#ent-isdoorlocked) | Documentation pending. |
| [`ENT:IsInLockOnCone`](#ent-isinlockoncone) | Returns true if ent is within the lock-on cone (default ±65° from the nextbot's own forward vector). |
| [`ENT:LAD_DoScreenShake`](#ent-lad-doscreenshake) | Documentation pending. |
| [`ENT:OnIdleEnemy`](#ent-onidleenemy) | Documentation pending. |
| [`ENT:OnMeleeAttack`](#ent-onmeleeattack) | Documentation pending. |
| [`ENT:OnPossessed`](#ent-onpossessed) | Documentation pending. |
| [`ENT:OnRangeAttack`](#ent-onrangeattack) | Documentation pending. |
| [`ENT:OnWaterLevelChange`](#ent-onwaterlevelchange) | Documentation pending. |
| [`ENT:PossessionR`](#ent-possessionr) | Grabbing/weapon pick up related |
| [`ENT:PossessionThink`](#ent-possessionthink) | Documentation pending. |
| [`ENT:PossessionX`](#ent-possessionx) | Guarding related |
| [`ENT:PredictNextPosition`](#ent-predictnextposition) | Documentation pending. |
| [`ENT:RegenerateHealth`](#ent-regeneratehealth) | Documentation pending. |
| [`ENT:RemovePerk`](#ent-removeperk) | Documentation pending. |
| [`ENT:ResetDownedState`](#ent-resetdownedstate) | Documentation pending. |
| [`ENT:ResetMovementAnimations`](#ent-resetmovementanimations) | Documentation pending. |
| [`ENT:ResetRates`](#ent-resetrates) | Documentation pending. |
| [`ENT:SetCommonFighterMoveset`](#ent-setcommonfightermoveset) | Documentation pending. |
| [`ENT:SetHyperArmor`](#ent-sethyperarmor) | Documentation pending. |
| [`ENT:SetMovementAnimations`](#ent-setmovementanimations) | Documentation pending. |
| [`ENT:SetupKeybinds`](#ent-setupkeybinds) | Documentation pending. |
| [`ENT:ShouldRun`](#ent-shouldrun) | Documentation pending. |
| [`ENT:SootheAnger`](#ent-sootheanger) | Documentation pending. |
| [`ENT:SwitchStyle`](#ent-switchstyle) | Documentation pending. |
| [`ENT:SwitchStyleUntilReady`](#ent-switchstyleuntilready) | Documentation pending. |
| [`ENT:TempHyperArmor`](#ent-temphyperarmor) | for use in CICO |

</div>

<a id="ent-activatecombat"></a>
## `ENT:ActivateCombat`

<div class="api-badges"><span class="api-badge api-badge--server">server</span></div>

<div class="api-signature" markdown>

```lua
function ENT:ActivateCombat(target, skipanim)
```

</div>

Activates combat of a LADBot that this function is ran on.

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `target` | `ent` | Snaps to whoever activates combat |
| `skipanim` | `boolean` | Whether to skip the battle-start animation. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:778</code>.</p>

<a id="ent-activateperk"></a>
## `ENT:ActivatePerk`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:ActivatePerk(time, pwr)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `time` | `any` | Not documented. |
| `pwr` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:1294</code>.</p>

<a id="ent-becomeconfused"></a>
## `ENT:BecomeConfused`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:BecomeConfused()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:920</code>.</p>

<a id="ent-becomepissed"></a>
## `ENT:BecomePissed`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:BecomePissed()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:964</code>.</p>

<a id="ent-becomescared"></a>
## `ENT:BecomeScared`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:BecomeScared()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:947</code>.</p>

<a id="ent-cancelguard"></a>
## `ENT:CancelGuard`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CancelGuard()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:1063</code>.</p>

<a id="ent-ceasemovementrates"></a>
## `ENT:CeaseMovementRates`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CeaseMovementRates()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:1261</code>.</p>

<a id="ent-cycletonextstyle"></a>
## `ENT:CycleToNextStyle`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CycleToNextStyle()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:359</code>.</p>

<a id="ent-deactivatecombat"></a>
## `ENT:DeactivateCombat`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:DeactivateCombat()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:864</code>.</p>

<a id="ent-deductareawidebravery"></a>
## `ENT:DeductAreaWideBravery`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:DeductAreaWideBravery(deduct, radius)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `deduct` | `any` | Not documented. |
| `radius` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:933</code>.</p>

<a id="ent-getdoorstate"></a>
## `ENT:GetDoorState`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetDoorState(door)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `door` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:719</code>.</p>

<a id="ent-getlockedindirectionaltarget"></a>
## `ENT:GetLockedInDirectionalTarget`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetLockedInDirectionalTarget(dirSnapshot)
```

</div>

Returns the best enemy candidate in the direction the possessor is pressing (WASD, 8-way),
or nil if no suitable candidate passes all three filters:
1. Edge-triggered: caller only invokes this on a direction change (see PossessionThink).
2. Angular separation: candidate must be >20 degrees away from current target
(avoids switching between enemies that are essentially overlapping from our POV).
3. Hysteresis: candidate must outscore the current target by a margin of 0.15
(avoids switching to a marginally better-aligned enemy in a tight cluster).

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `dirSnapshot` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:582</code>.</p>

<a id="ent-getlockindirsnapshot"></a>
## `ENT:GetLockInDirSnapshot`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetLockInDirSnapshot()
```

</div>

Used for edge-detection: a switch is only evaluated when this string changes.

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:553</code>.</p>

<a id="ent-getmovementdirection"></a>
## `ENT:GetMovementDirection`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetMovementDirection()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:1363</code>.</p>

<a id="ent-getnearestenemy"></a>
## `ENT:GetNearestEnemy`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetNearestEnemy()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:528</code>.</p>

<a id="ent-guard"></a>
## `ENT:Guard`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:Guard(isAI)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `isAI` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:999</code>.</p>

<a id="ent-interact"></a>
## `ENT:Interact`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:Interact()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:199</code>.</p>

<a id="ent-isdoorlocked"></a>
## `ENT:IsDoorLocked`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:IsDoorLocked(door)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `door` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:715</code>.</p>

<a id="ent-isinlockoncone"></a>
## `ENT:IsInLockOnCone`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:IsInLockOnCone(ent, halfAngleDeg)
```

</div>

Returns true if ent is within the lock-on cone (default ±65° from the
nextbot's own forward vector).

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `ent` | `any` | Not documented. |
| `halfAngleDeg` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:538</code>.</p>

<a id="ent-lad-doscreenshake"></a>
## `ENT:LAD_DoScreenShake`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:LAD_DoScreenShake(amplitude, frequency, duration, radius)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `amplitude` | `any` | Not documented. |
| `frequency` | `any` | Not documented. |
| `duration` | `any` | Not documented. |
| `radius` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:170</code>.</p>

<a id="ent-onidleenemy"></a>
## `ENT:OnIdleEnemy`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:OnIdleEnemy()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:1157</code>.</p>

<a id="ent-onmeleeattack"></a>
## `ENT:OnMeleeAttack`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:OnMeleeAttack(enemy)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `enemy` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:1118</code>.</p>

<a id="ent-onpossessed"></a>
## `ENT:OnPossessed`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:OnPossessed(ply)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `ply` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:690</code>.</p>

<a id="ent-onrangeattack"></a>
## `ENT:OnRangeAttack`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:OnRangeAttack(enemy)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `enemy` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:1079</code>.</p>

<a id="ent-onwaterlevelchange"></a>
## `ENT:OnWaterLevelChange`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:OnWaterLevelChange()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:1337</code>.</p>

<a id="ent-possessionr"></a>
## `ENT:PossessionR`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:PossessionR()
```

</div>

Grabbing/weapon pick up related

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:182</code>.</p>

<a id="ent-possessionthink"></a>
## `ENT:PossessionThink`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:PossessionThink()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:374</code>.</p>

<a id="ent-possessionx"></a>
## `ENT:PossessionX`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:PossessionX(hold)
```

</div>

Guarding related

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `hold` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:187</code>.</p>

<a id="ent-predictnextposition"></a>
## `ENT:PredictNextPosition`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:PredictNextPosition()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:1356</code>.</p>

<a id="ent-regeneratehealth"></a>
## `ENT:RegenerateHealth`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:RegenerateHealth(value)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `value` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:766</code>.</p>

<a id="ent-removeperk"></a>
## `ENT:RemovePerk`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:RemovePerk(pwr)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `pwr` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:1323</code>.</p>

<a id="ent-resetdownedstate"></a>
## `ENT:ResetDownedState`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:ResetDownedState()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:1211</code>.</p>

<a id="ent-resetmovementanimations"></a>
## `ENT:ResetMovementAnimations`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:ResetMovementAnimations()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:1195</code>.</p>

<a id="ent-resetrates"></a>
## `ENT:ResetRates`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:ResetRates()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:1253</code>.</p>

<a id="ent-setcommonfightermoveset"></a>
## `ENT:SetCommonFighterMoveset`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:SetCommonFighterMoveset()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:679</code>.</p>

<a id="ent-sethyperarmor"></a>
## `ENT:SetHyperArmor`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:SetHyperArmor(value)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `value` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:1285</code>.</p>

<a id="ent-setmovementanimations"></a>
## `ENT:SetMovementAnimations`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:SetMovementAnimations(combat, walk, run, idle, guard)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `combat` | `any` | Not documented. |
| `walk` | `any` | Not documented. |
| `run` | `any` | Not documented. |
| `idle` | `any` | Not documented. |
| `guard` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:1225</code>.</p>

<a id="ent-setupkeybinds"></a>
## `ENT:SetupKeybinds`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:SetupKeybinds()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:85</code>.</p>

<a id="ent-shouldrun"></a>
## `ENT:ShouldRun`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:ShouldRun()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:1164</code>.</p>

<a id="ent-sootheanger"></a>
## `ENT:SootheAnger`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:SootheAnger()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:992</code>.</p>

<a id="ent-switchstyle"></a>
## `ENT:SwitchStyle`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:SwitchStyle(id, force)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `id` | `any` | Not documented. |
| `force` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:301</code>.</p>

<a id="ent-switchstyleuntilready"></a>
## `ENT:SwitchStyleUntilReady`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:SwitchStyleUntilReady(id, force, onSuccess, retryDelay)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `id` | `any` | Not documented. |
| `force` | `any` | Not documented. |
| `onSuccess` | `any` | Not documented. |
| `retryDelay` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:262</code>.</p>

<a id="ent-temphyperarmor"></a>
## `ENT:TempHyperArmor`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:TempHyperArmor(ha)
```

</div>

for use in CICO

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `ha` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:1275</code>.</p>
