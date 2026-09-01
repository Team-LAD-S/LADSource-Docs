---
title: "ENT:LoadData"
status: realm-server
---

[Back to Shared](index.md)

<a id="ent-loaddata"></a>
# `ENT:LoadData` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:LoadData(type, id)
```

</div>

Loads a data asset.

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `type` | `string` | Yes | Type of asset to load, accepts "moveset", "voicebank", "hact", "dialogue", or "item". |
| `id` | `string` | Yes | File name of the asset to load. |

</div>

## Returns

| Type | Description |
| --- | --- |
| `table` | The loaded asset data. |

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:1488</code>.</p>
