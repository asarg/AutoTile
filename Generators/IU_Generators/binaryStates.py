
from UniversalClasses import State
from Assets.colors import *

# Border
border_state = State("Border", outer_space_crayola, " ", "black")

# Wires
northWire = State("NorthWire", Blue_Sapphire, "🡹")
southWire = State("SouthWire", Blue_Sapphire, "🡻")
westWire = State("WestWire", Blue_Sapphire, "🡸")
eastWire = State("EastWire", Blue_Sapphire, "🡺")

northEastWire = State("NorthEastWire", Blue_Sapphire, "🡹🡺")
northWestWire = State("NorthWestWire", Blue_Sapphire, "🡹🡸")
southEastWire = State("SouthEastWire", Blue_Sapphire, "🡻🡺")
southWestWire = State("SouthWestWire", Blue_Sapphire, "🡻🡸")

northProtectedWire = State("NorthProtectedWire", Blue_Sapphire, "|🡹|")
southProtectedWire = State("SouthProtectedWire", Blue_Sapphire, "|🡻|")
eastProtectedWire = State("EastProtectedWire", Blue_Sapphire, "|🡺|")
westProtectedWire = State("WestProtectedWire", Blue_Sapphire, "|🡸|")
northEastProtectedWire = State("NorthEastProtectedWire", Blue_Sapphire, "|🡹🡺|")
northWestProtectedWire = State("NorthWestProtectedWire", Blue_Sapphire, "|🡹🡸|")
southEastProtectedWire = State("SouthEastProtectedWire", Blue_Sapphire, "|🡻🡺|")
southWestProtectedWire = State("SouthWestProtectedWire", Blue_Sapphire, "|🡻🡸|")

protectWireWalker = State("ProtectWireWalker", Air_Superiority_Blue, "|🖋|")

northCopyWire = State("NorthCopyWire", light_blue, "⇈")
southCopyWire = State("SouthCopyWire", light_blue, "⇊")
westCopyWire = State("WestCopyWire", light_blue, "⇇")
eastCopyWire = State("EastCopyWire", light_blue, "⇉")



# Check For Num Equality
confirm_for_any_num = State("ConfirmForEqualityAnyNum", tea_green, "=*", "black")
confirm_for_equality_zero = State("ConfirmForEqualityZero", tea_green, "=0", "black")
confirm_for_equality_one = State("ConfirmForEqualityOne", tea_green, "=1", "black")

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

confirm_equal_any_prefix = State("ConfirmEqualAnyPrefix", tea_green, "=*ₚ", "black")
confirm_equal_N_prefix = State("ConfirmEqualNPrefix", tea_green, "=Nₚ", "black")
confirm_equal_S_prefix = State("ConfirmEqualSPrefix", tea_green, "=Sₚ", "black")
confirm_equal_E_prefix = State("ConfirmEqualEPrefix", tea_green, "=Eₚ", "black")
confirm_equal_W_prefix = State("ConfirmEqualWPrefix", tea_green, "=Wₚ", "black")
confirm_equal_C_prefix = State("ConfirmEqualCustomPrefix", tea_green, "=Cₚ", "black")
confirm_equal_P_prefix = State("ConfirmEqualProgramPrefix", tea_green, "=Pₚ", "black")

# Check For Caps
confirm_for_any_cap = State("ConfirmForAnyCap", tea_green, "=*₍₎", "black")
confirm_for_any_start_cap = State("ConfirmForStartCap", tea_green, "=*ᵦ₍", "black")
confirm_for_any_end_cap = State("ConfirmForEndCap", tea_green, "=*ₔ₎", "black")
confirm_for_start_state_cap = State("ConfirmForStartStateCap", tea_green, "=(ᵦ", "black")
confirm_for_end_state_cap = State("ConfirmForEndStateCap", tea_green, "=)ₔ", "black")
confirm_for_end_state_pair_cap = State("ConfirmForEndStatePairCap", tea_green, "=]ₔ", "black")
confirm_for_start_state_pair_cap = State("ConfirmForStartStatePairCap", tea_green, "=[ᵦ", "black")
confirm_end_string_cap = State("ConfirmEndStringCap", tea_green, "=﹞ₔ", "black")
confirm_start_string_cap = State("ConfirmStartStringCap", tea_green, "=﹝ᵦ", "black")

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
endcap_door_west_reset = State("EndcapDoorWestReset", mango_tango, "↺◨", "black")
endcap_door_west_handle_reset = State("EndCapDoorHandleWestReset", mango_tango, "↺◨~🔒", "black")
endcap_door_west_handle_reset_waiting = State("EndCapDoorHandleWestResetWaiting", mango_tango, "↺⏱◨~", "black")
endcap_door_west_reset_waiting = State("EndcapDoorWestResetWaiting", mango_tango, "↺⏱◨", "black")

### Single Doors
signal_door_inactive = State("LockedSignalDoorInactive", grey, "🔒▦", "black")
signal_door_handle_inactive = State("LockedSignalDoorHandleInactive", grey, "🗝~", "black")
signal_door_handle_reset = State("SignalDoorHandleReset", mango_tango, "↺🗝~", "black")
signal_door_open = State("SignalDoorOpen", persian_green, "🔓▦", "black")
signal_door_handle_open = State("SignalDoorHandleOpen", persian_green, "🗝~", "black")

signal_door_propped_open = State("SignalDoorProppedOpen", persian_green, "🔓", "black")
signal_door_reset = State("SignalDoorReset", mango_tango, "↺▦", "black")
signal_door_reset_walk = State("SignalDoorResetWalk", mango_tango, "↺▦◃", "black")
signal_door_send_confirmed_transmission = State("SignalDoorSendConfirmedTransmission", mango_tango, "▦⇉✅", "black")
reset_confirmed_transmission_westWire = State("ResetConfirmedTransmissionWest", mango_tango, "↺✅⇉", "black")


### Signal Door Checks
closed_endcap_door_check_signal = State("ClosedEndcapDoorCheckSignal", grey, "✅", "black")
closed_endcap_door_check_signal_inactive = State("ClosedEndcapDoorCheckSignalInactive", grey, "❌", "black")

signal_transmitter_turn_down_inactive = State("SignalTransmitterTurnDownInactive", grey, "⮮", "black")
signal_transmitter_turn_down_active = State("SignalTransmitterTurnDownActive", persian_green, "⮮", "black")
signal_transmitter_turn_down_open = State("SignalTransmitterTurnDownOpen", persian_green, "⮮", "black")
signal_transmitter_turn_down_reset = State("SignalTransmitterTurnDownReset", mango_tango, "↺⮮", "black")

signal_transmitter_turn_up_inactive = State("SignalTransmitterTurnUpInactive", grey, "⮲", "black")
signal_transmitter_turn_up_active = State("SignalTransmitterTurnUpActive", persian_green, "⮲", "black")
signal_transmitter_turn_up_reset = State("SignalTransmitterTurnUpReset", mango_tango, "↺⮲", "black")

row_signal_positive_inactive = State("RowSignalPositiveInactive", grey, "⊝", "black")

row_signal_positive_start_inactive = State("RowSignalPositiveStartInactive", green_yellow_crayola, "⊝", "black")

row_signal_positive_start_waiting = State("RowSignalPositiveStartWaiting", green_yellow_crayola, "⊝⏱", "black")

row_signal_positive_waiting = State("RowSignalPositiveWaiting", green_yellow_crayola, "⏱", "black")
row_signal_positive_full_accept = State("RowSignalPositiveFullAccept", Viridian_Green, "✅")
row_signal_intermediate_accept = State("RowSignalPositiveInterimAccept", pistachio, "✅")
row_signal_positive_reset = State("RowSignalPositiveReset", mango_tango, "↺", "black")





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
