# Soundtrack

Methods defined in `lua/entities/lad_framework_base/soundtrack.lua`.

!!! info "Generated reference"

    This page is generated from the current Lua source. Add API annotations
    above a method in the source file to improve its documentation.

## Methods

<div class="api-method-list" markdown>

| Method | Summary |
| --- | --- |
| [`ENT:GetActiveSoundtrackData`](get-active-soundtrack-data.md) | Returns { sdFile, weight } for the active style/moveset, falling back to defaults. Style-ID lookup is primary so temporary weapon/grab movesets do not override music. NOTE: SoundTracksByMoveset only accepts numeric style IDs (e.g., [1], [2], [3]). |
| [`ENT:SoundtrackEarlyStart`](soundtrack-early-start.md) | Public API: starts the combat soundtrack early without requiring FighterInCombat to be set. Pass directRecipient (Player) when the entity is not yet in a battle and not possessed (e.g. endless arena boss intro) so the track is delivered to the correct player. |
| [`ENT:SoundtrackMovesetUpdate`](soundtrack-moveset-update.md) | Checks if the active moveset changed the soundtrack and resends if so. Called from SetFighterMoveset (moveset.lua) after moveset initialises. Skips if a temporary weapon/grab moveset is active to avoid glitches during transitions. |
| [`ENT:_GetSoundtrackRecipients`](get-soundtrack-recipients.md) | Returns a list of all Player recipients for this entity's soundtrack events. Includes own possessor (if possessed and satisfies combatCheck) plus possessors of all other possessed fighters currently in the same battle. selfIgnoreCombat = true skips the FighterInCombat check for self only                     (used during battle-start anim where FighterInCombat is not yet set). |
| [`ENT:_LoadSoundtrackDef`](load-soundtrack-def.md) | Loads and caches a soundtrack definition file from data_static. Returns { name, hasEnd } or nil. |
| [`ENT:_SendSoundtrackStart`](send-soundtrack-start.md) | Sends LAD_SoundtrackStart to all eligible recipients (own possessor and battle allies' possessors). Pass ignoreCombatCheck = true to send before FighterInCombat is set (battle start anim path). Pass skipIntro = true to jump straight to the loop (used on moveset switches mid-combat). Pass waitForIntro = true to defer a moveset switch until the current _start intro finishes. Pass directRecipient (Player) to force-add a specific player when the entity is unpossessed and has no battle yet (e.g. endless boss intro). |
| [`ENT:_SendSoundtrackStop`](send-soundtrack-stop.md) | Sends LAD_SoundtrackStop to the possessing player |
| [`ENT:_SoundtrackActivateCombat`](soundtrack-activate-combat.md) | Called by ActivateCombat in fighter_command.lua (not a public hook). Skips sending if the soundtrack was already started during PlayBattleStartAnim. |
| [`ENT:_SoundtrackBattleStart`](soundtrack-battle-start.md) | Called from PlayBattleStartAnim in battle.lua when the intro anim/camera begins. Starts music early so it plays under the battle start animation. |
| [`ENT:_SoundtrackDeactivateCombat`](soundtrack-deactivate-combat.md) | Called by DeactivateCombat in fighter_command.lua (not a public hook) |
| [`ENT:_SoundtrackDeathThink`](soundtrack-death-think.md) | Called by DeathThink in events.lua (not a public hook) Sends the defeat signal exactly once to own possessor and all battle allies' possessors. |
| [`ENT:_SoundtrackOnDispossessed`](soundtrack-on-dispossessed.md) | Called by OnDispossessed in shared.lua (not a public hook) |
| [`ENT:_SoundtrackOnPossessed`](soundtrack-on-possessed.md) | Called by OnPossessed in fighter_command.lua (not a public hook) Sends own soundtrack if in combat, then syncs all other battle fighters to the new possessor. |
| [`ENT:_SoundtrackOnRemove`](soundtrack-on-remove.md) | Called by OnRemove in shared.lua (not a public hook) |

</div>
