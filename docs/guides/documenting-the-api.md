# Documenting the API

The API generator reads documentation comments immediately above LADBot `ENT`
methods, shared Entity metatable methods in `meta.lua`, and Battle Manager
methods in `battle_manager.lua`.

Documented, non-local functions declared with `function Name(...)` inside a
LADBot module are also included on that module's reference page. They must have
a structured `---` documentation block; ordinary comments and `local function`
helpers are ignored.

## Example

```lua
--- Activates combat of a LADBot that this function is ran on.
---@realm server
---@param target ent Snaps to whoever activates combat
---@param skipanim boolean Whether to skip the battle-start animation.
function ENT:ActivateCombat(target, skipanim)
    -- Implementation
end
```

The description uses lines beginning with `---`. Tags use `---@tag`.

## Supported tags

| Tag | Meaning |
| --- | --- |
| `---@realm server` | The method is server-only. `client` and `shared` are also accepted. |
| `---@param name Type description` | Documents a required argument. Add `?` after the name for an optional parameter. |
| `---@field argument.key Type description` | Documents a required key accepted by a table argument. Add `?` after the key for an optional field. |
| `---@return Type name description` | Documents a return value. The name is optional. |
| `---@example Optional title` | Starts a multiline Lua example. Following documentation lines contain its code. Repeat the tag to add another example. |
| `---@internal` | Marks an implementation detail that addon developers should not call. |
| `---@callback` | Marks a method intended to be overridden by a LADBot. |
| `---@deprecated message` | Marks an obsolete method and explains what to use instead. |

Lua Language Server-compatible `param` and `return` tags are used where
possible. LADSource-specific tags such as `realm` and `callback` are ignored by
Lua itself and consumed by the documentation generator.

Table fields are rendered in their own section on the method page. Prefix the
field name with its argument name so the generator can associate the key with
the correct table when a method accepts more than one table.

Optional method parameters use the same `?` convention:

```lua
---@param target ent Required target entity.
---@param skipAnimation? boolean Whether to skip the intro animation.
function ENT:StartExample(target, skipAnimation)
end
```

```lua
--- Configures an attack from an options table.
---@param options table Attack configuration.
---@field options.damage number Damage dealt by the attack.
---@field options.hitDelay? number Delay before the hit becomes active.
---@field options.ignoreGuard? boolean Whether the attack bypasses guarding.
function ENT:ConfigureAttack(options)
    -- Implementation
end
```

Examples are written last in the documentation block. Every documentation line
after `---@example` is treated as Lua code until another tag begins. An optional
title is useful when a method needs more than one example.

```lua
--- Runs state changes in sequence around an animation.
---@realm server
---@example Playing an animation
---self:CICO(function(self)
---    self.IsAttacking = true
---    self:PlaySequenceAndWait("attack_animation")
---    self.IsAttacking = false
---end)
function ENT:CICO(callback)
end
```

## Guidelines

- Describe observable behavior rather than restating the function name.
- State whether the method changes fighter state or starts asynchronous work.
- Document valid table fields when an argument accepts an options table.
- Mention required entity state, realm, and important side effects.
- Include an example when the correct call order is not obvious.
- Mark implementation helpers `internal` instead of silently publishing them as
  stable API.

Do not edit files under `docs/reference`; they are replaced whenever the
reference generator runs.
