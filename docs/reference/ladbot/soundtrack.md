# Soundtrack

Methods defined in `lua/entities/lad_framework_base/soundtrack.lua`.

!!! info "Generated reference"

    This page is generated from the current Lua source. Add API annotations
    above a method in the source file to improve its documentation.

## Methods

| Method | Summary |
| --- | --- |
| [`ENT:_GetSoundtrackRecipients`](#ent-getsoundtrackrecipients) | Returns a list of all Player recipients for this entity's soundtrack events. Includes own possessor (if possessed and satisfies combatCheck) plus possessors of all other possessed fighters currently in the same battle. selfIgnoreCombat = true skips the FighterInCombat check for self only (used during battle-start anim where FighterInCombat is not yet set). |
| [`ENT:_LoadSoundtrackDef`](#ent-loadsoundtrackdef) | Loads and caches a soundtrack definition file from data_static. Returns { name, hasEnd } or nil. |
| [`ENT:_SendSoundtrackStart`](#ent-sendsoundtrackstart) | Sends LAD_SoundtrackStart to all eligible recipients (own possessor and battle allies' possessors). Pass ignoreCombatCheck = true to send before FighterInCombat is set (battle start anim path). Pass skipIntro = true to jump straight to the loop (used on moveset switches mid-combat). Pass waitForIntro = true to defer a moveset switch until the current _start intro finishes. Pass directRecipient (Player) to force-add a specific player when the entity is unpossessed and has no battle yet (e.g. endless boss intro). |
| [`ENT:_SendSoundtrackStop`](#ent-sendsoundtrackstop) | Sends LAD_SoundtrackStop to the possessing player |
| [`ENT:_SoundtrackActivateCombat`](#ent-soundtrackactivatecombat) | Called by ActivateCombat in fighter_command.lua (not a public hook). Skips sending if the soundtrack was already started during PlayBattleStartAnim. |
| [`ENT:_SoundtrackBattleStart`](#ent-soundtrackbattlestart) | Called from PlayBattleStartAnim in battle.lua when the intro anim/camera begins. Starts music early so it plays under the battle start animation. |
| [`ENT:_SoundtrackDeactivateCombat`](#ent-soundtrackdeactivatecombat) | Called by DeactivateCombat in fighter_command.lua (not a public hook) |
| [`ENT:_SoundtrackDeathThink`](#ent-soundtrackdeaththink) | Called by DeathThink in events.lua (not a public hook) Sends the defeat signal exactly once to own possessor and all battle allies' possessors. |
| [`ENT:_SoundtrackOnDispossessed`](#ent-soundtrackondispossessed) | Called by OnDispossessed in shared.lua (not a public hook) |
| [`ENT:_SoundtrackOnPossessed`](#ent-soundtrackonpossessed) | Called by OnPossessed in fighter_command.lua (not a public hook) Sends own soundtrack if in combat, then syncs all other battle fighters to the new possessor. |
| [`ENT:_SoundtrackOnRemove`](#ent-soundtrackonremove) | Called by OnRemove in shared.lua (not a public hook) |
| [`ENT:GetActiveSoundtrackData`](#ent-getactivesoundtrackdata) | Returns { sdFile, weight } for the active style/moveset, falling back to defaults. Style-ID lookup is primary so temporary weapon/grab movesets do not override music. NOTE: SoundTracksByMoveset only accepts numeric style IDs (e.g., [1], [2], [3]). |
| [`ENT:SoundtrackEarlyStart`](#ent-soundtrackearlystart) | Public API: starts the combat soundtrack early without requiring FighterInCombat to be set. Pass directRecipient (Player) when the entity is not yet in a battle and not possessed (e.g. endless arena boss intro) so the track is delivered to the correct player. |
| [`ENT:SoundtrackMovesetUpdate`](#ent-soundtrackmovesetupdate) | Checks if the active moveset changed the soundtrack and resends if so. Called from SetFighterMoveset (moveset.lua) after moveset initialises. Skips if a temporary weapon/grab moveset is active to avoid glitches during transitions. |

<a id="ent-getsoundtrackrecipients"></a>
## `ENT:_GetSoundtrackRecipients`

<div class="api-badges"><span class="api-badge ">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_GetSoundtrackRecipients(selfIgnoreCombat)
```

</div>

Returns a list of all Player recipients for this entity's soundtrack events.
Includes own possessor (if possessed and satisfies combatCheck) plus possessors of
all other possessed fighters currently in the same battle.
selfIgnoreCombat = true skips the FighterInCombat check for self only
(used during battle-start anim where FighterInCombat is not yet set).

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

Loads and caches a soundtrack definition file from data_static. Returns { name, hasEnd } or nil.

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

Sends LAD_SoundtrackStart to all eligible recipients (own possessor and battle allies' possessors).
Pass ignoreCombatCheck = true to send before FighterInCombat is set (battle start anim path).
Pass skipIntro = true to jump straight to the loop (used on moveset switches mid-combat).
Pass waitForIntro = true to defer a moveset switch until the current _start intro finishes.
Pass directRecipient (Player) to force-add a specific player when the entity is unpossessed
and has no battle yet (e.g. endless boss intro).

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

Sends LAD_SoundtrackStop to the possessing player

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

Called by ActivateCombat in fighter_command.lua (not a public hook).
Skips sending if the soundtrack was already started during PlayBattleStartAnim.

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

Called from PlayBattleStartAnim in battle.lua when the intro anim/camera begins.
Starts music early so it plays under the battle start animation.

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

Called by DeactivateCombat in fighter_command.lua (not a public hook)

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

Called by DeathThink in events.lua (not a public hook)
Sends the defeat signal exactly once to own possessor and all battle allies' possessors.

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

Called by OnDispossessed in shared.lua (not a public hook)

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

Called by OnPossessed in fighter_command.lua (not a public hook)
Sends own soundtrack if in combat, then syncs all other battle fighters to the new possessor.

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

Called by OnRemove in shared.lua (not a public hook)

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

Returns { sdFile, weight } for the active style/moveset, falling back to defaults.
Style-ID lookup is primary so temporary weapon/grab movesets do not override music.
NOTE: SoundTracksByMoveset only accepts numeric style IDs (e.g., [1], [2], [3]).

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

Public API: starts the combat soundtrack early without requiring FighterInCombat to be set.
Pass directRecipient (Player) when the entity is not yet in a battle and not possessed
(e.g. endless arena boss intro) so the track is delivered to the correct player.

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

Checks if the active moveset changed the soundtrack and resends if so.
Called from SetFighterMoveset (moveset.lua) after moveset initialises.
Skips if a temporary weapon/grab moveset is active to avoid glitches during transitions.

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/soundtrack.lua:188</code>.</p>
