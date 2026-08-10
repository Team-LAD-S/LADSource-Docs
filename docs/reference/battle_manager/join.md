---
title: "BattleManager:Join"
status: realm-server
---

[Back to Battle Manager](index.md)

<a id="battlemanager-join"></a>
# `BattleManager:Join` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span></div>

<div class="api-signature" markdown>

```lua
function BattleManager:Join(fighter, battleID)
```

</div>

Add a fighter to an existing battle as a late joiner (no intro animation).
Returns true on success.

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `fighter` | `any` | Yes | Not documented. |
| `battleID` | `any` | Yes | Not documented. |

</div>

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/lad_framework/battle_manager.lua:175</code>.</p>
