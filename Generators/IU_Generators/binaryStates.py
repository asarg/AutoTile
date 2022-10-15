
from UniversalClasses import State
from Assets.colors import *





# Border
border_state = State("Border", rosy_brown, " ", "black")

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

protectWireWalker = State("ProtectWireWalker", writing_color, "|🖋|")

northCopyWire = State("NorthCopyWire", light_blue, "⇈")
southCopyWire = State("SouthCopyWire", light_blue, "⇊")
westCopyWire = State("WestCopyWire", light_blue, "⇇")
eastCopyWire = State("EastCopyWire", light_blue, "⇉")

checkCopyWireReachedInactive = State("CheckCopyWireReachedInactive", inactive_color, "*⇈")

# Signal Wire and states
verticalMacroCellDoorOpenSignal = State("VerticalMacroCellDoorOpenSignal", atomic_tangerine, "⭥⟥")
horizontalMacroCellDoorOpenSignal = State("HorizontalMacroCellDoorOpenSignal", atomic_tangerine, "⭤ ⟥")

writeOneInactive = State("WriteOneInactive", inactive_color, "1🖋")
writeZeroInactive = State("WriteZeroInactive", inactive_color, "0🖋")
writeOneWaiting = State("WriteOneWaiting", waiting_color, "1🖋")
writeZeroWaiting = State("WriteZeroWaiting", waiting_color, "0🖋")
writeOne = State("WriteOneActive", writing_color, "1🖋")
writeZero = State("WriteZeroActive", writing_color, "0🖋")
writeOneActivateNext = State("WriteOneActivateNext", activate_next_color, "1🖋")
writeZeroActivateNext = State("WriteZeroActivateNext", activate_next_color, "0🖋")
writeOneComplete = State("WriteOneComplete", complete_color, "1🖋")
writeZeroComplete = State("WriteZeroComplete", complete_color, "0🖋")
writeOneReset = State("WriteOneReset", waiting_color, "↺1🖋")
writeZeroReset = State("WriteZeroReset", waiting_color, "↺0🖋")

writeNorthPrefix = State("WriteNorthPrefix", writing_color, "𝗡🖋")
writeSouthPrefix = State("WriteSouthPrefix", writing_color, "𝗦🖋")
writeWestPrefix = State("WriteWestPrefix", writing_color, "𝗪🖋")
writeEastPrefix = State("WriteEastPrefix", writing_color, "𝗘🖋")

writeNorthPrefixInactive = State("WriteNorthPrefixInactive", inactive_color, "𝗡🖋")
writeSouthPrefixInactive = State("WriteSouthPrefixInactive", inactive_color, "𝗦🖋")
writeWestPrefixInactive = State("WriteWestPrefixInactive", inactive_color, "𝗪🖋")
writeEastPrefixInactive = State("WriteEastPrefixInactive", inactive_color, "𝗘🖋")

writeNorthPrefixWaiting = State("WriteNorthPrefixWaiting", waiting_color, "𝗡🖋")
writeSouthPrefixWaiting = State("WriteSouthPrefixWaiting", waiting_color, "𝗦🖋")
writeEastPrefixWaiting = State("WriteEastPrefixWaiting", waiting_color, "𝗘🖋")
writeWestPrefixWaiting = State("WriteWestPrefixWaiting", waiting_color, "𝗪🖋")

writeNorthPrefixActivateNext = State("WriteNorthPrefixActivateNext", activate_next_color, "𝗡🖋")
writeSouthPrefixActivateNext = State("WriteSouthPrefixActivateNext", activate_next_color, "𝗦🖋")
writeWestPrefixActivateNext = State("WriteWestPrefixActivateNext", activate_next_color, "𝗪🖋")
writeEastPrefixActivateNext = State("WriteEastPrefixActivateNext", activate_next_color, "𝗘🖋")

writeNorthPrefixComplete = State("WriteNorthPrefixComplete", complete_color, "𝗡🖋")
writeSouthPrefixComplete = State("WriteSouthPrefixComplete", complete_color, "𝗦🖋")
writeEastPrefixComplete = State("WriteEastPrefixComplete", complete_color, "𝗘🖋")
writeWestPrefixComplete = State("WriteWestPrefixComplete", complete_color, "𝗪🖋")

writeNorthPrefixReset = State("WriteNorthPrefixReset", waiting_color, "↺𝗡🖋")
writeSouthPrefixReset = State("WriteSouthPrefixReset", waiting_color, "↺𝗦🖋")
writeEastPrefixReset = State("WriteEastPrefixReset", waiting_color, "↺𝗘🖋")
writeWestPrefixReset = State("WriteWestPrefixReset", waiting_color, "↺𝗪🖋")

writeStartStateInactive = State("WriteStartStateInactive", inactive_color, "(🖋")
writeEndStateInactive = State("WriteEndStateInactive", inactive_color, ")🖋")
writeStartStatePairInactive = State("WriteStartStatePairInactive", inactive_color, "[🖋")
writeEndStatePairInactive = State("WriteEndStatePairInactive", inactive_color, "]🖋")
writeStateDataStringInactive = State(
    "WriteStateDataStringInactive", inactive_color, "🖋❲")
writeEndDataStringInactive = State(
    "WriteEndDataStringInactive", inactive_color, "🖋❳")

writeStartStateActivateNext = State("WriteStartStateActivateNext", activate_next_color, "(🖋")
writeEndStateActivateNext = State("WriteEndStateActivateNext", activate_next_color, ")🖋")
writeStartStatePairActivateNext = State("WriteStartStatePairActivateNext", activate_next_color, "[🖋")
writeEndStatePairActivateNext = State("WriteEndStatePairActivateNext", activate_next_color, "]🖋")
writeStartDataStringActivateNext = State(
    "WriteStartDataStringActivateNext", activate_next_color, "🖋❲")
writeEndDataStringActivateNext = State(
    "WriteEndDataStringActivateNext", activate_next_color, "🖋❳")

writeStartStateWaiting = State("WriteStartStateWaiting", waiting_color, "(🖋")
writeEndStateWaiting = State("WriteEndStateWaiting", waiting_color, ")🖋")
writeStartStatePairWaiting = State("WriteStartStatePairWaiting", waiting_color, "[🖋")
writeEndStatePairWaiting = State("WriteEndStatePairWaiting", waiting_color, "]🖋")
writeStartDataStringWaiting = State("WriteStartDataStringWaiting", waiting_color, "🖋❲")
writeEndDataStringWaiting = State("WriteEndDataStringWaiting", waiting_color, "🖋❳")

writeStartState = State("WriteStartState", writing_color, "(🖋")
writeEndState = State("WriteEndState", writing_color, ")🖋")
writeStartStatePair = State("WriteStartStatePair", writing_color, "[🖋")
writeEndStatePair = State("WriteEndStatePair", writing_color, "]🖋")
writeStartDataString = State("WriteStartDataString", writing_color, "🖋❲")
writeEndDataString = State("WriteEndDataString", writing_color, "🖋❳")

writeStartDataStringComplete = State("WriteStartDataStringComplete", complete_color, "🖋❲")
writeEndDataStringComplete = State("WriteStartDataStringComplete", complete_color, "🖋❳")
writeStartStateComplete = State("WriteStartStateComplete", complete_color, "(🖋")
writeEndStateComplete = State("WriteEndStateComplete", complete_color, ")🖋")
writeStartStatePairComplete = State("WriteStartStatePairComplete", complete_color, "[🖋")
writeEndStatePairComplete = State("WriteEndStatePairComplete", complete_color, "]🖋")

writeDoorInactive = State("WriteDoorInactive", inactive_color, "🖋🚪")
writeDoorActive = State("WriteDoorActive", active_color, "🖋🚪")


# Check For Num Equality
confirm_for_any_num = State("ConfirmForEqualityAnyNum", complete_color, "=*", "black")
confirm_for_equality_zero = State("ConfirmForEqualityZero", complete_color, "=0", "black")
confirm_for_equality_one = State("ConfirmForEqualityOne", complete_color, "=1", "black")

check_for_any_num = State("CheckForEqualityAnyNum", mid_pink, "=*", "black")
check_for_equality_zero = State("CheckForEqualityZero", mid_pink, "=0", "black")
check_for_equality_one = State("CheckForEqualityOne", mid_pink, "=1", "black")

check_for_any_num_inactive = State("CheckForEqualityAnyNum_Inactive", grey_pink, "=*", "black")
check_for_equality_zero_inactive = State("CheckForEqualityZero_Inactive", grey_pink, "=0", "black")
check_for_equality_one_inactive = State("CheckForEqualityOne_Inactive", grey_pink, "=1", "black")


# Check For Prefixes
check_equality_inactive = State("CheckEqualityInactive", grey_pink, "=", "black")
check_for_any_prefix_inactive = State("CheckForAnyPrefix", grey_pink, "=*ₚ", "black")
check_for_N_prefix_inactive = State("CheckForNPrefixInactive", grey_pink, "=Nₚ", "black")
check_for_S_prefix_inactive = State("CheckForSPrefixInactive", grey_pink, "=Sₚ", "black")
check_for_E_prefix_inactive = State("CheckForEPrefixInactive", grey_pink, "=Eₚ", "black")
check_for_W_prefix_inactive = State("CheckForWPrefixInactive", grey_pink, "=Wₚ", "black")
check_for_P_prefix_inactive = State("CheckForProgramPrefixInactive", grey_pink, "=Pₚ", "black")
check_for_C_prefix_inactive = State("CheckForCustomPrefixInactive", grey_pink, "=Cₚ", "black")

check_for_any_prefix = State("CheckForAnyPrefix", mid_pink, "=*ₚ", "black")
check_for_N_prefix = State("CheckForNPrefix", mid_pink, "=Nₚ", "black")
check_for_S_prefix = State("CheckForSPrefix", mid_pink, "=Sₚ", "black")
check_for_E_prefix = State("CheckForEPrefix", mid_pink, "=Eₚ", "black")
check_for_W_prefix = State("CheckForWPrefix", mid_pink, "=Wₚ", "black")
check_for_P_prefix = State("CheckForProgramPrefix", mid_pink, "=Pₚ", "black")
check_for_C_prefix = State("CheckForCustomPrefix", mid_pink, "=Cₚ", "black")

confirm_equal_any_prefix = State("ConfirmEqualAnyPrefix", complete_color, "=*ₚ", "black")
confirm_equal_N_prefix = State("ConfirmEqualNPrefix", complete_color, "=Nₚ", "black")
confirm_equal_S_prefix = State("ConfirmEqualSPrefix", complete_color, "=Sₚ", "black")
confirm_equal_E_prefix = State("ConfirmEqualEPrefix", complete_color, "=Eₚ", "black")
confirm_equal_W_prefix = State("ConfirmEqualWPrefix", complete_color, "=Wₚ", "black")
confirm_equal_C_prefix = State("ConfirmEqualCustomPrefix", complete_color, "=Cₚ", "black")
confirm_equal_P_prefix = State("ConfirmEqualProgramPrefix", complete_color, "=Pₚ", "black")

# Check For Caps
confirm_for_any_cap = State("ConfirmForAnyCap", complete_color, "=*₍₎", "black")
confirm_for_any_start_cap = State("ConfirmForStartCap", complete_color, "=*ᵦ₍", "black")
confirm_for_any_end_cap = State("ConfirmForEndCap", complete_color, "=*ₔ₎", "black")
confirm_for_start_state_cap = State("ConfirmForStartStateCap", complete_color, "=(ᵦ", "black")
confirm_for_end_state_cap = State("ConfirmForEndStateCap", complete_color, "=)ₔ", "black")
confirm_for_end_state_pair_cap = State("ConfirmForEndStatePairCap", complete_color, "=]ₔ", "black")
confirm_for_start_state_pair_cap = State("ConfirmForStartStatePairCap", complete_color, "=[ᵦ", "black")
confirm_end_string_cap = State("ConfirmEndStringCap", complete_color, "=﹞ₔ", "black")
confirm_start_string_cap = State("ConfirmStartStringCap", complete_color, "=﹝ᵦ", "black")

check_for_any_cap = State("CheckForAnyCap", mid_pink, "=*₍₎", "black")
check_for_any_start_cap = State("CheckForStartCap", mid_pink, "=*ᵦ₍", "black")
check_for_any_end_cap = State("CheckForEndCap", mid_pink, "=*ₔ₎", "black")
check_for_start_state_cap = State("CheckForStartStateCap", mid_pink, "=(ᵦ", "black")
check_for_end_state_cap = State("CheckForEndStateCap", mid_pink, "=)ₔ", "black")
check_for_end_state_pair_cap = State("CheckForEndStatePairCap", mid_pink, "=]ₔ", "black")
check_for_start_state_pair_cap = State("CheckForStartStatePairCap", mid_pink, "=[ᵦ", "black")
check_for_start_string = State("CheckForStartString", mid_pink, "=﹝ᵦ", "black")
check_for_end_string = State("CheckForEndString", mid_pink, "=﹞ₔ", "black")

check_for_any_cap_inactive = State("CheckForAnyCapInactive", grey_pink, "=*₍₎", "black")
check_for_any_start_cap_inactive = State("CheckForStartCapInactive", grey_pink, "=*ᵦ₍", "black")
check_for_any_end_cap_inactive = State("CheckForEndCapInactive", grey_pink, "=*ₔ₎", "black")
check_for_start_state_cap_inactive = State("CheckForStartStateCapInactive", grey_pink, "=(ᵦ", "black")
check_for_end_state_cap_inactive = State("CheckForEndStateCapInactive", grey_pink, "=)ₔ", "black")
check_for_start_state_pair_cap_inactive = State("CheckForStartStatePairCapInactive", grey_pink, "=[ᵦ", "black")
check_for_end_state_pair_cap_inactive = State("CheckForEndStatePairCapInactive", grey_pink, "=]ₔ", "black")
check_for_start_string_inactive = State("CheckForStartStringInactive", grey_pink, "=﹝", "black")
check_for_end_string_inactive = State("CheckForEndStringInactive", grey_pink, "=﹞", "black")

# Doors

## Copy Doors
northCopyDoor = State("NorthCopyDoor", light_blue, "⇈⬓", "black")
westCopyDoor = State("WestCopyDoor", light_blue, "⇇⬓", "black")
eastCopyDoor = State("EastCopyDoor", light_blue, "⇉⬓", "black")
southCopyDoor = State("SouthCopyDoor", light_blue, "⇊⬓", "black")
northCopySeriesCheckEast = State("NorthCopySeriesCheckEast", light_blue, "⇈⬓?", "black")

northCopyDoorInactive = State("NorthCopyDoorInactive", queen_blue, "⇈⬓")
southCopyDoorInactive = State("SouthCopyDoorInactive", queen_blue, "⇊⬓")
eastCopyDoorInactive = State("EastCopyDoorInactive", queen_blue, "⇉⬓")
westCopyDoorInactive = State("WestCopyDoorInactive", queen_blue, "⇇⬓")

northCopyDoorHandle = State("NorthCopyDoorHandle", terquoise_blue, "⇈⬓~")
northCopyDoorHandleInactive = State("NorthCopyDoorHandleInactive", ming, "⇈⬓~", "black")
westCopyDoorHandle = State("WestCopyDoorHandle", terquoise_blue, "⇇⬓~")
westCopyDoorHandleInactive = State("WestCopyDoorHandleInactive", ming, "⇇⬓~", "black")
eastCopyDoorHandle = State("EastCopyDoorHandle", terquoise_blue, "⇉⬓~")
eastCopyDoorHandleInactive = State("EastCopyDoorHandleInactive", ming, "⇉⬓~", "black")
southCopyDoorHandle = State("SouthCopyDoorHandle", terquoise_blue, "⇊⬓~")
southCopyDoorHandleInactive = State("SouthCopyDoorHandleInactive", ming, "⇊⬓~", "black")

## Trap Doors
trap_door_inactive = State("TrapDoorInactive", copper_rose, "▩", "black")
trap_door_active = State("TrapDoorActive", Barn_Red, "▩", "black")

## Endcap Doors
endcap_door_west_inactive = State("EndcapDoorWestInactive", grey, "◨", "black")
endcap_door_west_handle_inactive = State("EndCapDoorHandleWestInactive", grey, "◨~🔒", "black")
endcap_door_west_active = State("EndcapDoorWestActive", persian_green, "◨", "black")
endcap_door_west_handle_active = State("EndCapDoorHandleWestActive", persian_green, "◨~🔓", "black")
endcap_door_west_stop = State("EndcapDoorWestStop", Venetian_Red, "◨", "black")
endcap_door_west_handle_stop = State("EndCapDoorWestHandleStop", Venetian_Red, "◨~🔒", "black")
endcap_door_west_reset = State("EndcapDoorWestReset", waiting_color, "↺◨", "black")
endcap_door_west_handle_reset = State("EndCapDoorHandleWestReset", waiting_color, "↺◨~🔒", "black")
endcap_door_west_handle_reset_waiting = State("EndCapDoorHandleWestResetWaiting", waiting_color, "↺⏱◨~", "black")
endcap_door_west_reset_waiting = State("EndcapDoorWestResetWaiting", waiting_color, "↺⏱◨", "black")

### Single Doors
signal_door_inactive = State("LockedSignalDoorInactive", grey, "🔒▦", "black")
signal_door_handle_inactive = State("LockedSignalDoorHandleInactive", grey, "🗝~", "black")
signal_door_handle_reset = State("SignalDoorHandleReset", waiting_color, "↺🗝~", "black")
signal_door_open = State("SignalDoorOpen", persian_green, "🔓▦", "black")
signal_door_handle_open = State("SignalDoorHandleOpen", persian_green, "🗝~", "black")

signal_door_propped_open = State("SignalDoorProppedOpen", persian_green, "🔓", "black")
signal_door_reset = State("SignalDoorReset", waiting_color, "↺▦", "black")
signal_door_reset_walk = State("SignalDoorResetWalk", waiting_color, "↺▦◃", "black")
signal_door_send_confirmed_transmission = State("SignalDoorSendConfirmedTransmission", waiting_color, "▦⇉✅", "black")
reset_confirmed_transmission_westWire = State("ResetConfirmedTransmissionWest", waiting_color, "↺✅⇉", "black")


### Signal Door Checks
closed_endcap_door_check_signal = State("ClosedEndcapDoorCheckSignal", grey, "✅", "black")
closed_endcap_door_check_signal_inactive = State("ClosedEndcapDoorCheckSignalInactive", grey, "❌", "black")

signal_transmitter_turn_down_inactive = State("SignalTransmitterTurnDownInactive", grey, "⮮", "black")
signal_transmitter_turn_down_active = State("SignalTransmitterTurnDownActive", persian_green, "⮮", "black")
signal_transmitter_turn_down_open = State("SignalTransmitterTurnDownOpen", persian_green, "⮮", "black")
signal_transmitter_turn_down_reset = State("SignalTransmitterTurnDownReset", waiting_color, "↺⮮", "black")

signal_transmitter_turn_up_inactive = State("SignalTransmitterTurnUpInactive", grey, "⮲", "black")
signal_transmitter_turn_up_active = State("SignalTransmitterTurnUpActive", persian_green, "⮲", "black")
signal_transmitter_turn_up_reset = State("SignalTransmitterTurnUpReset", waiting_color, "↺⮲", "black")

row_signal_positive_inactive = State("RowSignalPositiveInactive", grey, "⊝", "black")

row_signal_positive_start_inactive = State("RowSignalPositiveStartInactive", green_yellow_crayola, "⊝", "black")

row_signal_positive_start_waiting = State("RowSignalPositiveStartWaiting", green_yellow_crayola, "⊝⏱", "black")

row_signal_positive_waiting = State("RowSignalPositiveWaiting", green_yellow_crayola, "⏱", "black")
row_signal_positive_full_accept = State("RowSignalPositiveFullAccept", Viridian_Green, "✅")
row_signal_intermediate_accept = State("RowSignalPositiveInterimAccept", activate_next_color, "✅")
row_signal_positive_reset = State("RowSignalPositiveReset", waiting_color, "↺", "black")

signal_inactive_color = grey
signal_receiver_inactive = State("SignalReceiverInactive", grey, "⊝", "black")
signal_received_accept = State("SignalReceivedAccept", persian_green, "✔✔", "black")
signal_recieved_reject = State("SignalReceivedReject", Venetian_Red, "✖", "black")
signal_receiver_passed = State("SignalReceiverPassed", persian_green, "⇉", "black")
signal_receiver_reset = State("SignalReceiverReset", waiting_color, "↺", "black")

signal_transmitter = State("SignalTransmitter", persian_green, "⇉⍼", "black")
signal_transmitter_inactive = State("SignalTransmitterInactive", grey, "⍼", "black")
signal_transmitter_reset = State( "SignalTransmitterReset", waiting_color, "⍼↺", "black")
signal_transmitter_accept = State("SignalTransmitterAccept", persian_green, "⍼✔", "black")
signal_transmitter_reject = State("SignalTransmitterReject", Venetian_Red, "⍼✖ ", "black")

signal_wire_inactive = State("SignalWireInactive", grey, "⇉", "black")
signal_wire_active = State("SignalWireActive", persian_green, "⇉", "black")

signal_start_checks_inactive = State("SignalStartChecksInactive", grey, "⏯")
signal_start_checks_active = State("SignalStartChecksActive", persian_green, "⏯")
signal_end_checks_inactive = State("SignalEndChecksInactive", grey, "⏱")
signal_end_checks_accept = State("SignalEndChecksAccept", persian_green, "✔✔")
signal_end_checks_reject = State("SignalEndChecksReject", Venetian_Red, "✖")

signal_conditional_inactive = State("SignalConditionalInactive", grey, "⏱")
signal_conditional_waiting = State("SignalConditionalWaiting", green_yellow_crayola, "⏱")
signal_conditional_intermediate_accept = State("SignalConditionalInterimAccept", activate_next_color, "✔")
signal_conditional_full_accept = State("SignalConditionalFullAccept", Viridian_Green, "✔✔")
signal_conditional_reject = State("SignalConditionalReject", Venetian_Red, "✖")
signal_conditional_reset = State("SignalConditionalReset", waiting_color, "↺")


### Data States
ds_1 = State("1", Papaya_Whip)
ds_0 = State("0", Papaya_Whip)

start_state = State("StartState", Papaya_Whip, "(", "black")
end_state = State("EndState", Papaya_Whip, ")", "black")

start_state_pair = State("StartStatePair", Papaya_Whip, "[", "black")
end_state_pair = State("EndStatePair", Papaya_Whip, "]", "black")

start_data_string = State("StartDataString", Papaya_Whip, "❲", "black")
end_data_string = State("EndDataString", Papaya_Whip, "❳", "black")

north_prefix =  State("NorthPrefix", Papaya_Whip, "𝗡", "black")
south_prefix =  State("SouthPrefix", Papaya_Whip, "𝗦", "black")
east_prefix =  State("EastPrefix", Papaya_Whip, "𝗘", "black")
west_prefix =  State("WestPrefix", Papaya_Whip, "𝗪", "black")
program_prefix =  State("ProgramPrefix", Papaya_Whip, "</>", "black")
reset_prefix =  State("ResetPrefix", Papaya_Whip, "⭯", "black")


ds_states = [ds_0, ds_1, start_state, end_state, start_state_pair, end_state_pair, start_data_string, end_data_string, north_prefix, south_prefix, east_prefix, west_prefix, program_prefix, reset_prefix]

data_states_list_binary_nums_only = [ds_0, ds_1]
data_states_list_all = [start_state] +  data_states_list_binary_nums_only + [end_state]

wire_states = [westWire, eastWire, northWire, southWire, northEastWire, northWestWire, southEastWire,
               southWestWire, westProtectedWire, eastProtectedWire, northProtectedWire, southProtectedWire]
data_states_list_prefixes = [north_prefix, south_prefix, east_prefix, west_prefix, program_prefix,
                             reset_prefix, start_state_pair, end_state_pair, start_data_string, end_data_string, start_state, end_state]
data_states_list_all_with_prefixes_no_order = data_states_list_prefixes + data_states_list_binary_nums_only
copy_wire_states = [northCopyWire, southCopyWire, eastCopyWire, westCopyWire]

# Loops
for i in ds_states:
    # Write the state name
    # Write Inactive
    # Write Writing
    # Write Reading
    # Write Activate Next State
    # Write Deactivate Next State
    # Write Next State Activated
    # Write Reset
    print("Done")

def writeResetStateToFile(name, additional_display_text=""):
    reset_color = waiting_color
    state_var = "reset_{}".format(name)
    state_name = "Reset" + name
    reset_symbol = "↺"
    reset_display_text = reset_symbol + additional_display_text




    return State(state_name + "Reset", waiting_color, "↺", "black")

def writeToFile(state_string):
    file_name = "binaryStates.txt"
    f = open(file_name, "w")




    return
def makeStateInFile(category, name, additional_display_text=""):
    if category == "reset":
        writeResetStateToFile(name, additional_display_text)

    state_var = "{}".format(name)
    state_name = name

class IUState:
    def __init__(self) -> None:
        pass
# Potential Symbols
# ⍼
# ⟥ , ⭤ ⟥, ⭥⟥, ⟥
# ⤕,🔎
