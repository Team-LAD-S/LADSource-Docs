---
title: "ENT:PlayBumpAnimation"
status: realm-server
---

[Back to Shared](index.md)

<a id="ent-playbumpanimation"></a>
# `ENT:PlayBumpAnimation` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:PlayBumpAnimation(anim)
```

</div>

CICO and PlaySequenceAndMove wrapper for bump animations. Plays the specified bump animation and sets self.IsBumped to true during the animation.

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `anim` | `string` | Yes | The name of the bump animation to play. |

</div>

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:1198</code>.</p>
