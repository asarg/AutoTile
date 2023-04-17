from Generators.IU_Generators.iu_states import *
from UniversalClasses import State, TransitionRule, AffinityRule, System, Tile, Assembly
from Assets.colors import *
import sys

exSt = [State("A", active_color), State("B", inactive_color), State("C", wire_color)]
xISt = [State("A", active_color), State("B", inactive_color), State("C", wire_color)]
xSSt = [State("A", active_color)]
vaff = [AffinityRule("A", "B", "v", 1), AffinityRule("C", "A", "v", 1), AffinityRule("C", "B", "v", 1)]
hAff = [AffinityRule("B", "B", "h", 1), AffinityRule("C", "C", "h", 1), AffinityRule("A", "C", "h", 1)]
vtr = [TransitionRule("A", "B", "A", "A", "v"), TransitionRule("B", "C", "A", "C", "v")]
htr = [TransitionRule("C", "C", "B", "A", "h"), TransitionRule("A", "C", "B", "C", "h")]
exampleSystem = System(1, exSt, xISt, xSSt, vaff, hAff, vtr, htr)  # seed assm)

class Gadget(Assembly):
    def __init__(self):
        super().__init__()


class Wire:
    def __init__(self, start_x, start_y, end_x, end_y, start_direction, label=None, input_state=None, input_state_dir=None, wire_len=-1):

        if label is None:
            if input_state is None:
                label = "wire|({},{}), ({},{})| {}".format(start_x, start_y, end_x, end_y, start_direction)
            else:
                if input_state_dir is None:
                    label = "wire{}|({},{}), ({},{})| {}".format(input_state.label, start_x, start_y, end_x, end_y, start_direction)
                else:
                    label = "wire{}_{}|({},{}), ({},{})| {}".format(input_state.label, input_state_dir, start_x, start_y, end_x, end_y, start_direction)

        self.label = label
        start_direction = start_direction.lower()
        self.start_direction = start_direction
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.input_state = input_state
        self.input_state_dir = input_state_dir
        self.wire_len = wire_len
        self.tiles = self.addWireTiles()

    def returnTiles(self):
        if self.tiles is None:
            self.tiles = self.addWireTiles()
        return self.tiles

    def addWireTiles(self):
        t = []
        sd = self.start_direction
        if sd == "w":
            dir_state = westWire
            for i in range(self.start_x, self.end_x):
                t.append(Tile(dir_state, i, self.start_y))
        elif sd == "n":
            dir_state = northWire
            for i in range(self.start_y, self.end_y, -1):
                t.append(Tile(dir_state, self.start_x, i))
        elif sd == "s":
            dir_state = southWire
            for i in range(self.start_y, self.end_y, -1):
                t.append(Tile(dir_state, self.start_x, i))
        elif sd == "e":
            dir_state = eastWire
            for i in range(self.start_x, self.end_x):
                t.append(Tile(dir_state, i, self.start_y))
        return t

class Row:
    def __init__(self, input_state, direction, start_x, start_y, row_width, row_height=None, row_num=None, incoming_tile_dir=None, map_dict=None):

        self.input_state = input_state
        self.input_wire_direction = direction
        self.start_x = start_x
        self.start_y = start_y
        self.wire_x = start_x
        self.wire_y = start_y - 1
        self.end_x = self.wire_x + row_width
        self.end_y = self.wire_y - 2
        self.border_y = self.wire_y - 3
        self.row_width = row_width
        self.row_height = row_height
        self.wire = Wire(start_x - 3, self.wire_y, start_x + row_width + 1,
                         "e", label=f'{row_num}_{input_state.label}_', input_state=input_state, input_state_dir=direction)
        self.wire_tiles = self.addWireTiles()
        self.enter_door = self.addDoorTiles()
        self.border_tiles = self.addBorderTiles()
        self.tiles = self.addWireTiles() + self.addBorderTiles() + self.addDoorTiles()



    def addWireTiles(self):
        t = self.wire.returnTiles()
        return t

    def addDoorTiles(self):
        t = [Tile(signal_door_inactive_east, self.start_x, self.wire_y),
             Tile(signal_door_handle_inactive, self.start_x, self.wire_y + 1),
             Tile(signal_receiver_inactive, self.start_x, self.wire_y - 1),
             Tile(signal_transmitter_inactive, self.start_x, self.wire_y - 2),
             Tile(row_border, self.start_x, self.border_y) ]
        return t

    def addBorderTiles(self):
        t = []
        for i in range(self.start_x + 1, self.start_x + self.row_width):
            t.append(Tile(row_border, i, self.border_y))
        return t

    def returnTiles(self):
        return self.tiles

class MacroCell:
    def __init__(self, row_state, col_state, dir, affinity=None, transition=None, mc_size_dimensions={}):

        self.col_state = col_state
        self.row_state = row_state
        self.dir = dir
        self.affinity = affinity
        self.transition = transition
        self.mc_size_dimensions = mc_size_dimensions



        # mc_size_dimensions={"unaryNumLen": 1, "writeRowSize": 3, "unBorderedMacroCellWidth": 5, "borderedMacroCellWidth": 7, "borderedMacroCellWidthTrapDoor": 8, "borderedMacroCellWidthWithTDAndWirePadding": 8, "unborderedMacrocellHeight": 4, "borderedMacroCellHeight": 6}

    def setAffinity(self, affinity):
        self.affinity = affinity

    def setTransition(self, transition):
        self.transition = transition

    def addColRowNumInfo(self, col_num, row_num):
        self.col_num = col_num
        self.row_num = row_num

    def addColumnTransitionNum(self, transition_num):
        self.transition_col_change_num = transition_num

    def addMCDimensions(self, unaryNumLen=None, writeRowSize=None, unBorderedMacroCellWidth=None, borderedMacroCellWidth=None, borderedMacroCellWidthTrapDoor=None, borderedMacroCellWidthWithTDAndWirePadding=None, unborderedMacrocellHeight=None, borderedMacroCellHeight=None, mc_demensions={}):
        #borderedMacroCellWidthWithTDAndWirePadding, borderedMacroCellHeight, unborderedMacrocellHeight, borderedMacroCellWidthTrapDoor, borderedMacroCellWidth, unBorderedMacroCellWidth, writeRowSize, unaryNumLen
        if mc_demensions != {}:
            self.mc_size_dimensions = mc_demensions
        else:
            self.mc_size_dimensions["unaryNumLen"] = unaryNumLen
            self.mc_size_dimensions["writeRowSize"] = writeRowSize
            self.mc_size_dimensions["unborderedMacroCellWidth"] = unBorderedMacroCellWidth
            self.mc_size_dimensions["borderedMacroCellWidth"] = borderedMacroCellWidth
            self.mc_size_dimensions["borderedMacroCellWidthTrapDoor"] = borderedMacroCellWidthTrapDoor
            self.mc_size_dimensions["borderedMacroCellWidthWithTDAndWirePadding"] = borderedMacroCellWidthWithTDAndWirePadding
            self.mc_size_dimensions["unborderedMacrocellHeight"] = unborderedMacrocellHeight
            self.mc_size_dimensions["borderedMacroCellHeight"] = borderedMacroCellHeight


    def addMcCoords(self, mc_neg_door_x, mc_door_y):
        self.mc_door_y = mc_door_y
        self.out_wire_y = int(self.mc_size_dimensions["unborderedMacroCellWidth"])
        self.mc_neg_door_x = mc_neg_door_x

        self.mc_pos_door_x = mc_neg_door_x + \
            int(self.mc_size_dimensions["unborderedMacroCellWidth"]) - 1
        self.mc_trap_door_x = self.mc_pos_door_x + 1
        self.mc_northmost_y = mc_door_y + 2
        self.mc_southmost_y = mc_door_y - 3
        self.mc_westmost_x = mc_neg_door_x
        self.mc_eastmost_x = self.mc_trap_door_x + 1


    def makeDoorPunchdownTiles(self):
        mc_door_tiles = []
        mc_door_tiles.append(Tile(mc_door_east_positive_inactive, self.mc_pos_door_x,  self.mc_door_y))
        mc_door_tiles.append(Tile(mc_door_east_negative_inactive, self.mc_neg_door_x, self.mc_door_y))
        mc_door_tiles.append(Tile(mc_door_handle_east_negative_inactive, self.mc_neg_door_x, self.mc_door_y + 1))
        mc_door_tiles.append(Tile(mc_door_handle_east_positive_inactive, self.mc_pos_door_x, self.mc_door_y + 1))
        mc_door_tiles.append(Tile(punch_down_ds_neg_active, self.mc_neg_door_x + 1, self.mc_door_y + 1))
        mc_door_tiles.append(Tile(punch_down_ds_active, self.mc_pos_door_x - 1, self.mc_door_y + 1))


        return mc_door_tiles
    def mc_signal_tiles(self):
        ### Signal Pass Column
        signal_tiles = []
        signal_tiles.append(Tile(signal_transmitter_inactive, self.mc_pos_door_x, self.mc_door_y + 2))
        signal_tiles.append(Tile(signal_wire_ns, self.mc_pos_door_x, self.mc_door_y + 3))
        signal_tiles.append(Tile(signal_transmitter_inactive, self.mc_neg_door_x, self.mc_door_y + 2))
        signal_tiles.append(Tile(signal_wire_ns, self.mc_pos_door_x, self.mc_door_y - 2))
        for i in range(self.mc_neg_door_x + 1, self.mc_pos_door_x):
                signal_tiles.append(Tile(signal_wire_active, i, self.mc_door_y + 2))

        return signal_tiles
    def makeMcEastWireTiles(self):
        mc_wire_tiles = []
        for i in range(self.mc_neg_door_x + 1, self.mc_trap_door_x + 4):
            if i != self.mc_pos_door_x:
                mc_wire_tiles.append(Tile(eastWire, i, self.mc_door_y))
        return mc_wire_tiles

    def makeWriteRowTiles(self,  tr_change_num=None):
        write_row_tiles = []
        dec = abs(tr_change_num)
        #write_row_tiles.append(Tile(mc_check_transition_affinity_inactive_neg, self.mc_neg_door_x, self.mc_door_y - 1))
        #write_row_tiles.append(Tile(mc_check_transition_affinity_inactive, self.mc_pos_door_x, self.mc_door_y - 1))
        write_row_tiles.append(Tile(signal_receiver_inactive, self.mc_neg_door_x, self.mc_door_y - 1))
        write_row_tiles.append(Tile(signal_receiver_inactive, self.mc_pos_door_x, self.mc_door_y - 1))
        if self.affinity == None and self.transition == None:
            for i in range(self.mc_neg_door_x + 1, self.mc_pos_door_x):
                write_row_tiles.append(Tile(no_affinity_state, i, self.mc_door_y - 1))

        elif self.transition_col_change_num < 0:
            write_row_tiles.append(
                Tile(neg_start_state_inactive, self.mc_pos_door_x - 1, self.mc_door_y - 1))
            for i in range(self.mc_pos_door_x - 2, self.mc_neg_door_x, -1):
                if dec > 0:
                    write_row_tiles.append(Tile(neg_ds_1_inactive_mc, i, self.mc_door_y - 1))
                    dec -= 1
                else:
                    write_row_tiles.append(Tile(inactive_blank_neg_data, i, self.mc_door_y - 1))

        elif self.transition_col_change_num > 0:
            write_row_tiles.append(Tile(start_state_inactive, self.mc_neg_door_x + 1, self.mc_door_y - 1))
            for i in range(self.mc_neg_door_x + 2, self.mc_pos_door_x):
                if dec > 0:
                    write_row_tiles.append(Tile(ds_1_inactive_mc, i, self.mc_door_y - 1))
                    dec -= 1
                else:
                    write_row_tiles.append(Tile(inactive_blank_pos_data, i, self.mc_door_y - 1))
        else:
            for i in range(self.mc_neg_door_x + 1, self.mc_pos_door_x):
                write_row_tiles.append(Tile(blank_state, i, self.mc_door_y - 1))
        return write_row_tiles

    def addTrapDoorTiles(self):
        trap_door_tiles = [Tile(trap_door_inactive, self.mc_trap_door_x, self.mc_door_y - 1),
                           Tile(southWire, self.mc_trap_door_x, self.mc_door_y - 2),
                           Tile(southWire, self.mc_trap_door_x, self.mc_door_y + 2),
                           Tile(southWire, self.mc_trap_door_x, self.mc_door_y + 1),
                           Tile(southWire, self.mc_trap_door_x, self.mc_door_y + 3)
                           ]

        return trap_door_tiles


    def makeBorderTiles(self):
        border_tiles = []
        for i in range(self.mc_neg_door_x, self.mc_pos_door_x):
            border_tiles.append(Tile(row_border, i, self.mc_size_dimensions[""]))

    def makeMacroCell_MC(self, mc_neg_door_x, mc_door_y, tr_change_num):
        self.transition_col_change_num = tr_change_num
        mc_a = Assembly()
        self.addMcCoords(mc_neg_door_x, mc_door_y)
        mc_a.setTiles(self.makeDoorPunchdownTiles())
        mc_a.setTiles(self.makeMcEastWireTiles())
        mc_a.setTiles(self.makeWriteRowTiles(tr_change_num))
        mc_a.setTiles(self.addTrapDoorTiles())
        mc_a.setTiles(self.mc_signal_tiles())
        self.mc_assembly = mc_a
        return mc_a.returnTiles()




class Column:
    def __init__(self, input_state, start_x, start_y, row_height, input_system, rows_mapped_to_input_states_dirs={1:("A", "N"), 2:"B", 3:"C"},
                 macro_cells_in_column=None, column_height=-1):
        self.input_state = input_state
        self.input_system_states = input_system.returnStates()
        self.column_num = input_system.returnStates().index(input_state)
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = start_x + (len(self.input_system_states) + 2 + 2)
        self.end_y = start_y - column_height - 1
        self.trap_door_y_sub = 1
        self.trap_door_x_add = 1
        self.column_width = len(self.input_system_states) + 2 + 1

        self.num_rows = len(rows_mapped_to_input_states_dirs)

        self.rows_mapped_to_input_states_dirs = rows_mapped_to_input_states_dirs
        if column_height == -1:
            column_height = row_height * self.num_rows
        self.column_height = column_height
        self.row_height = row_height
        self.row_wire_y_offset = row_height - 3
        self.col_wire = self.makeColWire()
        self.macro_cells_in_column = macro_cells_in_column
        self.tiles = self.makeColTiles()
    def makeColWire(self):
        c_start_x = self.start_x + (self.column_width - 1)
        c_start_y = self.start_y
        c_end_x = self.start_x + (self.column_width - 1)
        c_end_y = self.end_y
        print("c_start_x is:", c_start_x)
        print("c_start_y is:", c_start_y)
        print("c_end_x is:", c_end_x)
        print("c_end_y is:", c_end_y)
        col_wire = Wire(c_start_x, c_start_y, c_end_x, c_end_y, "s", label=None, input_state=self.input_state, input_state_dir=None)
        print("len of col wire is:", len(col_wire.returnTiles()))
        return col_wire

    def make_top_col(self):
        self.start_x = self.start_x + 1
        self.start_y = self.start_y + 1
    def makeColTiles(self):
        if self.col_wire is None:
            w = self.makeColWire()
        else:
            w = self.col_wire
        t = w.returnTiles()
        print("len of col tiles is:", len(t))
        end_t = []
        for i in range(1, len(t)):
            if i % self.row_height != (self.row_wire_y_offset):
                end_t.append(t[i])
        return end_t

    def returnColTiles(self):
        return self.tiles



class Table:
    def __init__(self, inputSystem, start_x=0, start_y=0):
        self.input_system = inputSystem
        self.input_system_states = inputSystem.returnStates()
        self.aff_tr_dict = self.makeAffTrDict()
        self.tl_corner_x_y = (start_x, start_y)
        self.cols_to_input_states_map, self.rows_to_input_states_dirs_map, self.input_states_to_rows_cols_map = self.mapInputStates()
        self.macrocell_size = self.calculateMacroCellSize()
        self.width, self.height, self.tr_corner_x_y, self.bl_corner_x_y, self.br_corner_x_y = self.calculateTableSize()
        self.start_intersections, self.cols_wires_intersections, self.macro_row_col_intersection_dict = self.calcIntersections()
        self.macrocells, self.macrocell_tiles = self.makeMacroCells_Table() # macrocells




    def mapInputStates(self):
        cols_to_states = {}
        rows_to_states_dirs = {}
        input_states_to_rows_cols= {}
        dirs_to_states = {"N":[], "E":[], "S":[], "W":[]}
        dirs = ["N", "E", "S", "W"]
        for i, j in enumerate(self.input_system_states):
            input_states_to_rows_cols[j.label] = {"col": i, "rows": {}}
            cols_to_states[i] = j
            for k in dirs:
                dirs_to_states[k].append(j)

        row_counter = 0
        for key, value in dirs_to_states.items():
            for i in value:
                rows_to_states_dirs[row_counter] = (i, key)

                input_states_to_rows_cols[i.label]["rows"][key] = row_counter
                row_counter += 1

        return cols_to_states, rows_to_states_dirs, input_states_to_rows_cols
    def calculateTableSize(self):
        mc_size = self.macrocell_size
        rows_num = len(self.input_system_states)*4
        cols_num = len(self.input_system_states)
        # 2 for the border, 3 for the starting wire padding
        table_width = cols_num * mc_size["borderedMacroCellWidthWithTDAndWirePadding"] + 2
        table_height = rows_num * mc_size["borderedMacroCellHeight"] + 2  # 2 for the border
        tr_corner_x_y = (self.tl_corner_x_y[0] + table_width, self.tl_corner_x_y[1])
        bl_corner_x_y = (self.tl_corner_x_y[0], self.tl_corner_x_y[1] - table_height)
        br_corner_x_y = (self.tl_corner_x_y[0] + table_width, self.tl_corner_x_y[1] - table_height)
        return table_width, table_height, tr_corner_x_y, bl_corner_x_y, br_corner_x_y

    def calculateColumnsLocations(self):
        mc_size = self.calculateMacroCellSize()
        begin_cols_x = self.tl_corner_x_y[0] + 3
        cols_size = mc_size["borderedMacroCellWidthWithTDAndWirePadding"]
        #end_cols_x = begin_cols_x + mc_size["unborderedMacroCellWidth"] * len(self.input_system_states)
        end_buffer = 3
        end_cols_x = begin_cols_x + cols_size*len(self.input_system_states) - end_buffer
        end_col_corners = begin_cols_x + cols_size - 5
        begin_col_wires = begin_cols_x + cols_size - 4

        cols_start_x_list = []
        cols_wire_start_list = []
        cols_end_x_list = []
        cols_start_placing_unary_nums = []
        cplaceux = end_col_corners - 2
        i = 0
        cx = begin_cols_x
        cw = begin_col_wires
        ce = end_col_corners

        while cx < self.tr_corner_x_y[0] - end_buffer:

            cols_start_x_list.append(cx)
            cols_wire_start_list.append(cw)
            cols_end_x_list.append(ce)
            cols_start_placing_unary_nums.append(cplaceux - i)
            cx += cols_size
            cw += cols_size
            ce += cols_size

            print("i: ", i, "cplaceux: ", cplaceux, "ce: ", ce)

            cplaceux += cols_size
            i += 1


        return cols_start_x_list, cols_wire_start_list, cols_end_x_list, cols_start_placing_unary_nums

    def calculateRowLocations(self):
        row_locations_dict = {}
        mc_size = self.calculateMacroCellSize()
        mc_top_size_with_border = 2
        begin_rows_y = self.tl_corner_x_y[1] - 1
        begin_rows_wires = begin_rows_y - mc_top_size_with_border - 1
        begin_rows_out_wires = begin_rows_wires - 3
        begin_row_end = begin_rows_out_wires - 2

        rows_start_y_list = []
        rows_wires_y_list = []
        row_out_wire_y_list = []
        row_end_y_list = []
        rs = begin_rows_y
        rw = begin_rows_wires
        rw_out = begin_rows_out_wires
        re = begin_row_end
        i = 0
        while rs > self.bl_corner_x_y[1]:
            row_locations_dict[i] = {"start_y": rs, "in_wire_y": rw, "out_wire_y": rw_out, "end_y": re}
            rows_start_y_list.append(rs)
            rows_wires_y_list.append(rw)
            row_out_wire_y_list.append(rw_out)
            row_end_y_list.append(re)


            rs -= mc_size["borderedMacroCellHeight"]
            rw -= mc_size["borderedMacroCellHeight"]
            rw_out -= mc_size["borderedMacroCellHeight"]
            re -= mc_size["borderedMacroCellHeight"]
            i += 1

        return row_locations_dict

    def calcIntersections(self):
        intersections_dict = {}
        cols_start_x_list = self.calculateColumnsLocations()[0]
        row_locations_dict = self.calculateRowLocations()
        row_col_intersections_dict = {}
        start_intersections = []
        wires_cols_start_intersections = []
        col_counter = 0
        row_counter = 0

        for e, i in enumerate(cols_start_x_list):
            for k, v in row_locations_dict.items():
                intersections_dict[(k, e)] = {}
                intersections_dict[(k, e)]["start_xy"] = (i, v["start_y"])
                intersections_dict[(k, e)]["in_wire_xy"] = (i, v["in_wire_y"])
                intersections_dict[(k, e)]["out_wire_xy"] = (i, v["out_wire_y"])
                intersections_dict[(k, e)]["end_xy"] = (i, v["end_y"])
                start_intersections.append((i, v["start_y"]))
                wires_cols_start_intersections.append((i, v["in_wire_y"]))
                row_col_intersections_dict[(k, e)] = (i, v["in_wire_y"])


        return start_intersections, wires_cols_start_intersections, row_col_intersections_dict
    def calculateMacroCellSize(self):
        unaryNumLen = len(self.input_system.returnStates())
        writeRowSize = unaryNumLen + 2  # 2 for the left and right write brackets
        unBorderedMacroCellWidth = writeRowSize + 2 # 2 for the doors
        borderedMacroCellWidth = unBorderedMacroCellWidth + 1 # 2 for the border
        borderedMacroCellWidthTrapDoor = borderedMacroCellWidth + 1 # 1 for the trap door and the column wire
        borderedMacroCellWidthWithTDAndWirePadding = borderedMacroCellWidthTrapDoor + 2 # 2 for the padding on each side
        rowsNorthOfInWire = 1
        rowsBetweenInAndOutWire = 3
        rowsSouthOfOutWire = 2

        # wire & doors, data action row north,

        unborderedMacrocellHeight = int(rowsNorthOfInWire) + int(rowsBetweenInAndOutWire) + rowsSouthOfOutWire + 2  # 1 for the wire
        borderedMacroCellHeight = unborderedMacrocellHeight + 2 # 2 for the border
        mc_size = {"unborderedMacroCellWidth": unBorderedMacroCellWidth, "borderedMacroCellWidth": borderedMacroCellWidth,
                   "borderedMacroCellWidthTrapDoor": borderedMacroCellWidthTrapDoor,
                   "borderedMacroCellWidthWithTDAndWirePadding": borderedMacroCellWidthWithTDAndWirePadding,
                   "borderedMacroCellHeight": borderedMacroCellHeight, "unborderedMacrocellHeight": unborderedMacrocellHeight,
                   "writeRowSize": writeRowSize, "unaryNumLen": unaryNumLen, "rowsNorthOfInWire": rowsNorthOfInWire,
                   "rowsBetweenInAndOutWire": rowsBetweenInAndOutWire, "rowsSouthOfOutWire": rowsSouthOfOutWire}

        return mc_size

    def makeAffTrDict(self):
        aff_tr_di = {"VerticalAffinities": self.input_system.returnVerticalAffinityDict(),
                     "HorizontalAffinities": self.input_system.returnHorizontalAffinityDict(),
                     "VerticalTransitions": self.input_system.returnVerticalTransitionDict(),
                     "HorizontalTransitions": self.input_system.returnHorizontalTransitionDict()}
        print(aff_tr_di)
        return aff_tr_di

    def makeMacroCell_Table(self, row_st, col_st, dir, mc_size):

        row = row_st
        col = col_st
        col_num = self.input_states_to_rows_cols_map[col.label]["col"]
        row_num = self.input_states_to_rows_cols_map[row.label]["rows"][dir]
        print(" Dir:", dir, " Row_num", row_num, " Row St:", row_st.label,
              " Column num:", col_num, " Column St:", col_st.label)
        transition_col_lookup = None
        tr_col_change_num = 0

        if dir == "N":
            aff = self.aff_tr_dict["VerticalAffinities"].get((row.label, col.label), None)
            tr = self.aff_tr_dict["VerticalTransitions"].get((row.label, col.label), None)
            if tr is not None:
                transition_col_lookup = tr[1]
                pair_label = (row.label, col.label)


        elif dir == "S":
            aff = self.aff_tr_dict["VerticalAffinities"].get((col.label, row.label), None)
            tr = self.aff_tr_dict["VerticalTransitions"].get((col.label, row.label), None)
            if tr is not None:
                transition_col_lookup = tr[0]
                pair_label = (col.label, row.label)


        elif dir == "E" :
            aff = self.aff_tr_dict["HorizontalAffinities"].get((col.label, row.label), None)
            tr=self.aff_tr_dict["HorizontalTransitions"].get((col.label, row.label), None)

            if tr is not None:
                transition_col_lookup = tr[0]
                pair_label = (col.label, row.label)

        elif dir == "W":
            aff=self.aff_tr_dict["HorizontalAffinities"].get((row.label, col.label), None)
            tr=self.aff_tr_dict["HorizontalTransitions"].get((row.label, col.label), None)

            if tr is not None:
                transition_col_lookup = tr[1]
                pair_label = (row.label, col.label)

        if transition_col_lookup is not None:
            tr_col_num = self.input_states_to_rows_cols_map[transition_col_lookup]["col"]
            if tr_col_num  == col_num:
                tr_col_change_num = 0
            elif tr_col_num > col_num:
                tr_col_change_num = tr_col_num - col_num
            elif tr_col_num < col_num:
                tr_col_change_num = -1 * (col_num - tr_col_num)

            #print("Transition pair:", pair_label, "Transition:", tr, "Transition col lookup:", transition_col_lookup, "tr_col_change_num:", tr_col_change_num)


        mc = MacroCell(row_st, col_st, dir, aff, tr, mc_size)

        row_wire_col = self.macro_row_col_intersection_dict[(row_num, col_num)]


        mc_tiles = mc.makeMacroCell_MC(row_wire_col[0], row_wire_col[1], tr_col_change_num)
        #mc.makeTiles(row_wire_col[0], row_wire_col[1])

        return mc, mc_tiles

    def makeMacroCells_Table(self):
        mc_size = self.calculateMacroCellSize()
        mcs = {}
        mc_tiles = []
        for i in self.input_system_states:
            for dir in ["N", "E", "W", "S" ]:
                for j in self.input_system_states:
                    mc, mc_t = self.makeMacroCell_Table(i, j, dir, mc_size)
                    mcs[(i.label, j.label, dir)] = mc
                    mc_tiles += mc_t
        return mcs, mc_tiles

    def sortColMC(self, col_state, mcs, rows_mapping=None, order=(dir, ["N", "E", "W", "S"])):

        col_mcs = []
        col_coords = {}
        if rows_mapping is None:
            rows_mapping = self.rows_to_input_states_dirs_map
        #self.rows_to_input_states_dirs_map [r] = (st, dir)
        # mcs[(i.label, j.label, dir)] = mc
        for i in range(len(rows_mapping)):
            row_state, row_dir = rows_mapping[i]
            mc = mcs[(row_state.label, col_state.label, row_dir)]
            col_mcs.append(mc)

    def makeMCAssembly(self):

        pass

    def makeMCAssemblies(self):
        pass
    def makeLeftEdge(self):
        left_x = self.tl_corner_x_y[0]
        dirs_order = ["E", "N", "W", "S"]

        row_locations_dict = self.calculateRowLocations()
        row_loc_items = row_locations_dict.items()
        row_start_top_y = [i[1]["start_y"] for i in row_loc_items]
        row_wire_y = [i[1]["in_wire_y"] for i in row_loc_items]
        row_out_wire_y_list = [i[1]["out_wire_y"] for i in row_loc_items]
        row_end_y = [i[1]["end_y"] for i in row_loc_items]

        left_edge_tiles = []
        row_counter = 0
        for y in range(self.tl_corner_x_y[1] - 1, self.bl_corner_x_y[1], -1):
            if y in row_start_top_y:
                left_edge_tiles.append(Tile(rowMarkerStartTop, left_x, y))
                rn = row_counter
                #rdst = dirs_order[]

            elif y in row_wire_y:

                left_edge_tiles.append(Tile(signal_door_inactive_east, left_x, y))
                left_edge_tiles.append(Tile(signal_door_handle_inactive, left_x, y + 1))
                left_edge_tiles.append(Tile(signal_transmitter_inactive, left_x, y + 2))
                left_edge_tiles.append(Tile(signal_receiver_inactive, left_x, y - 1))
                left_edge_tiles.append(Tile(signal_transmitter_inactive, left_x, y - 2))

                left_edge_tiles.append(Tile(eastWire, left_x + 1, y))
                left_edge_tiles.append(Tile(eastWire, left_x + 2, y))
                left_edge_tiles.append(Tile(eastWire, left_x - 1, y))
                left_edge_tiles.append(Tile(eastWire, left_x - 2, y))
            elif y in row_out_wire_y_list:
                left_edge_tiles.append(Tile(signal_door_inactive_west, left_x, y))
                left_edge_tiles.append(Tile(signal_door_handle_inactive, left_x, y - 1))


                left_edge_tiles.append(Tile(westWire, left_x + 1, y))
                left_edge_tiles.append(Tile(westWire, left_x + 2, y))
                left_edge_tiles.append(Tile(westWire, left_x - 1, y))
                left_edge_tiles.append(Tile(westWire, left_x - 2, y))

        return left_edge_tiles


    #### Pepe ####
    def makeRowLabels(self):
        """_summary_: This function creates the row labels and returns a list of tiles.
        Each row label is the start state, unary label, end state and the direction of the neighboring tile (E/N/W/S) then a border tile
        before the door to the table in that order.

        The states from (iu_states.py) to be used are ds_1_inactive, N/S/E/W, start_state_inactive, end_state_inactive, border.

        The row labels are placed on the left side of the table (west) right above the output wire.

        This should return a list of tiles. Test by calling this function in makeTable like the other there (at the bottom
        before the return statement)
        """
        pass

    def makeOutline(self):

        col_start_x, col_wire_x, col_end_x, col_unary_label_start_x = self.calculateColumnsLocations()
        outline_tiles = [Tile(northWestCorner, self.tl_corner_x_y[0], self.tl_corner_x_y[1]),
                         Tile(southWestCorner, self.bl_corner_x_y[0], self.bl_corner_x_y[1]),
                         Tile(northEastCorner, self.tr_corner_x_y[0], self.tr_corner_x_y[1]),
                         Tile(southEastCorner, self.br_corner_x_y[0], self.br_corner_x_y[1])
                         ]
        i = 0
        j = col_unary_label_start_x[0]
        cex = col_end_x[0]
        for x in range(self.tl_corner_x_y[0] + 1, self.tr_corner_x_y[0]):
            if x in col_start_x:

                outline_tiles.append(
                    Tile(columnMarkerTopStart, x, self.tl_corner_x_y[1]))

            elif x in col_end_x:

                print("col_num: ", i,"col_end_x", x)
                outline_tiles.append(
                    Tile(columnMarkerTopEnd, x, self.tl_corner_x_y[1]))
                i += 1


            elif x + 1 in col_end_x:
                outline_tiles.append(Tile(end_state, x, self.tl_corner_x_y[1]))


            elif x in col_unary_label_start_x:
                print("col_num: ", i,"col_unary_label_start_x", x)
                outline_tiles.append(Tile(ds_1_inactive, x, self.tl_corner_x_y[1]))

            elif i < len(col_end_x):
                if x > col_unary_label_start_x[i] and x < col_end_x[i] - 1:
                    outline_tiles.append(Tile(ds_1_inactive, x, self.tl_corner_x_y[1]))
                else:
                    outline_tiles.append(Tile(border_state, x, self.tl_corner_x_y[1]))


            else:
                outline_tiles.append(Tile(border_state, x, self.tl_corner_x_y[1]))


        for y in range(self.tl_corner_x_y[1] - 1, self.bl_corner_x_y[1], -1):
            outline_tiles.append(Tile(border_state, self.tr_corner_x_y[0], y))
        outline_tiles = outline_tiles + self.makeLeftEdge()
        return outline_tiles

    def makeTable(self):
        t_assem = Assembly()
        t_assem.setTiles(self.makeOutline())
        t_assem.setTiles(self.macrocell_tiles)
        t_assem.setTiles(self.makeLeftEdge())
        return t_assem, t_assem.returnTiles()


class IU_System:
    def __init__(self, name="Example", input_sys=exampleSystem):
        self.name = name
        self.input_system = input_sys
        self.table = Table(self.input_system)
        self.states = [northEastCorner, northWestCorner, southEastCorner, southWestCorner, border_state]
        self.seed_states = [northEastCorner, northWestCorner, southEastCorner, southWestCorner, border_state]
        self.initial_states =[]
        self.supertile_outline = None

        self.vaffinities = []
        self.haffinities = []
        self.vtransitions = []
        self.htransitions = []
        self.seed_assembly = self.makeSuperTileOutline()

    def makeEdgeDoors(self):
        """_summary_: This function creates the supertile edge doors and returns a list of tiles.
        Each edge door has an in and out edge door tile, a handle, maybe some signal passing between them and
        a store selected supertile state under construction. You can make an additional function to make a single edge door then call
        it repeatedly with whatever parameters you need to make the edge doors.

        This should return a list of tiles. Test by calling this function in makeTable like the other there (at the bottom
        before the return statement)
        """

        pass
    def makeSuperTileOutline(self):
        """_summary_: This function creates the super tile outline based on the size of the table, the number of states and
        how big the wires must be. This should also call the make edge doors function.
        Returns a list of tiles.
        """
        super_tile_outline = Assembly()
        table_outline = self.table.calculateTableSize()
        return super_tile_outline

    ######## Asher ########
    def calculateWires(self):
        """_summary_: This function calculates the in and out wire locations and returns a list of tiles.
        Each wire must run from the edge of the table to the edge of the super tile outline. The wires must
        be placed so when the supertiles are next to one another the wires will connect.
        If I were you I would start by making a dictionary[(state.label, direction)] = {"in_wire_edge": (x,y, WD),
                                                                                        "out_wire_edge": (x,y, WD),
                                                                                        in_wire_table_edge": (x,y, WD),
                                                                                        out_wire_table_edge": (x,y, WD),
                                                                                        "in_wire_corner_1": (x,y, WD),
                                                                                        ect...}


        """


    def makeWires(self):
        """_summary_: This function takes the output of calculateWires and returns a list of tiles. The states you need are
        in iu_states.py. northWire, southWire, eastWire, westWire, northEastWire, northWestWire, southEastWire, southWestWire

        """

        pass


    def returnIUsystem(self):
        table_seed_assembly, table_seed_tiles = self.table.makeTable()
        # table_seed_assembly.setTiles(self.makeWires())
        self.seed_assembly.setTiles(table_seed_tiles)
        iuSys = System(1, self.states, [], self.seed_states, self.vaffinities, self.haffinities,
                       self.vtransitions, self.htransitions, [], [], table_seed_assembly)
        return iuSys


if __name__ == "__main__":
    Table(exampleSystem)
    #iu_sys = IU_System(exampleSystem)


# class Table:
#     def __init__(self, inputSystem, start_x=0, start_y=0):
#         self.input_system = inputSystem
#         self.input_states_to_cols_dict, self.cols_to_input_states_dict = self.map_input_states_to_cols()
#         self.input_states_dirs_to_rows_dict, self.rows_to_input_states_dirs_dict = self.map_input_states_to_rows()
#         self.num_input_states = len(self.input_system.returnStates())
#         self.start_x = start_x
#         self.start_y = start_y
#         self.row_size = 5
#         self.column_size = len(self.input_system.returnStates()) + 2 + 2

#         self.coords = {}
#         self.num_rows = self.num_input_states * 4
#         self.num_cols = self.num_input_states
#         self.width = (self.column_size * self.num_cols) + 2
#         self.height = (self.row_size * self.num_rows)
#         self.rows = self.createRows()
#         self.columns = self.createColumns()

#         self.end_x = start_x + self.width
#         self.end_y = start_y - self.height
#         self.outline = self.createOutline(self.start_x, self.start_y, self.end_x, self.end_y)
#         self.TableAssembly, self.table_tiles = self.createTable()

#     def createTable(self):
#         outlineTiles = self.outline.returnTiles()
#         r = self.rows
#         c = self.columns
#         row_tiles = []
#         col_tiles = []
#         m = []
#         m_tiles = []


#         mc_wire_y_rows_list = []
#         mc_cols_x_start_end_pairs_list = []

#         for i in r:
#             mc_wire_y_rows_list.append(i.wire_y)
#             row_tiles = row_tiles + i.returnTiles()
#         for i in c:
#             xs = i.start_x
#             xe = i.end_x
#             mc_cols_x_start_end_pairs_list.append((xs, xe))
#             col_tiles = col_tiles + i.returnColTiles()

#         for i in range(len(mc_wire_y_rows_list)):
#             for j in range(len(mc_cols_x_start_end_pairs_list)):
#                 macrocell = MacroCell(mc_cols_x_start_end_pairs_list[j][0], mc_cols_x_start_end_pairs_list[j]
#                                [1], mc_wire_y_rows_list[i], j, i, self.num_input_states + 2)
#                 m.append(macrocell)
#                 m_tiles = m_tiles + macrocell.returnSeedTiles()

#         self.macrocells = m
#         #self.columns = self.create_columns()
#         tableAssem = Assembly()
#         table_tiles = outlineTiles + row_tiles + col_tiles
#         tableAssem.setTiles(outlineTiles)
#         tableAssem.setTiles(row_tiles)
#         tableAssem.setTiles(col_tiles)
#         tableAssem.setTiles(m_tiles)
#         return tableAssem, table_tiles

#     def returnSeedAssemblyTableTiles(self):
#         return self.TableAssembly, self.table_tiles


#     def createOutline(self,n_x, n_y, e_x, e_y):
#         tiles = []
#         end_x = e_x
#         end_y = e_y - 1
#         start_x = n_x
#         start_y = n_y
#         outline = Assembly()
#         tiles.append(Tile(northWestCorner, start_x, start_y))
#         tiles.append(Tile(northEastCorner, end_x, start_y))
#         tiles.append(Tile(southWestCorner, start_x, end_y))
#         tiles.append(Tile(southEastCorner, end_x, end_y))

#         for i in range(start_x + 1, end_x):
#             tiles.append(Tile(border_state, i, start_y))
#             tiles.append(Tile(border_state, i, end_y))

#         for i in range(start_y -1, end_y, -1):
#             tiles.append(Tile(border_state, end_x, i))

#         outline.setTiles(tiles)
#         return outline

#     def createRows(self):
#         r = []
#         s = self.input_system.returnStates()
#         row_num = 0
#         x = self.start_x
#         y = self.start_y - 1
#         for i in s:
#             for j in ["n", "s", "e", "w"]:
#                 r.append(Row(i, j, x, y, self.width))
#                 row_num += 1
#                 y -= 5
#         return r
#     def createColumns(self):
#         cols = []
#         x = self.start_x + 1
#         y = self.start_y
#         input_sys_states = self.input_system.returnStates()


#         for i in range(len(input_sys_states)):

#             print("X is: ", x)
#             cols.append(Column(input_sys_states[i], x, y, self.row_size, self.input_system, self.input_states_to_cols_dict, column_height=self.height))
#             x = x + self.column_size

#         return cols

#     def createMacroCells(self):
#         pass


#     def map_input_states_to_cols(self):
#         col_num = 0
#         input_states_to_cols = {}
#         cols_to_input_states = {}
#         for state in self.input_system.states:
#             input_states_to_cols[state.label] = col_num
#             cols_to_input_states[col_num] = state
#             col_num += 1
#         return input_states_to_cols, cols_to_input_states

#     def map_input_states_to_rows(self):
#         row_num = 0
#         input_states_dirs_to_rows = {}
#         rows_to_input_states_dirs = {}
#         len_to_south = len(self.input_system.states)*3
#         len_to_west = len(self.input_system.states) # Because row counter will already have iterated though the east states
#         whole_table_len = len(self.input_system.states)*4

#         for state in self.input_system.states.reverse():
#             input_states_dirs_to_rows[(state.label, "e")] = row_num
#             rows_to_input_states_dirs[row_num] = (state.label, "e")
#             input_states_dirs_to_rows[(state.label, "s")] = row_num + len_to_south
#             rows_to_input_states_dirs[row_num + len_to_south] = (state.label, "s")
#             row_num += 1


#         for state in self.input_system.states:
#             input_states_dirs_to_rows[(state.label, "n")] = row_num
#             rows_to_input_states_dirs[row_num] = (state.label, "n")
#             input_states_dirs_to_rows[(state.label, "w")] = row_num + len_to_west
#             rows_to_input_states_dirs[row_num + len_to_west] = (state.label, "w")
#             row_num += 1

#         return input_states_dirs_to_rows, rows_to_input_states_dirs

# class MacroCell:
#     def __init__(self, col_start_x, col_end_x, row_wire_y, column_num, row_num, cell_len=6, transition_num=None, column_state_sim=None, row_state_sim=None, dir=None):
#         # Starts at the neg door and ends at the pos door
#         self.mc_start_x = col_start_x
#         self.mc_start_y = row_wire_y + 1
#         self.mc_end_x = col_end_x - 2
#         self.mc_end_y = row_wire_y - 2
#         self.mc_door_y = row_wire_y
#         self.row_wire_y = row_wire_y
#         self.column_state = column_num
#         self.row_state = row_num
#         self.simulated_column_state = column_state_sim
#         self.simulated_row_state = row_state_sim
#         self.dir = dir
#         self.transition_num = transition_num

#         self.cell_len = cell_len

#         self.mc_states = [punch_down_ds_neg_active, punch_down_ds_active, punch_down_ds_neg_inactive,
#                           punch_down_ds_inactive, punch_down_ds_neg_end_found, punch_down_ds_end_found]
#         self.mc_seed_states = [punch_down_ds_neg_active, punch_down_ds_active, eastWire, mc_door_east_negative_inactive,
#                                mc_door_east_positive_inactive, mc_door_handle_east_negative_inactive, mc_door_handle_east_positive_inactive, trap_door_inactive]
#         self.mc_seed_assembly, self.mc_seed_tiles = self.makeSeedAssembly()

#         # self.mc_horizontal_affinities, self.mc_horizontal_transitions, self.mc_vertical_affinities, self.mc_vertical_transitions = self.makeHorizontalAffinitiesTransitions()
#     #def __init__(self, col_start_x, col_end_x, row_wire_y, column_num, row_num, cell_len=6, transition_num=None, column_state_sim=None, row_state_sim=None, dir=None):

#     def makeSeedAssembly(self):
#         mc_tiles = []

#         mc_tiles.append(Tile(punch_down_ds_neg_active, self.mc_start_x + 1, self.mc_door_y + 1))
#         mc_tiles.append(Tile(punch_down_ds_active, self.mc_end_x - 2, self.mc_door_y + 1))
#         mc_tiles.append(Tile(mc_door_east_negative_inactive, self.mc_start_x, self.mc_door_y))
#         mc_tiles.append(Tile(mc_door_handle_east_negative_inactive, self.mc_start_x, self.mc_door_y + 1))
#         mc_tiles.append(Tile(mc_door_east_positive_inactive, self.mc_end_x - 1, self.mc_door_y))
#         mc_tiles.append(Tile(mc_door_handle_east_positive_inactive, self.mc_end_x - 1, self.mc_door_y + 1))
#         mc_tiles.append(Tile(trap_door_inactive, self.mc_end_x, self.mc_door_y - 1))
#         mc_tiles.append(Tile(signal_end_checks_inactive, self.mc_start_x, self.mc_door_y - 1))
#         mc_tiles.append(Tile(signal_start_checks_inactive, self.mc_end_x - 1, self.mc_door_y - 1))
#         for i in (range(self.mc_start_x, self.mc_end_x)):
#             mc_tiles.append(Tile(signal_conditional_inactive, i, self.mc_door_y - 2))


#         seed_assembly = Assembly()
#         seed_assembly.setTiles(mc_tiles)

#         return seed_assembly, mc_tiles

#     def returnSeedTiles(self):
#         return self.mc_seed_tiles

    # def makeHorizontalAffinitiesTransitions(self):
    #     wire_aff_v, wire_tr_v = []
    #     wire_aff_h, wire_tr_h = wireAffinities(self)
    #     for i in wire_aff_h:
    #         if i.dir == "v":
    #             wire_aff_v.append(i)
    #             wire_aff_h.remove(i)
    #     for i in wire_tr_h:
    #         if i.dir == "v":
    #             wire_tr_v.append(i)
    #             wire_tr_h.remove(i)

    #     return wire_aff_h, wire_tr_h, wire_aff_v, wire_tr_v
