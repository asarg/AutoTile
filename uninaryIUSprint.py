# Hack Research Plan
from cProfile import label
from UniversalClasses import State, Tile, Assembly, AffinityRule, TransitionRule, System
from Generators.IU_Generators.binaryStates import eastWire, end_data_string, ds_1, northCorner, southCorner, start_state_pair, border_state, start_data_string, end_state_pair, activeStateColumnNorthEdge, activeStateColumnSouthEdge

from Generators.IU_Generators.binaryStates import signal_door_handle_inactive, signal_door_handle_active_waiting, signal_door_handle_inactive_waiting, signal_door_handle_reset, signal_door_handle_accept, signal_door_handle_intermediate_accept, signal_door_handle_pass_accept_north, signal_door_handle_pass_accept_south, signal_door_handle_find_corner_north, signal_door_handle_find_corner_south, signal_door_handle_pass_find_corner_north, signal_door_handle_pass_find_corner_south, signal_door_handle_accept_north, signal_door_handle_accept_south

from Generators.IU_Generators.binaryStates import signal_door_inactive_east, signal_door_find_corner_south, signal_door_find_corner_north, signal_door_pass_find_corner_south, signal_door_pass_find_corner_north, signal_door_active_waiting_east, signal_door_intermediate_accept, signal_door_propped_open,  signal_door_east_reset_walk, signal_door_east_reset, signal_door_pass_accept_north, signal_door_pass_accept_south, signal_door_east_stop, signal_door_open, signal_door_east_reset_walk_border

from Generators.IU_Generators.binaryStates import signal_transmitter_inactive, signal_transmitter_pass_find_corner_north, signal_transmitter_pass_find_corner_south, signal_transmitter_pass_accept_north, signal_transmitter_pass_accept_south

from Generators.IU_Generators.binaryStates import signal_receiver_inactive, signal_receiver_pass_find_corner_north, signal_receiver_pass_find_corner_south, signal_receiver_pass_accept_north, signal_receiver_pass_accept_south

from Generators.IU_Generators.binaryStates import neg_ds_1, neg_ds_1_inactive_mc, ds_1_inactive_mc, punch_down_ds_neg_active, punch_down_ds_active, punch_down_ds_inactive, punch_down_ds_neg_inactive, punch_down_ds_end_found, punch_down_ds_neg_end_found, mc_door_east_negative_inactive, mc_door_east_negative_active,  mc_door_east_positive_inactive, mc_door_east_positive_active, mc_door_trigger_transition, mc_door_handle_east_negative_inactive, mc_door_current_state_active, mc_door_current_state_inactive, mc_door_handle_current_state_active, mc_door_handle_trigger_transition, mc_door_handle_east_positive_inactive

states_list = [eastWire, end_data_string, ds_1, southCorner, northCorner, start_state_pair, border_state, end_state_pair, start_data_string,

               signal_door_handle_inactive, signal_door_handle_active_waiting, signal_door_handle_inactive_waiting, signal_door_handle_reset, signal_door_handle_accept, signal_door_handle_intermediate_accept, signal_door_handle_pass_accept_north, signal_door_handle_pass_accept_south, signal_door_handle_find_corner_north, signal_door_handle_find_corner_south, signal_door_handle_pass_find_corner_north, signal_door_handle_pass_find_corner_south, signal_door_handle_accept_north, signal_door_handle_accept_south,

               signal_door_find_corner_south, signal_door_find_corner_north, signal_door_propped_open, signal_door_intermediate_accept, signal_door_inactive_east, signal_door_pass_find_corner_south, signal_door_pass_find_corner_north, signal_door_pass_accept_north, signal_door_pass_accept_south, signal_door_east_reset_walk, signal_door_east_reset, signal_door_active_waiting_east, signal_door_east_stop, signal_door_open, signal_door_east_reset_walk_border,

               signal_transmitter_inactive, signal_transmitter_pass_find_corner_north, signal_transmitter_pass_find_corner_south, signal_transmitter_pass_accept_south, signal_transmitter_pass_accept_north,

               signal_receiver_inactive, signal_receiver_pass_find_corner_south, signal_receiver_pass_accept_north, signal_receiver_pass_accept_south, signal_receiver_pass_find_corner_north,

               neg_ds_1, neg_ds_1_inactive_mc, ds_1_inactive_mc, punch_down_ds_neg_active, punch_down_ds_active, punch_down_ds_inactive, punch_down_ds_neg_inactive, punch_down_ds_end_found, punch_down_ds_neg_end_found,

               mc_door_east_negative_inactive, mc_door_east_negative_active, mc_door_east_positive_inactive, mc_door_east_positive_active, mc_door_trigger_transition, mc_door_handle_trigger_transition, mc_door_handle_east_negative_inactive, mc_door_current_state_active, mc_door_current_state_inactive, mc_door_handle_current_state_active,  mc_door_handle_east_positive_inactive
               ]


def wireAffinities(self, wire_states=None, gsys=None):
    wire_affs = []
    wire_tr = []
    wire_aff_states = [signal_door_propped_open, signal_door_intermediate_accept, signal_door_inactive_east, signal_receiver_inactive, start_state_pair, ds_1, signal_door_east_stop, signal_door_east_reset_walk, signal_door_east_reset, signal_door_active_waiting_east, signal_door_pass_accept_north, signal_door_pass_accept_south, signal_door_pass_find_corner_north, signal_door_open, mc_door_east_negative_inactive, mc_door_east_negative_active, mc_door_east_positive_active, mc_door_east_positive_inactive]

    wire_tr_states = [ds_1, start_state_pair]

    wire_aff_v_states = [punch_down_ds_active, punch_down_ds_inactive, punch_down_ds_end_found, punch_down_ds_neg_active, punch_down_ds_neg_inactive, punch_down_ds_neg_end_found]

    for i in wire_aff_states:
        wire_affs.append(AffinityRule(eastWire.label, i.label, "h", 1))
        wire_affs.append(AffinityRule(i.label, eastWire.label, "h", 1))

        if i in wire_tr_states:
            wire_tr.append(TransitionRule(i.label, eastWire.label, eastWire.label, i.label, "h"))

    for i in wire_aff_v_states:
        wire_affs.append(AffinityRule(i.label, eastWire.label, "v", 1))

    return wire_affs, wire_tr

def add_example_tiles(start_x, start_y, end_x, end_y, state_list):
    example_tiles = []
    curr_x = start_x
    curr_y = start_y
    state_list_len = len(state_list)
    curr_index = 0

    for i in range(start_x, end_x):
        for j in range(start_y, end_y):
            if curr_index >= state_list_len - 1:
                print("Error: Not enough states to fill")
                return example_tiles
            example_tiles.append(Tile(curr_x, curr_y, state_list[curr_index]))
            curr_y += 1
            curr_index += 1

        curr_x += 1
        curr_y = start_y

    return example_tiles

def make_example_tiles():
    extra_wire_example_tiles = []
    for i in range(1, 4):
            extra_wire_example_tiles.append(Tile(eastWire, -i, 4))
            extra_wire_example_tiles.append(Tile(signal_door_east_reset_walk_border, -i, 3))

    extra_wire_example_tiles.append(Tile(eastWire, 1, 4))
    extra_wire_example_tiles.append(Tile(end_state_pair, -4, 4))
    extra_wire_example_tiles.append(Tile(ds_1, -4, 4))
    extra_wire_example_tiles.append(Tile(ds_1, -5, 4))
    extra_wire_example_tiles.append(Tile(start_state_pair, -6, 4))

    return extra_wire_example_tiles

class Gadget:
    def __init__(self, gadget_name=None):
        self.name = gadget_name
        self.seed_assembly = Assembly()
        self.seed_assembly_tiles = []
        # Local x, y coordinates of the tiles within the gadget
        pass


class MacroCell:
    def __init__(self, x, y, column_num, row_num, cell_len=6, transition_num=None, column_state_sim=None, row_state_sim=None, dir=None):
        # Starts at the neg door and ends at the pos door
        self.wire_start_x = x
        self.wire_start_y = y
        self.column_state = column_num
        self.row_state = row_num
        self.simulated_column_state = column_state_sim
        self.simulated_row_state = row_state_sim
        self.dir = dir
        self.transition_num = transition_num
        self.cell_len = cell_len

        self.mc_states = [punch_down_ds_neg_active, punch_down_ds_active, punch_down_ds_neg_inactive,
                          punch_down_ds_inactive, punch_down_ds_neg_end_found, punch_down_ds_end_found]
        self.mc_seed_states = [punch_down_ds_neg_active, punch_down_ds_active, eastWire, mc_door_east_negative_inactive,
                               mc_door_east_positive_inactive, mc_door_handle_east_negative_inactive, mc_door_handle_east_positive_inactive]
        self.mc_seed_assembly, self.mc_seed_tiles = self.makeSeedAssembly()

        self.mc_horizontal_affinities, self.mc_horizontal_transitions, self.mc_vertical_affinities, self.mc_vertical_transitions = self.makeHorizontalAffinitiesTransitions()

    def makeSeedAssembly(self):
        mc_tiles = []
        for i in range(self.cell_len - 1):
            #wire
            mc_tiles.append(
                Tile(eastWire, self.wire_start_x + i, self.wire_start_y))

        mc_tiles.append(Tile(punch_down_ds_neg_active,
                        self.wire_start_x + 1, self.wire_start_y + 1))
        mc_tiles.append(Tile(punch_down_ds_active, self.wire_start_x +
                        self.cell_len - 2, self.wire_start_y + 1))
        mc_tiles.append(Tile(mc_door_east_negative_inactive,
                        self.wire_start_x - 1, self.wire_start_y))
        mc_tiles.append(Tile(mc_door_handle_east_negative_inactive,
                        self.wire_start_x - 1, self.wire_start_y + 1))
        mc_tiles.append(Tile(mc_door_east_positive_inactive,
                        self.wire_start_x + self.cell_len, self.wire_start_y))
        mc_tiles.append(Tile(mc_door_handle_east_positive_inactive,
                        self.wire_start_x + self.cell_len, self.wire_start_y + 1))

        seed_assembly = Assembly()
        seed_assembly.setTiles(mc_tiles)

        return seed_assembly, mc_tiles

    def makeHorizontalAffinitiesTransitions(self):
        wire_aff_v, wire_tr_v = []
        wire_aff_h, wire_tr_h = wireAffinities(self)
        for i in wire_aff_h:
            if i.dir == "v":
                wire_aff_v.append(i)
                wire_aff_h.remove(i)
        for i in wire_tr_h:
            if i.dir == "v":
                wire_tr_v.append(i)
                wire_tr_h.remove(i)

        return wire_aff_h, wire_tr_h, wire_aff_v, wire_tr_v



# 1. Make a table class
class TableGadget:
    def __init__(self, num_doors):
        self.states = states_list
        self.tiles = []
        self.num_rows = 0
        self.num_cols = 0
        self.door_x_y_coors = []
        self.num_doors = num_doors



    def makeDoorAffinitiesTransitions(self):
        v_end = "v", 1
        h_end = "h", 1

        door_states = [northCorner, southCorner, signal_door_handle_inactive, signal_door_handle_active_waiting, signal_door_handle_inactive_waiting, signal_door_handle_reset, signal_door_handle_accept, signal_door_handle_intermediate_accept, signal_door_find_corner_north, signal_door_find_corner_south, signal_door_handle_find_corner_north, signal_door_handle_find_corner_south, signal_door_propped_open, signal_door_intermediate_accept, signal_door_inactive_east, signal_door_pass_accept_north, signal_door_pass_accept_south, signal_door_active_waiting_east, signal_transmitter_inactive, signal_receiver_inactive, start_state_pair, ds_1]

        h_affinity_rules = [AffinityRule(ds_1.label, signal_door_inactive_east.label, "h", 1),
                            AffinityRule(ds_1.label, signal_door_find_corner_north.label, "h", 1),
                            AffinityRule(ds_1.label, signal_door_find_corner_south.label, "h", 1),
                            AffinityRule(ds_1.label, signal_door_active_waiting_east.label, "h", 1),
                            AffinityRule(ds_1.label, signal_door_intermediate_accept.label, "h", 1),
                            AffinityRule(ds_1.label, signal_door_propped_open.label, "h", 1)
        ]

        v_affinity_rules = [AffinityRule(signal_door_handle_inactive.label, signal_door_inactive_east.label, "v", 1),
                            AffinityRule(signal_door_handle_inactive.label, signal_door_find_corner_north.label, "v", 1),
                            AffinityRule(signal_door_handle_inactive.label, signal_door_pass_find_corner_north.label, "v", 1),
                            AffinityRule(signal_door_handle_find_corner_north.label, signal_door_find_corner_north.label, "v", 1),
                            AffinityRule(signal_door_handle_find_corner_south.label, signal_door_find_corner_south.label, "v", 1),
                            AffinityRule(signal_door_handle_pass_find_corner_north.label, signal_door_pass_find_corner_north.label, "v", 1),


                            AffinityRule(signal_transmitter_inactive.label, signal_door_handle_find_corner_north.label, "v", 1),
                            AffinityRule(signal_transmitter_pass_find_corner_north.label, signal_door_handle_find_corner_north.label, "v", 1),
                            AffinityRule(signal_transmitter_pass_find_corner_north.label, signal_door_handle_pass_find_corner_north.label, "v", 1),
                            AffinityRule(signal_receiver_inactive.label, signal_transmitter_pass_find_corner_north.label, "v", 1),
                            AffinityRule(signal_receiver_pass_find_corner_north.label, signal_transmitter_pass_find_corner_north.label, "v", 1),
                            AffinityRule(signal_door_inactive_east.label, signal_receiver_pass_find_corner_north.label, "v", 1),
                            AffinityRule(signal_door_pass_find_corner_north.label, signal_receiver_pass_find_corner_north.label, "v", 1),
                            AffinityRule(border_state.label,signal_door_east_reset.label, "v", 1),
                            AffinityRule(signal_door_east_reset_walk.label, border_state.label, "v", 1),
                            AffinityRule(ds_1.label, signal_door_open.label, "v", 1),
                            AffinityRule(signal_door_open.label, ds_1.label, "v", 1),
                            AffinityRule(signal_transmitter_pass_find_corner_south.label, signal_door_handle_pass_find_corner_south.label, "v", 1),

                            ]

        horizontal_transition_rules = [TransitionRule(ds_1.label, signal_door_inactive_east.label, ds_1.label, signal_door_find_corner_north.label,"h"),
                                       TransitionRule(
                                           ds_1.label, signal_door_open.label, signal_door_open.label, ds_1.label, "h"),
                                       TransitionRule(start_state_pair.label, signal_door_open.label,
                                                      signal_door_east_stop.label, start_state_pair.label, "h"),
                                       TransitionRule(signal_door_east_stop.label, eastWire.label, eastWire.label, signal_door_east_reset.label, "h"),
                                       TransitionRule(signal_door_east_reset_walk.label, eastWire.label,
                                                      eastWire.label, signal_door_east_reset.label, "h"),
            ]

        vertical_transition_rules = [
            TransitionRule(signal_door_handle_inactive.label, signal_door_find_corner_north.label,
                           signal_door_handle_find_corner_north.label, signal_door_find_corner_south.label, "v"),
            TransitionRule(signal_door_find_corner_south.label, signal_receiver_inactive.label,
                           signal_door_active_waiting_east.label, signal_receiver_pass_find_corner_south.label, "v"),
            TransitionRule(signal_receiver_pass_find_corner_south.label, signal_transmitter_inactive.label,
                           signal_receiver_pass_find_corner_south.label, signal_transmitter_pass_find_corner_south.label, "v"),
            TransitionRule(signal_transmitter_inactive.label, signal_door_handle_find_corner_north.label,
                           signal_transmitter_pass_find_corner_north.label, signal_door_handle_find_corner_north.label, "v"),
            TransitionRule(signal_receiver_inactive.label, signal_transmitter_pass_find_corner_north.label,
                           signal_receiver_pass_find_corner_north.label, signal_transmitter_pass_find_corner_north.label, "v"),
            TransitionRule(signal_door_inactive_east.label, signal_receiver_pass_find_corner_north.label,
                           signal_door_pass_find_corner_north.label, signal_receiver_pass_find_corner_north.label, "v"),
            TransitionRule(signal_door_handle_inactive.label, signal_door_pass_find_corner_north.label,
                           signal_door_handle_pass_find_corner_north.label, signal_door_pass_find_corner_north.label, "v"),
            TransitionRule(signal_transmitter_inactive.label, signal_door_handle_pass_find_corner_north.label, signal_transmitter_pass_find_corner_north.label, signal_door_handle_pass_find_corner_north.label, "v"),
            TransitionRule(signal_transmitter_pass_find_corner_south.label, signal_door_handle_inactive.label,
                           signal_transmitter_pass_find_corner_south.label, signal_door_handle_pass_find_corner_south.label, "v"),
            TransitionRule(signal_door_handle_pass_find_corner_south.label, signal_door_inactive_east.label,
                           signal_door_handle_pass_find_corner_south.label, signal_door_pass_find_corner_south.label, "v"),
            TransitionRule(signal_door_pass_find_corner_south.label, signal_receiver_inactive.label,
                           signal_door_pass_find_corner_south.label, signal_receiver_pass_find_corner_south.label, "v"),
                                     ]
        v_affinities_accept = [
            AffinityRule(northCorner.label, signal_transmitter_pass_find_corner_north.label, "v", 1),
            AffinityRule(northCorner.label,signal_transmitter_pass_accept_north.label, "v", 1),
            AffinityRule(signal_receiver_pass_find_corner_south.label, southCorner.label, "v", 1),
            AffinityRule(signal_receiver_pass_accept_south.label, southCorner.label, "v", 1),
            AffinityRule(signal_door_pass_find_corner_south.label, signal_receiver_pass_accept_south.label, "v", 1),
            AffinityRule(signal_door_pass_accept_south.label, signal_receiver_pass_accept_south.label, "v", 1),
            AffinityRule(signal_transmitter_pass_accept_north.label, signal_door_handle_pass_find_corner_north.label, "v", 1),
            AffinityRule(signal_transmitter_pass_accept_north.label, signal_door_handle_pass_accept_north.label, "v", 1),
            AffinityRule(signal_door_handle_pass_accept_north.label, signal_door_pass_find_corner_north.label, "v", 1),
            AffinityRule(signal_door_handle_pass_accept_north.label, signal_door_pass_accept_north.label, "v", 1),
            AffinityRule(signal_door_pass_accept_north.label, signal_receiver_pass_find_corner_north.label, "v", 1),
            AffinityRule(signal_door_pass_accept_north.label, signal_receiver_pass_accept_north.label, "v", 1),
            AffinityRule(signal_receiver_pass_accept_north.label, signal_transmitter_pass_find_corner_north.label, "v", 1),
            AffinityRule(signal_receiver_pass_accept_north.label, signal_transmitter_pass_accept_north.label, "v", 1),
            AffinityRule(signal_transmitter_pass_accept_north.label, signal_door_handle_find_corner_north.label, "v", 1),
            AffinityRule(signal_transmitter_pass_accept_north.label, signal_door_handle_pass_accept_north.label, "v", 1),
            AffinityRule(signal_door_handle_accept_north.label, signal_door_active_waiting_east.label, "v", 1),
            AffinityRule(signal_door_handle_accept_north.label, signal_door_intermediate_accept.label, "v", 1),
            ]

        v_transition_rules_accept = [
            TransitionRule(northCorner.label, signal_transmitter_pass_find_corner_north.label,
                               northCorner.label, signal_transmitter_pass_accept_north.label, "v"),
            TransitionRule(signal_transmitter_pass_accept_north.label, signal_door_handle_pass_find_corner_north.label,
                           signal_transmitter_pass_accept_north.label, signal_door_handle_pass_accept_north.label, "v"),
            TransitionRule(signal_door_handle_pass_accept_north.label, signal_door_pass_find_corner_north.label,
                           signal_door_handle_pass_accept_north.label, signal_door_pass_accept_north.label, "v"),
            TransitionRule(signal_door_pass_accept_north.label, signal_receiver_pass_find_corner_north.label,
                           signal_door_pass_accept_north.label, signal_receiver_pass_accept_north.label, "v"),
            TransitionRule(signal_receiver_pass_accept_north.label, signal_transmitter_pass_find_corner_north.label,
                           signal_receiver_pass_accept_north.label, signal_transmitter_pass_accept_north.label, "v"),
            TransitionRule(signal_transmitter_pass_accept_north.label, signal_door_handle_find_corner_north.label,
                           signal_transmitter_pass_accept_north.label, signal_door_handle_accept_north.label, "v"),
            TransitionRule(signal_door_handle_accept_north.label, signal_door_active_waiting_east.label,
                           signal_door_handle_accept_north.label, signal_door_intermediate_accept.label, "v"),

            TransitionRule(signal_receiver_pass_find_corner_south.label, southCorner.label,
                           signal_receiver_pass_accept_south.label, southCorner.label, "v"),
            TransitionRule(signal_door_pass_find_corner_south.label, signal_receiver_pass_accept_south.label,
                           signal_door_pass_accept_south.label, signal_receiver_pass_accept_south.label, "v"),
            TransitionRule(signal_door_handle_pass_find_corner_south.label, signal_door_pass_accept_south.label,
                           signal_door_handle_pass_accept_south.label, signal_door_pass_accept_south.label, "v"),
            TransitionRule(signal_transmitter_pass_find_corner_south.label, signal_door_handle_pass_accept_south.label,
                           signal_transmitter_pass_accept_south.label, signal_door_handle_pass_accept_south.label, "v"),
            TransitionRule(signal_receiver_pass_find_corner_south.label, signal_transmitter_pass_accept_south.label,
                           signal_receiver_pass_accept_south.label, signal_transmitter_pass_accept_south.label, "v"),

            TransitionRule(signal_door_intermediate_accept.label, signal_receiver_pass_accept_south.label,
                           signal_door_open.label, signal_receiver_pass_accept_south.label, "v"),

            TransitionRule(signal_door_east_reset.label, signal_door_east_reset_walk_border.label,
                           signal_door_east_reset_walk.label, signal_door_east_reset_walk_border.label, "v"),
            TransitionRule(signal_door_handle_accept_north.label, signal_door_east_reset.label,
                           signal_door_handle_accept_north.label, signal_door_propped_open.label, "v"),
            ]

        v_affinity_rules = v_affinity_rules + v_affinities_accept
        vertical_transition_rules = vertical_transition_rules + v_transition_rules_accept

        return h_affinity_rules, v_affinity_rules, horizontal_transition_rules, vertical_transition_rules

    def makeEastTableDoor(self, x, y):
        d = Tile(signal_door_inactive_east, x, y)
        h = Tile(signal_door_handle_inactive, x, y + 1)
        t = Tile(signal_transmitter_inactive, x, y + 2)
        r = Tile(signal_receiver_inactive, x, y - 1)
        w = Tile(eastWire, x + 1, y)
        w2 = Tile(eastWire, x - 1, y)
        door_tiles = [d, h, t, r, w, w2]
        return door_tiles


    def makeEastEdge(self, num_doors=None):
        if num_doors is None:
            num_doors = self.num_doors

        door_seed_states = [signal_door_inactive_east, signal_door_handle_inactive,
                            signal_transmitter_inactive, signal_receiver_inactive, eastWire, end_data_string, ds_1, northCorner, southCorner, start_state_pair]
        curr_x, curr_y = 0, 0
        door_tiles = []
        for i in range(num_doors):
            dt = self.makeEastTableDoor(curr_x, curr_y)
            self.door_x_y_coors.append((curr_x, curr_y))
            curr_y = curr_y + 4
            door_tiles = door_tiles + dt

        extra_wire_example_tiles = make_example_tiles()


        door_tiles = door_tiles + extra_wire_example_tiles

        door_assembly = Assembly()
        door_assembly.setTiles(door_tiles)
        north_border = door_assembly.upMost
        south_border = door_assembly.downMost
        north_corner_tile = Tile(northCorner, 0, north_border + 1)
        south_corner_tile = Tile(southCorner, 0, south_border - 1)


        corner_tiles = [north_corner_tile, south_corner_tile]
        door_assembly.setTiles(corner_tiles)
        wire_aff_h, wire_tr_h = wireAffinities(self)
        door_aff_h, door_aff_v, door_tr_h, door_tr_v = self.makeDoorAffinitiesTransitions()
        h_affs = wire_aff_h + door_aff_h
        h_trs = wire_tr_h + door_tr_h
        v_affs = door_aff_v
        v_trs = door_tr_v



        edge_sys = System(1, states_list, [], door_seed_states, v_affs, h_affs, v_trs, h_trs, [], [], door_assembly)

        return edge_sys

    def makeEdgeWireMacroCells(self, num_h_cells, wire_right_of_door_x_y_coords):
        mc_tiles = []
        macro_cells = []
        row_x_y_coords = wire_right_of_door_x_y_coords

        for i in range(num_h_cells):
            for j in row_x_y_coords:
                curr_x, curr_y = j[0] + 2, j[1]
                m = MacroCell(curr_x, curr_y, i, 0, 6)
                mc_tiles = mc_tiles + m.seed_tiles
                macro_cells.append(m)

            mr = m.mc_seed_assembly.rightMost
            row_x_y_coords = [(mr, i[1]) for i in row_x_y_coords]

        return macro_cells, mc_tiles

    def makeMacroCellSystem(self, num_h_cells, edge_sys):
        wire_right_of_door_x_y_coords = [(i[0] + 1, i[1]) for i in self.door_x_y_coors]
        macro_cells, mc_tiles = self.makeEdgeWireMacroCells(num_h_cells, wire_right_of_door_x_y_coords)
        edge_assem = edge_sys.returnSeedAssembly()
        edge_tiles = edge_assem.returnTiles()
        mc_tiles = mc_tiles + edge_tiles

        mc_assembly = Assembly()
        mc_assembly.setTiles(mc_tiles)
        mc_sys = System(1, states_list, [], [], [], [], [], [], [], [], mc_assembly)
        return macro_cells, mc_sys

class SuperBlock(Assembly):
    def __init__(self, table):
        self.simulated_state = None
        self.table = table
        self.macro_x = None
        self.macro_y = None
        self.activity_state = None

    # def constructNeighbor(self, neighbor_dir, neighbor_state):


class IU_System(System):
    iu_states = []
    iu_seed_states = []
    iu_construction_states = []
    iu_vertical_affinities = {}
    iu_horizontal_affinities = {}
    iu_vertical_transitions = {}
    iu_horizontal_transitions = {}

    def __init__(self, input_system=None):

        super().__init__(1, self.iu_states, [], [], [], [], [], [], [], [], None)
        self.input_system = input_system
        self.state_table_column_mapping = {}  # StateColumnMapping()
        self.state_dir_wire_mapping = {}  # StateDirWireMapping()
        self.table = None #Table()
        self.super_seed = None #SuperBlock(self.table)


    def makeIU(self):
        edge_sys = self.edge_sys.makeEastEdge()
        edge_assem = edge_sys.returnSeedAssembly()
        edge_tiles = edge_assem.returnTiles()
        mc_tiles = self.macro_cell_sys.returnSeedAssembly().returnTiles()
        iu_tiles = edge_tiles + mc_tiles
        iu_assembly = Assembly()
        iu_assembly.setTiles(iu_tiles)
        iu_sys = System(1, states_list, [], [], [], [], [], [], [], [], iu_assembly)
        return iu_sys

    def makeStateColumnMapping(self):
        pass
    """ def makeIUSeed(self):
        iu_sys = self.makeIU()
        iu_assem = iu_sys.returnSeedAssembly()
        iu_tiles = iu_assem.returnTiles()
        iu_seed = Seed(iu_tiles)
        return iu_seed

    def makeIUSeedState(self):
        iu_seed = self.makeIUSeed()
        iu_seed_state = SeedState(iu_seed, 0, 0, 0, 0)
        return iu_seed_state

    def makeIUSeedStateList(self):
        iu_seed_state = self.makeIUSeedState()
        iu_seed_state_list = [iu_seed_state]
        return iu_seed_state_list

    def makeIUState(self):
        iu_seed_state_list = self.makeIUSeedStateList()
        iu_state = State(iu_seed_state_list, 0, 0, 0, 0)
        return iu_state

    def makeIUStateList(self):
        iu_state = self.makeIUState()
        iu_state_list = [iu_state]
        return iu_state_list

    def makeIUStatePair(self):
        iu_state_list = self.makeIUStateList()
        iu_state_pair = StatePair(iu_state_list, 0, 0, 0, 0)
        return iu_state_pair

    def makeIUStatePairList(self):
        iu_state_pair = self.makeIUStatePair() """
## 1.1 Make the east edge of the table

### A) Write a table edge door function that takes in an x and y and returns an inactive door gadget with a len 1 wire on the east side
### and a len 3 wire on west side

### B) Add door handles to the door

### C) Add signal gap tiles and corners

### D) Get door to recognize a data string has arrived and wait for confirmation before opening

### E) Get door to open when signal is received

### F) Get door to close but wait for table completion after data passed through

### G) Stack 3 doors on top of each other and confirm pass waiting up and down

# 2. Make Macrocell Class
## 2.1 Make a macrocell that can be placed on the table

## 2.2. Make Active Table Column

## 2.3. Make Table Transition

## 2.4. Make Table Reset Doors

# 3. Make Table Communicate Acceptance/Rejection of State Change

## 3.1. Make Neighboring Block Finalize State Change

## 3.2. Make Table Transmit New State to Adjacent Super Blocks

# 4. Program Construction of Table

# 5. Program Construction of Seed

# 6. Program Construction of New Super Blocks

if __name__ == "__main__":
    #system = make_system()
    #SaveFile.main(system, ["uniaryWiresIUTest.xml"])
    table_gadget = TableGadget()
    door_gadget = table_gadget.makeEastEdge(1)
