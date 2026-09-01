---
title: "ENT:GetActiveCounterWindow"
---

[Back to Moveset](index.md)

<a id="ent-getactivecounterwindow"></a>
# `ENT:GetActiveCounterWindow` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetActiveCounterWindow()
```

</div>

Returns the CounterWindows entry which is currently open for this fighter's
selected attack animation. Each entry opens at Cycle and is consumed by the
next attack event, allowing one animation to expose several separate windows.

## Parameters

This method takes no explicit arguments.

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/moveset.lua:82</code>.</p>
