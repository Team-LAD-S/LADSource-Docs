---
title: "ENT:_FindVoidRecoveryPos"
status: realm-server
---

[Back to Shared](index.md)

<a id="ent-findvoidrecoverypos"></a>
# `ENT:_FindVoidRecoveryPos` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_FindVoidRecoveryPos(origin)
```

</div>

Internal function used by ENT:RecoverFromVoid().

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `origin` | `Vector` | Yes | The position to search for a recovery point. |

</div>

## Returns

| Type | Description |
| --- | --- |
| `Vector?` | The position to recover to, or nil if no valid position is found. |

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:693</code>.</p>
