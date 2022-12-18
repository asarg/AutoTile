
from UniversalClasses import State
from Assets.colors import *

# Border
border_state = State("Border", rosy_brown, " ")
northCorner = State("NorthCorner", rosy_brown, "╔")
southCorner = State("SouthCorner", rosy_brown, "╚")
# Wires
northWire = State("NorthWire", wire_color, "🡹")
southWire = State("SouthWire", wire_color, "🡻")
westWire = State("WestWire", wire_color, "🡸")
eastWire = State("EastWire", wire_color, "🡺")

northEastWire = State("NorthEastWire", wire_color, "🡹🡺")
northWestWire = State("NorthWestWire", wire_color, "🡹🡸")
southEastWire = State("SouthEastWire", wire_color, "🡻🡺")
southWestWire = State("SouthWestWire", wire_color, "🡻🡸")

northProtectedWire = State("NorthProtectedWire", wire_color, "|🡹|")
southProtectedWire = State("SouthProtectedWire", wire_color, "|🡻|")
eastProtectedWire = State("EastProtectedWire", wire_color, "|🡺|")
westProtectedWire = State("WestProtectedWire", wire_color, "|🡸|")
northEastProtectedWire = State("NorthEastProtectedWire", wire_color, "|🡹🡺|")
northWestProtectedWire = State("NorthWestProtectedWire", wire_color, "|🡹🡸|")
southEastProtectedWire = State("SouthEastProtectedWire", wire_color, "|🡻🡺|")
southWestProtectedWire = State("SouthWestProtectedWire", wire_color, "|🡻🡸|")

protectWireWalker = State("ProtectWireWalker", writing_color, "|✑|")

northCopyWire = State("NorthCopyWire", light_blue, "⇈")
southCopyWire = State("SouthCopyWire", light_blue, "⇊")
westCopyWire = State("WestCopyWire", light_blue, "⇇")
eastCopyWire = State("EastCopyWire", light_blue, "⇉")

checkCopyWireReachedInactive = State("CheckCopyWireReachedInactive", inactive_color, "*⇈")

# Signal Wire and states
verticalMacroCellDoorOpenSignal = State("VerticalMacroCellDoorOpenSignal", atomic_tangerine, "⭥⟥")
horizontalMacroCellDoorOpenSignal = State("HorizontalMacroCellDoorOpenSignal", atomic_tangerine, "⭤ ⟥")

writeOneInactive = State("WriteOneInactive", inactive_color, "1✑")
writeZeroInactive = State("WriteZeroInactive", inactive_color, "0✑")
writeOneWaiting = State("WriteOneWaiting", waiting_color, "1✑")
writeZeroWaiting = State("WriteZeroWaiting", waiting_color, "0✑")
writeOne = State("WriteOneActive", writing_color, "1✑")
writeZero = State("WriteZeroActive", writing_color, "0✑")
writeOneActivateNext = State("WriteOneActivateNext", activate_next_color, "1✑")
writeZeroActivateNext = State("WriteZeroActivateNext", activate_next_color, "0✑")
writeOneComplete = State("WriteOneComplete", complete_color, "1✑")
writeZeroComplete = State("WriteZeroComplete", complete_color, "0✑")
writeOneReset = State("WriteOneReset", waiting_color, "↺1✑")
writeZeroReset = State("WriteZeroReset", waiting_color, "↺0✑")

writeNorthPrefix = State("WriteNorthPrefix", writing_color, "𝗡✑")
writeSouthPrefix = State("WriteSouthPrefix", writing_color, "𝗦✑")
writeWestPrefix = State("WriteWestPrefix", writing_color, "𝗪✑")
writeEastPrefix = State("WriteEastPrefix", writing_color, "𝗘✑")

writeNorthPrefixInactive = State("WriteNorthPrefixInactive", inactive_color, "𝗡✑")
writeSouthPrefixInactive = State("WriteSouthPrefixInactive", inactive_color, "𝗦✑")
writeWestPrefixInactive = State("WriteWestPrefixInactive", inactive_color, "𝗪✑")
writeEastPrefixInactive = State("WriteEastPrefixInactive", inactive_color, "𝗘✑")

writeNorthPrefixWaiting = State("WriteNorthPrefixWaiting", waiting_color, "𝗡✑")
writeSouthPrefixWaiting = State("WriteSouthPrefixWaiting", waiting_color, "𝗦✑")
writeEastPrefixWaiting = State("WriteEastPrefixWaiting", waiting_color, "𝗘✑")
writeWestPrefixWaiting = State("WriteWestPrefixWaiting", waiting_color, "𝗪✑")

writeNorthPrefixActivateNext = State("WriteNorthPrefixActivateNext", activate_next_color, "𝗡✑")
writeSouthPrefixActivateNext = State("WriteSouthPrefixActivateNext", activate_next_color, "𝗦✑")
writeWestPrefixActivateNext = State("WriteWestPrefixActivateNext", activate_next_color, "𝗪✑")
writeEastPrefixActivateNext = State("WriteEastPrefixActivateNext", activate_next_color, "𝗘✑")

writeNorthPrefixComplete = State("WriteNorthPrefixComplete", complete_color, "𝗡✑")
writeSouthPrefixComplete = State("WriteSouthPrefixComplete", complete_color, "𝗦✑")
writeEastPrefixComplete = State("WriteEastPrefixComplete", complete_color, "𝗘✑")
writeWestPrefixComplete = State("WriteWestPrefixComplete", complete_color, "𝗪✑")

writeNorthPrefixReset = State("WriteNorthPrefixReset", waiting_color, "↺𝗡✑")
writeSouthPrefixReset = State("WriteSouthPrefixReset", waiting_color, "↺𝗦✑")
writeEastPrefixReset = State("WriteEastPrefixReset", waiting_color, "↺𝗘✑")
writeWestPrefixReset = State("WriteWestPrefixReset", waiting_color, "↺𝗪✑")

writeStartStateInactive = State("WriteStartStateInactive", inactive_color, "(✑")
writeEndStateInactive = State("WriteEndStateInactive", inactive_color, ")✑")
writeStartStatePairInactive = State("WriteStartStatePairInactive", inactive_color, "[✑")
writeEndStatePairInactive = State("WriteEndStatePairInactive", inactive_color, "]✑")
writeStateDataStringInactive = State("WriteStateDataStringInactive", inactive_color, "✑❲")
writeEndDataStringInactive = State("WriteEndDataStringInactive", inactive_color, "✑❳")

writeStartStateActivateNext = State("WriteStartStateActivateNext", activate_next_color, "(✑")
writeEndStateActivateNext = State("WriteEndStateActivateNext", activate_next_color, ")✑")
writeStartStatePairActivateNext = State("WriteStartStatePairActivateNext", activate_next_color, "[✑")
writeEndStatePairActivateNext = State("WriteEndStatePairActivateNext", activate_next_color, "]✑")
writeStartDataStringActivateNext = State("WriteStartDataStringActivateNext", activate_next_color, "✑❲")
writeEndDataStringActivateNext = State("WriteEndDataStringActivateNext", activate_next_color, "✑❳")

writeStartStateWaiting = State("WriteStartStateWaiting", waiting_color, "(✑")
writeEndStateWaiting = State("WriteEndStateWaiting", waiting_color, ")✑")
writeStartStatePairWaiting = State("WriteStartStatePairWaiting", waiting_color, "[✑")
writeEndStatePairWaiting = State("WriteEndStatePairWaiting", waiting_color, "]✑")
writeStartDataStringWaiting = State("WriteStartDataStringWaiting", waiting_color, "✑❲")
writeEndDataStringWaiting = State("WriteEndDataStringWaiting", waiting_color, "✑❳")

writeStartState = State("WriteStartState", writing_color, "(✑")
writeEndState = State("WriteEndState", writing_color, ")✑")
writeStartStatePair = State("WriteStartStatePair", writing_color, "[✑")
writeEndStatePair = State("WriteEndStatePair", writing_color, "]✑")
writeStartDataString = State("WriteStartDataString", writing_color, "✑❲")
writeEndDataString = State("WriteEndDataString", writing_color, "✑❳")

writeStartDataStringComplete = State("WriteStartDataStringComplete", complete_color, "✑❲")
writeEndDataStringComplete = State("WriteStartDataStringComplete", complete_color, "✑❳")
writeStartStateComplete = State("WriteStartStateComplete", complete_color, "(✑")
writeEndStateComplete = State("WriteEndStateComplete", complete_color, ")✑")
writeStartStatePairComplete = State("WriteStartStatePairComplete", complete_color, "[✑")
writeEndStatePairComplete = State("WriteEndStatePairComplete", complete_color, "]✑")

write_data_states = [writeOneInactive, writeZeroInactive, writeOneActivateNext, writeZeroActivateNext, writeOneWaiting, writeZeroWaiting, writeOne, writeZero, writeOneComplete, writeZeroComplete, writeOneReset, writeZeroReset]
write_data_states_dirs = [writeEastPrefixInactive, writeWestPrefixInactive, writeNorthPrefixInactive, writeSouthPrefixInactive, writeEastPrefixActivateNext, writeWestPrefixActivateNext, writeNorthPrefixActivateNext, writeSouthPrefixActivateNext, writeEastPrefixWaiting, writeWestPrefixWaiting, writeNorthPrefixWaiting, writeSouthPrefixWaiting, writeEastPrefix, writeWestPrefix, writeNorthPrefix, writeSouthPrefix, writeEastPrefixComplete, writeWestPrefixComplete, writeNorthPrefixComplete, writeSouthPrefixComplete, writeEastPrefixReset, writeWestPrefixReset, writeNorthPrefixReset, writeSouthPrefixReset]
write_data_states_caps = [writeStartStateInactive, writeStartState, writeStartStateActivateNext, writeStartStateWaiting, writeStartStateComplete, writeEndStateInactive, writeEndState, writeEndStateActivateNext, writeEndStateWaiting, writeEndStateComplete, writeStartStatePairInactive, writeStartStatePair, writeStartStatePairActivateNext, writeStartStatePairWaiting, writeStartStatePairComplete, writeEndStatePairInactive, writeEndStatePair, writeEndStatePairActivateNext, writeEndStatePairWaiting, writeEndStatePairComplete, writeStartDataString, writeStartDataStringActivateNext, writeStartDataStringWaiting, writeStartDataStringComplete, writeEndDataStringInactive, writeEndDataString, writeEndDataStringActivateNext, writeEndDataStringWaiting, writeEndDataStringComplete]
writeStatesAll = write_data_states + write_data_states_dirs + write_data_states_caps
writeDoorInactive = State("WriteDoorInactive", inactive_color, "✑🚪")
writeDoorActive = State("WriteDoorActive", active_color, "✑🚪")


# Check For Num Equality
confirm_for_any_num = State("ConfirmForEqualityAnyNum", complete_color, "=*")
confirm_for_equality_zero = State("ConfirmForEqualityZero", complete_color, "=0")
confirm_for_equality_one = State("ConfirmForEqualityOne", complete_color, "=1")

check_for_any_num = State("CheckForEqualityAnyNum", mid_pink, "=*")
check_for_equality_zero = State("CheckForEqualityZero", mid_pink, "=0")
check_for_equality_one = State("CheckForEqualityOne", mid_pink, "=1")

check_for_any_num_inactive = State("CheckForEqualityAnyNum_Inactive", grey_pink, "=*")
check_for_equality_zero_inactive = State("CheckForEqualityZero_Inactive", grey_pink, "=0")
check_for_equality_one_inactive = State("CheckForEqualityOne_Inactive", grey_pink, "=1")


# Check For Prefixes
check_equality_inactive = State("CheckEqualityInactive", grey_pink, "=")
check_for_any_prefix_inactive = State("CheckForAnyPrefix", grey_pink, "=*ₚ")
check_for_N_prefix_inactive = State("CheckForNPrefixInactive", grey_pink, "=Nₚ")
check_for_S_prefix_inactive = State("CheckForSPrefixInactive", grey_pink, "=Sₚ")
check_for_E_prefix_inactive = State("CheckForEPrefixInactive", grey_pink, "=Eₚ")
check_for_W_prefix_inactive = State("CheckForWPrefixInactive", grey_pink, "=Wₚ")
check_for_P_prefix_inactive = State("CheckForProgramPrefixInactive", grey_pink, "=Pₚ")
check_for_C_prefix_inactive = State("CheckForCustomPrefixInactive", grey_pink, "=Cₚ")

check_for_any_prefix = State("CheckForAnyPrefix", mid_pink, "=*ₚ")
check_for_N_prefix = State("CheckForNPrefix", mid_pink, "=Nₚ")
check_for_S_prefix = State("CheckForSPrefix", mid_pink, "=Sₚ")
check_for_E_prefix = State("CheckForEPrefix", mid_pink, "=Eₚ")
check_for_W_prefix = State("CheckForWPrefix", mid_pink, "=Wₚ")
check_for_P_prefix = State("CheckForProgramPrefix", mid_pink, "=Pₚ")
check_for_C_prefix = State("CheckForCustomPrefix", mid_pink, "=Cₚ")

confirm_equal_any_prefix = State("ConfirmEqualAnyPrefix", complete_color, "=*ₚ")
confirm_equal_N_prefix = State("ConfirmEqualNPrefix", complete_color, "=Nₚ")
confirm_equal_S_prefix = State("ConfirmEqualSPrefix", complete_color, "=Sₚ")
confirm_equal_E_prefix = State("ConfirmEqualEPrefix", complete_color, "=Eₚ")
confirm_equal_W_prefix = State("ConfirmEqualWPrefix", complete_color, "=Wₚ")
confirm_equal_C_prefix = State("ConfirmEqualCustomPrefix", complete_color, "=Cₚ")
confirm_equal_P_prefix = State("ConfirmEqualProgramPrefix", complete_color, "=Pₚ")

# Check For Caps
confirm_for_any_cap = State("ConfirmForAnyCap", complete_color, "=*₍₎")
confirm_for_any_start_cap = State("ConfirmForStartCap", complete_color, "=*ᵦ₍")
confirm_for_any_end_cap = State("ConfirmForEndCap", complete_color, "=*ₔ₎")
confirm_for_start_state_cap = State("ConfirmForStartStateCap", complete_color, "=(ᵦ")
confirm_for_end_state_cap = State("ConfirmForEndStateCap", complete_color, "=)ₔ")
confirm_for_end_state_pair_cap = State("ConfirmForEndStatePairCap", complete_color, "=]ₔ")
confirm_for_start_state_pair_cap = State("ConfirmForStartStatePairCap", complete_color, "=[ᵦ")
confirm_end_string_cap = State("ConfirmEndStringCap", complete_color, "=﹞ₔ")
confirm_start_string_cap = State("ConfirmStartStringCap", complete_color, "=﹝ᵦ")

check_for_any_cap = State("CheckForAnyCap", mid_pink, "=*₍₎")
check_for_any_start_cap = State("CheckForStartCap", mid_pink, "=*ᵦ₍")
check_for_any_end_cap = State("CheckForEndCap", mid_pink, "=*ₔ₎")
check_for_start_state_cap = State("CheckForStartStateCap", mid_pink, "=(ᵦ")
check_for_end_state_cap = State("CheckForEndStateCap", mid_pink, "=)ₔ")
check_for_end_state_pair_cap = State("CheckForEndStatePairCap", mid_pink, "=]ₔ")
check_for_start_state_pair_cap = State("CheckForStartStatePairCap", mid_pink, "=[ᵦ")
check_for_start_string = State("CheckForStartString", mid_pink, "=﹝ᵦ")
check_for_end_string = State("CheckForEndString", mid_pink, "=﹞ₔ")

check_for_any_cap_inactive = State("CheckForAnyCapInactive", grey_pink, "=*₍₎")
check_for_any_start_cap_inactive = State("CheckForStartCapInactive", grey_pink, "=*ᵦ₍")
check_for_any_end_cap_inactive = State("CheckForEndCapInactive", grey_pink, "=*ₔ₎")
check_for_start_state_cap_inactive = State("CheckForStartStateCapInactive", grey_pink, "=(ᵦ")
check_for_end_state_cap_inactive = State("CheckForEndStateCapInactive", grey_pink, "=)ₔ")
check_for_start_state_pair_cap_inactive = State("CheckForStartStatePairCapInactive", grey_pink, "=[ᵦ")
check_for_end_state_pair_cap_inactive = State("CheckForEndStatePairCapInactive", grey_pink, "=]ₔ")
check_for_start_string_inactive = State("CheckForStartStringInactive", grey_pink, "=﹝")
check_for_end_string_inactive = State("CheckForEndStringInactive", grey_pink, "=﹞")

# Doors

## Copy Doors
northCopyDoor = State("NorthCopyDoor", light_blue, "⇈⬓")
westCopyDoor = State("WestCopyDoor", light_blue, "⇇⬓")
eastCopyDoor = State("EastCopyDoor", light_blue, "⇉⬓")
southCopyDoor = State("SouthCopyDoor", light_blue, "⇊⬓")
northCopySeriesCheckEast = State("NorthCopySeriesCheckEast", light_blue, "⇈⬓?")

northCopyDoorInactive = State("NorthCopyDoorInactive", queen_blue, "⇈⬓")
southCopyDoorInactive = State("SouthCopyDoorInactive", queen_blue, "⇊⬓")
eastCopyDoorInactive = State("EastCopyDoorInactive", queen_blue, "⇉⬓")
westCopyDoorInactive = State("WestCopyDoorInactive", queen_blue, "⇇⬓")

northCopyDoorHandle = State("NorthCopyDoorHandle", terquoise_blue, "⇈⬓~")
northCopyDoorHandleInactive = State("NorthCopyDoorHandleInactive", ming, "⇈⬓~")
westCopyDoorHandle = State("WestCopyDoorHandle", terquoise_blue, "⇇⬓~")
westCopyDoorHandleInactive = State("WestCopyDoorHandleInactive", ming, "⇇⬓~")
eastCopyDoorHandle = State("EastCopyDoorHandle", terquoise_blue, "⇉⬓~")
eastCopyDoorHandleInactive = State("EastCopyDoorHandleInactive", ming, "⇉⬓~")
southCopyDoorHandle = State("SouthCopyDoorHandle", terquoise_blue, "⇊⬓~")
southCopyDoorHandleInactive = State("SouthCopyDoorHandleInactive", ming, "⇊⬓~")

## Trap Doors
trap_door_inactive = State("TrapDoorInactive", copper_rose, "▩")
trap_door_active = State("TrapDoorActive", Barn_Red, "▩")

## Endcap Doors
endcap_door_west_inactive = State("EndcapDoorWestInactive", inactive_color, "◨")
endcap_door_west_handle_inactive = State("EndCapDoorHandleWestInactive", inactive_color, "◨~🔒")
endcap_door_west_active = State("EndcapDoorWestActive", full_accept_color, "◨")
endcap_door_west_handle_active = State("EndCapDoorHandleWestActive", full_accept_color, "◨~🔓")
endcap_door_west_stop = State("EndcapDoorWestStop", reject_color, "◨")
endcap_door_west_handle_stop = State("EndCapDoorWestHandleStop", reject_color, "◨~🔒")
endcap_door_west_reset = State("EndcapDoorWestReset", waiting_color, "↺◨")
endcap_door_west_handle_reset = State("EndCapDoorHandleWestReset", waiting_color, "↺◨~🔒")
endcap_door_west_handle_reset_waiting = State("EndCapDoorHandleWestResetWaiting", waiting_color, "↺⏱◨~")
endcap_door_west_reset_waiting = State("EndcapDoorWestResetWaiting", waiting_color, "↺⏱◨")
endcap_doors_west_list = [endcap_door_west_inactive, endcap_door_west_handle_inactive, endcap_door_west_active, endcap_door_west_handle_active, endcap_door_west_stop, endcap_door_west_handle_stop, endcap_door_west_reset, endcap_door_west_handle_reset, endcap_door_west_handle_reset_waiting, endcap_door_west_reset_waiting]

## Endcap Doors East
endcap_door_east_inactive = State("EndcapDoorEastInactive", inactive_color, "◨")
endcap_door_east_handle_inactive = State("EndCapDoorHandleEastInactive", inactive_color, "◨~🔒")
endcap_door_east_active = State("EndcapDoorEastActive", full_accept_color, "◨")
endcap_door_east_handle_active = State("EndCapDoorHandleEastActive", full_accept_color, "◨~🔓")
endcap_door_east_stop = State("EndcapDoorEastStop", reject_color, "◨")
endcap_door_east_handle_stop = State("EndCapDoorEastHandleStop", reject_color, "◨~🔒")
endcap_door_east_reset = State("EndcapDoorEastReset", waiting_color, "↺◨")
endcap_door_east_handle_reset = State("EndCapDoorHandleEastReset", waiting_color, "↺◨~🔒")
endcap_door_east_handle_reset_waiting = State("EndCapDoorHandleEastResetWaiting", waiting_color, "↺⏱◨~")
endcap_door_east_reset_waiting = State("EndcapDoorEastResetWaiting", waiting_color, "↺⏱◨")
endcap_doors_east_list = [endcap_door_east_inactive, endcap_door_east_handle_inactive, endcap_door_east_active, endcap_door_east_handle_active, endcap_door_east_stop, endcap_door_east_handle_stop, endcap_door_east_reset, endcap_door_east_handle_reset, endcap_door_east_handle_reset_waiting, endcap_door_east_reset_waiting]
### Signal Doors
signal_door_inactive = State("LockedSignalDoorInactive", inactive_color, "🔒◨")
signal_door_inactive_east = State("LockedSignalDoorInactiveEast", inactive_color, "◨⇉")
signal_door_intermediate_accept = State("SignalDoorIntermediateAccept", intermediate_accept_color, "◨↯")
signal_door_open = State("SignalDoorOpen", full_accept_color, "🔓◨")
signal_door_transmit = State("SignalDoorTransmit", waiting_color, "◨↯")
signal_door_active_waiting_east = State("SignalDoorActiveWaitingEast", waiting_color, "◨⇉⏱")
signal_door_handle_inactive = State("LockedSignalDoorHandleInactive", inactive_color, "🗝~")
signal_door_handle_reset = State("SignalDoorHandleReset", reset_color, "↺🗝~")


signal_door_handle_open = State("SignalDoorHandleOpen", full_accept_color, "🗝~")
signal_door_handle_active_waiting = State("SignalDoorHandleActiveWaiting", waiting_color, "⏱🗝~")
signal_door_handle_inactive_waiting = State("SignalDoorHandleInactiveWaiting", inactive_waiting_color, "⏱🗝~")
signal_door_handle_accept = State("SignalDoorHandleAccept", full_accept_color, "🗝~")
signal_door_handle_intermediate_accept = State("SignalDoorHandleIntermediateAccept", intermediate_accept_color, "🗝~")
signal_door_handle_pass_accept_south = State("SignalDoorHandlePassAcceptSouth", intermediate_accept_color, "🗝~↧↯")
signal_door_handle_pass_accept_north = State("SignalDoorHandlePassAcceptNorth", intermediate_accept_color, "🗝~↥↯")
signal_door_handle_find_corner_north = State("SignalDoorHandleFindCornerNorth", waiting_color, "🗝~↥↯")
signal_door_handle_find_corner_south = State("SignalDoorHandleFindCornerSouth", waiting_color, "🗝~↧↯")
signal_door_handle_pass_find_corner_north = State("SignalDoorHandlePassFindCornerNorth", waiting_color, "🗝~↥↯")
signal_door_handle_pass_find_corner_south = State("SignalDoorHandlePassFindCornerSouth", waiting_color, "🗝~↧↯")


signal_door_pass_accept_south = State("SignalDoorPassAcceptSouth", intermediate_accept_color, "◨↧↯")
signal_door_pass_accept_north = State("SignalDoorPassAcceptNorth", intermediate_accept_color, "◨↥↯")
signal_door_pass_find_corner_north = State("SignalDoorPassFindCornerNorth", waiting_color, "◨↥↯")
signal_door_pass_find_corner_south = State("SignalDoorPassFindCornerSouth", waiting_color, "◨↧↯")

signal_door_find_corner_north = State("SignalDoorFindCornerNorth", inactive_waiting_color, "◨↥↯")
signal_door_find_corner_south = State("SignalDoorFindCornerSouth", inactive_waiting_color, "◨↧↯")

signal_door_propped_open = State("SignalDoorProppedOpen", full_accept_color, "🔓")
signal_door_reset = State("SignalDoorReset", reset_color, "↺▦")
signal_door_east_reset = State("SignalDoorEastReset", reset_color, "↺⇉▦")
signal_door_east_stop = State("SignalDoorEastStop", reject_color, "⇉▦")
signal_door_reset_walk = State("SignalDoorResetWalk", reset_color, "↺▦◃")
signal_door_east_reset_walk = State(
    "SignalDoorEastResetWalk", reset_color, "↺⇉▦◃")
signal_door_send_confirmed_transmission = State("SignalDoorSendConfirmedTransmission", waiting_color, "▦⇉✅")
reset_confirmed_transmission_westWire = State("ResetConfirmedTransmissionWest", waiting_color, "↺✅⇉")


### Signal Door Checks
closed_endcap_door_check_signal = State("ClosedEndcapDoorCheckSignal", inactive_color, "✅")
closed_endcap_door_check_signal_inactive = State("ClosedEndcapDoorCheckSignalInactive", inactive_color, "❌")

signal_transmitter_turn_down_inactive = State("SignalTransmitterTurnDownInactive", inactive_color, "⮮")
signal_transmitter_turn_down_active = State("SignalTransmitterTurnDownActive", full_accept_color, "⮮")
signal_transmitter_turn_down_open = State("SignalTransmitterTurnDownOpen", full_accept_color, "⮮")
signal_transmitter_turn_down_reset = State("SignalTransmitterTurnDownReset", waiting_color, "↺⮮")

signal_transmitter_turn_up_inactive = State("SignalTransmitterTurnUpInactive", inactive_color, "⮲")
signal_transmitter_turn_up_active = State("SignalTransmitterTurnUpActive", full_accept_color, "⮲")
signal_transmitter_turn_up_reset = State("SignalTransmitterTurnUpReset", waiting_color, "↺⮲")

row_signal_positive_inactive = State("RowSignalPositiveInactive", inactive_color, "⊝")

row_signal_positive_start_inactive = State("RowSignalPositiveStartInactive", waiting_color, "⊝")

row_signal_positive_start_waiting = State("RowSignalPositiveStartWaiting", waiting_color, "⊝⏱")

row_signal_positive_waiting = State("RowSignalPositiveWaiting", waiting_color, "⏱")
row_signal_positive_full_accept = State("RowSignalPositiveFullAccept", full_accept_color, "✅")
row_signal_intermediate_accept = State("RowSignalPositiveInterimAccept", activate_next_color, "✅")
row_signal_positive_reset = State("RowSignalPositiveReset", waiting_color, "↺")

signal_inactive_color = grey
signal_receiver_inactive = State("SignalReceiverInactive", inactive_color, "⊝")
signal_received_accept = State("SignalReceivedAccept", full_accept_color, "✔✔")
signal_received_reject = State("SignalReceivedReject", reject_color, "✖")
signal_receiver_passed = State("SignalReceiverPassed", full_accept_color, "⇉")
signal_receiver_reset = State("SignalReceiverReset", waiting_color, "↺")
signal_receiver_pass_find_corner_north = State("SignalReceiverPassFindCornerNorth", waiting_color, "?↥↯")
signal_receiver_pass_find_corner_south = State("SignalReceiverPassFindCornerSouth", waiting_color, "?↧↯")
signal_receiver_pass_accept_north = State("SignalReceiverPassAcceptNorth", full_accept_color, "✔↥↯")
signal_receiver_pass_accept_south = State("SignalReceiverPassAcceptSouth", full_accept_color, "✔↧↯")

signal_transmitter = State("SignalTransmitter", full_accept_color, "⇉⍼")
signal_transmitter_inactive = State("SignalTransmitterInactive", inactive_color, "⍼")
signal_transmitter_reset = State( "SignalTransmitterReset", waiting_color, "⍼↺")
signal_transmitter_accept = State("SignalTransmitterAccept", full_accept_color, "⍼✔")
signal_transmitter_reject = State("SignalTransmitterReject", reject_color, "⍼✖ ")
signal_transmitter_pass_find_corner_north = State("SignalTransmitterPassFindCornerNorth", waiting_color, "?↥⍼")
signal_transmitter_pass_find_corner_south = State("SignalTransmitterPassFindCornerSouth", waiting_color, "?↧⍼")
signal_transmitter_pass_accept_north = State(
    "SignalTransmitterPassAcceptNorth", intermediate_accept_color, "◨↥⍼")
signal_transmitter_pass_accept_south = State(
    "SignalTransmitterPassAcceptSouth", intermediate_accept_color, "◨↧⍼")

signal_wire_inactive = State("SignalWireInactive", inactive_color, "⇉")
signal_wire_active = State("SignalWireActive", full_accept_color, "⇉")

signal_start_checks_inactive = State("SignalStartChecksInactive", inactive_color, "⏯")
signal_start_checks_active = State("SignalStartChecksActive", full_accept_color, "⏯")
signal_end_checks_inactive = State("SignalEndChecksInactive", inactive_color, "⏱")
signal_end_checks_accept = State("SignalEndChecksAccept", full_accept_color, "✔✔")
signal_end_checks_reject = State("SignalEndChecksReject", reject_color, "✖")

signal_conditional_inactive = State("SignalConditionalInactive", inactive_color, "⏱")
signal_conditional_waiting = State("SignalConditionalWaiting", waiting_color, "⏱")
signal_conditional_intermediate_accept = State("SignalConditionalInterimAccept", activate_next_color, "✔")
signal_conditional_full_accept = State("SignalConditionalFullAccept", full_accept_color, "✔✔")
signal_conditional_reject = State("SignalConditionalReject", reject_color, "✖")
signal_conditional_reset = State("SignalConditionalReset", waiting_color, "↺")


### Data States
ds_1 = State("1", data_color)
ds_0 = State("0", data_color)

start_state = State("StartState", data_color, "(")
end_state = State("EndState", data_color, ")")

start_state_pair = State("StartStatePair", data_color, "[")
end_state_pair = State("EndStatePair", data_color, "]")

start_data_string = State("StartDataString", data_color, "{")
end_data_string = State("EndDataString", data_color, "}")

north_prefix =  State("NorthPrefix", data_color, "𝗡")
south_prefix =  State("SouthPrefix", data_color, "𝗦")
east_prefix =  State("EastPrefix", data_color, "𝗘")
west_prefix =  State("WestPrefix", data_color, "𝗪")
program_prefix =  State("ProgramPrefix", data_color, "</>")
reset_prefix =  State("ResetPrefix", data_color, "⭯")


ds_states = [ds_0, ds_1, start_state, end_state, start_state_pair, end_state_pair, start_data_string, end_data_string, north_prefix, south_prefix, east_prefix, west_prefix, program_prefix, reset_prefix]

data_states_list_binary_nums_only = [ds_0, ds_1]
data_states_list_all = [start_state] +  data_states_list_binary_nums_only + [end_state]

wire_states = [westWire, eastWire, northWire, southWire, northEastWire, northWestWire, southEastWire,
               southWestWire, westProtectedWire, eastProtectedWire, northProtectedWire, southProtectedWire]
data_states_list_prefixes = [north_prefix, south_prefix, east_prefix, west_prefix, program_prefix,
                             reset_prefix, start_state_pair, end_state_pair, start_data_string, end_data_string, start_state, end_state]
data_states_list_all_with_prefixes_no_order = data_states_list_prefixes + data_states_list_binary_nums_only
copy_wire_states = [northCopyWire, southCopyWire, eastCopyWire, westCopyWire]

# Potential Symbols
# ⍼
# ⟥ , ⭤ ⟥, ⭥⟥, ⟥
# ⤕,🔎
