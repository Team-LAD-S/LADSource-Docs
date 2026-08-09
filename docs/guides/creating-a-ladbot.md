# Creating a LADBot

A LADBot is a DrGBase NextBot derived from `lad_framework_base`. Put the entity
in your addon's `lua/entities` directory.

## Minimal fighter

```lua
if not DrGBase or LADSource then return end

ENT.Base = "lad_framework_base"

ENT.PrintName = "My Fighter"
ENT.Category = "LADSource: Custom"
ENT.Models = {"models/example/my_fighter.mdl"}
ENT.Factions = {"YAK_PLAYER"}
ENT.SpawnHealth = 500

ENT.FighterMoveset = "MY_FIGHTER_MOVESET"
ENT.FighterVoicebank = "my_fighter"
ENT.FighterName = "My Fighter"

AddCSLuaFile()
DrGBase.AddNextbot(ENT)
```

Replace the example model, moveset, voicebank, and faction with content that is
available in your addon set.

## Overriding behavior

Methods defined by the base can be overridden on your fighter. For example:

```lua
function ENT:CustomFighterInitialize()
    self:SetSkin(1)
end
```

Some methods are callbacks intended for overrides while others are internal
implementation details. Check the method's reference page before overriding it.
Until a method is explicitly marked as public or as a callback, treat it as
unstable framework internals.

## Registering the fighter

`DrGBase.AddNextbot(ENT)` registers the scripted entity with DrGBase. LADSource
also has optional registration functions for specific modes, such as its arena
character list; those should only be used when the fighter is meant to appear in
that system.

## Next steps

- Browse the [generated framework reference](../reference/index.md).
- Read [Documenting the API](documenting-the-api.md) before contributing API
  descriptions.
- Use existing LADSource and LADSource-Yakuza0 fighters as working examples.
