---
title: "ENT:VFX_MeshTrail"
status: realm-server
---

[Back to VFX](index.md)

<a id="ent-vfx-meshtrail"></a>
# `ENT:VFX_MeshTrail` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:VFX_MeshTrail(cfg)
```

</div>

Serverside caller for the MeshTrail system.

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `cfg` | `table` | Yes | A table containing all the data needed to render individual ribbons for a mesh trail. |

</div>

### `cfg` table fields

<div class="api-parameter-table api-parameter-fields" markdown>

| Key | Type | Required | Description |
| --- | --- | :---: | --- |
| `lifetime` | `float` | Yes | The total amount of time a trail can live after being instanced by a node (in seconds). |
| `trailtime` | `float` | Yes | The time it takes for a trail ribbon to catch up to itself on the V-axis. |
| `start` | `string` | Yes | The starting point for the trail, can be a bone or an attachment. Preferably use a bone. |
| `endpoint` | `string/vector` | Yes | The end point for the trail, can be a bone attachment, or a Vector. Preferably use a bone. |
| `endIsVec` | `bool` | Yes | Used internally if a vector is passed in the CFG table's endpoint field, tells the system to use that Vector(X,Y,Z) as the end point for the trail. |

</div>

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/vfx.lua:92</code>.</p>
