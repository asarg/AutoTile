# Hack Research Plan
from UniversalClasses import State, Tile, Assembly, AffinityRule, TransitionRule, System
from Generators.IU_Generators.binaryStates import eastWire, end_data_string, ds_1, northCorner, southCorner, start_state_pair, border_state

from Generators.IU_Generators.binaryStates import signal_door_handle_inactive, signal_door_handle_active_waiting, signal_door_handle_inactive_waiting, signal_door_handle_reset, signal_door_handle_accept, signal_door_handle_intermediate_accept, signal_door_handle_pass_accept_north, signal_door_handle_pass_accept_south, signal_door_handle_find_corner_north, signal_door_handle_find_corner_south, signal_door_handle_pass_find_corner_north, signal_door_handle_pass_find_corner_south

from Generators.IU_Generators.binaryStates import signal_door_inactive_east, signal_door_find_corner_south, signal_door_find_corner_north, signal_door_pass_find_corner_south, signal_door_pass_find_corner_north, signal_door_active_waiting_east, signal_door_intermediate_accept, signal_door_propped_open,  signal_door_east_reset_walk, signal_door_east_reset, signal_door_pass_accept_north, signal_door_pass_accept_south, signal_door_east_stop

from Generators.IU_Generators.binaryStates import signal_transmitter_inactive, signal_transmitter_pass_find_corner_north, signal_transmitter_pass_find_corner_south, signal_transmitter_pass_accept_north, signal_transmitter_pass_accept_south

from Generators.IU_Generators.binaryStates import signal_receiver_inactive, signal_receiver_pass_find_corner_north, signal_receiver_pass_find_corner_south, signal_receiver_pass_accept_north, signal_receiver_pass_accept_south

states_list = [eastWire, end_data_string, ds_1, southCorner, northCorner, start_state_pair, border_state,

               signal_door_handle_inactive, signal_door_handle_active_waiting, signal_door_handle_inactive_waiting, signal_door_handle_reset, signal_door_handle_accept, signal_door_handle_intermediate_accept, signal_door_handle_pass_accept_north, signal_door_handle_pass_accept_south, signal_door_handle_find_corner_north, signal_door_handle_find_corner_south, signal_door_handle_pass_find_corner_north, signal_door_handle_pass_find_corner_south,

               signal_door_find_corner_south, signal_door_find_corner_north, signal_door_propped_open, signal_door_intermediate_accept, signal_door_inactive_east, signal_door_pass_find_corner_south, signal_door_pass_find_corner_north, signal_door_pass_accept_north, signal_door_pass_accept_south, signal_door_east_reset_walk, signal_door_east_reset, signal_door_active_waiting_east, signal_door_east_stop,

               signal_transmitter_inactive, signal_transmitter_pass_find_corner_north, signal_transmitter_pass_find_corner_south,

               signal_receiver_inactive, signal_receiver_pass_find_corner_south, signal_receiver_pass_accept_north, signal_receiver_pass_accept_south, signal_receiver_pass_find_corner_north]


def wireAffinities(self, wire_states=None, gsys=None):
    wire_affs = []
    wire_tr = []
    wire_aff_states = [signal_door_propped_open, signal_door_intermediate_accept, signal_door_inactive_east, signal_receiver_inactive, start_state_pair, ds_1, signal_door_east_stop, signal_door_east_reset_walk, signal_door_east_reset, signal_door_active_waiting_east, signal_door_pass_accept_north, signal_door_pass_accept_south, signal_door_pass_find_corner_north]

    wire_tr_states = [ds_1, start_state_pair]

    for i in wire_aff_states:
        wire_affs.append(AffinityRule(eastWire.label, i.label, "h", 1))
        wire_affs.append(AffinityRule(i.label, eastWire.label, "h", 1))

        if i in wire_tr_states:
            wire_tr.append(TransitionRule(i.label, eastWire.label, eastWire.label, i.label, "h"))

    return wire_affs, wire_tr



# 1. Make a table class
class TableGadget:
    def __init__(self):
        self.states = states_list
        self.tiles = []



    def makeDoorAffinitiesTransitions(self):
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
                            AffinityRule(signal_door_east_reset_walk.label, border_state.label, "v", 1)
                            ]

        horizontal_transition_rules = [TransitionRule(ds_1.label, signal_door_inactive_east.label, ds_1.label, signal_door_find_corner_north.label,"h"),
                                       TransitionRule(ds_1.label, signal_door_intermediate_accept.label, signal_door_intermediate_accept.label, ds_1.label, "h"),
                                       TransitionRule(start_state_pair.label, signal_door_intermediate_accept.label,
                                                      signal_door_east_stop.label, start_state_pair.label, "h"),
                                       TransitionRule(signal_door_east_stop.label, eastWire.label, eastWire.label, signal_door_east_reset.label, "h")
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
            TransitionRule(signal_transmitter_inactive.label, signal_door_handle_pass_find_corner_north.label, signal_transmitter_pass_find_corner_north.label, signal_door_handle_pass_find_corner_north.label, "v")
                                     ]

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


    def makeEastEdge(self, num_doors):
        door_seed_states = [signal_door_inactive_east, signal_door_handle_inactive,
                            signal_transmitter_inactive, signal_receiver_inactive, eastWire, end_data_string, ds_1, northCorner, southCorner, start_state_pair]
        curr_x, curr_y = 0, 0
        door_tiles = []
        for i in range(num_doors):
            dt = self.makeEastTableDoor(curr_x, curr_y)
            curr_y = curr_y + 4
            door_tiles = door_tiles + dt

        extra_wire_example_tiles = []
        for i in range(1, 4):
            extra_wire_example_tiles.append(Tile(eastWire, i, 0))
            extra_wire_example_tiles.append(Tile(eastWire, -i, 0))
        extra_wire_example_tiles.append(Tile(ds_1, -4, 0))
        extra_wire_example_tiles.append(Tile(ds_1, -5, 0))
        extra_wire_example_tiles.append(Tile(start_state_pair, -6, 0))

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
