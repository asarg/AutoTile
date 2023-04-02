from Generators.IU_Generators.binary_symbols_colors import *
from UniversalClasses import State

# Border States
border_state = State("Border", border_color, " ")

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

# Data states
ds_1_active = State("1_Active", data_color, "1")
ds_1_inactive = State("1_Inactive", inactive_data_color, "1")

ds_blank_active = State("DataBlankActive", data_color, " ")
ds_blank_inactive = State("DataBlankInactive", inactive_data_color, " ")

start_state_pair = State("StartStatePair", data_color, start_state_pair_marker)
end_state_pair = State("EndStatePair", data_color, end_state_pair_marker)

# Wire States
westWire = State("WestWire", wire_color, "🡸")
eastWire = State("EastWire", wire_color, "🡺")
northWire = State("NorthWire", wire_color, "🡹")
southWire = State("SouthWire", wire_color, "🡻")

northEastWire = State("NorthEastWire", wire_color, "🡽")
northWestWire = State("NorthWestWire", wire_color, "🡼")
southEastWire = State("SouthEastWire", wire_color, "🡾")
southWestWire = State("SouthWestWire", wire_color, "🡿")
