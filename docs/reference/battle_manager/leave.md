---
title: "BattleManager:Leave"
status: realm-server
---

[Back to Battle Manager](index.md)

<a id="battlemanager-leave"></a>
# `BattleManager:Leave` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span></div>

<div class="api-signature" markdown>

```lua
function BattleManager:Leave(fighter, checkEnd)
```

</div>

Remove a fighter from their current battle.
checkEnd: pass true to immediately re-evaluate whether the battle should end
           (e.g. after a kill). Pass false during bulk cleanup (OnRemove) to
           avoid operating on partially-removed entity state.

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `fighter` | `any` | Yes | Not documented. |
| `checkEnd` | `any` | Yes | Not documented. |

</div>

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/lad_framework/battle_manager.lua:236</code>.</p>
