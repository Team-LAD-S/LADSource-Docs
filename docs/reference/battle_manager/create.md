---
title: "BattleManager:Create"
status: realm-server
---

[Back to Battle Manager](index.md)

<a id="battlemanager-create"></a>
# `BattleManager:Create` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span></div>

<div class="api-signature" markdown>

```lua
function BattleManager:Create(participants, opts)
```

</div>

Create a new battle from a list of participant entities. Returns the battle ID.
All listed fighters receive _battleID = <id> immediately so that ActivateCombat
(which may fire later inside a CICO coroutine) can find the existing battle.
opts (optional table): { endless = true } — battle never declares victory/defeat;
   CheckBattleEnd returns early so the record stays alive for the next wave.

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `participants` | `any` | Yes | Not documented. |
| `opts` | `any` | Yes | Not documented. |

</div>

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/lad_framework/battle_manager.lua:140</code>.</p>
