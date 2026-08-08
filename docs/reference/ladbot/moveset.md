# Moveset

Methods defined in `lua/entities/lad_framework_base/moveset.lua`.

!!! info "Generated reference"

    This page is generated from the current Lua source. Add API annotations
    above a method in the source file to improve its documentation.

## Methods

| Method | Summary |
| --- | --- |
| [`ENT:_ApplyMoveAnim`](#ent-applymoveanim) | Documentation pending. |
| [`ENT:_ApplyMoveAnimBlend`](#ent-applymoveanimblend) | Documentation pending. |
| [`ENT:_ApplyMoveLure`](#ent-applymovelure) | Documentation pending. |
| [`ENT:_ApplyMoveProperties`](#ent-applymoveproperties) | Documentation pending. |
| [`ENT:_ApplyMoveRecoverFast`](#ent-applymoverecoverfast) | Documentation pending. |
| [`ENT:_ApplyMoveSway`](#ent-applymovesway) | Documentation pending. |
| [`ENT:_ApplyMoveSyncHit`](#ent-applymovesynchit) | Documentation pending. |
| [`ENT:_ApplyMoveTags`](#ent-applymovetags) | Documentation pending. |
| [`ENT:_CleanupDynamicSlowDown`](#ent-cleanupdynamicslowdown) | Documentation pending. |
| [`ENT:_CleanupNodeSounds`](#ent-cleanupnodesounds) | Documentation pending. |
| [`ENT:_GetCachedMovesetData`](#ent-getcachedmovesetdata) | Documentation pending. |
| [`ENT:_StartDynamicSlowDown`](#ent-startdynamicslowdown) | Documentation pending. |
| [`ENT:AddUpgrade`](#ent-addupgrade) | Documentation pending. |
| [`ENT:CacheNodeFollowUps`](#ent-cachenodefollowups) | Documentation pending. |
| [`ENT:CheckConditions`](#ent-checkconditions) | Documentation pending. |
| [`ENT:CheckCustomConditions`](#ent-checkcustomconditions) | Documentation pending. |
| [`ENT:CheckIFrameState`](#ent-checkiframestate) | Documentation pending. |
| [`ENT:CheckRemoveButtonHoldCycle`](#ent-checkremovebuttonholdcycle) | Documentation pending. |
| [`ENT:ClearUpgrades`](#ent-clearupgrades) | Documentation pending. |
| [`ENT:ExecuteFollowUp`](#ent-executefollowup) | Documentation pending. |
| [`ENT:ExecuteMove`](#ent-executemove) | Documentation pending. |
| [`ENT:FindMatchingFollowUp`](#ent-findmatchingfollowup) | Documentation pending. |
| [`ENT:GetCurrentAnimCycle`](#ent-getcurrentanimcycle) | Documentation pending. |
| [`ENT:GetCurrentMoveNode`](#ent-getcurrentmovenode) | Documentation pending. |
| [`ENT:GetMoveName`](#ent-getmovename) | Documentation pending. |
| [`ENT:GetMoveName`](#ent-getmovename-2111) | Documentation pending. |
| [`ENT:GetMoveset`](#ent-getmoveset) | Documentation pending. |
| [`ENT:GetMoveset`](#ent-getmoveset-2121) | Documentation pending. |
| [`ENT:GetPlayerDir`](#ent-getplayerdir) | Documentation pending. |
| [`ENT:GetRelativeDirection`](#ent-getrelativedirection) | Documentation pending. |
| [`ENT:GetUpgrade`](#ent-getupgrade) | Documentation pending. |
| [`ENT:InvalidateMovesetCache`](#ent-invalidatemovesetcache) | Documentation pending. |
| [`ENT:MovesetEventThink`](#ent-moveseteventthink) | Documentation pending. |
| [`ENT:MovesetExists`](#ent-movesetexists) | Documentation pending. |
| [`ENT:PlayMovementDirAnimation`](#ent-playmovementdiranimation) | Documentation pending. |
| [`ENT:PrintNodeFollowUps`](#ent-printnodefollowups) | Documentation pending. |
| [`ENT:RecoverFast`](#ent-recoverfast) | Documentation pending. |
| [`ENT:ResetNodeParams`](#ent-resetnodeparams) | Documentation pending. |
| [`ENT:SetBusy`](#ent-setbusy) | Documentation pending. |
| [`ENT:SetFighterMoveset`](#ent-setfightermoveset) | Documentation pending. |
| [`ENT:SetNextMoveNode`](#ent-setnextmovenode) | Documentation pending. |
| [`ENT:SwayNoded`](#ent-swaynoded) | Documentation pending. |

<a id="ent-applymoveanim"></a>
## `ENT:_ApplyMoveAnim`

<div class="api-badges"><span class="api-badge ">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_ApplyMoveAnim(move, moveName, capturedGen, nodeAnimRate, AIFaceCycle, startDowned)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `move` | `any` | Not documented. |
| `moveName` | `any` | Not documented. |
| `capturedGen` | `any` | Not documented. |
| `nodeAnimRate` | `any` | Not documented. |
| `AIFaceCycle` | `any` | Not documented. |
| `startDowned` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:1529</code>.</p>

<a id="ent-applymoveanimblend"></a>
## `ENT:_ApplyMoveAnimBlend`

<div class="api-badges"><span class="api-badge ">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_ApplyMoveAnimBlend(move, moveName, capturedGen, nodeAnimRate)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `move` | `any` | Not documented. |
| `moveName` | `any` | Not documented. |
| `capturedGen` | `any` | Not documented. |
| `nodeAnimRate` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:1642</code>.</p>

<a id="ent-applymovelure"></a>
## `ENT:_ApplyMoveLure`

<div class="api-badges"><span class="api-badge ">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_ApplyMoveLure(move, moveName, capturedGen, nodeAnimRate, syncPos)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `move` | `any` | Not documented. |
| `moveName` | `any` | Not documented. |
| `capturedGen` | `any` | Not documented. |
| `nodeAnimRate` | `any` | Not documented. |
| `syncPos` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:1668</code>.</p>

<a id="ent-applymoveproperties"></a>
## `ENT:_ApplyMoveProperties`

<div class="api-badges"><span class="api-badge ">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_ApplyMoveProperties(move, moveName, nodeAnimRate)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `move` | `any` | Not documented. |
| `moveName` | `any` | Not documented. |
| `nodeAnimRate` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:1217</code>.</p>

<a id="ent-applymoverecoverfast"></a>
## `ENT:_ApplyMoveRecoverFast`

<div class="api-badges"><span class="api-badge ">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_ApplyMoveRecoverFast(move, moveName, capturedGen)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `move` | `any` | Not documented. |
| `moveName` | `any` | Not documented. |
| `capturedGen` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:1633</code>.</p>

<a id="ent-applymovesway"></a>
## `ENT:_ApplyMoveSway`

<div class="api-badges"><span class="api-badge ">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_ApplyMoveSway(move, moveName, capturedGen)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `move` | `any` | Not documented. |
| `moveName` | `any` | Not documented. |
| `capturedGen` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:1614</code>.</p>

<a id="ent-applymovesynchit"></a>
## `ENT:_ApplyMoveSyncHit`

<div class="api-badges"><span class="api-badge ">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_ApplyMoveSyncHit(move, syncPos, syncAng)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `move` | `any` | Not documented. |
| `syncPos` | `any` | Not documented. |
| `syncAng` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:1686</code>.</p>

<a id="ent-applymovetags"></a>
## `ENT:_ApplyMoveTags`

<div class="api-badges"><span class="api-badge ">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_ApplyMoveTags(move)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `move` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:1494</code>.</p>

<a id="ent-cleanupdynamicslowdown"></a>
## `ENT:_CleanupDynamicSlowDown`

<div class="api-badges"><span class="api-badge ">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_CleanupDynamicSlowDown(completed)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `completed` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:1960</code>.</p>

<a id="ent-cleanupnodesounds"></a>
## `ENT:_CleanupNodeSounds`

<div class="api-badges"><span class="api-badge ">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_CleanupNodeSounds(moveName)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `moveName` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:1474</code>.</p>

<a id="ent-getcachedmovesetdata"></a>
## `ENT:_GetCachedMovesetData`

<div class="api-badges"><span class="api-badge ">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_GetCachedMovesetData(ms)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `ms` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:172</code>.</p>

<a id="ent-startdynamicslowdown"></a>
## `ENT:_StartDynamicSlowDown`

<div class="api-badges"><span class="api-badge ">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_StartDynamicSlowDown()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:1905</code>.</p>

<a id="ent-addupgrade"></a>
## `ENT:AddUpgrade`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:AddUpgrade(upgrade)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `upgrade` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:2022</code>.</p>

<a id="ent-cachenodefollowups"></a>
## `ENT:CacheNodeFollowUps`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CacheNodeFollowUps(secondaryMoveTable)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `secondaryMoveTable` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:640</code>.</p>

<a id="ent-checkconditions"></a>
## `ENT:CheckConditions`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CheckConditions(conditions, ply, input)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `conditions` | `any` | Not documented. |
| `ply` | `any` | Not documented. |
| `input` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:692</code>.</p>

<a id="ent-checkcustomconditions"></a>
## `ENT:CheckCustomConditions`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CheckCustomConditions()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:971</code>.</p>

<a id="ent-checkiframestate"></a>
## `ENT:CheckIFrameState`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CheckIFrameState()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:1976</code>.</p>

<a id="ent-checkremovebuttonholdcycle"></a>
## `ENT:CheckRemoveButtonHoldCycle`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CheckRemoveButtonHoldCycle()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:1989</code>.</p>

<a id="ent-clearupgrades"></a>
## `ENT:ClearUpgrades`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:ClearUpgrades()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:2037</code>.</p>

<a id="ent-executefollowup"></a>
## `ENT:ExecuteFollowUp`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:ExecuteFollowUp(moveToExecute)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `moveToExecute` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:1017</code>.</p>

<a id="ent-executemove"></a>
## `ENT:ExecuteMove`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:ExecuteMove(moveName, options)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `moveName` | `any` | Not documented. |
| `options` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:1043</code>.</p>

<a id="ent-findmatchingfollowup"></a>
## `ENT:FindMatchingFollowUp`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:FindMatchingFollowUp(input, ply)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `input` | `any` | Not documented. |
| `ply` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:982</code>.</p>

<a id="ent-getcurrentanimcycle"></a>
## `ENT:GetCurrentAnimCycle`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetCurrentAnimCycle()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:2008</code>.</p>

<a id="ent-getcurrentmovenode"></a>
## `ENT:GetCurrentMoveNode`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetCurrentMoveNode()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:71</code>.</p>

<a id="ent-getmovename"></a>
## `ENT:GetMoveName`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetMoveName()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:2046</code>.</p>

<a id="ent-getmovename-2111"></a>
## `ENT:GetMoveName`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetMoveName()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:2111</code>.</p>

<a id="ent-getmoveset"></a>
## `ENT:GetMoveset`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetMoveset()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:2042</code>.</p>

<a id="ent-getmoveset-2121"></a>
## `ENT:GetMoveset`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetMoveset()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:2121</code>.</p>

<a id="ent-getplayerdir"></a>
## `ENT:GetPlayerDir`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetPlayerDir(ply)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `ply` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:105</code>.</p>

<a id="ent-getrelativedirection"></a>
## `ENT:GetRelativeDirection`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetRelativeDirection(direction, nextbot)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `direction` | `any` | Not documented. |
| `nextbot` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:79</code>.</p>

<a id="ent-getupgrade"></a>
## `ENT:GetUpgrade`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetUpgrade(upgrade)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `upgrade` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:2013</code>.</p>

<a id="ent-invalidatemovesetcache"></a>
## `ENT:InvalidateMovesetCache`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:InvalidateMovesetCache(ms)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `ms` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:188</code>.</p>

<a id="ent-moveseteventthink"></a>
## `ENT:MovesetEventThink`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:MovesetEventThink()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:2103</code>.</p>

<a id="ent-movesetexists"></a>
## `ENT:MovesetExists`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:MovesetExists(ms)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `ms` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:2003</code>.</p>

<a id="ent-playmovementdiranimation"></a>
## `ENT:PlayMovementDirAnimation`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:PlayMovementDirAnimation(tbl, animOptions)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `tbl` | `any` | Not documented. |
| `animOptions` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:2054</code>.</p>

<a id="ent-printnodefollowups"></a>
## `ENT:PrintNodeFollowUps`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:PrintNodeFollowUps(moveName)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `moveName` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:1719</code>.</p>

<a id="ent-recoverfast"></a>
## `ENT:RecoverFast`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:RecoverFast(tbl)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `tbl` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:2094</code>.</p>

<a id="ent-resetnodeparams"></a>
## `ENT:ResetNodeParams`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:ResetNodeParams(fromMove, capturedGen)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `fromMove` | `any` | Not documented. |
| `capturedGen` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:1835</code>.</p>

<a id="ent-setbusy"></a>
## `ENT:SetBusy`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:SetBusy(busy)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `busy` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:153</code>.</p>

<a id="ent-setfightermoveset"></a>
## `ENT:SetFighterMoveset`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:SetFighterMoveset(ms, hasSwitched, isWeaponMoveset, isHiddenWeapon, stool, grabsync, skipSwitchAnim)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `ms` | `any` | Not documented. |
| `hasSwitched` | `any` | Not documented. |
| `isWeaponMoveset` | `any` | Not documented. |
| `isHiddenWeapon` | `any` | Not documented. |
| `stool` | `any` | Not documented. |
| `grabsync` | `any` | Not documented. |
| `skipSwitchAnim` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:212</code>.</p>

<a id="ent-setnextmovenode"></a>
## `ENT:SetNextMoveNode`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:SetNextMoveNode(nodeName)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `nodeName` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:128</code>.</p>

<a id="ent-swaynoded"></a>
## `ENT:SwayNoded`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:SwayNoded(tbl, animOptions)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `tbl` | `any` | Not documented. |
| `animOptions` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:2086</code>.</p>
