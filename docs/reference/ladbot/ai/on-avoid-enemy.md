---
title: "ENT:OnAvoidEnemy"
status: realm-server
---

[Back to AI](index.md)

<a id="ent-onavoidenemy"></a>
# `ENT:OnAvoidEnemy` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span></div>

<div class="api-signature" markdown>

```lua
function ENT:OnAvoidEnemy(enemy)
```

</div>

Belongs to DrGBase, whether the LADBot should avoid entity.
Can be overriden to implement custom behavior.

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `enemy` | `ent` | Yes | The enemy entity to check. |

</div>

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:1672</code>.</p>
