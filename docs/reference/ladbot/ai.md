# AI

Methods defined in `lua/entities/lad_framework_base/ai.lua`.

!!! info "Generated reference"

    This page is generated from the current Lua source. Add API annotations
    above a method in the source file to improve its documentation.

## Methods

| Method | Summary |
| --- | --- |
| [`ENT:AIAttemptReload`](#ent-aiattemptreload) | Documentation pending. |
| [`ENT:AICheckEnemyWeaponClass`](#ent-aicheckenemyweaponclass) | Documentation pending. |
| [`ENT:AICheckObstacles`](#ent-aicheckobstacles) | Documentation pending. |
| [`ENT:AIDefaultAttackRoutine`](#ent-aidefaultattackroutine) | Documentation pending. |
| [`ENT:AIDefaultFlinchAttack`](#ent-aidefaultflinchattack) | Documentation pending. |
| [`ENT:AIDefaultGuardAction`](#ent-aidefaultguardaction) | Documentation pending. |
| [`ENT:AIDefaultGuardAttack`](#ent-aidefaultguardattack) | Documentation pending. |
| [`ENT:AIDefaultRangeAttackRoutine`](#ent-aidefaultrangeattackroutine) | Documentation pending. |
| [`ENT:AIDefaultRecoverFast`](#ent-aidefaultrecoverfast) | Documentation pending. |
| [`ENT:AIDefaultStrafingRoutine`](#ent-aidefaultstrafingroutine) | Documentation pending. |
| [`ENT:AIDefaultSwayGuardRoutine`](#ent-aidefaultswayguardroutine) | Documentation pending. |
| [`ENT:AIFaceEnemy`](#ent-aifaceenemy) | Documentation pending. |
| [`ENT:AIFlinchReGuard`](#ent-aiflinchreguard) | Documentation pending. |
| [`ENT:AIForceEnemyMovesetActivation`](#ent-aiforceenemymovesetactivation) | Documentation pending. |
| [`ENT:AIGrabAttackRoutine`](#ent-aigrabattackroutine) | Documentation pending. |
| [`ENT:AIGrabMovementRoutine`](#ent-aigrabmovementroutine) | Documentation pending. |
| [`ENT:AIHactBBoxAvoidance`](#ent-aihactbboxavoidance) | Documentation pending. |
| [`ENT:AILoopFar`](#ent-ailoopfar) | Documentation pending. |
| [`ENT:AILoopNear`](#ent-ailoopnear) | Documentation pending. |
| [`ENT:AIManageAnger`](#ent-aimanageanger) | Documentation pending. |
| [`ENT:AIManageBravery`](#ent-aimanagebravery) | Documentation pending. |
| [`ENT:AIManageTauntAnger`](#ent-aimanagetauntanger) | Documentation pending. |
| [`ENT:AINodedComboThink`](#ent-ainodedcombothink) | Documentation pending. |
| [`ENT:AINodeExecute`](#ent-ainodeexecute) | Documentation pending. |
| [`ENT:AIOpenDoors`](#ent-aiopendoors) | Documentation pending. |
| [`ENT:AIRunAttackRoutine`](#ent-airunattackroutine) | Documentation pending. |
| [`ENT:AIScanAndExecuteHacts`](#ent-aiscanandexecutehacts) | Documentation pending. |
| [`ENT:AIWeaponThrowRoutine`](#ent-aiweaponthrowroutine) | Documentation pending. |
| [`ENT:BattleAILoopFar`](#ent-battleailoopfar) | override this function in your ladbot to make custom battle AI (when farther away from enemy) |
| [`ENT:BattleAILoopNear`](#ent-battleailoopnear) | override this function in your ladbot to make custom battle AI (when close to the enemy) |
| [`ENT:FindNearbyAlliesInCombat`](#ent-findnearbyalliesincombat) | find nearby Nextbots of the same type |
| [`ENT:GetEncirclementStrafeBias`](#ent-getencirclementstrafebias) | Documentation pending. |
| [`ENT:GetSwayFrequency`](#ent-getswayfrequency) | Documentation pending. |
| [`ENT:GetSwayNextAttack`](#ent-getswaynextattack) | Documentation pending. |
| [`ENT:GoToWall`](#ent-gotowall) | Documentation pending. |
| [`ENT:GoToWeapon`](#ent-gotoweapon) | Documentation pending. |
| [`ENT:OnLastEnemy`](#ent-onlastenemy) | Documentation pending. |
| [`ENT:ScanForNearestWallAndJump`](#ent-scanfornearestwallandjump) | Documentation pending. |
| [`ENT:ScanForNearestWeaponAndMove`](#ent-scanfornearestweaponandmove) | Documentation pending. |
| [`ENT:SetNextAttack`](#ent-setnextattack) | Documentation pending. |

<a id="ent-aiattemptreload"></a>
## `ENT:AIAttemptReload`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:AIAttemptReload()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:1481</code>.</p>

<a id="ent-aicheckenemyweaponclass"></a>
## `ENT:AICheckEnemyWeaponClass`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:AICheckEnemyWeaponClass(enemy)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `enemy` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:1419</code>.</p>

<a id="ent-aicheckobstacles"></a>
## `ENT:AICheckObstacles`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:AICheckObstacles()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:573</code>.</p>

<a id="ent-aidefaultattackroutine"></a>
## `ENT:AIDefaultAttackRoutine`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:AIDefaultAttackRoutine(enemy)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `enemy` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:1101</code>.</p>

<a id="ent-aidefaultflinchattack"></a>
## `ENT:AIDefaultFlinchAttack`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:AIDefaultFlinchAttack(enemy)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `enemy` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:1374</code>.</p>

<a id="ent-aidefaultguardaction"></a>
## `ENT:AIDefaultGuardAction`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:AIDefaultGuardAction(enemy)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `enemy` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:1350</code>.</p>

<a id="ent-aidefaultguardattack"></a>
## `ENT:AIDefaultGuardAttack`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:AIDefaultGuardAttack(enemy)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `enemy` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:1338</code>.</p>

<a id="ent-aidefaultrangeattackroutine"></a>
## `ENT:AIDefaultRangeAttackRoutine`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:AIDefaultRangeAttackRoutine(enemy)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `enemy` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:1055</code>.</p>

<a id="ent-aidefaultrecoverfast"></a>
## `ENT:AIDefaultRecoverFast`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:AIDefaultRecoverFast(enemy)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `enemy` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:1362</code>.</p>

<a id="ent-aidefaultstrafingroutine"></a>
## `ENT:AIDefaultStrafingRoutine`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:AIDefaultStrafingRoutine(enemy)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `enemy` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:914</code>.</p>

<a id="ent-aidefaultswayguardroutine"></a>
## `ENT:AIDefaultSwayGuardRoutine`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:AIDefaultSwayGuardRoutine(enemy)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `enemy` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:764</code>.</p>

<a id="ent-aifaceenemy"></a>
## `ENT:AIFaceEnemy`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:AIFaceEnemy(enemy)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `enemy` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:671</code>.</p>

<a id="ent-aiflinchreguard"></a>
## `ENT:AIFlinchReGuard`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:AIFlinchReGuard()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:850</code>.</p>

<a id="ent-aiforceenemymovesetactivation"></a>
## `ENT:AIForceEnemyMovesetActivation`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:AIForceEnemyMovesetActivation(enemy)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `enemy` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:648</code>.</p>

<a id="ent-aigrabattackroutine"></a>
## `ENT:AIGrabAttackRoutine`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:AIGrabAttackRoutine(enemy)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `enemy` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:681</code>.</p>

<a id="ent-aigrabmovementroutine"></a>
## `ENT:AIGrabMovementRoutine`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:AIGrabMovementRoutine(enemy)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `enemy` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:699</code>.</p>

<a id="ent-aihactbboxavoidance"></a>
## `ENT:AIHactBBoxAvoidance`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:AIHactBBoxAvoidance()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:414</code>.</p>

<a id="ent-ailoopfar"></a>
## `ENT:AILoopFar`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:AILoopFar(enemy)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `enemy` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:405</code>.</p>

<a id="ent-ailoopnear"></a>
## `ENT:AILoopNear`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:AILoopNear(enemy)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `enemy` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:399</code>.</p>

<a id="ent-aimanageanger"></a>
## `ENT:AIManageAnger`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:AIManageAnger(enemy, ftype)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `enemy` | `any` | Not documented. |
| `ftype` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:624</code>.</p>

<a id="ent-aimanagebravery"></a>
## `ENT:AIManageBravery`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:AIManageBravery(enemy, cof, ftype)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `enemy` | `any` | Not documented. |
| `cof` | `any` | Not documented. |
| `ftype` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:634</code>.</p>

<a id="ent-aimanagetauntanger"></a>
## `ENT:AIManageTauntAnger`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:AIManageTauntAnger(enemy, cof, ftype)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `enemy` | `any` | Not documented. |
| `cof` | `any` | Not documented. |
| `ftype` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:614</code>.</p>

<a id="ent-ainodedcombothink"></a>
## `ENT:AINodedComboThink`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:AINodedComboThink()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:192</code>.</p>

<a id="ent-ainodeexecute"></a>
## `ENT:AINodeExecute`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:AINodeExecute(nodeType)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `nodeType` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:322</code>.</p>

<a id="ent-aiopendoors"></a>
## `ENT:AIOpenDoors`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:AIOpenDoors(door)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `door` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:560</code>.</p>

<a id="ent-airunattackroutine"></a>
## `ENT:AIRunAttackRoutine`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:AIRunAttackRoutine(enemy, mincof, cof)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `enemy` | `any` | Not documented. |
| `mincof` | `any` | Not documented. |
| `cof` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:1400</code>.</p>

<a id="ent-aiscanandexecutehacts"></a>
## `ENT:AIScanAndExecuteHacts`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:AIScanAndExecuteHacts()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:661</code>.</p>

<a id="ent-aiweaponthrowroutine"></a>
## `ENT:AIWeaponThrowRoutine`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:AIWeaponThrowRoutine(enemy, cof)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `enemy` | `any` | Not documented. |
| `cof` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:1389</code>.</p>

<a id="ent-battleailoopfar"></a>
## `ENT:BattleAILoopFar`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:BattleAILoopFar(enemy)
```

</div>

override this function in your ladbot to make custom battle AI (when farther away from enemy)

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `enemy` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:526</code>.</p>

<a id="ent-battleailoopnear"></a>
## `ENT:BattleAILoopNear`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:BattleAILoopNear(enemy)
```

</div>

override this function in your ladbot to make custom battle AI (when close to the enemy)

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `enemy` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:489</code>.</p>

<a id="ent-findnearbyalliesincombat"></a>
## `ENT:FindNearbyAlliesInCombat`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:FindNearbyAlliesInCombat(radius)
```

</div>

find nearby Nextbots of the same type

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `radius` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:1071</code>.</p>

<a id="ent-getencirclementstrafebias"></a>
## `ENT:GetEncirclementStrafeBias`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetEncirclementStrafeBias(enemy)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `enemy` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:871</code>.</p>

<a id="ent-getswayfrequency"></a>
## `ENT:GetSwayFrequency`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetSwayFrequency()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:831</code>.</p>

<a id="ent-getswaynextattack"></a>
## `ENT:GetSwayNextAttack`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetSwayNextAttack()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:843</code>.</p>

<a id="ent-gotowall"></a>
## `ENT:GoToWall`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GoToWall(pos, tolerance, callback)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `pos` | `any` | Not documented. |
| `tolerance` | `any` | Not documented. |
| `callback` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:1585</code>.</p>

<a id="ent-gotoweapon"></a>
## `ENT:GoToWeapon`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GoToWeapon(pos, tolerance, callback)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `pos` | `any` | Not documented. |
| `tolerance` | `any` | Not documented. |
| `callback` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:1499</code>.</p>

<a id="ent-onlastenemy"></a>
## `ENT:OnLastEnemy`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:OnLastEnemy(enemy)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `enemy` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:1627</code>.</p>

<a id="ent-scanfornearestwallandjump"></a>
## `ENT:ScanForNearestWallAndJump`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:ScanForNearestWallAndJump()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:1546</code>.</p>

<a id="ent-scanfornearestweaponandmove"></a>
## `ENT:ScanForNearestWeaponAndMove`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:ScanForNearestWeaponAndMove()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:1450</code>.</p>

<a id="ent-setnextattack"></a>
## `ENT:SetNextAttack`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:SetNextAttack(min, max)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `min` | `any` | Not documented. |
| `max` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:1433</code>.</p>
