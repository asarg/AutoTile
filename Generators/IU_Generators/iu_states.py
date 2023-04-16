from Generators.IU_Generators.binary_symbols_colors import *
from UniversalClasses import State

# Border States
border_state = State("Border", border_color, " ")
row_border = State("RowBorder", border_color, "═")
blank_state = State("BlankState", border_color, " ")
no_affinity_state = State("NoAffinityState", no_affinity_color, "✖")
nonDeterministicSelector = State("NonDeterministicSelector", signal_wire_color, " ")

## Corner Border States
northWestCorner = State("NorthWestCorner", border_color, "╔")
southWestCorner = State("SouthWestCorner", border_color, "╚")
northEastCorner = State("NorthEastCorner", border_color, "╗")
southEastCorner = State("SouthEastCorner", border_color, "╝")

## Column Border States
columnMarkerTopStart = State("ColumnMarkerTopStart", column_marker_color, column_top_start_sym)
columnMarkerTopEnd = State("ColumnMarkerTopEnd", column_marker_color, column_top_end_sym)
columnMarkerBottomStart = State("ColumnMarkerBottomStart", column_marker_color, column_bottom_start_sym)
columnMarkerBottomEnd = State("ColumnMarkerBottomEnd", column_marker_color, column_bottom_end_sym)
activeStateColumnTopStart = State("ActiveStateColumnTopStart", active_column_marker_color, column_top_start_sym)
activeStateColumnTopEnd = State("ActiveStateColumnTopEnd", active_column_marker_color, column_top_end_sym)
columnBorder = State("ColumnBorder", column_marker_color, "║")

## Row Border States
rowMarkerStartTop = State("RowMarkerStartTop", row_marker_color, row_start_top_sym)
rowMarkerStartBottom = State("RowMarkerStartBottom", row_marker_color, row_start_bottom_sym)
rowMarkerEndTop = State("RowMarkerEndTop", row_marker_color, row_end_top_sym)
rowMarkerEndBottom = State("RowMarkerEndBottom", row_marker_color, row_end_bottom_sym)
rowStartMarker = State("RowStartMarker", border_color, "╠")

# Data states
ds_1_active = State("1_Active", data_color, "1")
ds_1_inactive = State("1_Inactive", inactive_data_color, "1")

ds_blank_active = State("DataBlankActive", data_color, " ")
ds_blank_inactive = State("DataBlankInactive", inactive_data_color, " ")

start_state = State("StartState", data_color, start_state_pair_marker_sym)
start_state_inactive = State("StartStateInactive", inactive_data_color, start_state_pair_marker_sym)
neg_start_state = State("NegStartState", neg_data_color, end_state_pair_marker_sym)
neg_start_state_inactive = State("NegStartStateInactive", neg_inactive_data_color, end_state_pair_marker_sym)

end_state = State("EndState", data_color, end_state_pair_marker_sym)
end_state_inactive = State("EndStateInactive", inactive_data_color, end_state_pair_marker_sym)

ds_1_inactive_mc = State("1InactiveMC", inactive_data_color, "1")
ds_pos_placeholder = State("PosPlaceholder", data_color, " ")
inactive_blank_pos_data = State("InactiveBlankPosData", inactive_data_color, " ")
neg_ds_1 = State("-1", neg_data_color, "-1")
neg_ds_1_inactive_mc = State("-1InactiveMC", neg_inactive_data_color, "-1")
inactive_blank_neg_data = State("InactiveBlankNegData", neg_inactive_data_color, " ")

# Wire States
westWire = State("WestWire", wire_color, "🡸")
eastWire = State("EastWire", wire_color, "🡺")
northWire = State("NorthWire", wire_color, "🡹")
southWire = State("SouthWire", wire_color, "🡻")

northEastWire = State("NorthEastWire", wire_color, "🡽")
northWestWire = State("NorthWestWire", wire_color, "🡼")
southEastWire = State("SouthEastWire", wire_color, "🡾")
southWestWire = State("SouthWestWire", wire_color, "🡿")

signal_wire_inactive = State("SignalWireInactive", signal_wire_color, "⇇")
signal_wire_ns = State("SignalWireNS", signal_wire_color, "⭥⟥")
signal_wire_active = State("SignalWireActive", signal_wire_color, "⇉")
######## Doors ########

## Macrotile Edge Doors
tile_edge_center_handle_east_inactive = State("TileEdgeCenterHandleEastInactive", block_edge_handle_color, "╠ ⍨")  # ₑ
tile_edge_center_handle_west_inactive = State("TileEdgeCenterHandleWestInactive", block_edge_handle_color, "⍨ ╣")  # ʷ ⬓
tile_edge_center_handle_south_inactive = State("TileEdgeCenterHandleSouthInactive", block_edge_handle_color, "⍨ ╦")
tile_edge_center_handle_north_inactive = State("TileEdgeCenterHandleNorthInactive", block_edge_handle_color, "╩ ⍨")

tile_east_edge_door_out_wire_inactive = State("TileEastEdgeDoorOutWireInactive", block_edge_door_color, "╠ ⬓")
tile_west_edge_door_out_wire_inactive = State("TileWestEdgeDoorOutWireInactive", block_edge_door_color, "⬓ ╣")
tile_north_edge_door_out_wire_inactive = State("TileNorthEdgeDoorOutWireInactive", block_edge_door_color, "╩ ⬓")
tile_south_edge_door_out_wire_inactive = State("TileSouthEdgeDoorOutWireInactive", block_edge_door_color, "⬓ ╦")

tile_east_edge_door_out_wire_active = State("TileEastEdgeDoorOutWireActive", block_edge_door_color, "╠ ⬓")
tile_east_edge_door_in_wire_active = State("TileEastEdgeDoorInWireActive", block_edge_door_color, "╠ ⬓")
## Trap Doors
trap_door_inactive = State("TrapDoorInactive", trap_door_inactive_color, "⬓")  # 🚪 ▩
trap_door_active = State("TrapDoorActive", trap_door_color, "⬓")
trap_door_used = State("TrapDoorUsed", reset_color, "⬓")

### Signal Doors
signal_door_inactive = State("LockedSignalDoorInactive", signal_door_inactive_color, "🔒🚪")  # 🚪 ◨
signal_door_intermediate_accept = State("SignalDoorIntermediateAccept", signal_door_inactive_color, "🚪↯")  # ◨↯
signal_door_open = State("SignalDoorOpen", signal_door_accept_color, "🔓◨") # 🔓◨
signal_door_transmit = State("SignalDoorTransmit",signal_door_waiting_color, "◨↯") # ◨↯
signal_door_active_waiting_east = State("SignalDoorActiveWaitingEast",signal_door_waiting_color, "◨⇉⏱") # ◨⇉⏱
signal_door_handle_inactive = State("LockedSignalDoorHandleInactive", signal_door_inactive_color, "🗝~") # 🗝~
signal_door_handle_reset = State("SignalDoorHandleReset", reset_color, "↺🗝~") # ↺🗝~
signal_door_inactive_east = State("LockedSignalDoorInactiveEast", signal_door_inactive_color, "🚪⇉")  # ◨⇉

signal_door_north_handle_inactive = State("LockedSignalDoorNorthHandleInactive", signal_door_inactive_color, "🗝~⇈")
signal_door_handle_open = State("SignalDoorHandleOpen", signal_door_color, "🗝~")
signal_door_handle_active_waiting = State("SignalDoorHandleActiveWaiting", signal_door_waiting_color, "⏱🗝~")
signal_door_handle_accept = State("SignalDoorHandleAccept", signal_door_color, "🗝~")
signal_door_handle_intermediate_accept = State("SignalDoorHandleIntermediateAccept", signal_door_accept_color, "🗝~")
signal_door_handle_pass_accept_south = State("SignalDoorHandlePassAcceptSouth", signal_door_color, "🗝~↧↯")
signal_door_handle_pass_accept_north = State("SignalDoorHandlePassAcceptNorth", signal_door_color, "🗝~↥↯")
signal_door_handle_find_corner_north=State("SignalDoorHandleFindCornerNorth", signal_door_waiting_color, "🗝~↥↯")
signal_door_handle_find_corner_south = State("SignalDoorHandleFindCornerSouth",signal_door_waiting_color, "🗝~↧↯")
signal_door_handle_pass_find_corner_north = State("SignalDoorHandlePassFindCornerNorth",signal_door_waiting_color, "🗝~↥↯")
signal_door_handle_pass_find_corner_south = State("SignalDoorHandlePassFindCornerSouth",signal_door_waiting_color, "🗝~↧↯")
signal_door_handle_accept_north = State("SignalDoorHandleAcceptNorth", signal_door_accept_color, "🗝~↥↯")
signal_door_handle_accept_south = State("SignalDoorHandleAcceptSouth", signal_door_accept_color, "🗝~↧↯")



##### Signal Receivers and Transmitters
signal_receiver_inactive = State("SignalReceiverInactive", signal_inactive_color, "⊝")
signal_received_accept = State("SignalReceivedAccept", signal_accept_color, "✔✔")
signal_received_reject = State("SignalReceivedReject", signal_reject_color, "✖")
signal_receiver_passed = State("SignalReceiverPassed", signal_accept_color, "⇉")
signal_receiver_reset = State("SignalReceiverReset", signal_receiver_color, "↺")
signal_receiver_pass_find_corner_north = State("SignalReceiverPassFindCornerNorth", signal_waiting_color, "?↥↯")
signal_receiver_pass_find_corner_south = State("SignalReceiverPassFindCornerSouth", signal_waiting_color, "?↧↯")
signal_receiver_pass_accept_north = State("SignalReceiverPassAcceptNorth", signal_accept_color, "✔↥↯")
signal_receiver_pass_accept_south = State("SignalReceiverPassAcceptSouth", signal_accept_color, "✔↧↯")

signal_transmitter = State("SignalTransmitter", signal_accept_color, "⇉⍼")
signal_transmitter_inactive = State("SignalTransmitterInactive", signal_inactive_color, "⍼")
signal_transmitter_reset = State( "SignalTransmitterReset", signal_waiting_color, "⍼↺")
signal_transmitter_accept = State("SignalTransmitterAccept", signal_accept_color, "⍼✔")
signal_transmitter_reject = State("SignalTransmitterReject", signal_reject_color, "⍼✖ ")
signal_transmitter_pass_find_corner_north = State("SignalTransmitterPassFindCornerNorth", signal_waiting_color, "?↥⍼")
signal_transmitter_pass_find_corner_south = State("SignalTransmitterPassFindCornerSouth", signal_waiting_color, "?↧⍼")
signal_transmitter_pass_accept_north = State("SignalTransmitterPassAcceptNorth", signal_waiting_color, "◨↥⍼")
signal_transmitter_pass_accept_south = State("SignalTransmitterPassAcceptSouth", signal_waiting_color, "◨↧⍼")

################ Macrocell States ################
# Macrocell Components
punch_down_ds_active = State("PunchDownDSActive", punch_down_color, "V")
punch_down_ds_end_found = State("PunchDownDSEndFound", punch_down_color, "V*")
punch_down_ds_inactive = State("PunchDownDSInactive", inactive_punch_down_color, "V")
punch_down_ds_neg_active = State("PunchDownNegActive", neg_punch_down_color, "V")
punch_down_ds_neg_inactive = State("PunchDownNegInactive", inactive_neg_punch_down_color, "V")
punch_down_ds_neg_end_found = State("PunchDownNegEndFound", neg_punch_down_color, "V*")
mc_door_east_positive_inactive = State("MCDoorEast+Inactive", inactive_punch_down_color, "+⬓")
mc_door_handle_east_positive_inactive = State("MCDoorHandleEast+Inactive", inactive_punch_down_color, "+~")
mc_door_east_negative_inactive = State("MCDoorEast-Inactive", inactive_neg_punch_down_color, "-⬓")
mc_door_handle_east_negative_inactive = State("MCDoorHandleEast-Inactive", inactive_neg_punch_down_color, "-~")
mc_door_east_positive_active = State("MCDoorEast+Active", punch_down_color, "+⬓")
mc_door_handle_east_positive_active = State("MCDoorHandleEast+Active", punch_down_color, "+~")
mc_door_east_negative_active = State("MCDoorEast-Active", neg_punch_down_color, "-⬓")
mc_door_handle_current_state_active = State("MCDoorHandleCurrentStateActive", punch_down_color, "~")
mc_door_current_state_active = State("MCDoorCurrentStateActive", punch_down_color, "⬓")
mc_door_current_state_inactive = State("MCDoorCurrentStateInactive", inactive_punch_down_color, "⬓")
mc_door_handle_current_state_inactive = State("MCDoorHandleCurrentStateInactive", inactive_punch_down_color, "~")
mc_door_trigger_transition = State("MCDoorTriggerTransition", punch_down_color, "⬓**")
mc_door_handle_trigger_transition = State("MCDoorHandleTriggerTransition", punch_down_color, "~**")
mc_check_transition_affinity_inactive = State("MCDoorCheckTransitionAffinityInactive", inactive_punch_down_color, "✑?")
mc_check_transition_affinity_inactive_neg = State("MCDoorCheckTransitionAffinityInactiveNeg", inactive_neg_punch_down_color, "✑?")
mc_door_neg_signal_transmitter = State("MCDoorNegSignalTransmitter", neg_punch_down_color, "✑")


####### Table lookup states
columnOutputRowNorthMarker = State("columnOutputRowNorthMarker", col_output_row_marker_color, "𝗡⎋")
columnOutputRowSouthMarker = State("columnOutputRowSouthMarker", col_output_row_marker_color, "𝗦⎋")
columnOutputRowEastMarker = State("columnOutputRowEastMarker", col_output_row_marker_color, "𝗘⎋")
columnOutputRowWestMarker = State("columnOutputRowWestMarker", col_output_row_marker_color, "𝗪⎋")

## Construction States
selectedAttachmentState = State("SelectedAttachmentState", selected_attachment_color, "S*")
selectedAttachmentStateHolder = State("SelectedAttachmentStateHolder", selected_attachment_inactive_color, "|S*|")
selectedAttachmentStateHolderActive = State("SelectedAttachmentStateHolderActive", selected_attachment_color, "|S*|")
