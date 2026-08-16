---
title: "ENT:CreateAfterImage"
status: realm-server
---

[Back to VFX](index.md)

<a id="ent-createafterimage"></a>
# `ENT:CreateAfterImage` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:CreateAfterImage(color, mat, customFadeTime, drawChildOnly, NoBlurPass)
```

</div>

Serverside caller for the AfterImage system. Used by moveset properties to apply the after image effect to certain moves.

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `color` | `Color(R,G,B)` | Yes | The color of the AfterImage. |
| `mat` | `string` | No | Path to the material you want this after image to use. If a material was applied by the Material Tool to this model, it will use that by default, however this can also override that for the specific after image. |
| `customFadeTime` | `any` | Yes | Not documented. |
| `drawChildOnly` | `bool` | No | Only draw parented children to a model in this after image instance. |
| `NoBlurPass` | `bool` | No | Don't apply a blur effect to the model, if enabled. |

</div>

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/vfx.lua:793</code>.</p>
