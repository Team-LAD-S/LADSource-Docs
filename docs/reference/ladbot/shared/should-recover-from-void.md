---
title: "ENT:_ShouldRecoverFromVoid"
status: realm-server
---

[Back to Shared](index.md)

<a id="ent-shouldrecoverfromvoid"></a>
# `ENT:_ShouldRecoverFromVoid` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:_ShouldRecoverFromVoid()
```

</div>

Internal function used by ENT:RecoverFromVoid().

## Parameters

This method takes no explicit arguments.

## Returns

| Type | Description |
| --- | --- |
| `boolean` | True if the LADBot should attempt to recover from being in the void, false otherwise. |

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:741</code>.</p>
