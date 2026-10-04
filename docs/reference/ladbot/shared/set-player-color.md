---
title: "ENT:SetPlayerColor"
status: realm-shared
---

[Back to Shared](index.md)

<a id="ent-setplayercolor"></a>
# `ENT:SetPlayerColor` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--shared">shared</span></div>

<div class="api-signature" markdown>

```lua
function ENT:SetPlayerColor(color)
```

</div>

Sets the $color2 tint used by models with a PlayerColor material proxy.
Call this on the server when the color needs to be shared with every client.

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `color` | `Color\|Vector` | Yes | A Color (0-255) or normalized Vector (0-1). |

</div>

## Returns

| Type | Description |
| --- | --- |
| `Vector\|nil` | playerColor The normalized color, or nil for an invalid value. |

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:240</code>.</p>
