---
title: "ENT:OnTraceAttack"
---

[Back to Events](index.md)

<a id="ent-ontraceattack"></a>
# `ENT:OnTraceAttack` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:OnTraceAttack(dmg, direction, tr)
```

</div>

Source generates character blood separately from LAD's damage feedback.
Suppress it at the victim for the duration of a guarded trace, then restore
the fighter's configured blood type after the bullet stack has completed.

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `dmg` | `any` | Yes | Not documented. |
| `direction` | `any` | Yes | Not documented. |
| `tr` | `any` | Yes | Not documented. |

</div>

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/events.lua:90</code>.</p>
