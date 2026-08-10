---
title: "BattleManager:CheckBattleEnd"
status: realm-server
---

[Back to Battle Manager](index.md)

<a id="battlemanager-checkbattleend"></a>
# `BattleManager:CheckBattleEnd` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span></div>

<div class="api-signature" markdown>

```lua
function BattleManager:CheckBattleEnd(battleID)
```

</div>

Evaluate whether the battle is over for any remaining participant.
Deactivates combat on any fighter who no longer has a living enemy in the battle.
Dissolves the battle record once everyone has left.

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `battleID` | `any` | Yes | Not documented. |

</div>

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/lad_framework/battle_manager.lua:264</code>.</p>
