---
title: "ENT:DebugDrawCone"
status: realm-server
---

[Back to Shared](index.md)

<a id="ent-debugdrawcone"></a>
# `ENT:DebugDrawCone` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:DebugDrawCone(origin, direction, angle, range, segments, duration, color)
```

</div>

Draws a debug cone. Must enable `developer` mode to see the cone.

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `origin` | `Vector` | Yes | The starting point of the cone. |
| `direction` | `Vector` | Yes | The direction the cone points. |
| `angle` | `number` | Yes | The angle of the cone. |
| `range` | `number` | Yes | The range of the cone. |
| `segments` | `number` | No | The number of segments to use for the cone, defaults to 16 if not specified. |
| `duration` | `number` | No | The duration (in seconds) to display the cone, defaults to 2 if not specified. |
| `color` | `Color(r,g,b,a?)` | Yes | The color of the cone. |

</div>

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:667</code>.</p>
