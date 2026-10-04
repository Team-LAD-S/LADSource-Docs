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

Returns whether the prop has motion disabled or is a prop_dynamic with VPhysics collision.

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

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:671</code>.</p>
