---
title: "ENT:_RagdollApplyHitImpulse"
---

[Back to Ragdoll](index.md)

<a id="ent-ragdollapplyhitimpulse"></a>
# `ENT:_RagdollApplyHitImpulse` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_RagdollApplyHitImpulse(hitPos, impulse)
```

</div>

Applies a physics impulse to the active ragdoll at the nearest bone to hitPos.
Used by ApplyAttackDamage to make the ragdoll react to incoming hits.

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `hitPos` | `any` | Yes | Not documented. |
| `impulse` | `any` | Yes | Not documented. |

</div>

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ragdoll.lua:559</code>.</p>
