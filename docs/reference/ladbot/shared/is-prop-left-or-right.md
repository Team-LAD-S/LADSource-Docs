---
title: "ENT:IsPropLeftOrRight"
status: realm-server
---

[Back to Shared](index.md)

<a id="ent-ispropleftorright"></a>
# `ENT:IsPropLeftOrRight` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span></div>

<div class="api-signature" markdown>

```lua
function ENT:IsPropLeftOrRight(prop)
```

</div>

Returns whether the given prop entity is to the left or right side of a LADBot.
Uses the cross product of the forward vector and the vector to the prop to determine the side.

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `prop` | `any` | Yes | Not documented. |

</div>

## Returns

| Type | Description |
| --- | --- |
| `string` | "_left" if the prop is to the left, "_right" if the prop is to the right. |

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:575</code>.</p>
