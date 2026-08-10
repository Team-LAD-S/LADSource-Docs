# HACT

Methods defined in `lua/entities/lad_framework_base/hact.lua`.

!!! info "Generated reference"

    This page is generated from the current Lua source. Add API annotations
    above a method in the source file to improve its documentation.

## Methods

<div class="api-method-list" markdown>

| Method | Summary |
| --- | --- |
| [`ENT:AbortHact`](abort-hact.md) | Cleans up a mid-hact state when the activator dies before the hact finishes normally. Without this, subjects remain stuck in IsInHact = true indefinitely. |
| [`ENT:AddHeat`](add-heat.md) | Documentation pending. |
| [`ENT:CacheAvailableHacts`](cache-available-hacts.md) | Documentation pending. |
| [`ENT:CanForcePositionToNearestWall`](can-force-position-to-nearest-wall.md) | Documentation pending. |
| [`ENT:CleanupHactViewState`](cleanup-hact-view-state.md) | Documentation pending. |
| [`ENT:ConsumeHeat`](consume-heat.md) | Documentation pending. |
| [`ENT:DeductHeat`](deduct-heat.md) | Documentation pending. |
| [`ENT:DetectEnvironment`](detect-environment.md) | Documentation pending. |
| [`ENT:EndHact`](end-hact.md) | Documentation pending. |
| [`ENT:EndHactViews`](end-hact-views.md) | Documentation pending. |
| [`ENT:ExecuteHact`](execute-hact.md) | Documentation pending. |
| [`ENT:FindNearestNavWall`](find-nearest-nav-wall.md) | Documentation pending. |
| [`ENT:FindSafePosition`](find-safe-position.md) | Documentation pending. |
| [`ENT:ForcePositionToNearestWall`](force-position-to-nearest-wall.md) | Documentation pending. |
| [`ENT:GetAvailableHactActions`](get-available-hact-actions.md) | Documentation pending. |
| [`ENT:GetBlueHeatBarCount`](get-blue-heat-bar-count.md) | Documentation pending. |
| [`ENT:GetBlueHeatBarValue`](get-blue-heat-bar-value.md) | Documentation pending. |
| [`ENT:GetCurrentHeatGear`](get-current-heat-gear.md) | Documentation pending. |
| [`ENT:GetForcePositionToWallCandidate`](get-force-position-to-wall-candidate.md) | Documentation pending. |
| [`ENT:GetForcePositionToWallSearchParams`](get-force-position-to-wall-search-params.md) | Documentation pending. |
| [`ENT:GetHact`](get-hact.md) | Documentation pending. |
| [`ENT:GetHactCameraDataEntry`](get-hact-camera-data-entry.md) | Documentation pending. |
| [`ENT:GetHactCamPos`](get-hact-cam-pos.md) | Documentation pending. |
| [`ENT:GetHactFrameProgressionEntry`](get-hact-frame-progression-entry.md) | Documentation pending. |
| [`ENT:GetHeat`](get-heat.md) | Documentation pending. |
| [`ENT:GetHeatGearCount`](get-heat-gear-count.md) | Documentation pending. |
| [`ENT:GetHeatGearForAmount`](get-heat-gear-for-amount.md) | Documentation pending. |
| [`ENT:GetHeatSystemType`](get-heat-system-type.md) | Documentation pending. |
| [`ENT:GetMaxHeat`](get-max-heat.md) | Documentation pending. |
| [`ENT:GetNetworkedBlueHeatBarCount`](get-networked-blue-heat-bar-count.md) | Documentation pending. |
| [`ENT:GetNetworkedBlueHeatBarValue`](get-networked-blue-heat-bar-value.md) | Documentation pending. |
| [`ENT:GetNetworkedHeat`](get-networked-heat.md) | Documentation pending. |
| [`ENT:GetNetworkedHeatGearCount`](get-networked-heat-gear-count.md) | Documentation pending. |
| [`ENT:GetNetworkedHeatSystemType`](get-networked-heat-system-type.md) | Documentation pending. |
| [`ENT:GetNetworkedRedHeatBarCount`](get-networked-red-heat-bar-count.md) | Documentation pending. |
| [`ENT:GetRedHeatAmount`](get-red-heat-amount.md) | Documentation pending. |
| [`ENT:GetRedHeatBarCount`](get-red-heat-bar-count.md) | Documentation pending. |
| [`ENT:GetRedHeatStart`](get-red-heat-start.md) | Documentation pending. |
| [`ENT:GetWallHactFaceAwayFromWall`](get-wall-hact-face-away-from-wall.md) | Documentation pending. |
| [`ENT:GetWallHactReferenceEntity`](get-wall-hact-reference-entity.md) | Documentation pending. |
| [`ENT:HactBridge`](hact-bridge.md) | Documentation pending. |
| [`ENT:HactBridgeTo`](hact-bridge-to.md) | Documentation pending. |
| [`ENT:HactExists`](hact-exists.md) | Documentation pending. |
| [`ENT:HactFOVEvent`](hact-fov-event.md) | Documentation pending. |
| [`ENT:HeatPopBehavior`](heat-pop-behavior.md) | Documentation pending. |
| [`ENT:HeatThink`](heat-think.md) | Documentation pending. |
| [`ENT:IsInRedHeat`](is-in-red-heat.md) | Documentation pending. |
| [`ENT:LAD_HactEventFramesHasKey`](lad-hact-event-frames-has-key.md) | Documentation pending. |
| [`ENT:LAD_HactEventFramesUseDamageEvents`](lad-hact-event-frames-use-damage-events.md) | Documentation pending. |
| [`ENT:LAD_ShouldSuppressHactModelEvent`](lad-should-suppress-hact-model-event.md) | Documentation pending. |
| [`ENT:PlayDynamicIntro`](play-dynamic-intro.md) | Documentation pending. |
| [`ENT:PlayLocalSound`](play-local-sound.md) | Documentation pending. |
| [`ENT:PlayVictimHact`](play-victim-hact.md) | Documentation pending. |
| [`ENT:PopHeat`](pop-heat.md) | Documentation pending. |
| [`ENT:PosToWall`](pos-to-wall.md) | Documentation pending. |
| [`ENT:RefreshHactBridgeViewers`](refresh-hact-bridge-viewers.md) | Documentation pending. |
| [`ENT:RemoveHeatAura`](remove-heat-aura.md) | Documentation pending. |
| [`ENT:ResetHactEventFrames`](reset-hact-event-frames.md) | Documentation pending. |
| [`ENT:ResetHactViewFOV`](reset-hact-view-fov.md) | Documentation pending. |
| [`ENT:ResetHeatDecayTimers`](reset-heat-decay-timers.md) | Documentation pending. |
| [`ENT:RunHactEventFrame`](run-hact-event-frame.md) | Documentation pending. |
| [`ENT:ScanAndExecuteHacts`](scan-and-execute-hacts.md) | Documentation pending. |
| [`ENT:SendHactView`](send-hact-view.md) | Documentation pending. |
| [`ENT:SetHactBridge`](set-hact-bridge.md) | Documentation pending. |
| [`ENT:SetHeat`](set-heat.md) | Documentation pending. |
| [`ENT:StartHactBridgeAnimation`](start-hact-bridge-animation.md) | Documentation pending. |
| [`ENT:StartHactFrameProgression`](start-hact-frame-progression.md) | Documentation pending. |
| [`ENT:StartHeatDecayTimer`](start-heat-decay-timer.md) | Documentation pending. |
| [`ENT:StopHactFrameProgression`](stop-hact-frame-progression.md) | Documentation pending. |
| [`ENT:SyncHeatNetworkVars`](sync-heat-network-vars.md) | Documentation pending. |
| [`ENT:UpdateHactEventFrames`](update-hact-event-frames.md) | Documentation pending. |
| [`ENT:UpdateHactFrameBridge`](update-hact-frame-bridge.md) | Documentation pending. |
| [`ENT:UpdateHactSubjectEventFrames`](update-hact-subject-event-frames.md) | Documentation pending. |
| [`ENT:UpdateHeatAura`](update-heat-aura.md) | Documentation pending. |
| [`ENT:UpdateHeatHUD`](update-heat-hud.md) | Documentation pending. |
| [`ENT:UpdateHeatPopAura`](update-heat-pop-aura.md) | Documentation pending. |

</div>
