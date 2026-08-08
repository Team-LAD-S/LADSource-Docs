---
title: "ENT:ActivateCombat"
---

[Back to Fighter Command](index.md)

<a id="ent-activatecombat"></a>
# `ENT:ActivateCombat` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span></div>

<div class="api-signature" markdown>

```lua
function ENT:ActivateCombat(target, skipanim)
```

</div>

Activates combat of a LADBot that this function is ran on.

## Parameters

| Name | Type | Description |
| --- | --- | --- |
| `target` | `ent` | Snaps to whoever activates combat |
| `skipanim` | `boolean` | Whether to skip the battle-start animation. |

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:778</code>.</p>
