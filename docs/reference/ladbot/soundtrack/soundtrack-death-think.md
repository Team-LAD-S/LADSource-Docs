---
title: "ENT:_SoundtrackDeathThink"
---

[Back to Soundtrack](index.md)

<a id="ent-soundtrackdeaththink"></a>
# `ENT:_SoundtrackDeathThink` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_SoundtrackDeathThink()
```

</div>

Called by DeathThink in events.lua (not a public hook)
Sends the defeat signal exactly once to own possessor and all battle allies' possessors.

## Parameters

This method takes no explicit arguments.

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/soundtrack.lua:404</code>.</p>
