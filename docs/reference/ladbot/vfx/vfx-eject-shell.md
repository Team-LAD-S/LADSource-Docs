---
title: "ENT:VFX_EjectShell"
status: realm-server
---

[Back to VFX](index.md)

<a id="ent-vfx-ejectshell"></a>
# `ENT:VFX_EjectShell` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:VFX_EjectShell(bulletVFX)
```

</div>

Creates the bullet shell cartrage at the specified position on an object. Used Internally.

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `bulletVFX` | `table` | Yes | Data used by the function to create a bullet shell at the specified point. |

</div>

### `bulletVFX` table fields

<div class="api-parameter-table api-parameter-fields" markdown>

| Key | Type | Required | Description |
| --- | --- | :---: | --- |
| `ShellEjectPos` | `string` | Yes | The attachment name where the bullet is to be ejected from. |
| `Shell` | `string` | Yes | The name of the effect you want to use. Falls back to `"ShellEject"`. |

</div>

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/vfx.lua:251</code>.</p>
