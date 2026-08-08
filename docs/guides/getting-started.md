# Getting started

## Requirements

Before developing a LADBot, install and enable:

- Garry's Mod
- LADSource
- DrGBase
- Any addon that supplies the models, animations, sounds, movesets, or heat
  actions used by your fighter

LADSource is built on DrGBase. A fighter entity will stop loading when either
dependency is unavailable, so dependency errors should be resolved before
debugging fighter code.

## Addon layout

A small fighter addon commonly starts with this structure:

```text
my-ladsource-addon/
└─ lua/
   └─ entities/
      └─ lad_my_fighter.lua
```

Movesets, heat actions, models, materials, and sounds can be added as the
fighter grows. Keeping your fighter in a separate addon makes LADSource updates
safer and makes the fighter easier to distribute.

## Development workflow

1. Create the fighter entity and verify that it appears in the spawn menu.
2. Give it a known model, faction, moveset, and voicebank.
3. Test spawning and basic combat before adding custom callbacks.
4. Add one system at a time and watch the Garry's Mod console for Lua errors.
5. Test both autonomous AI and possession when your fighter supports both.

The generated [framework reference](../reference/index.md) lists the methods
currently defined by `lad_framework_base`.
