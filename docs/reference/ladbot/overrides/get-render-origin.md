---
title: "ENT:GetRenderOrigin"
---

[Back to Overrides](index.md)

<a id="ent-getrenderorigin"></a>
# `ENT:GetRenderOrigin` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetRenderOrigin()
```

</div>

Return our client-predicted position for rendering instead of the network-interpolated
origin.  GetPos() (hitboxes/physics) is never touched — only the visual draw position
is overridden.  During non-PSAW states _LAD_predictedPos is nil so it falls back to
the normal GetPos() path.

## Parameters

This method takes no explicit arguments.

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/overrides.lua:1922</code>.</p>
