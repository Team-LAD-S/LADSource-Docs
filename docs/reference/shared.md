# Shared

Methods defined in `lua/entities/lad_framework_base/shared.lua`.

!!! info "Generated reference"

    This page is generated from the current Lua source. Add API annotations
    above a method in the source file to improve its documentation.

## Methods

| Method | Summary |
| --- | --- |
| [`ENT:_FindVoidRecoveryPos`](#ent-findvoidrecoverypos) | Documentation pending. |
| [`ENT:_InitDebugText`](#ent-initdebugtext) | Documentation pending. |
| [`ENT:_InitMaterials`](#ent-initmaterials) | Documentation pending. |
| [`ENT:_ShouldRecoverFromVoid`](#ent-shouldrecoverfromvoid) | Documentation pending. |
| [`ENT:BumpAnim`](#ent-bumpanim) | Documentation pending. |
| [`ENT:CICO`](#ent-cico) | Documentation pending. |
| [`ENT:CICO`](#ent-cico-1433) | clientside CICO |
| [`ENT:CreateDirectionCompass`](#ent-createdirectioncompass) | Documentation pending. |
| [`ENT:CustomDraw`](#ent-customdraw) | Documentation pending. |
| [`ENT:CustomInitialize`](#ent-custominitialize) | Documentation pending. |
| [`ENT:CustomInitialize`](#ent-custominitialize-1480) | Documentation pending. |
| [`ENT:CustomThink`](#ent-customthink) | Documentation pending. |
| [`ENT:CustomThink`](#ent-customthink-1495) | Documentation pending. |
| [`ENT:DebugDrawCone`](#ent-debugdrawcone) | Documentation pending. |
| [`ENT:GetPlayerColor`](#ent-getplayercolor) | Documentation pending. |
| [`ENT:IsPropLeftOrRight`](#ent-ispropleftorright) | Documentation pending. |
| [`ENT:LoadData`](#ent-loaddata) | Documentation pending. |
| [`ENT:Multithread`](#ent-multithread) | Trust me, this works, you just haven't seen it used all that much yet |
| [`ENT:OnAvoidEnemy`](#ent-onavoidenemy) | Documentation pending. |
| [`ENT:OnChaseEnemy`](#ent-onchaseenemy) | Documentation pending. |
| [`ENT:OnContact`](#ent-oncontact) | Documentation pending. |
| [`ENT:OnDispossessed`](#ent-ondispossessed) | Documentation pending. |
| [`ENT:OnDowned`](#ent-ondowned) | Documentation pending. |
| [`ENT:OnFatalDamage`](#ent-onfataldamage) | Documentation pending. |
| [`ENT:OnIdle`](#ent-onidle) | Documentation pending. |
| [`ENT:OnPatrolling`](#ent-onpatrolling) | Documentation pending. |
| [`ENT:OnPatrolUnreachable`](#ent-onpatrolunreachable) | Documentation pending. |
| [`ENT:OnReachedPatrol`](#ent-onreachedpatrol) | Documentation pending. |
| [`ENT:OnRemove`](#ent-onremove) | Documentation pending. |
| [`ENT:OnRemove`](#ent-onremove-1500) | Documentation pending. |
| [`ENT:OnSpawn`](#ent-onspawn) | Documentation pending. |
| [`ENT:OnTookDamage`](#ent-ontookdamage) | Documentation pending. |
| [`ENT:PlayBumpAnimation`](#ent-playbumpanimation) | Documentation pending. |
| [`ENT:RecoverFromVoid`](#ent-recoverfromvoid) | Documentation pending. |
| [`ENT:SetNexbotColor`](#ent-setnexbotcolor) | Documentation pending. |
| [`ENT:ShouldIgnore`](#ent-shouldignore) | Documentation pending. |
| [`ENT:UpdateTransmitState`](#ent-updatetransmitstate) | fixes the attachment point bullshit |

<a id="ent-findvoidrecoverypos"></a>
## `ENT:_FindVoidRecoveryPos`

<div class="api-badges"><span class="api-badge ">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_FindVoidRecoveryPos(origin)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `origin` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:636</code>.</p>

<a id="ent-initdebugtext"></a>
## `ENT:_InitDebugText`

<div class="api-badges"><span class="api-badge ">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_InitDebugText()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:1454</code>.</p>

<a id="ent-initmaterials"></a>
## `ENT:_InitMaterials`

<div class="api-badges"><span class="api-badge ">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_InitMaterials()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:1488</code>.</p>

<a id="ent-shouldrecoverfromvoid"></a>
## `ENT:_ShouldRecoverFromVoid`

<div class="api-badges"><span class="api-badge ">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_ShouldRecoverFromVoid()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:688</code>.</p>

<a id="ent-bumpanim"></a>
## `ENT:BumpAnim`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:BumpAnim(ent)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `ent` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:1047</code>.</p>

<a id="ent-cico"></a>
## `ENT:CICO`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CICO(callback)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `callback` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:591</code>.</p>

<a id="ent-cico-1433"></a>
## `ENT:CICO`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CICO(callback)
```

</div>

clientside CICO

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `callback` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:1433</code>.</p>

<a id="ent-createdirectioncompass"></a>
## `ENT:CreateDirectionCompass`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CreateDirectionCompass()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:1349</code>.</p>

<a id="ent-customdraw"></a>
## `ENT:CustomDraw`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CustomDraw()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:1515</code>.</p>

<a id="ent-custominitialize"></a>
## `ENT:CustomInitialize`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CustomInitialize()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:242</code>.</p>

<a id="ent-custominitialize-1480"></a>
## `ENT:CustomInitialize`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CustomInitialize()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:1480</code>.</p>

<a id="ent-customthink"></a>
## `ENT:CustomThink`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CustomThink()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:774</code>.</p>

<a id="ent-customthink-1495"></a>
## `ENT:CustomThink`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CustomThink()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:1495</code>.</p>

<a id="ent-debugdrawcone"></a>
## `ENT:DebugDrawCone`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:DebugDrawCone(origin, direction, angle, range, segments, duration, color)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `origin` | `any` | Not documented. |
| `direction` | `any` | Not documented. |
| `angle` | `any` | Not documented. |
| `range` | `any` | Not documented. |
| `segments` | `any` | Not documented. |
| `duration` | `any` | Not documented. |
| `color` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:613</code>.</p>

<a id="ent-getplayercolor"></a>
## `ENT:GetPlayerColor`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetPlayerColor()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:1523</code>.</p>

<a id="ent-ispropleftorright"></a>
## `ENT:IsPropLeftOrRight`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:IsPropLeftOrRight(prop)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `prop` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:567</code>.</p>

<a id="ent-loaddata"></a>
## `ENT:LoadData`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:LoadData(type, id)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `type` | `any` | Not documented. |
| `id` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:1361</code>.</p>

<a id="ent-multithread"></a>
## `ENT:Multithread`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:Multithread(funcs)
```

</div>

Trust me, this works, you just haven't seen it used all that much yet

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `funcs` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:745</code>.</p>

<a id="ent-onavoidenemy"></a>
## `ENT:OnAvoidEnemy`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:OnAvoidEnemy(enemy)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `enemy` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:1020</code>.</p>

<a id="ent-onchaseenemy"></a>
## `ENT:OnChaseEnemy`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:OnChaseEnemy(enemy)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `enemy` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:1010</code>.</p>

<a id="ent-oncontact"></a>
## `ENT:OnContact`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:OnContact(ent)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `ent` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:1022</code>.</p>

<a id="ent-ondispossessed"></a>
## `ENT:OnDispossessed`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:OnDispossessed(ply)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `ply` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:1238</code>.</p>

<a id="ent-ondowned"></a>
## `ENT:OnDowned`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:OnDowned(dmg, hitgroup)
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

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:1147</code>.</p>

<a id="ent-onfataldamage"></a>
## `ENT:OnFatalDamage`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:OnFatalDamage(dmg, hitgroup)
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

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:1142</code>.</p>

<a id="ent-onidle"></a>
## `ENT:OnIdle`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:OnIdle()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:1118</code>.</p>

<a id="ent-onpatrolling"></a>
## `ENT:OnPatrolling`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:OnPatrolling(pos)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `pos` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:1128</code>.</p>

<a id="ent-onpatrolunreachable"></a>
## `ENT:OnPatrolUnreachable`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:OnPatrolUnreachable(pos)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `pos` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:1124</code>.</p>

<a id="ent-onreachedpatrol"></a>
## `ENT:OnReachedPatrol`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:OnReachedPatrol(pos)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `pos` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:1113</code>.</p>

<a id="ent-onremove"></a>
## `ENT:OnRemove`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:OnRemove()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:1149</code>.</p>

<a id="ent-onremove-1500"></a>
## `ENT:OnRemove`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:OnRemove()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:1500</code>.</p>

<a id="ent-onspawn"></a>
## `ENT:OnSpawn`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:OnSpawn()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:1134</code>.</p>

<a id="ent-ontookdamage"></a>
## `ENT:OnTookDamage`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:OnTookDamage(dmg, hitgroup)
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

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:1145</code>.</p>

<a id="ent-playbumpanimation"></a>
## `ENT:PlayBumpAnimation`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:PlayBumpAnimation(anim)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `anim` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:1101</code>.</p>

<a id="ent-recoverfromvoid"></a>
## `ENT:RecoverFromVoid`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:RecoverFromVoid()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:730</code>.</p>

<a id="ent-setnexbotcolor"></a>
## `ENT:SetNexbotColor`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:SetNexbotColor()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:1519</code>.</p>

<a id="ent-shouldignore"></a>
## `ENT:ShouldIgnore`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:ShouldIgnore(ent)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `ent` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:1014</code>.</p>

<a id="ent-updatetransmitstate"></a>
## `ENT:UpdateTransmitState`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:UpdateTransmitState()
```

</div>

fixes the attachment point bullshit

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:587</code>.</p>
