# Soundtrack

Methods defined in `lua/entities/lad_framework_base/soundtrack.lua`.

!!! info "Generated reference"

    This page is generated from the current Lua source. Add API annotations
    above a method in the source file to improve its documentation.

## Methods

| Method | Summary |
| --- | --- |
| [`ENT:_GetSoundtrackRecipients`](#ent-getsoundtrackrecipients) | Documentation pending. |
| [`ENT:_LoadSoundtrackDef`](#ent-loadsoundtrackdef) | Documentation pending. |
| [`ENT:_SendSoundtrackStart`](#ent-sendsoundtrackstart) | Documentation pending. |
| [`ENT:_SendSoundtrackStop`](#ent-sendsoundtrackstop) | Documentation pending. |
| [`ENT:_SoundtrackActivateCombat`](#ent-soundtrackactivatecombat) | Documentation pending. |
| [`ENT:_SoundtrackBattleStart`](#ent-soundtrackbattlestart) | Documentation pending. |
| [`ENT:_SoundtrackDeactivateCombat`](#ent-soundtrackdeactivatecombat) | Documentation pending. |
| [`ENT:_SoundtrackDeathThink`](#ent-soundtrackdeaththink) | Documentation pending. |
| [`ENT:_SoundtrackOnDispossessed`](#ent-soundtrackondispossessed) | Documentation pending. |
| [`ENT:_SoundtrackOnPossessed`](#ent-soundtrackonpossessed) | Documentation pending. |
| [`ENT:_SoundtrackOnRemove`](#ent-soundtrackonremove) | Documentation pending. |
| [`ENT:GetActiveSoundtrackData`](#ent-getactivesoundtrackdata) | Documentation pending. |
| [`ENT:SoundtrackEarlyStart`](#ent-soundtrackearlystart) | Documentation pending. |
| [`ENT:SoundtrackMovesetUpdate`](#ent-soundtrackmovesetupdate) | Documentation pending. |

<a id="ent-getsoundtrackrecipients"></a>
## `ENT:_GetSoundtrackRecipients`

<div class="api-badges"><span class="api-badge ">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_GetSoundtrackRecipients(selfIgnoreCombat)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `selfIgnoreCombat` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/soundtrack.lua:107</code>.</p>

<a id="ent-loadsoundtrackdef"></a>
## `ENT:_LoadSoundtrackDef`

<div class="api-badges"><span class="api-badge ">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_LoadSoundtrackDef(sdFile)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `sdFile` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/soundtrack.lua:91</code>.</p>

<a id="ent-sendsoundtrackstart"></a>
## `ENT:_SendSoundtrackStart`

<div class="api-badges"><span class="api-badge ">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_SendSoundtrackStart(ignoreCombatCheck, skipIntro, waitForIntro, directRecipient)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `ignoreCombatCheck` | `any` | Not documented. |
| `skipIntro` | `any` | Not documented. |
| `waitForIntro` | `any` | Not documented. |
| `directRecipient` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/soundtrack.lua:144</code>.</p>

<a id="ent-sendsoundtrackstop"></a>
## `ENT:_SendSoundtrackStop`

<div class="api-badges"><span class="api-badge ">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_SendSoundtrackStop(ply)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `ply` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/soundtrack.lua:177</code>.</p>

<a id="ent-soundtrackactivatecombat"></a>
## `ENT:_SoundtrackActivateCombat`

<div class="api-badges"><span class="api-badge ">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_SoundtrackActivateCombat()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/soundtrack.lua:224</code>.</p>

<a id="ent-soundtrackbattlestart"></a>
## `ENT:_SoundtrackBattleStart`

<div class="api-badges"><span class="api-badge ">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_SoundtrackBattleStart(directRecipient)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `directRecipient` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/soundtrack.lua:209</code>.</p>

<a id="ent-soundtrackdeactivatecombat"></a>
## `ENT:_SoundtrackDeactivateCombat`

<div class="api-badges"><span class="api-badge ">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_SoundtrackDeactivateCombat()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/soundtrack.lua:234</code>.</p>

<a id="ent-soundtrackdeaththink"></a>
## `ENT:_SoundtrackDeathThink`

<div class="api-badges"><span class="api-badge ">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_SoundtrackDeathThink()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/soundtrack.lua:404</code>.</p>

<a id="ent-soundtrackondispossessed"></a>
## `ENT:_SoundtrackOnDispossessed`

<div class="api-badges"><span class="api-badge ">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_SoundtrackOnDispossessed(ply)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `ply` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/soundtrack.lua:326</code>.</p>

<a id="ent-soundtrackonpossessed"></a>
## `ENT:_SoundtrackOnPossessed`

<div class="api-badges"><span class="api-badge ">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_SoundtrackOnPossessed()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/soundtrack.lua:294</code>.</p>

<a id="ent-soundtrackonremove"></a>
## `ENT:_SoundtrackOnRemove`

<div class="api-badges"><span class="api-badge ">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_SoundtrackOnRemove()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/soundtrack.lua:348</code>.</p>

<a id="ent-getactivesoundtrackdata"></a>
## `ENT:GetActiveSoundtrackData`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetActiveSoundtrackData()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/soundtrack.lua:60</code>.</p>

<a id="ent-soundtrackearlystart"></a>
## `ENT:SoundtrackEarlyStart`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:SoundtrackEarlyStart(directRecipient)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `directRecipient` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/soundtrack.lua:218</code>.</p>

<a id="ent-soundtrackmovesetupdate"></a>
## `ENT:SoundtrackMovesetUpdate`

<div class="api-badges"><span class="api-badge ">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:SoundtrackMovesetUpdate()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/soundtrack.lua:188</code>.</p>
