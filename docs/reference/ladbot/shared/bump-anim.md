---
title: "ENT:BumpAnim"
status: realm-server
---

[Back to Shared](index.md)

<a id="ent-bumpanim"></a>
# `ENT:BumpAnim` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:BumpAnim(ent)
```

</div>

Code handling what bump animations should play when the LADBot comes into contact with another entity.

ENT:OnBumpAnim(ent) is called at the end of this function, allowing for additional custom behavior.

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `ent` | `ent` | Yes | The entity passed from OnContact which triggered the bump animation. |

</div>

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:1131</code>.</p>
