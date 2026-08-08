---
title: "ENT:_SoundtrackOnPossessed"
---

[Back to Soundtrack](index.md)

<a id="ent-soundtrackonpossessed"></a>
# `ENT:_SoundtrackOnPossessed`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_SoundtrackOnPossessed()
```

</div>

Called by OnPossessed in fighter_command.lua (not a public hook)
Sends own soundtrack if in combat, then syncs all other battle fighters to the new possessor.

## Parameters

This method takes no explicit arguments.

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/soundtrack.lua:294</code>.</p>
