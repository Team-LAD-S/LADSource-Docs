# Shared

Methods defined in `lua/entities/lad_framework_base/shared.lua`.

!!! info "Generated reference"

    This page is generated from the current Lua source. Add API annotations
    above a method in the source file to improve its documentation.

## Methods

<div class="api-method-list" markdown>

| Method | Summary |
| --- | --- |
| [`ENT:CICO`](cico.md) | Call In Coroutine Override (CICO), originally created by NextBot developer Roach. Temporarily replaces LADBot's normal behavior coroutine with a callback. The callback may use yielding helpers such as PlaySequenceAndWait, allowing code to run sequentially before and after animations or other waits. Normal behavior remains paused until the callback returns, after which the previous behavior coroutine is restored if another system has not already replaced it. |
| [`ENT:CustomThink`](custom-think.md) | Only calls self:_InitDebugText(). Called internally only. |
| [`devprint`](devprint.md) | Prints debug information to the console if the developer mode is enabled. This is basically a wrapper for print() and PrintTable(). |
| [`ENT:GetPlayerColor`](get-player-color.md) | Retrieves "PlayerColor" on a LADBot. For example, PlayerColor is used to color the suit on the Dummy model. |
| [`ENT:IsFrozenProp`](is-frozen-prop.md) | Returns whether the given prop entity has motion disabled (i.e. frozen with Physgun). |
| [`ENT:IsPropLeftOrRight`](is-prop-left-or-right.md) | Returns whether the given prop entity is to the left or right side of a LADBot. Uses the cross product of the forward vector and the vector to the prop to determine the side. |
| [`ENT:Multithread`](multithread.md) | Cooperatively runs multiple callbacks as child coroutines and waits for all of them to finish. Each suspended callback is resumed once per update, allowing callbacks which yield to make progress alongside one another. This is not true parallel execution: a callback which never yields runs to completion before the next callback is resumed. Call this from a yieldable coroutine, such as a CICO callback. Return values are discarded, and errors raised by callbacks are not propagated by the current implementation. |
| [`ENT:OnContact`](on-contact.md) | Belongs to DrGBase, code to run when the LADBot comes into contact with another entity.  By default currently checks if the entity is a LADBot and pushes it away, or pushes other entities away. Also plays a bump animation if the entity is a LADBot and the LADBot is possessed and not in combat.  ENT:CustomOnContact(ent) is called at the end of this function, allowing for additional custom behavior. |
| [`ENT:OnSpawn`](on-spawn.md) | Belongs to DrGBase, called when the LADBot is spawned. Can be overriden to add custom behavior. |
| [`switch`](switch.md) | Switch statement implementation for Lua. |
| [`ENT:_FindVoidRecoveryPos`](find-void-recovery-pos.md) | Internal function used by ENT:RecoverFromVoid(). |
| [`ENT:_InitDebugText`](init-debug-text.md) | Initializes 3D debug text for the LADBot, displaying information such as moveset, faction, voicebank, health, and heat. Called internally only. |
| [`ENT:_InitMaterials`](init-materials.md) | Prints a material list for the LADBot. Temporary. Called internally only. |
| [`ENT:_ShouldRecoverFromVoid`](should-recover-from-void.md) | Internal function used by ENT:RecoverFromVoid(). |
| [`ENT:BumpAnim`](bump-anim.md) | Code handling what bump animations should play when the LADBot comes into contact with another entity.  ENT:OnBumpAnim(ent) is called at the end of this function, allowing for additional custom behavior. |
| [`ENT:CreateDirectionCompass`](create-direction-compass.md) | Creates a small invisible cube attached to the LADBot which can be used as a reference for direction. This is only used for debugging. |
| [`ENT:CustomDraw`](custom-draw.md) | Seems unused. |
| [`ENT:CustomInitialize`](custom-initialize.md) | Sets up the LADBot. Use ENT:CustomFighterInitialize() to set up custom variables and other stuff for your fighter. |
| [`ENT:DebugDrawCone`](debug-draw-cone.md) | Draws a debug cone. Must enable `developer` mode to see the cone. |
| [`ENT:LoadData`](load-data.md) | Loads a data asset. |
| [`ENT:OnDispossessed`](on-dispossessed.md) | Internal function called by DrGBase when the LADBot is dispossessed. Cleans up LADBot related stuff, namely Player Fighter, weapon info and soundtrack. |
| [`ENT:OnRemove`](on-remove.md) | Serverside clean up function. Called automatically by DrGBase, cleans up LADBot related stuff, use ENT:CustomOnRemove() to clean up any additional things you may need. |
| [`ENT:PlayBumpAnimation`](play-bump-animation.md) | CICO and PlaySequenceAndMove wrapper for bump animations. Plays the specified bump animation and sets self.IsBumped to true during the animation. |
| [`ENT:RecoverFromVoid`](recover-from-void.md) | More aggressive function which attempts to recover LADBot from out of bounds. Called internally by ENT:CustomThink(). |
| [`ENT:SetNexbotColor`](set-nexbot-color.md) | Unimplemented/redundant, sets the color of the LADBot. Called internally only. |
| [`ENT:UpdateTransmitState`](update-transmit-state.md) | Called whenever the transmit state should be updated. Default GLua Entity function. |

</div>
