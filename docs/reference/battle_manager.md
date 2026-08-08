# Battle Manager

Server-side battle lifecycle methods exposed through `LADSource.BattleManager`.

Methods defined in `lua/lad_framework/battle_manager.lua`.

!!! info "Generated reference"

    This page is generated from the current Lua source. Add API annotations
    above a method in the source file to improve its documentation.

## Methods

| Method | Summary |
| --- | --- |
| [`BattleManager:BattleCount`](#battlemanager-battlecount) | Debug: returns how many battles are currently tracked. |
| [`BattleManager:CheckBattleEnd`](#battlemanager-checkbattleend) | Evaluate whether the battle is over for any remaining participant. Deactivates combat on any fighter who no longer has a living enemy in the battle. Dissolves the battle record once everyone has left. |
| [`BattleManager:Create`](#battlemanager-create) | Create a new battle from a list of participant entities. Returns the battle ID. All listed fighters receive _battleID = <id> immediately so that ActivateCombat (which may fire later inside a CICO coroutine) can find the existing battle. opts (optional table): { endless = true } — battle never declares victory/defeat; CheckBattleEnd returns early so the record stays alive for the next wave. |
| [`BattleManager:FindNearestBattle`](#battlemanager-findnearestbattle) | Find the ID of the nearest active battle within maxDist units of pos. Returns nil if none is found. |
| [`BattleManager:Join`](#battlemanager-join) | Add a fighter to an existing battle as a late joiner (no intro animation). Returns true on success. |
| [`BattleManager:Leave`](#battlemanager-leave) | Remove a fighter from their current battle. checkEnd: pass true to immediately re-evaluate whether the battle should end (e.g. after a kill). Pass false during bulk cleanup (OnRemove) to avoid operating on partially-removed entity state. |
| [`BattleManager:Merge`](#battlemanager-merge) | Merge two battles into one. All fighters from dissolveID are re-registered under keepID. The dissolveID battle record is dissolved. All fighter._battleID values are updated. |

<a id="battlemanager-battlecount"></a>
## `BattleManager:BattleCount`

<div class="api-badges"><span class="api-badge ">server</span></div>

<div class="api-signature" markdown>

```lua
function BattleManager:BattleCount()
```

</div>

Debug: returns how many battles are currently tracked.

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/lad_framework/battle_manager.lua:504</code>.</p>

<a id="battlemanager-checkbattleend"></a>
## `BattleManager:CheckBattleEnd`

<div class="api-badges"><span class="api-badge ">server</span></div>

<div class="api-signature" markdown>

```lua
function BattleManager:CheckBattleEnd(battleID)
```

</div>

Evaluate whether the battle is over for any remaining participant.
Deactivates combat on any fighter who no longer has a living enemy in the battle.
Dissolves the battle record once everyone has left.

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `battleID` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/lad_framework/battle_manager.lua:264</code>.</p>

<a id="battlemanager-create"></a>
## `BattleManager:Create`

<div class="api-badges"><span class="api-badge ">server</span></div>

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

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `participants` | `any` | Not documented. |
| `opts` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/lad_framework/battle_manager.lua:140</code>.</p>

<a id="battlemanager-findnearestbattle"></a>
## `BattleManager:FindNearestBattle`

<div class="api-badges"><span class="api-badge ">server</span></div>

<div class="api-signature" markdown>

```lua
function BattleManager:FindNearestBattle(pos, maxDist)
```

</div>

Find the ID of the nearest active battle within maxDist units of pos.
Returns nil if none is found.

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `pos` | `any` | Not documented. |
| `maxDist` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/lad_framework/battle_manager.lua:484</code>.</p>

<a id="battlemanager-join"></a>
## `BattleManager:Join`

<div class="api-badges"><span class="api-badge ">server</span></div>

<div class="api-signature" markdown>

```lua
function BattleManager:Join(fighter, battleID)
```

</div>

Add a fighter to an existing battle as a late joiner (no intro animation).
Returns true on success.

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `fighter` | `any` | Not documented. |
| `battleID` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/lad_framework/battle_manager.lua:175</code>.</p>

<a id="battlemanager-leave"></a>
## `BattleManager:Leave`

<div class="api-badges"><span class="api-badge ">server</span></div>

<div class="api-signature" markdown>

```lua
function BattleManager:Leave(fighter, checkEnd)
```

</div>

Remove a fighter from their current battle.
checkEnd: pass true to immediately re-evaluate whether the battle should end
(e.g. after a kill). Pass false during bulk cleanup (OnRemove) to
avoid operating on partially-removed entity state.

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `fighter` | `any` | Not documented. |
| `checkEnd` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/lad_framework/battle_manager.lua:230</code>.</p>

<a id="battlemanager-merge"></a>
## `BattleManager:Merge`

<div class="api-badges"><span class="api-badge ">server</span></div>

<div class="api-signature" markdown>

```lua
function BattleManager:Merge(keepID, dissolveID)
```

</div>

Merge two battles into one. All fighters from dissolveID are re-registered under keepID.
The dissolveID battle record is dissolved. All fighter._battleID values are updated.

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `keepID` | `any` | Not documented. |
| `dissolveID` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/lad_framework/battle_manager.lua:196</code>.</p>
