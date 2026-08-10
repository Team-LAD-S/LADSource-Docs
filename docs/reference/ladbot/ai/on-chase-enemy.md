---
title: "ENT:OnChaseEnemy"
status: realm-server
---

[Back to AI](index.md)

<a id="ent-onchaseenemy"></a>
# `ENT:OnChaseEnemy` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span></div>

<div class="api-signature" markdown>

```lua
function ENT:OnChaseEnemy(enemy)
```

</div>

Belongs to DrGBase, called when the LADBot is chasing an enemy (inside the coroutine).
Can be overriden to implement custom behavior when the LADBot is chasing an enemy.
By default currently checks if the LADBot IsOverworldStationary() and returns true to stop chasing any other enemies.

## Example

```lua
function ENT:OnChaseEnemy(enemy)
	if self:IsOverworldStationary() then return true end
end
```

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `enemy` | `ent` | Yes | The enemy entity to check. |

</div>

## Returns

| Type | Description |
| --- | --- |
| `boolean` | True if the LADBot should stop chasing the enemy, false otherwise. |

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:1646</code>.</p>
