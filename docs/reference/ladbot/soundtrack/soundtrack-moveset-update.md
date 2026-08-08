---
title: "ENT:SoundtrackMovesetUpdate"
---

[Back to Soundtrack](index.md)

<a id="ent-soundtrackmovesetupdate"></a>
# `ENT:SoundtrackMovesetUpdate`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:SoundtrackMovesetUpdate()
```

</div>

Checks if the active moveset changed the soundtrack and resends if so.
Called from SetFighterMoveset (moveset.lua) after moveset initialises.
Skips if a temporary weapon/grab moveset is active to avoid glitches during transitions.

## Parameters

This method takes no explicit arguments.

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/soundtrack.lua:188</code>.</p>
