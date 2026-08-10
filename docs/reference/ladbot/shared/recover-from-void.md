---
title: "ENT:RecoverFromVoid"
status: realm-server
---

[Back to Shared](index.md)

<a id="ent-recoverfromvoid"></a>
# `ENT:RecoverFromVoid` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:RecoverFromVoid()
```

</div>

More aggressive function which attempts to recover LADBot from out of bounds. Called internally by ENT:CustomThink().

## Parameters

This method takes no explicit arguments.

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:786</code>.</p>
