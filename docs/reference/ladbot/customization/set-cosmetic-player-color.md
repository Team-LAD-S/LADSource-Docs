---
title: "ENT:SetCosmeticPlayerColor"
status: realm-server
---

[Back to Customization](index.md)

<a id="ent-setcosmeticplayercolor"></a>
# `ENT:SetCosmeticPlayerColor` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span></div>

<div class="api-signature" markdown>

```lua
function ENT:SetCosmeticPlayerColor(cosmetic, palette)
```

</div>

Sets a cosmetic's networked $color2 tint. Without a palette it inherits this fighter's tint.

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `cosmetic` | `Entity` | Yes | Not documented. |
| `palette` | `string\|function\|table\|Color\|Vector\|nil` | Yes | Not documented. |

</div>

## Returns

| Type | Description |
| --- | --- |
| `Vector\|nil` | playerColor |

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/customization.lua:151</code>.</p>
