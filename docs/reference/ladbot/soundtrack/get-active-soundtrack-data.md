---
title: "ENT:GetActiveSoundtrackData"
---

[Back to Soundtrack](index.md)

<a id="ent-getactivesoundtrackdata"></a>
# `ENT:GetActiveSoundtrackData` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetActiveSoundtrackData()
```

</div>

Returns { sdFile, weight } for the active style/moveset, falling back to defaults.
Style-ID lookup is primary so temporary weapon/grab movesets do not override music.
NOTE: SoundTracksByMoveset only accepts numeric style IDs (e.g., [1], [2], [3]).

## Parameters

This method takes no explicit arguments.

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/soundtrack.lua:60</code>.</p>
