---
title: "ENT:IsFrozenProp"
status: realm-server
---

[Back to Shared](index.md)

<a id="ent-isfrozenprop"></a>
# `ENT:IsFrozenProp` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span></div>

<div class="api-signature" markdown>

```lua
function ENT:IsFrozenProp(ent)
```

</div>

Returns whether the given prop entity has motion disabled (i.e. frozen with Physgun).

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `ent` | `ent` | Yes | The prop entity to check. |

</div>

## Returns

| Type | Description |
| --- | --- |
| `boolean` | True if the prop is frozen, false otherwise. |

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:599</code>.</p>
