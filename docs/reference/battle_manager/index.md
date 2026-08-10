# Battle Manager

Server-side battle lifecycle methods exposed through `LADSource.BattleManager`.

Methods defined in `lua/lad_framework/battle_manager.lua`.

!!! info "Generated reference"

    This page is generated from the current Lua source. Add API annotations
    above a method in the source file to improve its documentation.

## Methods

<div class="api-method-list" markdown>

| Method | Summary |
| --- | --- |
| [`BattleManager:BattleCount`](battle-count.md) | Debug: returns how many battles are currently tracked. |
| [`BattleManager:CheckBattleEnd`](check-battle-end.md) | Evaluate whether the battle is over for any remaining participant. Deactivates combat on any fighter who no longer has a living enemy in the battle. Dissolves the battle record once everyone has left. |
| [`BattleManager:Create`](create.md) | Create a new battle from a list of participant entities. Returns the battle ID. All listed fighters receive _battleID = <id> immediately so that ActivateCombat (which may fire later inside a CICO coroutine) can find the existing battle. opts (optional table): { endless = true } — battle never declares victory/defeat;    CheckBattleEnd returns early so the record stays alive for the next wave. |
| [`BattleManager:FindNearestBattle`](find-nearest-battle.md) | Find the ID of the nearest active battle within maxDist units of pos. Returns nil if none is found. |
| [`BattleManager:Join`](join.md) | Add a fighter to an existing battle as a late joiner (no intro animation). Returns true on success. |
| [`BattleManager:Leave`](leave.md) | Remove a fighter from their current battle. checkEnd: pass true to immediately re-evaluate whether the battle should end            (e.g. after a kill). Pass false during bulk cleanup (OnRemove) to            avoid operating on partially-removed entity state. |
| [`BattleManager:Merge`](merge.md) | Merge two battles into one. All fighters from dissolveID are re-registered under keepID. The dissolveID battle record is dissolved. All fighter._battleID values are updated. |

</div>
