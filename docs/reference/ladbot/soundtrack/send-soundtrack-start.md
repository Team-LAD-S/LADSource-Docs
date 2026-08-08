---
title: "ENT:_SendSoundtrackStart"
---

[Back to Soundtrack](index.md)

<a id="ent-sendsoundtrackstart"></a>
# `ENT:_SendSoundtrackStart` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

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

## Parameters

| Name | Type | Description |
| --- | --- | --- |
| `ignoreCombatCheck` | `any` | Not documented. |
| `skipIntro` | `any` | Not documented. |
| `waitForIntro` | `any` | Not documented. |
| `directRecipient` | `any` | Not documented. |

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/soundtrack.lua:144</code>.</p>
