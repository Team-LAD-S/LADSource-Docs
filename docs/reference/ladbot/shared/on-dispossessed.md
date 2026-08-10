---
title: "ENT:OnDispossessed"
status: realm-server
---

[Back to Shared](index.md)

<a id="ent-ondispossessed"></a>
# `ENT:OnDispossessed` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span><span class="api-badge api-badge--internal">internal</span></div>

<div class="api-signature" markdown>

```lua
function ENT:OnDispossessed(ply)
```

</div>

Internal function called by DrGBase when the LADBot is dispossessed. Cleans up LADBot related stuff, namely
Player Fighter, weapon info and soundtrack.

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `ply` | `ent` | Yes | The player who dispossessed the LADBot. |

</div>

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:1318</code>.</p>
