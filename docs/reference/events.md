# Events

Methods defined in `lua/entities/lad_framework_base/events.lua`.

!!! info "Generated reference"

    This page is generated from the current Lua source. Add API annotations
    above a method in the source file to improve its documentation.

## Methods

| Method | Summary |
| --- | --- |
| [`ENT:_DownedStandup`](#ent-downedstandup) | Documentation pending. |
| [`ENT:_HandleDMGAnim`](#ent-handledmganim) | Documentation pending. |
| [`ENT:_SwitchWBType`](#ent-switchwbtype) | Documentation pending. |
| [`ENT:AlignToSlope`](#ent-aligntoslope) | Documentation pending. |
| [`ENT:AntiJuggleEscape`](#ent-antijuggleescape) | Documentation pending. |
| [`ENT:CheckForWallbound`](#ent-checkforwallbound) | this is only supposed to be ran inside PSAM otherwise how the hell you gonna check fo that |
| [`ENT:CheckGuardBreakBeforeDamage`](#ent-checkguardbreakbeforedamage) | Documentation pending. |
| [`ENT:CheckJuggleState`](#ent-checkjugglestate) | Documentation pending. |
| [`ENT:CheckWallboundState`](#ent-checkwallboundstate) | Documentation pending. |
| [`ENT:CreateParentedProp`](#ent-createparentedprop) | Documentation pending. |
| [`ENT:CustomHandleAnimEvent`](#ent-customhandleanimevent) | Documentation pending. |
| [`ENT:CustomOnDealtDamage`](#ent-customondealtdamage) | Documentation pending. |
| [`ENT:DamageDirection`](#ent-damagedirection) | Documentation pending. |
| [`ENT:DeathThink`](#ent-deaththink) | Documentation pending. |
| [`ENT:Downed`](#ent-downed) | Documentation pending. |
| [`ENT:DropParentedProp`](#ent-dropparentedprop) | Documentation pending. |
| [`ENT:ForeignDMGGuardingBehavior`](#ent-foreigndmgguardingbehavior) | Documentation pending. |
| [`ENT:GetSyncAttacker`](#ent-getsyncattacker) | Documentation pending. |
| [`ENT:GetSyncVictim`](#ent-getsyncvictim) | Documentation pending. |
| [`ENT:HandleAnimEvent`](#ent-handleanimevent) | Documentation pending. |
| [`ENT:HandleBulletDamage`](#ent-handlebulletdamage) | Documentation pending. |
| [`ENT:Juggle`](#ent-juggle) | Documentation pending. |
| [`ENT:OnDealtDamage`](#ent-ondealtdamage) | the beautiful damage feedback. |
| [`ENT:OnDeath`](#ent-ondeath) | Documentation pending. |
| [`ENT:OnIgnite`](#ent-onignite) | Documentation pending. |
| [`ENT:OnLandOnGround`](#ent-onlandonground) | Documentation pending. |
| [`ENT:OnLeaveGround`](#ent-onleaveground) | Documentation pending. |
| [`ENT:OnStairs`](#ent-onstairs) | Documentation pending. |
| [`ENT:OnTakeDamage`](#ent-ontakedamage) | Documentation pending. |
| [`ENT:PlayAgonyAnimations`](#ent-playagonyanimations) | wtf is happening here |
| [`ENT:PlayDamageAnimations`](#ent-playdamageanimations) | we gotta play the anims themselves |
| [`ENT:PlayDeathAnimations`](#ent-playdeathanimations) | Documentation pending. |
| [`ENT:PlayDuoSync`](#ent-playduosync) | Documentation pending. |
| [`ENT:PlayGuardingAnimations`](#ent-playguardinganimations) | Documentation pending. |
| [`ENT:PlayStairRolling`](#ent-playstairrolling) | Documentation pending. |
| [`ENT:PlayWallboundAnim`](#ent-playwallboundanim) | oldest function ever (2023 february) |
| [`ENT:ResetSyncEnts`](#ent-resetsyncents) | Documentation pending. |
| [`ENT:SendHactKey`](#ent-sendhactkey) | Documentation pending. |
| [`ENT:SendLastKey`](#ent-sendlastkey) | Documentation pending. |
| [`ENT:SetSolidLAD`](#ent-setsolidlad) | Documentation pending. |
| [`ENT:SetSyncAttacker`](#ent-setsyncattacker) | Documentation pending. |
| [`ENT:SetSyncVictim`](#ent-setsyncvictim) | Documentation pending. |
| [`ENT:StandUp`](#ent-standup) | Documentation pending. |
| [`ENT:TakeDamageLastAttacker`](#ent-takedamagelastattacker) | Documentation pending. |
| [`ENT:UpdateStun`](#ent-updatestun) | Documentation pending. |

<a id="ent-downedstandup"></a>
## `ENT:_DownedStandup`

<div class="api-badges"><span class="api-badge ">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_DownedStandup(part, dmg, dmgdir)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `part` | `any` | Not documented. |
| `dmg` | `any` | Not documented. |
| `dmgdir` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:2794</code>.</p>

<a id="ent-handledmganim"></a>
## `ENT:_HandleDMGAnim`

<div class="api-badges"><span class="api-badge ">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_HandleDMGAnim(status, anim, dmgdir, dmg, wallbound, wallboundtype, ragcycle, ragdur)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `status` | `any` | Not documented. |
| `anim` | `any` | Not documented. |
| `dmgdir` | `any` | Not documented. |
| `dmg` | `any` | Not documented. |
| `wallbound` | `any` | Not documented. |
| `wallboundtype` | `any` | Not documented. |
| `ragcycle` | `any` | Not documented. |
| `ragdur` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:2631</code>.</p>

<a id="ent-switchwbtype"></a>
## `ENT:_SwitchWBType`

<div class="api-badges"><span class="api-badge ">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_SwitchWBType(wbtype, ragdur)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `wbtype` | `any` | Not documented. |
| `ragdur` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:2448</code>.</p>

<a id="ent-aligntoslope"></a>
## `ENT:AlignToSlope`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:AlignToSlope(reset)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `reset` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:2496</code>.</p>

<a id="ent-antijuggleescape"></a>
## `ENT:AntiJuggleEscape`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:AntiJuggleEscape(dmgdir)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `dmgdir` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:1321</code>.</p>

<a id="ent-checkforwallbound"></a>
## `ENT:CheckForWallbound`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CheckForWallbound()
```

</div>

this is only supposed to be ran inside PSAM otherwise how the hell you gonna check fo that

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:293</code>.</p>

<a id="ent-checkguardbreakbeforedamage"></a>
## `ENT:CheckGuardBreakBeforeDamage`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CheckGuardBreakBeforeDamage(cond, dmg, dmgdir, bypassFlinch, damageOverride)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `cond` | `any` | Not documented. |
| `dmg` | `any` | Not documented. |
| `dmgdir` | `any` | Not documented. |
| `bypassFlinch` | `any` | Not documented. |
| `damageOverride` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:1187</code>.</p>

<a id="ent-checkjugglestate"></a>
## `ENT:CheckJuggleState`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CheckJuggleState()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:3265</code>.</p>

<a id="ent-checkwallboundstate"></a>
## `ENT:CheckWallboundState`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CheckWallboundState()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:3273</code>.</p>

<a id="ent-createparentedprop"></a>
## `ENT:CreateParentedProp`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CreateParentedProp(mdl, attach, pos, ang, skin)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `mdl` | `any` | Not documented. |
| `attach` | `any` | Not documented. |
| `pos` | `any` | Not documented. |
| `ang` | `any` | Not documented. |
| `skin` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:2879</code>.</p>

<a id="ent-customhandleanimevent"></a>
## `ENT:CustomHandleAnimEvent`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CustomHandleAnimEvent(event, _, _, _, key)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `event` | `any` | Not documented. |
| `_` | `any` | Not documented. |
| `_` | `any` | Not documented. |
| `_` | `any` | Not documented. |
| `key` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:291</code>.</p>

<a id="ent-customondealtdamage"></a>
## `ENT:CustomOnDealtDamage`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CustomOnDealtDamage(ent, dmg)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `ent` | `any` | Not documented. |
| `dmg` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:3250</code>.</p>

<a id="ent-damagedirection"></a>
## `ENT:DamageDirection`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:DamageDirection(dmg, legacy)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `dmg` | `any` | Not documented. |
| `legacy` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:801</code>.</p>

<a id="ent-deaththink"></a>
## `ENT:DeathThink`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:DeathThink()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:3686</code>.</p>

<a id="ent-downed"></a>
## `ENT:Downed`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:Downed(str, fatal)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `str` | `any` | Not documented. |
| `fatal` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:64</code>.</p>

<a id="ent-dropparentedprop"></a>
## `ENT:DropParentedProp`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:DropParentedProp(obj)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `obj` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:2895</code>.</p>

<a id="ent-foreigndmgguardingbehavior"></a>
## `ENT:ForeignDMGGuardingBehavior`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:ForeignDMGGuardingBehavior(dmg)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `dmg` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:725</code>.</p>

<a id="ent-getsyncattacker"></a>
## `ENT:GetSyncAttacker`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetSyncAttacker()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:3233</code>.</p>

<a id="ent-getsyncvictim"></a>
## `ENT:GetSyncVictim`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetSyncVictim()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:3241</code>.</p>

<a id="ent-handleanimevent"></a>
## `ENT:HandleAnimEvent`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:HandleAnimEvent(event, _, _, _, key)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `event` | `any` | Not documented. |
| `_` | `any` | Not documented. |
| `_` | `any` | Not documented. |
| `_` | `any` | Not documented. |
| `key` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:3744</code>.</p>

<a id="ent-handlebulletdamage"></a>
## `ENT:HandleBulletDamage`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:HandleBulletDamage(dmg, attacker)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `dmg` | `any` | Not documented. |
| `attacker` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:3341</code>.</p>

<a id="ent-juggle"></a>
## `ENT:Juggle`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:Juggle(ent, dmg)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `ent` | `any` | Not documented. |
| `dmg` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:3252</code>.</p>

<a id="ent-ondealtdamage"></a>
## `ENT:OnDealtDamage`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:OnDealtDamage(ent, dmg)
```

</div>

the beautiful damage feedback.

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `ent` | `any` | Not documented. |
| `dmg` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:869</code>.</p>

<a id="ent-ondeath"></a>
## `ENT:OnDeath`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:OnDeath(dmg, delay, hitgroup)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `dmg` | `any` | Not documented. |
| `delay` | `any` | Not documented. |
| `hitgroup` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:3593</code>.</p>

<a id="ent-onignite"></a>
## `ENT:OnIgnite`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:OnIgnite()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:2870</code>.</p>

<a id="ent-onlandonground"></a>
## `ENT:OnLandOnGround`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:OnLandOnGround()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:3309</code>.</p>

<a id="ent-onleaveground"></a>
## `ENT:OnLeaveGround`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:OnLeaveGround()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:3281</code>.</p>

<a id="ent-onstairs"></a>
## `ENT:OnStairs`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:OnStairs()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:2465</code>.</p>

<a id="ent-ontakedamage"></a>
## `ENT:OnTakeDamage`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:OnTakeDamage(dmg, hitgroup)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `dmg` | `any` | Not documented. |
| `hitgroup` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:538</code>.</p>

<a id="ent-playagonyanimations"></a>
## `ENT:PlayAgonyAnimations`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:PlayAgonyAnimations(str, bodypart, bodyrng)
```

</div>

wtf is happening here

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `str` | `any` | Not documented. |
| `bodypart` | `any` | Not documented. |
| `bodyrng` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:251</code>.</p>

<a id="ent-playdamageanimations"></a>
## `ENT:PlayDamageAnimations`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:PlayDamageAnimations(cond, dmg, dmgdir)
```

</div>

we gotta play the anims themselves

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `cond` | `any` | Not documented. |
| `dmg` | `any` | Not documented. |
| `dmgdir` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:1398</code>.</p>

<a id="ent-playdeathanimations"></a>
## `ENT:PlayDeathAnimations`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:PlayDeathAnimations(dmg, dmgdir)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `dmg` | `any` | Not documented. |
| `dmgdir` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:3551</code>.</p>

<a id="ent-playduosync"></a>
## `ENT:PlayDuoSync`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:PlayDuoSync(ent, sync, sync1, offset, ang, CanWallboundSync1, grabswitch, noENTreset, ragcycle, ragdur)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `ent` | `any` | Not documented. |
| `sync` | `any` | Not documented. |
| `sync1` | `any` | Not documented. |
| `offset` | `any` | Not documented. |
| `ang` | `any` | Not documented. |
| `CanWallboundSync1` | `any` | Not documented. |
| `grabswitch` | `any` | Not documented. |
| `noENTreset` | `any` | Not documented. |
| `ragcycle` | `any` | Not documented. |
| `ragdur` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:3031</code>.</p>

<a id="ent-playguardinganimations"></a>
## `ENT:PlayGuardingAnimations`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:PlayGuardingAnimations(cond, dmg, damageOverride)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `cond` | `any` | Not documented. |
| `dmg` | `any` | Not documented. |
| `damageOverride` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:1218</code>.</p>

<a id="ent-playstairrolling"></a>
## `ENT:PlayStairRolling`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:PlayStairRolling()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:2545</code>.</p>

<a id="ent-playwallboundanim"></a>
## `ENT:PlayWallboundAnim`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:PlayWallboundAnim(anim, dmg, ragcycle, ragdur)
```

</div>

oldest function ever (2023 february)

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `anim` | `any` | Not documented. |
| `dmg` | `any` | Not documented. |
| `ragcycle` | `any` | Not documented. |
| `ragdur` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:461</code>.</p>

<a id="ent-resetsyncents"></a>
## `ENT:ResetSyncEnts`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:ResetSyncEnts()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:3245</code>.</p>

<a id="ent-sendhactkey"></a>
## `ENT:SendHactKey`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:SendHactKey(key)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `key` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:3260</code>.</p>

<a id="ent-sendlastkey"></a>
## `ENT:SendLastKey`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:SendLastKey(key)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `key` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:3256</code>.</p>

<a id="ent-setsolidlad"></a>
## `ENT:SetSolidLAD`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:SetSolidLAD(solid)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `solid` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:3715</code>.</p>

<a id="ent-setsyncattacker"></a>
## `ENT:SetSyncAttacker`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:SetSyncAttacker(ent)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `ent` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:3229</code>.</p>

<a id="ent-setsyncvictim"></a>
## `ENT:SetSyncVictim`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:SetSyncVictim(ent)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `ent` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:3237</code>.</p>

<a id="ent-standup"></a>
## `ENT:StandUp`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:StandUp(str)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `str` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:179</code>.</p>

<a id="ent-takedamagelastattacker"></a>
## `ENT:TakeDamageLastAttacker`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:TakeDamageLastAttacker(damage, type)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `damage` | `any` | Not documented. |
| `type` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:3727</code>.</p>

<a id="ent-updatestun"></a>
## `ENT:UpdateStun`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:UpdateStun(ent, defcond, stuncond, mult, dmg)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `ent` | `any` | Not documented. |
| `defcond` | `any` | Not documented. |
| `stuncond` | `any` | Not documented. |
| `mult` | `any` | Not documented. |
| `dmg` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:2907</code>.</p>
