---
title: "ENT:CreatePibTrail"
status: realm-server
---

[Back to VFX](index.md)

<a id="ent-createpibtrail"></a>
# `ENT:CreatePibTrail` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span><span class="api-badge api-badge--internal">internal</span><span class="api-badge api-badge--deprecated">deprecated</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CreatePibTrail(attachment_ID, Color_Table, Is_it_Additive, start_Width, end_Width, lifetime, Decay_Time, Path_To_Texture, Res)
```

</div>

An old remainant of the early trails system that served as a proof of concept.

!!! warning "Deprecated"

    Has been entirely replaced by VFX_MeshTrail, use that instead. This function will be removed in a later update.

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `attachment_ID` | `any` | Yes | Not documented. |
| `Color_Table` | `any` | Yes | Not documented. |
| `Is_it_Additive` | `any` | Yes | Not documented. |
| `start_Width` | `any` | Yes | Not documented. |
| `end_Width` | `any` | Yes | Not documented. |
| `lifetime` | `any` | Yes | Not documented. |
| `Decay_Time` | `any` | Yes | Not documented. |
| `Path_To_Texture` | `any` | Yes | Not documented. |
| `Res` | `any` | Yes | Not documented. |

</div>

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/vfx.lua:723</code>.</p>
