---
title: "ENT:_BaseInitialize (line 2003)"
---

[Back to Overrides](index.md)

<a id="ent-baseinitialize-2003"></a>
# `ENT:_BaseInitialize` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_BaseInitialize()
```

</div>

_BaseInitialize is an empty stub in DRGBase called after _InitModules() completes,
so all internal fields (_DrGBaseSequenceEvents etc.) are already set up by the time
this runs.  Overriding Initialize() directly would skip _InitModules() entirely.

## Parameters

This method takes no explicit arguments.

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/overrides.lua:2003</code>.</p>
