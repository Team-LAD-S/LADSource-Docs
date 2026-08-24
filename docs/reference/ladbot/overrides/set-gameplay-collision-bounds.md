---
title: "ENT:SetGameplayCollisionBounds"
---

[Back to Overrides](index.md)

<a id="ent-setgameplaycollisionbounds"></a>
# `ENT:SetGameplayCollisionBounds` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:SetGameplayCollisionBounds(mins, maxs)
```

</div>

SetCollisionBounds is affected by ModelScale on anim/NextBot entities. Keep
fighter navigation bounds in gameplay units so a larger visual model does not
grow an OBB corner into nearby map geometry when the AI turns in place.

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `mins` | `any` | Yes | Not documented. |
| `maxs` | `any` | Yes | Not documented. |

</div>

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/overrides.lua:68</code>.</p>
