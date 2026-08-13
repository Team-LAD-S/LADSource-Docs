---
title: "ENT:DisplaySubtitle"
status: realm-server
---

[Back to Subtitles](index.md)

<a id="ent-displaysubtitle"></a>
# `ENT:DisplaySubtitle` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span></div>

<div class="api-signature" markdown>

```lua
function ENT:DisplaySubtitle(text, time, radius)
```

</div>

Yakuza Cutscene type subtitle text, called by LADBot and networked to all possessed LADBots in a radius.

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `text` | `string` | Yes | The subtitle text to display. |
| `time` | `number` | Yes | The duration to display the subtitle. |
| `radius` | `number` | Yes | The radius in which to display the subtitle. |

</div>

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/subtitles.lua:23</code>.</p>
