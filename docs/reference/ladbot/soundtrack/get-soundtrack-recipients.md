---
title: "ENT:_GetSoundtrackRecipients"
---

[Back to Soundtrack](index.md)

<a id="ent-getsoundtrackrecipients"></a>
# `ENT:_GetSoundtrackRecipients` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

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

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `selfIgnoreCombat` | `any` | Yes | Not documented. |

</div>

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/soundtrack.lua:107</code>.</p>
