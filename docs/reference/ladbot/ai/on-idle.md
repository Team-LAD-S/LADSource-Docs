---
title: "ENT:OnIdle"
status: realm-server
---

[Back to AI](index.md)

<a id="ent-onidle"></a>
# `ENT:OnIdle` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span></div>

<div class="api-signature" markdown>

```lua
function ENT:OnIdle()
```

</div>

Belongs to DrGBase, called after the LADBot successfully reaches its current patrol destination. (inside the coroutine).
Can be overriden to implement custom behavior.
By default currently waits for 1 second before setting self._patrolling to false.

## Parameters

This method takes no explicit arguments.

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:1688</code>.</p>
