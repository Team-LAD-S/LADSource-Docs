# Documenting the API

The API generator reads documentation comments immediately above `ENT` methods
inside `lua/entities/lad_framework_base`.

## Example

```lua
--- Starts combat against the supplied target.
---@realm server
---@param target Entity Fighter or NPC to engage.
---@param skipanim boolean Whether to skip the battle-start animation.
---@return boolean started Whether combat was started.
function ENT:ActivateCombat(target, skipanim)
    -- Implementation
end
```

The description uses lines beginning with `---`. Tags use `---@tag`.

## Supported tags

| Tag | Meaning |
| --- | --- |
| `---@realm server` | The method is server-only. `client` and `shared` are also accepted. |
| `---@param name Type description` | Documents an argument. |
| `---@return Type name description` | Documents a return value. The name is optional. |
| `---@internal` | Marks an implementation detail that addon developers should not call. |
| `---@callback` | Marks a method intended to be overridden by a LADBot. |
| `---@deprecated message` | Marks an obsolete method and explains what to use instead. |

Lua Language Server-compatible `param` and `return` tags are used where
possible. LADSource-specific tags such as `realm` and `callback` are ignored by
Lua itself and consumed by the documentation generator.

## Guidelines

- Describe observable behavior rather than restating the function name.
- State whether the method changes fighter state or starts asynchronous work.
- Document valid table fields when an argument accepts an options table.
- Mention required entity state, realm, and important side effects.
- Include an example when the correct call order is not obvious.
- Mark implementation helpers `internal` instead of silently publishing them as
  stable API.

Do not edit files under `docs/reference`; they are replaced during each build.
