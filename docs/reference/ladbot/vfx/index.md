# VFX

Methods defined in `lua/entities/lad_framework_base/vfx.lua`.

!!! info "Generated reference"

    This page is generated from the current Lua source. Add API annotations
    above a method in the source file to improve its documentation.

## Methods

<div class="api-method-list" markdown>

| Method | Summary |
| --- | --- |
| [`ENT:EnableLimbFlash`](enable-limb-flash.md) | Serverside caller for the Aura effect around specific limbs. Used internally by many functions in `moveset.lua` but can also be used externally where required. |
| [`ENT:GetGuardFX`](get-guard-fx.md) | Serverside caller that fires back to LAD:Source's internal events system to assert which sound is required if guarding against specific attacks with something specific in hand. |
| [`ENT:SetGreyscaleEffect`](set-greyscale-effect.md) | Serverside caller that makes everything, excluding the Player's current fighter, black and white. |
| [`ENT:VFX_Shock`](vfx-shock.md) | Triggers a simple "Tesla" visual effect from HL2 |
| [`ENT:VFX_SparkOnce`](vfx-spark-once.md) | Triggers a simple "Sparks" visual effect from HL2 |
| [`ENT:ChargeAura`](charge-aura.md) | Serverside caller for the Aura effect used when charging attacks. |
| [`ENT:CreateAfterImage`](create-after-image.md) | Serverside caller for the AfterImage system. Used by moveset properties to apply the after image effect to certain moves. |
| [`ENT:CreatePibTrail`](create-pib-trail.md) | An old remainant of the early trails system that served as a proof of concept. |
| [`ENT:DispatchAttackTrails`](dispatch-attack-trails.md) | Serverside tracker that dispatches active MeshTrails to their intended entities and bones. |
| [`ENT:DispatchLimbFlashes`](dispatch-limb-flashes.md) | Serverside tracker that dispatches active LimbFlashes to their intended entities and bones. |
| [`ENT:DispatchParticleTrails`](dispatch-particle-trails.md) | Serverside tracker that dispatches active ParticleTrails to their intended entities and bones. The system makes use of the ParticleTrail table which has its own unique parameters. This is passed via `moveset.lua`. |
| [`ENT:HeatAura`](heat-aura.md) | Serverside caller for the HeatAura system. Relies on the provided moveset in order to create a particle instance of the heat aura. |
| [`ENT:VFX_EjectShell`](vfx-eject-shell.md) | Creates the bullet shell cartrage at the specified position on an object. Used Internally. |
| [`ENT:VFX_HandSpark`](vfx-hand-spark.md) | Same as `VFX_SparkOnce`. |
| [`ENT:VFX_MeshTrail`](vfx-mesh-trail.md) | Serverside caller for the MeshTrail system. |
| [`ENT:VFX_WeaponSpark`](vfx-weapon-spark.md) | Same as `VFX_SparkOnce`, but this confines it to a weapon slot. |

</div>
