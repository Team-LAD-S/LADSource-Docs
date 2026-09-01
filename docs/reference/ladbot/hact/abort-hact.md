---
title: "ENT:AbortHact"
---

[Back to HACT](index.md)

<a id="ent-aborthact"></a>
# `ENT:AbortHact` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:AbortHact()
```

</div>

Cleans up a mid-hact state when the activator dies before the hact finishes normally.
Without this, subjects remain stuck in IsInHact = true indefinitely.

## Parameters

This method takes no explicit arguments.

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/hact.lua:3513</code>.</p>
