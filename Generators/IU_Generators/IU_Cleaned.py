from cProfile import label
from tracemalloc import start
from Generators.IU_Generators.binaryStates import *
from UniversalClasses import State, TransitionRule, AffinityRule, System, Tile, Assembly
from Assets.colors import *
from Generators.IU_Generators.binaryStates import *
import sys
import Generators.IU_Generators.WireFunctions as wf
import Generators.IU_Generators.ShapeGenerationFunctions as sf

exSt = [State("A", active_color), State(
    "B", inactive_color), State("C", wire_color)]
xISt = [State("A", active_color), State(
    "B", inactive_color), State("C", wire_color)]
xSSt = [State("A", active_color)]
vaff = [AffinityRule("A", "B", "v", 1), AffinityRule(
    "C", "A", "v", 1), AffinityRule("C", "B", "v", 1)]
hAff = [AffinityRule("B", "B", "h", 1), AffinityRule(
    "C", "C", "h", 1), AffinityRule("A", "C", "h", 1)]
vtr = [TransitionRule("A", "B", "A", "A", "v"),
       TransitionRule("B", "C", "A", "C", "v")]
htr = [TransitionRule("C", "C", "B", "A", "h"),
       TransitionRule("A", "C", "B", "C", "h")]
exampleSystem = System(1, exSt, xISt, xSSt, vaff, hAff, vtr, htr)  # seed assm)

class AttachmentPoint(AffinityRule):

    def __init__(self, gadget1, tile1, gadget2, tile2, dir, strength=None):
        """
        gadget 1 is the gadget that is being attached to gadget 2
        the tiles are the tiles being attached the other
        tiles must be in a state that is compatible with the attachment
        dir is the direction of the attachment to gadget 2
        if gadget 1 is being attached to the north of gadget 2 then dir = 'N'
        The combined assembly will have the x and y coordinates of gadget 2
        Tile 2 must use local gadget coordinates rather than global coordinates
        """
        self.gadget1 = gadget1
        self.tile1 = tile1

        self.gadget2 = gadget2
        self.tile2 = tile2

        self.dir = dir # direction of g1s attachment to g2 at xy point (N, S, E, W)
        if dir == 'N':
            label1 = gadget1.label_id
            label2 = gadget2.label_id
            aff_dir = 'v'
        elif dir == 'S':
            label1 = gadget2.label_id
            label2 = gadget1.label_id
            aff_dir = 'v'
        elif dir == 'E':
            label1 = gadget1.label_id
            label2 = gadget2.label_id
            aff_dir = 'h'
        else:
            label1 = gadget2.label_id
            label2 = gadget1.label_id
            aff_dir = 'h'

        super().__init__(label1, label2, aff_dir, strength)


class SuperState(State):
    # unary_state_num=0, row_dir_nums_dict={"N": int, "S": int, "E": int, "W": int}
    def __init__(self, input_state, state_num):
        self.input_state = input_state
        self.state_num = state_num
        self.unary_state_num = ''
        for i in range(state_num):
            self.unary_state_num += str(1)

        self.unary_state_string = '[' + self.unary_state_num + ']'
        self.information_dictionary = { "Column": {"TopLeftCoords": None,
                                                   "TopRightCoords": None,
                                                   "BottomLeftCoords": None,
                                                   "BottomRightCoords": None},
                                        "Rows": {"North": {"TopLeftCoords": None,
                                                           "TopRightCoords": None,
                                                           "BottomLeftCoords": None,
                                                           "BottomRightCoords": None},
                                                 "South": {"TopLeftCoords": None,
                                                           "TopRightCoords": None,
                                                           "BottomLeftCoords": None,
                                                           "BottomRightCoords": None},
                                                 "East": {"TopLeftCoords": None,
                                                          "TopRightCoords": None,
                                                          "BottomLeftCoords": None,
                                                          "BottomRightCoords": None},
                                                 "West": {"TopLeftCoords": None,
                                                          "TopRightCoords": None,
                                                          "BottomLeftCoords": None,
                                                          "BottomRightCoords": None}, },
                                       "EdgeDoors": {"North": {"WireBorder": {"East": None,
                                                                              "West": None,
                                                                              "InternalBorder": None},
                                                               "InWire": None,
                                                               "InDoor": None,
                                                               "OutWire": None,
                                                               "OutDoor": None,},
                                                     "South": {"WireBorder": {"East": None,
                                                                              "West": None,
                                                                              "InternalBorder": None},
                                                               "InWire": None,
                                                               "InDoor": None,
                                                               "OutWire": None,
                                                               "OutDoor": None, },
                                                     "East": {"WireBorder": {"North": None,
                                                                             "South": None,
                                                                             "InternalBorder": None},
                                                              "InWire": None,
                                                              "InDoor": None,
                                                              "OutWire": None,
                                                              "OutDoor": None, },
                                                     "West": {"WireBorder": {"North": None,
                                                                             "South": None,
                                                                             "InternalBorder": None},
                                                              "InWire": None,
                                                              "InDoor": None,
                                                              "OutWire": None,
                                                              "OutDoor": None}, },

            }
    def __str__(self):
        return '{}_{}_superstate'.format(self.input_state.label, self.state_num)


    # def __repr__(self, include_python_variable_name=False):
    #     if include_python_variable_name:
    #         f'{self.input_state.label}_{self.unary_state_num}_superstate = SuperState({self.input_state.label}, {self.unary_state_num})'
    #     return SuperState(self.input_state, self.unary_state_num)


class Gadget(Assembly):
    """_summary_

    Args:
        Assembly (_type_): _description_
    """

    def __init__(self, id=-1, label=' ', gadget_type='abstract gadget', relative_coords={}, seedStates=[]):
        super().__init__()
        self.label_id = label + '_' + str(id)
        self.gadget_type = gadget_type
        self.id = id
        self.relative_coords = relative_coords # relative coordinates of the tiles/states in the gadget
        self.seedStates = seedStates

    def update_gadget_location(self, local_x, local_y, global_x, global_y):
        pass

    def appendSeedAssembly(self, assem):
        pass

    def appendToSeedAssembly(self, tile, x, y):
        pass
    @property
    def seed_tiles(self):
        pass

    @property
    def vertical_transitions(self):
        pass

    @property
    def horizontal_transitions(self):
        pass

    @property
    def vertical_affinities(self):
        pass

    @property
    def horizontal_affinities(self):
        pass

    @property
    def gadget_id(self):
        pass




    # @property
    # def attachment_points(self):

    #     return self._attachment_points

    # @attachment_points.setter()
    # def attachment_points(self, att_points_list):
    #     pass

    # def append_attachment_point(self, local_x, local_y, global_x, global_y, direction):
    #     pass

class CompoundGadget(Gadget):
    def __init__(self, label, id=-1, seed_gadget=None, child_gadgets=[], attachment_points=[], padding = {'top':0, 'bottom':0, 'left':0, 'right':0}):
        super().__init__(self, label=label)
        self.label_id = label + '_' + str(id)
        self.seed_gadget = seed_gadget
        self.child_gadgets = child_gadgets
        self.attachment_points = attachment_points
        self.padding_top = padding['top']
        self.padding_bottom = padding['bottom']
        self.padding_left = padding['left']
        self.padding_right = padding['right']
    def collectTiles(self):
        t = []
        t += self.seed_gadget.returnTiles()

        print("collected seed tiles")
        for c in self.child_gadgets:
            t += c.returnTiles()
        print("collected child tiles")
        print(t)
        return t





class Door(Gadget):
    def __init__(self, id=-1, label=' ', door_type='standard', door_open_direction='E', door_handle_type='standard', door_handle_direction='N', x=0, y=0):
        self.door_open_direction = door_open_direction
        self.door_handle_direction = door_handle_direction
        self.door_type = door_type
        self.door_handle_type = door_handle_type

        if door_type == 'standard':
            self.tiles = self.makeDoor()
        super().__init__(id=id, label=label, gadget_type='door', relative_coords=[(x, y)], seedStates=self.tiles)
    def makeDoor(self, door_type='standard', door_handle_type='standard'):
        t = []
        if door_type == 'standard':
            if self.door_open_direction == 'N':
                self.tiles.append(Tile(signal_door_north_inactive, self.x, self.y))
                t.append(Tile(signal_door_north_inactive, self.x, self.y))
                self.relative_coords.append((self.x, self.y))
            elif self.door_open_direction == 'E':
                self.tiles.append(Tile(signal_door_inactive, self.x, self.y))
                t.append(Tile(signal_door_inactive, self.x, self.y))
        return t




class TableEntranceDoor(Door):
    def __init__(self, super_state, incoming_dir, x=0, y=1):
        self.label = 'table_entrance_door'
        self.door_handle_type = 'table_entrance'
        self.door_handle_direction = 'N'
        self.door_open_direction = 'E'

        self.super_state = super_state
        self.incoming_dir = incoming_dir

        self.wire_attachment_points = [(x+1, y, "E"), (x-3, y, "W")]
        self.signal_control_attachment_points = [(x, y+2, "N"), (x, y-1, "S")]
        self.start_x = x
        self.start_y = y
        self.tiles = self.makeTiles()
        super().__init__(self, label=self.label, door_type='table_door', door_open_direction=self.door_open_direction, door_handle_type=self.door_handle_type, door_handle_direction=self.door_handle_direction, x=x, y=y)

        self.relative_coords = self.coords
    def makeDoor(self):
        print("making door")
        return self.makeTiles()
    def makeTiles(self):
        x = self.start_x
        y = self.start_y
        tiles = [Tile(signal_door_east_inactive, x, y),
                 Tile(signal_door_handle_east_inactive, x, y+1),
                 Tile(punch_down_ds_inactive, x-1, y+1),
                 Tile(inactiveEastWire, x-1, y),
                 Tile(endcap_door_handle_east_inactive, x-2, y+1),
                 Tile(endcap_door_east_inactive, x-2, y),
                 ]
        return tiles

    def returnHeight(self):
        return 3

class DisplayRow(Gadget):
    def __init__(self, super_state_unary_string, max_state_unary_len=1, row_type = 'display', start_x=0, start_y=0):
        self.row_type = row_type
        self.display_string = super_state_unary_string

        self.max_state_unary_len = max_state_unary_len + 1
        self.start_x = start_x
        self.start_y = start_y
        l = 'state_display_row_' + self.display_string
        #super.__init__(self, label='l', id=0, gadget_type='state_display_row')
        super().__init__(self)
        self.tiles = self.makeRow()
        self.relative_coords = self.coords

    def makeRow(self):
        t = []
        x = self.start_x
        if self.row_type == 'display':
            t.append(Tile(start_data_string, x, self.start_y))
            print(self.max_state_unary_len)

            for j in range(self.max_state_unary_len - len(self.display_string)):
                x = x + 1
                t.append(Tile(blank_state, x + j, self.start_y))

            # if len(self.display_string) == 2:
            #     t.append(Tile(blank_state, x + 2, self.start_y))




            for i in self.display_string:
                print(self.display_string)
                print(i)
                if i == "1":
                    t.append(Tile(ds_1_inactive_mc, x, self.start_y))
                    x = x + 1
                elif i == "]":
                    t.append(Tile(end_data_string, x, self.start_y))
                    x = x + 1


        self.setTiles(t)
        return t



class Wire(Gadget):
    def __init__(self, id=-1, label=' ', wire_type='standard', x=0, y=0):
        # We have the need to make the wire extend from the edge of the table to the edge of the tile
        pass


class SuperStateWire(CompoundGadget):
    def __init__(self, label, id, super_state, seed_gadget=None, other_gadgets=[], attachment_points=[]):
        super().__init__(label, id, seed_gadget, other_gadgets, attachment_points)
    pass
class MacroCell(CompoundGadget):
    """The Super States of the intersection of a row and a column with the direction the row is
        coming from and the column of the current superblocks state

    Args:
        CompoundGadget (_type_): _description_
        super_state (SuperState): _description_
    """
    def __init__(self, col_super_state, row_super_state, row_dir):
        super().__init__()
        self.col_super_state = col_super_state
        self.row_super_state = row_super_state
        self.row_dir = row_dir
        self.affinity = None
        self.transition = None



class Column(CompoundGadget):
    # seed_gadget=None, other_gadgets=[], attachment_points=[]
    # , top_left_x_y, macrocell_dimensions, row_dimensions): label, id,
    def __init__(self, super_state, max_state_len, label='col', id=-1, width=5, height=5):
        #self.top_left_x = top_left_x_y[0]
        #self.top_left_y = top_left_x_y[1]
        #self.macrocell_dimensions = macrocell_dimensions
        #self.row_dimensions = row_dimensions
        self.super_state = super_state
        self.max_state_len = max_state_len
        self.width = width
        self.seed_gadget = DisplayRow(super_state.unary_state_string, max_state_len, row_type='display')
        self.child_gadgets = []
        self.attachment_points = []
        super().__init__(label, id, self.seed_gadget, self.child_gadgets)
        self.tiles = self.makeColumnTiles()
        self.relative_coords = self.coords



    def makeColumnTiles(self):
        t = []
        trw = self.makeTopRow()
        print(trw)
        t.append(trw)
        self.setTiles(t)
        return t

    def makeTopRow(self):
        print("Making top row")

        sdt = self.seed_gadget.returnTiles()
        tp = Assembly()
        tp.setTiles(sdt)
        tp_borders = tp.returnBorders()
        print("seed borders: " + str(tp_borders))
        west_corner_x = tp_borders[0] - self.padding_left - 1
        east_corner_x = tp_borders[1] + self.padding_right + 1
        top_corner_y = tp_borders[2] + self.padding_top
        print("west corner x: " + str(west_corner_x))
        print("east corner x: " + str(east_corner_x))


        print("Seed display tiles: ")
        for i in sdt:
            print(i.state.label)


        top_row = [Tile(columnStartMarkerTop, west_corner_x, top_corner_y), Tile(columnEndMarkerTop, east_corner_x, top_corner_y)]
        tp.setTiles(top_row)
        for i in range(self.padding_left):
            x = west_corner_x + i
            if tp.coords.get([(x, top_corner_y)], None) is None:
                top_row.append(Tile(border_state, x, top_corner_y))
            else:
                "Overlapping tiles at x: " + str(x) + " y: " + str(top_corner_y) + " in top row"
        tp.setTiles(top_row)


        for i in range(self.padding_right):
            x = east_corner_x - i
            if tp.coords.get([(x, top_corner_y)], None) is None:
                top_row.append(Tile(border_state, x, top_corner_y))
        tp.setTiles(top_row)

        return tp.returnTiles()

class Row(CompoundGadget):
    def __init__(self, super_state, incoming_dir, x=0, y=-3, label='row', id=-1):
        #super().__init__(label, id, seed_gadget, child_gadgets, attachment_points, padding)
        self.seed_gadget = TableEntranceDoor(super_state, incoming_dir, x, y)
        self.tiles = self.makeRowTiles()
        self.incoming_dir = incoming_dir
        self.x = x
        self.y = y
        self.super_state = super_state

    def makeRowTiles(self):

        t = self.seed_gadget.returnTiles()
        self.setTiles(t)
        return t

    def returnTiles(self):
        a = Assembly()
        sg = TableEntranceDoor(
            self.super_state, self.incoming_dir, self.x, self.y)
        t = sg.returnTiles()
        a.setTiles(sg.returnTiles())
        self.tiles = self.makeRowTiles()
        a = self.makeRowDoor()
        return t
    def makeRowDoor(self):
        a = Assembly()
        sg = TableEntranceDoor(self.super_state, self.incoming_dir, self.x, self.y)
        a.setTiles(sg.returnTiles())
        return a

class Table(CompoundGadget):
    def __init__(self, label="table", id=1, super_states=None, input_system=None):
        self.super_states = super_states
        self.input_system = input_system
        self.padding_left = 2
        self.padding_right = 2
        self.padding_between_cols = 2
        self.padding_top = 1
        self.padding_bottom = 1
        self.padding_between_rows = 1
        self.max_unary_state_len = len(self.input_system.returnStates())
        self.columns = self.defineColumns()
        self.rows = self.makeRows()
        seed_gadget = Assembly()
        self.macrocell_height = 9
        self.row_height = TableEntranceDoor(self.super_states[0], 'N', 0, -3).returnHeight()
        self.row_height = self.row_height + (self.macrocell_height - self.row_height)

        self.width = len(self.input_system.states) * (self.max_unary_state_len + 4) + (len(self.input_system.states) -1) * \
            self.padding_between_cols + self.padding_left + self.padding_right + 2
        self.height = len(self.input_system.states) * 4 * self.row_height + (len(self.input_system.states) - 1) * \
            self.padding_between_rows + self.padding_top + self.padding_bottom + 2


        super().__init__(label, id, seed_gadget, [self.columns, self.rows])

    def makeColumns(self):
        print("Making columns")
        return self.defineColumns()
    def defineColumns(self):

        cols = []
        i = 0
        for s in self.super_states:
            l = str(s.__str__)
            l += "_col"
            cols.append(Column(s, self.max_unary_state_len, label=l, id=i))
            i += 1
        print("Columns Defined")
        return cols

    def makeRows(self):
        print("Making rows")
        rows = self.defineRows()
        t = []
        for row in rows:
            t1 = row.returnTiles()
            t = t + t1

        return t

    def defineRows(self):
        rows = []
        i = 0


        x = 0
        y = -3
        for d in ['N', 'E', 'S', 'W']:
            for s in self.super_states:
                l = str(s.__str__)
                l += "_row"
                rows.append(Row(s, d, x, y, label=l, id=i))
                i += 1
                y = y - self.h - self.padding_between_rows
        print("Rows Defined")
        return rows

    def runCalculations(self):
        print("Running calculations")
        width = 0
        self.columns = self.makeColumns()
        self.rows = self.makeRows()

    def calculateTableWidth(self):
        width = -1

        print("Calculating width")
        return self.width
    def returnAssembly(self):
        print("Returning assembly")
        tiles = self.columns[0].returnTiles()[0]
        # r = self.rows.returnTiles()
        # print("Row tiles: ")
        # for i in r:
        #     print(i.state.label)
        # tiles = tiles + r


        a = Assembly()
        a.setTiles(tiles)

        return a





class MacroBlock(CompoundGadget):
    pass

class IU_System(System):
    full_tileset_unit_states = {}
    full_tileset_unit_initial_states = {}
    full_tileset_unit_seed_states = {}
    full_tileset_vertical_affinities_dict = {}
    full_tileset_horizontal_affinities_dict = {}
    full_tileset_vertical_transitions_dict = {}
    full_tileset_horizontal_transitions_dict = {}

    # def __new__(cls, *args, **kwargs):
    #     return super().__new__(cls, *args, **kwargs)

    def __init__(self, input_system=exampleSystem):
        self.input_system = input_system
        self.temp = input_system.temp
        self.states, self.initial_states, self.seed_states = self.collectStates(), self.collectStates(), self.collectStates()
        self.vertical_transitions_dict = {}
        self.horizontal_transitions_dict = {}
        self.vertical_affinities_dict = {}
        self.horizontal_affinities_dict = {}
        self.super_states = [SuperState(j, i) for i, j in enumerate(input_system.states)]
        self.table = Table(super_states=self.super_states, input_system=input_system)
        self.seed_assembly = Assembly()
        self.seed_assembly.setTiles(self.table.returnTiles())
        self.seed_assembly.setTiles(self.seed_assembly.returnBorders())
        # super().__init__(self.temp, self.states, self.initial_states, self.seed_states, self.vertical_transitions_dict, self.horizontal_transitions_dict, self.vertical_affinities_dict, self.horizontal_affinities_dict, self.seed_assembly)

    def collectStates(self):
        st = [border_state, signal_door_east_inactive, signal_door_handle_east_inactive, punch_down_ds_inactive,
              ds_1_inactive_mc, start_state_pair, end_state_pair, inactiveEastWire, endcap_door_handle_east_inactive,
              endcap_door_east_inactive, eastWire, westWire, northWire, southWire, northWestCorner, northEastCorner,
              southEastCorner, southWestCorner, columnStartMarkerTop, columnEndMarkerTop, row_border, rowStartMarker,
              tile_edge_center_handle_east_inactive, tile_east_edge_door_in_wire_active,
              tile_east_edge_door_out_wire_active, tile_east_edge_door_out_wire_inactive ]
        return st

    def makeAllTileWires(self, start_wx=0, start_wy=0, end_wx=None, end_wy=None,
                         out_start_wx=None, out_start_wy=None, out_end_wx=None, out_end_wy=None, y_offset=5):
        tiles = []
        max_len = self.table.max_unary_state_len + 2


        in_start_wire_coords = (start_wx, start_wy)
        #in_start_wire_y = start_wy
        if end_wx == None:
            end_wx = start_wx + max_len
        if end_wy == None:
            end_wy = start_wy
        if out_start_wx == None:
            out_start_wx = start_wx
        if out_start_wy == None:
            out_start_wy = start_wy - y_offset
        in_end_wire_coords = (end_wx, end_wy)
        #in_end_wire_y = end_wy
        out_start_wire_coords = (out_start_wx, out_start_wy)
        out_end_wire_coords = (out_end_wx, out_end_wy)

        direction_label_offset = 2
        direction_label_coords = (start_wx, start_wy - direction_label_offset)

        state_label_x_offset = 2
        state_label_initial_x = direction_label_coords[0] - state_label_x_offset

        in_wire_start_x = start_wx
        in_wire_start_y = start_wy
        out_wire_start_x = out_start_wx
        out_wire_start_y = out_start_wy
        in_wire_end_x = end_wx
        in_wire_end_y = end_wy
        out_wire_end_x = out_end_wx
        out_wire_end_y = out_end_wy

        direction_label_x = start_wx + 1
        direction_label_y = start_wy - direction_label_offset
        state_label_x = state_label_initial_x
        state_label_y = start_wy - direction_label_offset

        for d in ['N', 'E', 'W', 'S']:

            for s in self.super_states:
                if d == 'N' or d == 'S':
                    pass
                elif d == 'E' or d == 'W':

                    tiles = tiles + wf.makeTableInOutWire((in_wire_end_x, in_wire_end_y), (in_wire_start_x, in_wire_start_y),
                                                      (out_wire_end_x, out_wire_end_y), (out_wire_start_x, out_wire_end_y), d,
                                                      (state_label_x,  s.unary_state_string ,
                                                      self.temp))

    def makeBlockOutline(self, height, width, starting_from="center", starting_coords=(0, 0)):
        # t = [Tile(northWestCorner, ne_x, ne_y), Tile(northEastCorner, ne_x + width, ne_y),
        #      Tile(southEastCorner, ne_x, ne_y - height), Tile(southEastCorner, ne_x + width, ne_y - height)]
        # a = Assembly()
        # y = ne_y - 1
        # x = ne_x
        # for i in range(y, y - height, -1):
        #     if i == -1:
        #         t.append(Tile(border_state, x, y))
        #         t.append(Tile(border_state, x + width, y))
        #     t.append(Tile(border_state, x, i))
        #     t.append(Tile(border_state, x + width, i))

        # for i in range(x + 1, x + width):

        #     t.append(Tile(border_state, i, y + 1))
        #     t.append(Tile(border_state, i, y - height + 1))

        # a.setTiles(t)
        # genSys = System(self.temp, self.states, self.initial_states, self.seed_states,
        #                 self.vertical_transitions_dict, self.horizontal_transitions_dict,
        #                 self.vertical_affinities_dict, self.horizontal_affinities_dict,
        #                 seed_assembly=a)
        if starting_from == "center":
            center = starting_coords
            tl = (starting_coords[0] - width//2, starting_coords[1] + height//2)
            br = (starting_coords[0] + width//2, starting_coords[1] - height//2)
        elif starting_from == "top_left":
            center = (starting_coords[0] + width//2, starting_coords[1] - height//2)
            tl = starting_coords
            br = (starting_coords[0] + width, starting_coords[1] - height)
        elif starting_from == "top_right":
            center = (starting_coords[0] - width//2, starting_coords[1] - height//2)
            tl = (starting_coords[0] - width, starting_coords[1])
            br = starting_coords
        elif starting_from == "bottom_left":
            center = (starting_coords[0] + width//2, starting_coords[1] + height//2)
            tl = (starting_coords[0], starting_coords[1] + height)
            br = (starting_coords[0] + width, starting_coords[1])
        else:
            center = (starting_coords[0] - width//2, starting_coords[1] + height//2)
            tl = (starting_coords[0] - width, starting_coords[1] + height)
            br = starting_coords

        a = sf.makeRectangleOutline(tl, br)

        return a

    def addOuterBlockWireDoors(self, assembly, number_of_states, table_order):

        pass


    def returnWireSystem(self):
        tiles = []


    def returnSystem(self):

        # table_assm = self.table.returnAssembly()
        # width = self.table.width + (len(self.input_system.states) * 6 * 2) + 2
        # height = -(self.table.height + (len(self.input_system.states) * 6 * 2) + 4)
        # start_block_y = -self.table.height
        # start_block_x = ((len(self.input_system.states) * 6) + 4) - 1
        # num_states = len(self.input_system.states)

        # outline_assm = self.makeBlockOutline(
        #     height, width, len(self.input_system.states), start_block_x, start_block_y)

        # col_assem = Assembly()

        # outline_assm.setTiles(table_assm.returnTiles())
        # col_assem.setTiles(self.table.columns[1].tiles[0])
        a = self.makeBlockOutline(20, 20)

        gen_sys = System(self.temp, self.states, self.initial_states, self.seed_states, self.vertical_transitions_dict,
                         self.horizontal_transitions_dict, self.vertical_affinities_dict, self.horizontal_affinities_dict,
                         seed_assembly=a)

        return gen_sys


    def write_all_to_file(self, filename="iu_system_all_states_aff_tr.txt", open_type='x'):
        self.write_all_states_to_file_in_list(filename, open_type)
        self.write_all_initial_states_to_file_in_list(filename, open_type)
        self.write_all_seed_states_to_file_in_list(filename, open_type)

    def write_all_states_to_file_in_list(self, file_name="iu_system_all_states.txt", open_type='x'):

        with open(file_name, open_type) as file:
            file.write('\# States \n \n')
            file.write(f'{state.label}_state = State({state.label}, {state.color}, {state.display_label}) \n'
             for state in self.initial_states)

            file.write(f'states = [')
            for state in self.states:
                var_name = f'{state.label}_state,\n'
                file.write(var_name)
            file.write(f'] \n')

    def write_all_initial_states_to_file_in_list(self, file_name="iu_system_all_initial_states.txt", open_type='x'):
        with open(file_name, open_type) as file:
            file.write('\# Initial States \n \n')
            file.write(f'initial_states = [')
            for state in self.initial_states:
                var_name = f'{state.label}_state, \n'
                file.write(var_name)
            file.write(f'] \n')


    def write_all_seed_states_to_file_in_list(self, file_name="iu_system_all_seed_states.txt", open_type='x'):
        with open(file_name, open_type) as file:
            file.write('\# Seed States \n \n')
            file.write(f'seed_states = [')
            for state in self.seed_states:
                var_name = f'{state.label}_state, \n'
                file.write(var_name)
            file.write(f'] \n')

    def write_all_horizontal_affinities_to_file_in_list(self, file_name="iu_system_all_horizontal_affinities.txt", open_type='x'):
        with open(file_name, open_type) as file:
            file.write('\# Horizontal Affinities \n \n')
            file.write(f'horizontal_affinities = [')
            for aff in self.horizontal_affinities_dict:
                var_name = f'{aff.state1.label}_{aff.state2.label}_h_aff = AffinityRule(\'{aff.label1}\', \'{aff.label2}\', \'h\' {aff.strength}), \n'
                file.write(var_name)
            file.write(f'] \n')

    def write_all_vertical_affinities_to_file_in_list(self, file_name="iu_system_all_vertical_affinities.txt", open_type='x'):
        with open(file_name, open_type) as file:
            file.write('\# Vertical Affinities \n \n')
            file.write(f'vertical_affinities = [')
            for aff in self.vertical_affinities_dict:
                var_name = f'{aff.label1}_{aff.label2}_v_aff = AffinityRule(\'{aff.label1}\', \'{aff.label2}\', \'v\', {aff.strength}) \n'
                file.write(var_name)
            file.write(f'] \n')

    def write_all_horizontal_transitions_to_file_in_list(self, file_name="iu_system_all_horizontal_transitions.txt", open_type='x'):
        with open(file_name, open_type) as file:
            file.write('\# Horizontal Transitions \n \n')
            file.write(f'horizontal_transitions = [')
            for tr in self.horizontal_transitions_dict:
                var_name = f'{tr.label1}_{tr.label2}_h_tr = TransitionRule(\'{tr.label1}\', \'{tr.label2}\', \'{tr.label1Final}\', \'{tr.label2Final}\',\'h\') \n'
                file.write(var_name)
            file.write(f'] \n')

    def write_all_vertical_transitions_to_file_in_list(self, file_name="iu_system_all_vertical_tr.txt", open_type='x'):
        with open(file_name, open_type) as file:
            file.write('\# Horizontal Transitions \n \n')
            file.write(f'vertical_transitions = [')
            for tr in self.horizontal_transitions_dict:
                var_name = f'{tr.label1}_{tr.label2}_h_tr = TransitionRule(\'{tr.label1}\', \'{tr.label2}\', \'{tr.label1Final}\', \'{tr.label2Final}\',\'v\') \n'
                file.write(var_name)
            file.write(f'] \n')

if __name__ == '__main__':
    iu_system = IU_System(exampleSystem)
    print("success")
    st = iu_system.super_states
    for s in st: print(s)
