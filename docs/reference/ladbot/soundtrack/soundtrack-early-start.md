---
title: "ENT:SoundtrackEarlyStart"
---

[Back to Soundtrack](index.md)

<a id="ent-soundtrackearlystart"></a>
# `ENT:SoundtrackEarlyStart`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:SoundtrackEarlyStart(directRecipient)
```

</div>

Public API: starts the combat soundtrack early without requiring FighterInCombat to be set.
Pass directRecipient (Player) when the entity is not yet in a battle and not possessed
(e.g. endless arena boss intro) so the track is delivered to the correct player.

## Parameters

| Name | Type | Description |
| --- | --- | --- |
| `directRecipient` | `any` | Not documented. |

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/soundtrack.lua:218</code>.</p>
