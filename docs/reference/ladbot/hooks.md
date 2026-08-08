# Hooks

Methods defined in `lua/entities/lad_framework_base/hooks.lua`.

!!! info "Generated reference"

    This page is generated from the current Lua source. Add API annotations
    above a method in the source file to improve its documentation.

## Methods

<div class="api-method-list" markdown>

| Method | Summary |
| --- | --- |
| [`ENT:CheckCustomConditions`](#ent-checkcustomconditions) | for moveset conditions specific to an entity. |
| [`ENT:CustomAfterBattleStart`](#ent-customafterbattlestart) | Documentation pending. |
| [`ENT:CustomAfterHeatPopped`](#ent-customafterheatpopped) | Documentation pending. |
| [`ENT:CustomAfterStandingUp`](#ent-customafterstandingup) | Inside CICO |
| [`ENT:CustomAIDefaultAttackRoutine`](#ent-customaidefaultattackroutine) | Documentation pending. |
| [`ENT:CustomBeforeBattleStart`](#ent-custombeforebattlestart) | Documentation pending. |
| [`ENT:CustomBeforeHeatPopped`](#ent-custombeforeheatpopped) | Documentation pending. |
| [`ENT:CustomBeforeStandingUp`](#ent-custombeforestandingup) | Outside CICO |
| [`ENT:CustomBeforeTakeDamage`](#ent-custombeforetakedamage) | Documentation pending. |
| [`ENT:CustomDeathThink`](#ent-customdeaththink) | Documentation pending. |
| [`ENT:CustomFighterInitialize`](#ent-customfighterinitialize) | Documentation pending. |
| [`ENT:CustomFighterThink`](#ent-customfighterthink) | Documentation pending. |
| [`ENT:CustomMidFighterInitialize`](#ent-custommidfighterinitialize) | this runs in the middle of CustomInitialize, redundant, needs rework |
| [`ENT:CustomOnDeath`](#ent-customondeath) | Documentation pending. |
| [`ENT:CustomOnLandOnGround`](#ent-customonlandonground) | Documentation pending. |
| [`ENT:CustomOnPossessed`](#ent-customonpossessed) | Documentation pending. |
| [`ENT:CustomOnRemove`](#ent-customonremove) | Documentation pending. |
| [`ENT:CustomOnTakeDamage`](#ent-customontakedamage) | Documentation pending. |
| [`ENT:CustomPostMovesetInit`](#ent-custompostmovesetinit) | ran after moveset initialized |
| [`ENT:OnActivateCombat`](#ent-onactivatecombat) | Documentation pending. |
| [`ENT:OnBumpAnim`](#ent-onbumpanim) | Documentation pending. |
| [`ENT:OnCosmeticKnockoff`](#ent-oncosmeticknockoff) | Documentation pending. |
| [`ENT:OnDeactivateCombat`](#ent-ondeactivatecombat) | Documentation pending. |
| [`ENT:OnDrawMovesetWeapon`](#ent-ondrawmovesetweapon) | Documentation pending. |
| [`ENT:SetupExclusiveMoveset`](#ent-setupexclusivemoveset) | Documentation pending. |

</div>

<a id="ent-checkcustomconditions"></a>
## `ENT:CheckCustomConditions`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CheckCustomConditions()
```

</div>

for moveset conditions specific to an entity.

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hooks.lua:9</code>.</p>

<a id="ent-customafterbattlestart"></a>
## `ENT:CustomAfterBattleStart`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CustomAfterBattleStart()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hooks.lua:45</code>.</p>

<a id="ent-customafterheatpopped"></a>
## `ENT:CustomAfterHeatPopped`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CustomAfterHeatPopped()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hooks.lua:20</code>.</p>

<a id="ent-customafterstandingup"></a>
## `ENT:CustomAfterStandingUp`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CustomAfterStandingUp()
```

</div>

Inside CICO

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hooks.lua:34</code>.</p>

<a id="ent-customaidefaultattackroutine"></a>
## `ENT:CustomAIDefaultAttackRoutine`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CustomAIDefaultAttackRoutine(enemy)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `enemy` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hooks.lua:48</code>.</p>

<a id="ent-custombeforebattlestart"></a>
## `ENT:CustomBeforeBattleStart`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CustomBeforeBattleStart()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hooks.lua:44</code>.</p>

<a id="ent-custombeforeheatpopped"></a>
## `ENT:CustomBeforeHeatPopped`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CustomBeforeHeatPopped()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hooks.lua:19</code>.</p>

<a id="ent-custombeforestandingup"></a>
## `ENT:CustomBeforeStandingUp`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CustomBeforeStandingUp()
```

</div>

Outside CICO

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hooks.lua:33</code>.</p>

<a id="ent-custombeforetakedamage"></a>
## `ENT:CustomBeforeTakeDamage`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CustomBeforeTakeDamage(dmg, hitgroup)
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

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hooks.lua:38</code>.</p>

<a id="ent-customdeaththink"></a>
## `ENT:CustomDeathThink`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CustomDeathThink()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hooks.lua:13</code>.</p>

<a id="ent-customfighterinitialize"></a>
## `ENT:CustomFighterInitialize`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CustomFighterInitialize()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hooks.lua:3</code>.</p>

<a id="ent-customfighterthink"></a>
## `ENT:CustomFighterThink`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CustomFighterThink()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hooks.lua:15</code>.</p>

<a id="ent-custommidfighterinitialize"></a>
## `ENT:CustomMidFighterInitialize`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CustomMidFighterInitialize()
```

</div>

this runs in the middle of CustomInitialize, redundant, needs rework

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hooks.lua:5</code>.</p>

<a id="ent-customondeath"></a>
## `ENT:CustomOnDeath`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CustomOnDeath()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hooks.lua:11</code>.</p>

<a id="ent-customonlandonground"></a>
## `ENT:CustomOnLandOnGround`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CustomOnLandOnGround()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hooks.lua:42</code>.</p>

<a id="ent-customonpossessed"></a>
## `ENT:CustomOnPossessed`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CustomOnPossessed()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hooks.lua:17</code>.</p>

<a id="ent-customonremove"></a>
## `ENT:CustomOnRemove`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CustomOnRemove()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hooks.lua:7</code>.</p>

<a id="ent-customontakedamage"></a>
## `ENT:CustomOnTakeDamage`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CustomOnTakeDamage(dmg, hitgroup)
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

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hooks.lua:40</code>.</p>

<a id="ent-custompostmovesetinit"></a>
## `ENT:CustomPostMovesetInit`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CustomPostMovesetInit()
```

</div>

ran after moveset initialized

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hooks.lua:22</code>.</p>

<a id="ent-onactivatecombat"></a>
## `ENT:OnActivateCombat`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:OnActivateCombat()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hooks.lua:30</code>.</p>

<a id="ent-onbumpanim"></a>
## `ENT:OnBumpAnim`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:OnBumpAnim(ent)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `ent` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hooks.lua:24</code>.</p>

<a id="ent-oncosmeticknockoff"></a>
## `ENT:OnCosmeticKnockoff`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:OnCosmeticKnockoff(cosmetic)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `cosmetic` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hooks.lua:26</code>.</p>

<a id="ent-ondeactivatecombat"></a>
## `ENT:OnDeactivateCombat`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:OnDeactivateCombat()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hooks.lua:31</code>.</p>

<a id="ent-ondrawmovesetweapon"></a>
## `ENT:OnDrawMovesetWeapon`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:OnDrawMovesetWeapon(wep)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `wep` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hooks.lua:28</code>.</p>

<a id="ent-setupexclusivemoveset"></a>
## `ENT:SetupExclusiveMoveset`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:SetupExclusiveMoveset()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hooks.lua:36</code>.</p>
