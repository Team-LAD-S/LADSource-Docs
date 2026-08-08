# HACT

Methods defined in `lua/entities/lad_framework_base/hact.lua`.

!!! info "Generated reference"

    This page is generated from the current Lua source. Add API annotations
    above a method in the source file to improve its documentation.

## Methods

| Method | Summary |
| --- | --- |
| [`ENT:AbortHact`](#ent-aborthact) | Documentation pending. |
| [`ENT:AddHeat`](#ent-addheat) | Documentation pending. |
| [`ENT:CacheAvailableHacts`](#ent-cacheavailablehacts) | Documentation pending. |
| [`ENT:CanForcePositionToNearestWall`](#ent-canforcepositiontonearestwall) | Documentation pending. |
| [`ENT:CleanupHactViewState`](#ent-cleanuphactviewstate) | Documentation pending. |
| [`ENT:ConsumeHeat`](#ent-consumeheat) | Documentation pending. |
| [`ENT:DeductHeat`](#ent-deductheat) | Documentation pending. |
| [`ENT:DetectEnvironment`](#ent-detectenvironment) | Documentation pending. |
| [`ENT:EndHact`](#ent-endhact) | Documentation pending. |
| [`ENT:EndHactViews`](#ent-endhactviews) | Documentation pending. |
| [`ENT:ExecuteHact`](#ent-executehact) | Documentation pending. |
| [`ENT:FindNearestNavWall`](#ent-findnearestnavwall) | Documentation pending. |
| [`ENT:FindSafePosition`](#ent-findsafeposition) | Documentation pending. |
| [`ENT:ForcePositionToNearestWall`](#ent-forcepositiontonearestwall) | Documentation pending. |
| [`ENT:GetAvailableHactActions`](#ent-getavailablehactactions) | Documentation pending. |
| [`ENT:GetBlueHeatBarCount`](#ent-getblueheatbarcount) | Documentation pending. |
| [`ENT:GetBlueHeatBarValue`](#ent-getblueheatbarvalue) | Documentation pending. |
| [`ENT:GetCurrentHeatGear`](#ent-getcurrentheatgear) | Documentation pending. |
| [`ENT:GetForcePositionToWallCandidate`](#ent-getforcepositiontowallcandidate) | Documentation pending. |
| [`ENT:GetForcePositionToWallSearchParams`](#ent-getforcepositiontowallsearchparams) | Documentation pending. |
| [`ENT:GetHact`](#ent-gethact) | Documentation pending. |
| [`ENT:GetHactCameraDataEntry`](#ent-gethactcameradataentry) | Documentation pending. |
| [`ENT:GetHactCamPos`](#ent-gethactcampos) | Documentation pending. |
| [`ENT:GetHactFrameProgressionEntry`](#ent-gethactframeprogressionentry) | Documentation pending. |
| [`ENT:GetHeat`](#ent-getheat) | Documentation pending. |
| [`ENT:GetHeatGearCount`](#ent-getheatgearcount) | Documentation pending. |
| [`ENT:GetHeatGearForAmount`](#ent-getheatgearforamount) | Documentation pending. |
| [`ENT:GetHeatSystemType`](#ent-getheatsystemtype) | Documentation pending. |
| [`ENT:GetMaxHeat`](#ent-getmaxheat) | Documentation pending. |
| [`ENT:GetNetworkedBlueHeatBarCount`](#ent-getnetworkedblueheatbarcount) | Documentation pending. |
| [`ENT:GetNetworkedBlueHeatBarValue`](#ent-getnetworkedblueheatbarvalue) | Documentation pending. |
| [`ENT:GetNetworkedHeat`](#ent-getnetworkedheat) | Documentation pending. |
| [`ENT:GetNetworkedHeatGearCount`](#ent-getnetworkedheatgearcount) | Documentation pending. |
| [`ENT:GetNetworkedHeatSystemType`](#ent-getnetworkedheatsystemtype) | Documentation pending. |
| [`ENT:GetNetworkedRedHeatBarCount`](#ent-getnetworkedredheatbarcount) | Documentation pending. |
| [`ENT:GetRedHeatAmount`](#ent-getredheatamount) | Documentation pending. |
| [`ENT:GetRedHeatBarCount`](#ent-getredheatbarcount) | Documentation pending. |
| [`ENT:GetRedHeatStart`](#ent-getredheatstart) | Documentation pending. |
| [`ENT:GetWallHactFaceAwayFromWall`](#ent-getwallhactfaceawayfromwall) | Documentation pending. |
| [`ENT:GetWallHactReferenceEntity`](#ent-getwallhactreferenceentity) | Documentation pending. |
| [`ENT:HactBridge`](#ent-hactbridge) | Documentation pending. |
| [`ENT:HactBridgeTo`](#ent-hactbridgeto) | Documentation pending. |
| [`ENT:HactExists`](#ent-hactexists) | Documentation pending. |
| [`ENT:HactFOVEvent`](#ent-hactfovevent) | Documentation pending. |
| [`ENT:HeatPopBehavior`](#ent-heatpopbehavior) | Documentation pending. |
| [`ENT:HeatThink`](#ent-heatthink) | Documentation pending. |
| [`ENT:IsFrozenProp`](#ent-isfrozenprop) | Documentation pending. |
| [`ENT:IsInRedHeat`](#ent-isinredheat) | Documentation pending. |
| [`ENT:LAD_HactEventFramesHasKey`](#ent-lad-hacteventframeshaskey) | Documentation pending. |
| [`ENT:LAD_HactEventFramesUseDamageEvents`](#ent-lad-hacteventframesusedamageevents) | Documentation pending. |
| [`ENT:LAD_ShouldSuppressHactModelEvent`](#ent-lad-shouldsuppresshactmodelevent) | Documentation pending. |
| [`ENT:PlayDynamicIntro`](#ent-playdynamicintro) | Documentation pending. |
| [`ENT:PlayLocalSound`](#ent-playlocalsound) | Documentation pending. |
| [`ENT:PlayVictimHact`](#ent-playvictimhact) | Documentation pending. |
| [`ENT:PopHeat`](#ent-popheat) | Documentation pending. |
| [`ENT:PosToWall`](#ent-postowall) | Documentation pending. |
| [`ENT:RefreshHactBridgeViewers`](#ent-refreshhactbridgeviewers) | Documentation pending. |
| [`ENT:RemoveHeatAura`](#ent-removeheataura) | Documentation pending. |
| [`ENT:ResetHactEventFrames`](#ent-resethacteventframes) | Documentation pending. |
| [`ENT:ResetHactViewFOV`](#ent-resethactviewfov) | Documentation pending. |
| [`ENT:ResetHeatDecayTimers`](#ent-resetheatdecaytimers) | Documentation pending. |
| [`ENT:RunHactEventFrame`](#ent-runhacteventframe) | Documentation pending. |
| [`ENT:ScanAndExecuteHacts`](#ent-scanandexecutehacts) | Documentation pending. |
| [`ENT:SendHactView`](#ent-sendhactview) | Documentation pending. |
| [`ENT:SetHactBridge`](#ent-sethactbridge) | Documentation pending. |
| [`ENT:SetHeat`](#ent-setheat) | Documentation pending. |
| [`ENT:StartHactBridgeAnimation`](#ent-starthactbridgeanimation) | Documentation pending. |
| [`ENT:StartHactFrameProgression`](#ent-starthactframeprogression) | Documentation pending. |
| [`ENT:StartHeatDecayTimer`](#ent-startheatdecaytimer) | Documentation pending. |
| [`ENT:StopHactFrameProgression`](#ent-stophactframeprogression) | Documentation pending. |
| [`ENT:SyncHeatNetworkVars`](#ent-syncheatnetworkvars) | Documentation pending. |
| [`ENT:UpdateHactEventFrames`](#ent-updatehacteventframes) | Documentation pending. |
| [`ENT:UpdateHactFrameBridge`](#ent-updatehactframebridge) | Documentation pending. |
| [`ENT:UpdateHactSubjectEventFrames`](#ent-updatehactsubjecteventframes) | Documentation pending. |
| [`ENT:UpdateHeatAura`](#ent-updateheataura) | Documentation pending. |
| [`ENT:UpdateHeatHUD`](#ent-updateheathud) | Documentation pending. |
| [`ENT:UpdateHeatPopAura`](#ent-updateheatpopaura) | Documentation pending. |

<a id="ent-aborthact"></a>
## `ENT:AbortHact`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:AbortHact()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:3173</code>.</p>

<a id="ent-addheat"></a>
## `ENT:AddHeat`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:AddHeat(var)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `var` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:1283</code>.</p>

<a id="ent-cacheavailablehacts"></a>
## `ENT:CacheAvailableHacts`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CacheAvailableHacts()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:1466</code>.</p>

<a id="ent-canforcepositiontonearestwall"></a>
## `ENT:CanForcePositionToNearestWall`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CanForcePositionToNearestWall(curhactOrRadius, maxWallDist)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `curhactOrRadius` | `any` | Not documented. |
| `maxWallDist` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:2124</code>.</p>

<a id="ent-cleanuphactviewstate"></a>
## `ENT:CleanupHactViewState`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CleanupHactViewState(duration)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `duration` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:1153</code>.</p>

<a id="ent-consumeheat"></a>
## `ENT:ConsumeHeat`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:ConsumeHeat(curhact)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `curhact` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:1516</code>.</p>

<a id="ent-deductheat"></a>
## `ENT:DeductHeat`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:DeductHeat(var)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `var` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:1293</code>.</p>

<a id="ent-detectenvironment"></a>
## `ENT:DetectEnvironment`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:DetectEnvironment()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:1602</code>.</p>

<a id="ent-endhact"></a>
## `ENT:EndHact`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:EndHact(suppressEvents)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `suppressEvents` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:3122</code>.</p>

<a id="ent-endhactviews"></a>
## `ENT:EndHactViews`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:EndHactViews()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:1123</code>.</p>

<a id="ent-executehact"></a>
## `ENT:ExecuteHact`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:ExecuteHact(hact, subjects, ding, resetPos, executedManually, qte)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `hact` | `any` | Not documented. |
| `subjects` | `any` | Not documented. |
| `ding` | `any` | Not documented. |
| `resetPos` | `any` | Not documented. |
| `executedManually` | `any` | Not documented. |
| `qte` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:2521</code>.</p>

<a id="ent-findnearestnavwall"></a>
## `ENT:FindNearestNavWall`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:FindNearestNavWall(searchRadius, maxWallDist)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `searchRadius` | `any` | Not documented. |
| `maxWallDist` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:1996</code>.</p>

<a id="ent-findsafeposition"></a>
## `ENT:FindSafePosition`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:FindSafePosition(origin, bbMin, bbMax)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `origin` | `any` | Not documented. |
| `bbMin` | `any` | Not documented. |
| `bbMax` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:1532</code>.</p>

<a id="ent-forcepositiontonearestwall"></a>
## `ENT:ForcePositionToNearestWall`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:ForcePositionToNearestWall(subjects, curhactOrRadius, wallCandidate, maxWallDist)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `subjects` | `any` | Not documented. |
| `curhactOrRadius` | `any` | Not documented. |
| `wallCandidate` | `any` | Not documented. |
| `maxWallDist` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:2128</code>.</p>

<a id="ent-getavailablehactactions"></a>
## `ENT:GetAvailableHactActions`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetAvailableHactActions()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:1489</code>.</p>

<a id="ent-getblueheatbarcount"></a>
## `ENT:GetBlueHeatBarCount`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetBlueHeatBarCount()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:69</code>.</p>

<a id="ent-getblueheatbarvalue"></a>
## `ENT:GetBlueHeatBarValue`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetBlueHeatBarValue()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:65</code>.</p>

<a id="ent-getcurrentheatgear"></a>
## `ENT:GetCurrentHeatGear`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetCurrentHeatGear()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:105</code>.</p>

<a id="ent-getforcepositiontowallcandidate"></a>
## `ENT:GetForcePositionToWallCandidate`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetForcePositionToWallCandidate(curhactOrRadius, maxWallDist)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `curhactOrRadius` | `any` | Not documented. |
| `maxWallDist` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:2109</code>.</p>

<a id="ent-getforcepositiontowallsearchparams"></a>
## `ENT:GetForcePositionToWallSearchParams`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetForcePositionToWallSearchParams(curhactOrRadius, maxWallDist)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `curhactOrRadius` | `any` | Not documented. |
| `maxWallDist` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:2097</code>.</p>

<a id="ent-gethact"></a>
## `ENT:GetHact`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetHact()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:1313</code>.</p>

<a id="ent-gethactcameradataentry"></a>
## `ENT:GetHactCameraDataEntry`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetHactCameraDataEntry(cameraAnims)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `cameraAnims` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:933</code>.</p>

<a id="ent-gethactcampos"></a>
## `ENT:GetHactCamPos`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetHactCamPos()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:3114</code>.</p>

<a id="ent-gethactframeprogressionentry"></a>
## `ENT:GetHactFrameProgressionEntry`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetHactFrameProgressionEntry(frameProgression, index)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `frameProgression` | `any` | Not documented. |
| `index` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:968</code>.</p>

<a id="ent-getheat"></a>
## `ENT:GetHeat`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetHeat()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:1309</code>.</p>

<a id="ent-getheatgearcount"></a>
## `ENT:GetHeatGearCount`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetHeatGearCount()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:61</code>.</p>

<a id="ent-getheatgearforamount"></a>
## `ENT:GetHeatGearForAmount`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetHeatGearForAmount(heat)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `heat` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:96</code>.</p>

<a id="ent-getheatsystemtype"></a>
## `ENT:GetHeatSystemType`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetHeatSystemType()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:54</code>.</p>

<a id="ent-getmaxheat"></a>
## `ENT:GetMaxHeat`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetMaxHeat()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:1353</code>.</p>

<a id="ent-getnetworkedblueheatbarcount"></a>
## `ENT:GetNetworkedBlueHeatBarCount`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetNetworkedBlueHeatBarCount()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:141</code>.</p>

<a id="ent-getnetworkedblueheatbarvalue"></a>
## `ENT:GetNetworkedBlueHeatBarValue`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetNetworkedBlueHeatBarValue()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:149</code>.</p>

<a id="ent-getnetworkedheat"></a>
## `ENT:GetNetworkedHeat`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetNetworkedHeat()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:133</code>.</p>

<a id="ent-getnetworkedheatgearcount"></a>
## `ENT:GetNetworkedHeatGearCount`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetNetworkedHeatGearCount()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:137</code>.</p>

<a id="ent-getnetworkedheatsystemtype"></a>
## `ENT:GetNetworkedHeatSystemType`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetNetworkedHeatSystemType()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:153</code>.</p>

<a id="ent-getnetworkedredheatbarcount"></a>
## `ENT:GetNetworkedRedHeatBarCount`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetNetworkedRedHeatBarCount()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:145</code>.</p>

<a id="ent-getredheatamount"></a>
## `ENT:GetRedHeatAmount`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetRedHeatAmount()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:88</code>.</p>

<a id="ent-getredheatbarcount"></a>
## `ENT:GetRedHeatBarCount`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetRedHeatBarCount()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:75</code>.</p>

<a id="ent-getredheatstart"></a>
## `ENT:GetRedHeatStart`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetRedHeatStart()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:81</code>.</p>

<a id="ent-getwallhactfaceawayfromwall"></a>
## `ENT:GetWallHactFaceAwayFromWall`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetWallHactFaceAwayFromWall(curhact, wallReference)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `curhact` | `any` | Not documented. |
| `wallReference` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:1927</code>.</p>

<a id="ent-getwallhactreferenceentity"></a>
## `ENT:GetWallHactReferenceEntity`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetWallHactReferenceEntity(curhact, subjects)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `curhact` | `any` | Not documented. |
| `subjects` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:1882</code>.</p>

<a id="ent-hactbridge"></a>
## `ENT:HactBridge`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:HactBridge()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:2451</code>.</p>

<a id="ent-hactbridgeto"></a>
## `ENT:HactBridgeTo`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:HactBridgeTo(id)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `id` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:2397</code>.</p>

<a id="ent-hactexists"></a>
## `ENT:HactExists`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:HactExists(hact)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `hact` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:396</code>.</p>

<a id="ent-hactfovevent"></a>
## `ENT:HactFOVEvent`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:HactFOVEvent(targetFOV, startFrame, endFrame)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `targetFOV` | `any` | Not documented. |
| `startFrame` | `any` | Not documented. |
| `endFrame` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:1167</code>.</p>

<a id="ent-heatpopbehavior"></a>
## `ENT:HeatPopBehavior`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:HeatPopBehavior(time)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `time` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:1401</code>.</p>

<a id="ent-heatthink"></a>
## `ENT:HeatThink`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:HeatThink()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:1192</code>.</p>

<a id="ent-isfrozenprop"></a>
## `ENT:IsFrozenProp`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:IsFrozenProp(ent)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `ent` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:1595</code>.</p>

<a id="ent-isinredheat"></a>
## `ENT:IsInRedHeat`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:IsInRedHeat()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:92</code>.</p>

<a id="ent-lad-hacteventframeshaskey"></a>
## `ENT:LAD_HactEventFramesHasKey`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:LAD_HactEventFramesHasKey(key)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `key` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:725</code>.</p>

<a id="ent-lad-hacteventframesusedamageevents"></a>
## `ENT:LAD_HactEventFramesUseDamageEvents`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:LAD_HactEventFramesUseDamageEvents()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:717</code>.</p>

<a id="ent-lad-shouldsuppresshactmodelevent"></a>
## `ENT:LAD_ShouldSuppressHactModelEvent`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:LAD_ShouldSuppressHactModelEvent(key)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `key` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:738</code>.</p>

<a id="ent-playdynamicintro"></a>
## `ENT:PlayDynamicIntro`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:PlayDynamicIntro(enemy)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `enemy` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:1523</code>.</p>

<a id="ent-playlocalsound"></a>
## `ENT:PlayLocalSound`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:PlayLocalSound(path, volume)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `path` | `any` | Not documented. |
| `volume` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:1344</code>.</p>

<a id="ent-playvictimhact"></a>
## `ENT:PlayVictimHact`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:PlayVictimHact(hact, subjects)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `hact` | `any` | Not documented. |
| `subjects` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:3270</code>.</p>

<a id="ent-popheat"></a>
## `ENT:PopHeat`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:PopHeat(hyperarmor, anim)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `hyperarmor` | `any` | Not documented. |
| `anim` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:1361</code>.</p>

<a id="ent-postowall"></a>
## `ENT:PosToWall`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:PosToWall(offset, wallReference, faceAwayFromWall)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `offset` | `any` | Not documented. |
| `wallReference` | `any` | Not documented. |
| `faceAwayFromWall` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:1797</code>.</p>

<a id="ent-refreshhactbridgeviewers"></a>
## `ENT:RefreshHactBridgeViewers`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:RefreshHactBridgeViewers(bridgeEntry, cameraDataPath, cameraFOVOptions, frameProgressionPath, fov)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `bridgeEntry` | `any` | Not documented. |
| `cameraDataPath` | `any` | Not documented. |
| `cameraFOVOptions` | `any` | Not documented. |
| `frameProgressionPath` | `any` | Not documented. |
| `fov` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:2273</code>.</p>

<a id="ent-removeheataura"></a>
## `ENT:RemoveHeatAura`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:RemoveHeatAura()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:1277</code>.</p>

<a id="ent-resethacteventframes"></a>
## `ENT:ResetHactEventFrames`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:ResetHactEventFrames(frame)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `frame` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:745</code>.</p>

<a id="ent-resethactviewfov"></a>
## `ENT:ResetHactViewFOV`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:ResetHactViewFOV(duration)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `duration` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:1135</code>.</p>

<a id="ent-resetheatdecaytimers"></a>
## `ENT:ResetHeatDecayTimers`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:ResetHeatDecayTimers()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:1340</code>.</p>

<a id="ent-runhacteventframe"></a>
## `ENT:RunHactEventFrame`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:RunHactEventFrame(entry, track)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `entry` | `any` | Not documented. |
| `track` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:751</code>.</p>

<a id="ent-scanandexecutehacts"></a>
## `ENT:ScanAndExecuteHacts`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:ScanAndExecuteHacts()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:1415</code>.</p>

<a id="ent-sendhactview"></a>
## `ENT:SendHactView`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:SendHactView(ply, ent, subjects, hactcam, fov, fps, dontHideEnts, smoothReturn, cameraAxisOffset, cameraDataPath, cameraFOVOptions, frameProgressionPath)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `ply` | `any` | Not documented. |
| `ent` | `any` | Not documented. |
| `subjects` | `any` | Not documented. |
| `hactcam` | `any` | Not documented. |
| `fov` | `any` | Not documented. |
| `fps` | `any` | Not documented. |
| `dontHideEnts` | `any` | Not documented. |
| `smoothReturn` | `any` | Not documented. |
| `cameraAxisOffset` | `any` | Not documented. |
| `cameraDataPath` | `any` | Not documented. |
| `cameraFOVOptions` | `any` | Not documented. |
| `frameProgressionPath` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:1086</code>.</p>

<a id="ent-sethactbridge"></a>
## `ENT:SetHactBridge`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:SetHactBridge(id)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `id` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:2402</code>.</p>

<a id="ent-setheat"></a>
## `ENT:SetHeat`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:SetHeat(var)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `var` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:1299</code>.</p>

<a id="ent-starthactbridgeanimation"></a>
## `ENT:StartHactBridgeAnimation`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:StartHactBridgeAnimation(bridgeName, bridgeEntry, animName)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `bridgeName` | `any` | Not documented. |
| `bridgeEntry` | `any` | Not documented. |
| `animName` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:2325</code>.</p>

<a id="ent-starthactframeprogression"></a>
## `ENT:StartHactFrameProgression`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:StartHactFrameProgression(path)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `path` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:883</code>.</p>

<a id="ent-startheatdecaytimer"></a>
## `ENT:StartHeatDecayTimer`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:StartHeatDecayTimer()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:1321</code>.</p>

<a id="ent-stophactframeprogression"></a>
## `ENT:StopHactFrameProgression`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:StopHactFrameProgression()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:852</code>.</p>

<a id="ent-syncheatnetworkvars"></a>
## `ENT:SyncHeatNetworkVars`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:SyncHeatNetworkVars()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:109</code>.</p>

<a id="ent-updatehacteventframes"></a>
## `ENT:UpdateHactEventFrames`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:UpdateHactEventFrames(frameOverride)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `frameOverride` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:769</code>.</p>

<a id="ent-updatehactframebridge"></a>
## `ENT:UpdateHactFrameBridge`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:UpdateHactFrameBridge()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:2257</code>.</p>

<a id="ent-updatehactsubjecteventframes"></a>
## `ENT:UpdateHactSubjectEventFrames`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:UpdateHactSubjectEventFrames(frame)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `frame` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:822</code>.</p>

<a id="ent-updateheataura"></a>
## `ENT:UpdateHeatAura`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:UpdateHeatAura()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:1252</code>.</p>

<a id="ent-updateheathud"></a>
## `ENT:UpdateHeatHUD`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:UpdateHeatHUD()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:1426</code>.</p>

<a id="ent-updateheatpopaura"></a>
## `ENT:UpdateHeatPopAura`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:UpdateHeatPopAura(color, turnOn)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `color` | `any` | Not documented. |
| `turnOn` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:1258</code>.</p>
