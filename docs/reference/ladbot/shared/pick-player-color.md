---
title: "ENT:PickPlayerColor"
status: realm-server
---

[Back to Shared](index.md)

<a id="ent-pickplayercolor"></a>
# `ENT:PickPlayerColor` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span></div>

<div class="api-signature" markdown>

```lua
function ENT:PickPlayerColor(palette)
```

</div>

Chooses a color from a palette. A palette may be a registered palette name,
a function returning a Color/Vector, a list of Color/Vector values, or one Color/Vector value.

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `palette` | `string\|function\|table\|Color\|Vector\|nil` | Yes | Not documented. |

</div>

## Returns

| Type | Description |
| --- | --- |
| `Color\|Vector` | Not documented. |

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:273</code>.</p>
