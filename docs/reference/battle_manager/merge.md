---
title: "BattleManager:Merge"
status: realm-server
---

[Back to Battle Manager](index.md)

<a id="battlemanager-merge"></a>
# `BattleManager:Merge` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span></div>

<div class="api-signature" markdown>

```lua
function BattleManager:Merge(keepID, dissolveID)
```

</div>

Merge two battles into one. All fighters from dissolveID are re-registered under keepID.
The dissolveID battle record is dissolved. All fighter._battleID values are updated.

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `keepID` | `any` | Yes | Not documented. |
| `dissolveID` | `any` | Yes | Not documented. |

</div>

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/lad_framework/battle_manager.lua:196</code>.</p>
