---
title: "ENT:_GetRootAnimVelocity"
---

[Back to Ragdoll](index.md)

<a id="ent-getrootanimvelocity"></a>
# `ENT:_GetRootAnimVelocity`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_GetRootAnimVelocity()
```

</div>

Returns the root-motion velocity of the current animation sequence in world space.
Source model space: +X = forward, +Y = LEFT, +Z = up.
ang:Right() points to the RIGHT (-Y in model space), so the Y component must be
negated; otherwise lateral root-motion is applied in the opposite direction.

## Parameters

This method takes no explicit arguments.

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ragdoll.lua:74</code>.</p>
