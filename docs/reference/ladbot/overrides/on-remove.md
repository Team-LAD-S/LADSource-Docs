---
title: "ENT:OnRemove"
---

[Back to Overrides](index.md)

<a id="ent-onremove"></a>
# `ENT:OnRemove`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:OnRemove()
```

</div>

Weak keys handle GC cleanup, but CallOnRemove fires before GC so explicit nil is cleaner.

## Parameters

This method takes no explicit arguments.

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/overrides.lua:1915</code>.</p>
