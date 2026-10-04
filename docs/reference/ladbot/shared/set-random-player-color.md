---
title: "ENT:SetRandomPlayerColor"
status: realm-server
---

[Back to Shared](index.md)

<a id="ent-setrandomplayercolor"></a>
# `ENT:SetRandomPlayerColor` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span></div>

<div class="api-signature" markdown>

```lua
function ENT:SetRandomPlayerColor(palette)
```

</div>

Chooses from a palette and networks the result to every client.

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `palette` | `string\|function\|table\|Color\|Vector\|nil` | Yes | Not documented. |

</div>

## Returns

| Type | Description |
| --- | --- |
| `Vector\|nil` | playerColor |

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:294</code>.</p>
