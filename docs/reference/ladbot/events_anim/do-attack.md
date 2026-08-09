---
title: "ENT:DoAttack"
---

[Back to Events Anim](index.md)

<a id="ent-doattack"></a>
# `ENT:DoAttack` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span></div>

<div class="api-signature" markdown>

```lua
function ENT:DoAttack(attack, key, atker)
```

</div>

Runs the attack code, also internally passes information to ENT:Attack(attack, callback, attacker) function from Overrides module.

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `attack` | `table` | Yes | Attack configuration. |
| `key` | `string` | No | Event name for HandleAnimEvent. |
| `atker` | `ent` | No | The attacker entity. |

</div>

### `attack` table fields

<div class="api-parameter-table api-parameter-fields" markdown>

| Key | Type | Required | Description |
| --- | --- | :---: | --- |
| `Damage` | `number` | No | Damage dealt by the attack, defaults to 15 if not specified. |
| `DamageType` | `enum` | No | Damage type dealt by the attack, defaults to DMG_GENERIC if not specified, see https://wiki.facepunch.com/gmod/Enums/DMG for more information. |
| `Range` | `number` | No | Range of the attack, defaults to 23 if not specified. |
| `Angle` | `number` | No | Angle of the attack, defaults to 150° if not specified. |
| `HitSounds` | `table/string` | No | A table of random sounds to play when the attack hits a target, also accepts strings "p" for stronger punch sounds and "none" for no hit sounds at all, defaults to weak punch sounds if not specified. |
| `MissSounds` | `table/string` | No | A table of random sounds to play when the attack misses a target, also accepts strings "swing_kick" for stronger miss sounds and "none" for no miss sounds at all, defaults to weak swing sounds if not specified. |
| `HitDowned` | `boolean` | No | Whether the attack hits downed targets, defaults to false if not specified. |
| `HitOnce` | `boolean` | No | Whether the attack hits one target once, defaults to false if not specified. |
| `HitReset` | `number` | No | Used in conjuction with HitOnce, defaults to 3 if not specified. |
| `HitProps` | `boolean` | No | Whether the attack hits props, defaults to false if not specified. |
| `HitPropsUp` | `number` | No | Upward velocity when a prop is hit, defaults to 200 if not specified. |
| `HitPropsForward` | `number` | No | Forward velocity when a prop is hit, defaults to 500 if not specified. |
| `TargetiFrames` | `boolean` | No | Whether the attack can target immunity frames, defaults to false if not specified. |
| `Bone` | `string` | No | TBD |
| `Delay` | `number` | No | Delay before the attack code runs, defaults to 0 if not specified. |
| `Side` | `string` | No | Side of the attack, accepts "front", "back", "left", "right", defaults to "front" if not specified. |
| `Knockback` | `number` | No | Knockback force of the attack which affects regular NPCs, defaults to a math.random(120, 140) if not specified. |
| `KnockbackUp` | `number` | No | Knockback upwards force of the attack which affects regular NPCs, defaults to 10 if not specified. |
| `DamageBuddha` | `boolean` | No | Attack doesn't kill the target, even if damage is greater than their health, defaults to false if not specified. |
| `Wallbounce` | `boolean` | No | TBD |
| `WallbounceReaction` | `boolean` | No | TBD |
| `Attacker` | `ent` | No | Who performed the attack? Defaults to self if not specified. |
| `Origin` | `Vector(x,y,z)` | No | Origin of the attack, defaults to self:WorldSpaceCenter() if not specified. |
| `AttackType` | `string` | No | Defines attack type specifically when hitting guards, accepts "sude", "metal", "katana", "bokuto", "bullet"; defaults to "sude" if not specified. TODO: rename this to something else? The naming is a bit confusing. |
| `WeaponSlot` | `number` | No | Defines which weapon slot the attack is coming from, defaults to 1 (right hand) if not specified (attacker must have a weapon). |
| `DeductWeaponDurability` | `boolean/number` | No | How much weapon durability to deduct if attack hits a target, defaults to true/1 if not specified (attacker must have a weapon). |
| `WeaponDamageMultiplier` | `number` | No | Multiplies weapon damage by this value, defaults to 1 if not specified (attacker must have a weapon). |
| `UseWeaponDamage` | `boolean` | No | Whether to use weapon attack damage, defaults to false if not specified (attacker must have a weapon). |
| `UseWeaponRange` | `boolean` | No | Whether to use weapon attack range, defaults to false if not specified (attacker must have a weapon). |
| `UseWeaponAngle` | `boolean` | No | Whether to use weapon attack angle, defaults to false if not specified (attacker must have a weapon). |
| `UseWeaponHitSounds` | `boolean` | No | Whether to use weapon attack hit sounds, defaults to false if not specified (attacker must have a weapon). |
| `UseWeaponMissSounds` | `boolean` | No | Whether to use weapon attack miss sounds, defaults to false if not specified (attacker must have a weapon). |
| `UseWeaponAttackType` | `boolean` | No | Whether to use weapon attack type, defaults to false if not specified (attacker must have a weapon). |
| `Force` | `Vector(x,y,z)` | No | Force of the attack, defaults to Vector(3000,0,0) if not specified, mainly affects ragdolls and physics props. |
| `ViewPunch` | `Angle(pitch,yaw,roll)` | No | View punch, only affects default GMod player entities. |
| `_syncvictim` | `ent` | No | Sync victim, internal use only, defaults to nil if not specified. |

</div>

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events_anim.lua:150</code>.</p>
