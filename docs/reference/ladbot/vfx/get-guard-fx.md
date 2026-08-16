---
title: "ENT:GetGuardFX"
status: realm-server
---

[Back to VFX](index.md)

<a id="ent-getguardfx"></a>
# `ENT:GetGuardFX` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetGuardFX(attacker, attackData)
```

</div>

Serverside caller that fires back to LAD:Source's internal events system to assert which sound is required if guarding against specific attacks with something specific in hand.

!!! warning "Warning"

    It is reccommended never to use this as it is an internal function. Instead, rely on passing "GuardSound" in the actual weapon's table.

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `attacker` | `ent` | Yes | The entity that is currently attacking us and we need to assert it to figure out what sound we need to fire based on what we are holding and what they are holding. |
| `attackData` | `table` | Yes | The table that contains data about this specific attack being applied to us. (Refer to `events_anim.lua` for the full table used here.) |

</div>

## Returns

| Type | Description |
| --- | --- |
| `sound` | The path to the sound that is to be played based on what you are holding and what you are being attacked with. |

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/vfx.lua:307</code>.</p>
