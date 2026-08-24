---
title: "ENT:Think"
---

[Back to Overrides](index.md)

<a id="ent-think"></a>
# `ENT:Think` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:Think()
```

</div>

ENT:Think() override (source: drgbase_nextbot/shared.lua)
Eliminates 10-12 redundant CurTime() C calls per tick by caching one value at the top.
In the medium-delay block, reuses self._DrGBaseWaterLevel (already maintained at 20Hz by
the short-delay block) instead of calling WaterLevel() a second time per 0.1s interval.

## Parameters

This method takes no explicit arguments.

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/overrides.lua:1410</code>.</p>
