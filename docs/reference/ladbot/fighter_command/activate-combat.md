---
title: "ENT:ActivateCombat"
status: realm-server
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

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `target` | `ent` | Yes | Snaps to whoever activates combat |
| `skipanim` | `boolean` | Yes | Whether to skip the battle-start animation. |

</div>

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:767</code>.</p>
