---
title: "ENT:ShouldIgnore"
status: realm-server
---

[Back to AI](index.md)

<a id="ent-shouldignore"></a>
# `ENT:ShouldIgnore` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span></div>

<div class="api-signature" markdown>

```lua
function ENT:ShouldIgnore(ent)
```

</div>

Belongs to DrGBase, whether the LADBot should ignore an entity.
Can be overriden to implement custom behavior.
By default currently checks if the LADBot should ignore other LADBots which are IsOverworldStationary().

## Example

```lua
function ENT:ShouldIgnore(ent)
	if IsValid(ent) and ent:GetIsLADFighter() and ent:IsOverworldStationary() then
		return true
	end
end
```

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `ent` | `any` | Yes | Not documented. |

</div>

## Returns

| Type | Description |
| --- | --- |
| `boolean` | True if the LADBot should ignore the entity, false otherwise. |

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/ai.lua:1662</code>.</p>
