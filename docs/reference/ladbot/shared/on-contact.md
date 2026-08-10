---
title: "ENT:OnContact"
status: realm-server
---

[Back to Shared](index.md)

<a id="ent-oncontact"></a>
# `ENT:OnContact` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span></div>

<div class="api-signature" markdown>

```lua
function ENT:OnContact(ent)
```

</div>

Belongs to DrGBase, code to run when the LADBot comes into contact with another entity.

By default currently checks if the entity is a LADBot and pushes it away, or pushes other entities away.
Also plays a bump animation if the entity is a LADBot and the LADBot is possessed and not in combat.

ENT:CustomOnContact(ent) is called at the end of this function, allowing for additional custom behavior.

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `ent` | `ent` | Yes | The entity to check. |

</div>

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:1099</code>.</p>
