---
title: "ENT:_SoundtrackActivateCombat"
---

[Back to Soundtrack](index.md)

<a id="ent-soundtrackactivatecombat"></a>
# `ENT:_SoundtrackActivateCombat`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_SoundtrackActivateCombat()
```

</div>

Called by ActivateCombat in fighter_command.lua (not a public hook).
Skips sending if the soundtrack was already started during PlayBattleStartAnim.

## Parameters

This method takes no explicit arguments.

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/soundtrack.lua:224</code>.</p>
