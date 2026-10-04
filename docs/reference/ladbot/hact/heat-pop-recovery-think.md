---
title: "ENT:HeatPopRecoveryThink"
---

[Back to HACT](index.md)

<a id="ent-heatpoprecoverythink"></a>
# `ENT:HeatPopRecoveryThink` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:HeatPopRecoveryThink(now)
```

</div>

Runs outside the behaviour coroutine: an interrupted callback cannot prevent
recovery. Also covers fighters overriding HeatPopBehavior directly.

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `now` | `any` | Yes | Not documented. |

</div>

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:1984</code>.</p>
