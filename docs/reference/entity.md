# Entity extensions

These methods extend Garry's Mod's `Entity` metatable, so they can be called on any entity and are not limited to LADBots.

Methods defined in `lua/lad_framework/meta.lua`.

!!! info "Generated reference"

    This page is generated from the current Lua source. Add API annotations
    above a method in the source file to improve its documentation.

## Methods

| Method | Summary |
| --- | --- |
| [`Entity:CheckDownedState`](#entity-checkdownedstate) | Documentation pending. |
| [`Entity:Defeated`](#entity-defeated) | Documentation pending. |
| [`Entity:GetIsLADFighter`](#entity-getisladfighter) | Returns true if this entity is a LADFighter (LADBot). |
| [`Entity:GetSideDirection`](#entity-getsidedirection) | Retrieves the side for an entity |
| [`Entity:HUDFindEntityName`](#entity-hudfindentityname) | function to find the name of an entity for HUD |
| [`Entity:LADS_GetHullRangeSquaredTo`](#entity-lads-gethullrangesquaredto) | Documentation pending. |
| [`Entity:LADS_GetHullRangeTo`](#entity-lads-gethullrangeto) | Documentation pending. |
| [`Entity:LADS_IsEnemyInFront`](#entity-lads-isenemyinfront) | Documentation pending. |
| [`Entity:LADS_IsInCone`](#entity-lads-isincone) | Documentation pending. |
| [`Entity:LADS_IsInRange`](#entity-lads-isinrange) | Documentation pending. |

<a id="entity-checkdownedstate"></a>
## `Entity:CheckDownedState`

<div class="api-badges"><span class="api-badge ">shared</span></div>

<div class="api-signature" markdown>

```lua
function Entity:CheckDownedState()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/lad_framework/meta.lua:24</code>.</p>

<a id="entity-defeated"></a>
## `Entity:Defeated`

<div class="api-badges"><span class="api-badge ">shared</span></div>

<div class="api-signature" markdown>

```lua
function Entity:Defeated()
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

This method takes no explicit arguments.

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/lad_framework/meta.lua:32</code>.</p>

<a id="entity-getisladfighter"></a>
## `Entity:GetIsLADFighter`

<div class="api-badges"><span class="api-badge ">server</span></div>

<div class="api-signature" markdown>

```lua
function Entity:GetIsLADFighter()
```

</div>

Returns true if this entity is a LADFighter (LADBot).

### Parameters

This method takes no explicit arguments.

### Returns

| Type | Description |
| --- | --- |
| `boolean` | IsLADFighter. |

<p class="api-source">Defined in <code>lua/lad_framework/meta.lua:88</code>.</p>

<a id="entity-getsidedirection"></a>
## `Entity:GetSideDirection`

<div class="api-badges"><span class="api-badge ">shared</span></div>

<div class="api-signature" markdown>

```lua
function Entity:GetSideDirection(side)
```

</div>

Retrieves the side for an entity

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `side` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/lad_framework/meta.lua:42</code>.</p>

<a id="entity-hudfindentityname"></a>
## `Entity:HUDFindEntityName`

<div class="api-badges"><span class="api-badge ">shared</span></div>

<div class="api-signature" markdown>

```lua
function Entity:HUDFindEntityName(entity)
```

</div>

function to find the name of an entity for HUD

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `entity` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/lad_framework/meta.lua:5</code>.</p>

<a id="entity-lads-gethullrangesquaredto"></a>
## `Entity:LADS_GetHullRangeSquaredTo`

<div class="api-badges"><span class="api-badge ">shared</span></div>

<div class="api-signature" markdown>

```lua
function Entity:LADS_GetHullRangeSquaredTo(pos)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `pos` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/lad_framework/meta.lua:79</code>.</p>

<a id="entity-lads-gethullrangeto"></a>
## `Entity:LADS_GetHullRangeTo`

<div class="api-badges"><span class="api-badge ">shared</span></div>

<div class="api-signature" markdown>

```lua
function Entity:LADS_GetHullRangeTo(pos)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `pos` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/lad_framework/meta.lua:74</code>.</p>

<a id="entity-lads-isenemyinfront"></a>
## `Entity:LADS_IsEnemyInFront`

<div class="api-badges"><span class="api-badge ">shared</span></div>

<div class="api-signature" markdown>

```lua
function Entity:LADS_IsEnemyInFront(enemy)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `enemy` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/lad_framework/meta.lua:100</code>.</p>

<a id="entity-lads-isincone"></a>
## `Entity:LADS_IsInCone`

<div class="api-badges"><span class="api-badge ">shared</span></div>

<div class="api-signature" markdown>

```lua
function Entity:LADS_IsInCone(ent, angle, distance, side, origin, direction)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `ent` | `any` | Not documented. |
| `angle` | `any` | Not documented. |
| `distance` | `any` | Not documented. |
| `side` | `any` | Not documented. |
| `origin` | `any` | Not documented. |
| `direction` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/lad_framework/meta.lua:61</code>.</p>

<a id="entity-lads-isinrange"></a>
## `Entity:LADS_IsInRange`

<div class="api-badges"><span class="api-badge ">shared</span></div>

<div class="api-signature" markdown>

```lua
function Entity:LADS_IsInRange(pos, range)
```

</div>

*Documentation pending. The signature and source location were generated automatically.*

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `pos` | `any` | Not documented. |
| `range` | `any` | Not documented. |

### Returns

No return values are documented.

<p class="api-source">Defined in <code>lua/lad_framework/meta.lua:70</code>.</p>
