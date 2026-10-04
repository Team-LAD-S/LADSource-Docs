---
title: "ENT:PlayBulletGuardFX"
status: realm-server
---

[Back to VFX](index.md)

<a id="ent-playbulletguardfx"></a>
# `ENT:PlayBulletGuardFX` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span></div>

<div class="api-signature" markdown>

```lua
function ENT:PlayBulletGuardFX(attacker, hitPos)
```

</div>

Plays the standard guard feedback for a successfully blocked bullet.
GetGuardFX also dispatches the correct hand/weapon spark for the guard type.

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `attacker` | `ent` | Yes | The entity that fired the bullet. |
| `hitPos` | `Vector` | Yes | The bullet impact position. |

</div>

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/vfx.lua:445</code>.</p>
