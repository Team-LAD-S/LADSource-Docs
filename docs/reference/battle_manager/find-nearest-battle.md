---
title: "BattleManager:FindNearestBattle"
---

[Back to Battle Manager](index.md)

<a id="battlemanager-findnearestbattle"></a>
# `BattleManager:FindNearestBattle` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span></div>

<div class="api-signature" markdown>

```lua
function BattleManager:FindNearestBattle(pos, maxDist)
```

</div>

Find the ID of the nearest active battle within maxDist units of pos.
Returns nil if none is found.

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `pos` | `any` | Yes | Not documented. |
| `maxDist` | `any` | Yes | Not documented. |

</div>

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/lad_framework/battle_manager.lua:484</code>.</p>
