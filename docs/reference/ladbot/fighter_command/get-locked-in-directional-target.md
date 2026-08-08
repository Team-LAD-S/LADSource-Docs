---
title: "ENT:GetLockedInDirectionalTarget"
---

[Back to Fighter Command](index.md)

<a id="ent-getlockedindirectionaltarget"></a>
# `ENT:GetLockedInDirectionalTarget`

<div class="api-badges"><span class="api-badge api-badge--not-documented">not documented</span></div>

<div class="api-signature" markdown>

```lua
function ENT:GetLockedInDirectionalTarget(dirSnapshot)
```

</div>

Returns the best enemy candidate in the direction the possessor is pressing (WASD, 8-way),
or nil if no suitable candidate passes all three filters:
1. Edge-triggered: caller only invokes this on a direction change (see PossessionThink).
2. Angular separation: candidate must be >20 degrees away from current target
(avoids switching between enemies that are essentially overlapping from our POV).
3. Hysteresis: candidate must outscore the current target by a margin of 0.15
(avoids switching to a marginally better-aligned enemy in a tight cluster).

## Parameters

| Name | Type | Description |
| --- | --- | --- |
| `dirSnapshot` | `any` | Not documented. |

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/fighter_command.lua:582</code>.</p>
