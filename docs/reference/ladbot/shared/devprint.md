---
title: "devprint"
status: realm-server
---

[Back to Shared](index.md)

<a id="devprint"></a>
# `devprint` { .api-method-title }

<div class="api-badges"><span class="api-badge api-badge--server">server</span></div>

<div class="api-signature" markdown>

```lua
function devprint(string)
```

</div>

Prints debug information to the console if the developer mode is enabled. This is basically a wrapper for print() and PrintTable().

## Parameters

<div class="api-parameter-table" markdown>

| Name | Type | Required | Description |
| --- | --- | :---: | --- |
| `string` | `string/table` | Yes | The string or table to print. If it's a table, it will be printed using PrintTable. |

</div>

## Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:1380</code>.</p>
