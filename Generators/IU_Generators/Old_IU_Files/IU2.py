import UniversalClasses as uc
from Assets.colors import *
import sys

class DataString: # Takes in a list of data objects and
    def __init__(self, data, color):
        self.data = data

class IUGenerators:
    all_states = []
    all_aff = []
    all_tr = []
    all_sys = {}

    def __init__(self, exampleSysName=""):
        self.exampleSysName = exampleSysName
        self.genSys = None
        self.example_states_data = [start_state, ds_1, ds_2, ds_5, end_state]
        self.example_states_data2 = [north_prefix,
                                    start_state, ds_1, ds_2, ds_5, end_state]
        self.aff_list = []

    def basicWireSeedAssembly(self):
        seed_states = [westWire]
        seed_tiles = []
        for i in self.example_states_data:
            seed_states.append(i)

        for i in range(4):
            temp_tile = uc.Tile(westWire, i, 0)
            seed_tiles.append(temp_tile)

        c = 4
        for i in self.example_states_data:
            temp_tile = uc.Tile(i, c, 0)
            seed_tiles.append(temp_tile)
            c = c + 1

        asb = uc.Assembly()
        asb.setTiles(seed_tiles)
        return asb, seed_states, seed_tiles

    def basicWireSeedAssembly2(self):
        seed_states = [westWire]
        seed_tiles = []
        for i in self.example_states_data2:
            seed_states.append(i)

        for i in range(4):
            temp_tile = uc.Tile(westWire, i, 0)
            seed_tiles.append(temp_tile)

        c = 4
        for i in self.example_states_data2:
            temp_tile = uc.Tile(i, c, 0)
            seed_tiles.append(temp_tile)
            c = c + 1

        asb = uc.Assembly()
        asb.setTiles(seed_tiles)
        return asb, seed_states, seed_tiles



    def basicWireGenerator(self):
        asb, seed_states, seed_tiles = self.basicWireSeedAssembly()

        #System takes in temp, states, initial states, seed states, vertical_affinitys, horizontal_affinitys, vert transitions, horiz transitions, tile vertical transitions, tile horizontal transitions, seed assembly
        self.genSys = uc.System(1, seed_states, [], seed_states,  [], [], [], [], [], [], asb)

        for i in self.example_states_data:
            aff = uc.AffinityRule(westWire.label, i.label, "h", 1)
            self.all_aff.append(aff)
            self.genSys.addAffinity(aff)
            aff = uc.AffinityRule(i.label, westWire.label, "h", 1)
            self.genSys.addAffinity(aff)
            self.all_aff.append(aff)
            tr = uc.TransitionRule(westWire.label, i.label, i.label, westWire.label, "h")
            self.genSys.addTransitionRule(tr)
            self.all_tr.append(tr)

        aff = uc.AffinityRule(westWire.label, westWire.label, "h", 1)
        self.genSys.addAffinity(aff)
        self.all_aff.append(aff)
        self.all_sys["basicWire"] = self.genSys

        return self.genSys

    def basicWireGenerator2(self):
        asb, seed_states, seed_tiles = self.basicWireSeedAssembly2()

        #System takes in temp, states, initial states, seed states, vertical_affinitys, horizontal_affinitys, vert transitions, horiz transitions, tile vertical transitions, tile horizontal transitions, seed assembly
        self.genSys = uc.System(1, seed_states, [], seed_states,  [], [], [], [], [], [], asb)

        for i in self.example_states_data2:
            aff = uc.AffinityRule(westWire.label, i.label, "h", 1)
            self.all_aff.append(aff)
            self.genSys.addAffinity(aff)
            aff = uc.AffinityRule(i.label, westWire.label, "h", 1)
            self.genSys.addAffinity(aff)
            self.all_aff.append(aff)
            tr = uc.TransitionRule(westWire.label, i.label, i.label, westWire.label, "h")
            self.genSys.addTransitionRule(tr)
            self.all_tr.append(tr)

        aff = uc.AffinityRule(westWire.label, westWire.label, "h", 1)
        self.genSys.addAffinity(aff)
        self.all_aff.append(aff)
        self.all_sys["basicWire"] = self.genSys

        return self.genSys

    def wireGeneratorWithEndcapDoorNoSignalGadget(self):

        wire_sys = self.basicWireGenerator()
        end_cap_asb = wire_sys.returnSeedAssembly()
        endcap_door_tile = uc.Tile(endcap_door_west_inactive, -1, 0)
        ec_seed_tiles = [endcap_door_tile]
        for i in range (-2, -7, -1):
            temp_tile = uc.Tile(westWire, i, 0)
            ec_seed_tiles.append(temp_tile)

        endcap_seed_states = [endcap_door_west_inactive]

        end_cap_asb.setTiles(ec_seed_tiles)
        endcap_states = [endcap_door_west_inactive, endcap_door_west_active, endcap_door_west_stop] + wire_sys.returnStates()
        endcap_all_seed_states = endcap_seed_states + wire_sys.returnSeedStates()
        horizontal_transitions = wire_sys.returnHorizontalTransitionList()
        horizontal_affinities = wire_sys.returnHorizontalAffinityList()
        endcap_genSys = uc.System(1, endcap_states, [], endcap_all_seed_states, [], horizontal_affinities, [], horizontal_transitions, [], [], end_cap_asb)

        endcap_genSys.addAffinity(uc.AffinityRule(endcap_door_west_inactive.label, westWire.label, "h", 1))

        endcap_genSys.addAffinity(uc.AffinityRule(endcap_door_west_inactive.label, start_state.label, "h", 1))

        endcap_genSys.addAffinity(uc.AffinityRule(endcap_door_west_stop.label, end_state.label, "h", 1))

        endcap_genSys.addAffinity(uc.AffinityRule(endcap_door_west_stop.label, westWire.label, "h", 1))
        endcap_genSys.addAffinity(uc.AffinityRule(westWire.label, endcap_door_west_stop.label, "h", 1))

        for i in self.example_states_data:
            endcap_genSys.addAffinity(uc.AffinityRule(endcap_door_west_active.label, i.label, "h", 1))
            endcap_genSys.addAffinity(uc.AffinityRule(i.label, endcap_door_west_active.label, "h", 1))
            if i != end_state:
                endcap_genSys.addTransitionRule(uc.TransitionRule(endcap_door_west_active.label, i.label, i.label, endcap_door_west_active.label, "h"))
            else:
                endcap_genSys.addTransitionRule(uc.TransitionRule(    endcap_door_west_active.label, i.label, i.label, endcap_door_west_stop.label, "h"))

        endcap_genSys.addTransitionRule(uc.TransitionRule(endcap_door_west_inactive.label, start_state.label, endcap_door_west_active.label, start_state.label, "h"))

        endcap_genSys.addTransitionRule(uc.TransitionRule(westWire.label, endcap_door_west_stop.label, endcap_door_west_stop.label, westWire.label, "h"))
        self.all_sys["endCapBasic"] = endcap_genSys
        return endcap_genSys

    def wireGeneratorWithEndcapDoorNoSignalGadget2(self):

        wire_sys = self.basicWireGenerator2()
        end_cap_asb = wire_sys.returnSeedAssembly()
        endcap_door_tile = uc.Tile(endcap_door_west_inactive, -1, 0)
        ec_seed_tiles = [endcap_door_tile]
        for i in range(-2, -8, -1):
            temp_tile = uc.Tile(westWire, i, 0)
            ec_seed_tiles.append(temp_tile)

        endcap_seed_states = [endcap_door_west_inactive]

        end_cap_asb.setTiles(ec_seed_tiles)
        endcap_states = [endcap_door_west_inactive, endcap_door_west_active,
                         endcap_door_west_stop] + wire_sys.returnStates()
        endcap_all_seed_states = endcap_seed_states + wire_sys.returnSeedStates()
        horizontal_transitions = wire_sys.returnHorizontalTransitionList()
        horizontal_affinities = wire_sys.returnHorizontalAffinityList()
        endcap_genSys = uc.System(1, endcap_states, [], endcap_all_seed_states, [
        ], horizontal_affinities, [], horizontal_transitions, [], [], end_cap_asb)

        endcap_genSys.addAffinity(uc.AffinityRule(endcap_door_west_inactive.label, westWire.label, "h", 1))

        endcap_genSys.addAffinity(uc.AffinityRule(endcap_door_west_inactive.label, north_prefix.label, "h", 1))

        endcap_genSys.addAffinity(uc.AffinityRule(endcap_door_west_stop.label, end_state.label, "h", 1))

        endcap_genSys.addAffinity(uc.AffinityRule(endcap_door_west_stop.label, westWire.label, "h", 1))
        endcap_genSys.addAffinity(uc.AffinityRule(westWire.label, endcap_door_west_stop.label, "h", 1))

        for i in self.example_states_data2:
            endcap_genSys.addAffinity(uc.AffinityRule(endcap_door_west_active.label, i.label, "h", 1))
            endcap_genSys.addAffinity(uc.AffinityRule(i.label, endcap_door_west_active.label, "h", 1))
            if i != end_state:
                endcap_genSys.addTransitionRule(uc.TransitionRule(    endcap_door_west_active.label, i.label, i.label, endcap_door_west_active.label, "h"))
            else:
                endcap_genSys.addTransitionRule(uc.TransitionRule(    endcap_door_west_active.label, i.label, i.label, endcap_door_west_stop.label, "h"))

        endcap_genSys.addTransitionRule(uc.TransitionRule(endcap_door_west_inactive.label, north_prefix.label, endcap_door_west_active.label, north_prefix.label, "h"))

        endcap_genSys.addTransitionRule(uc.TransitionRule(westWire.label, endcap_door_west_stop.label, endcap_door_west_stop.label, westWire.label, "h"))
        self.all_sys["endCapBasic"] = endcap_genSys
        return endcap_genSys

    def wireGeneratorWithEndcapDoorNoSignalGadget_Protected_Trapdoor(self):

        wire_sys = self.basicWireGenerator2()
        end_cap_asb = wire_sys.returnSeedAssembly()
        endcap_door_tile = uc.Tile(endcap_door_west_inactive, -1, 0)
        ec_seed_tiles = [endcap_door_tile]
        for i in range(-2, -8, -1):
            temp_tile = uc.Tile(westWire, i, 0)
            ec_seed_tiles.append(temp_tile)
            if i < -7:
                temp_tile = uc.Tile(border_state, i, 1)
                ec_seed_tiles.append(temp_tile)
            else:
                pass #TD South

        endcap_seed_states = [endcap_door_west_inactive]

        end_cap_asb.setTiles(ec_seed_tiles)
        endcap_states = [endcap_door_west_inactive, endcap_door_west_active,
                         endcap_door_west_stop] + wire_sys.returnStates()
        endcap_all_seed_states = endcap_seed_states + wire_sys.returnSeedStates()
        horizontal_transitions = wire_sys.returnHorizontalTransitionList()
        horizontal_affinities = wire_sys.returnHorizontalAffinityList()
        endcap_genSys = uc.System(1, endcap_states, [], endcap_all_seed_states, [
        ], horizontal_affinities, [], horizontal_transitions, [], [], end_cap_asb)

        endcap_genSys.addAffinity(uc.AffinityRule(endcap_door_west_inactive.label, westWire.label, "h", 1))

        endcap_genSys.addAffinity(uc.AffinityRule(endcap_door_west_inactive.label, north_prefix.label, "h", 1))

        endcap_genSys.addAffinity(uc.AffinityRule(endcap_door_west_stop.label, end_state.label, "h", 1))

        endcap_genSys.addAffinity(uc.AffinityRule(endcap_door_west_stop.label, westWire.label, "h", 1))
        endcap_genSys.addAffinity(uc.AffinityRule(westWire.label, endcap_door_west_stop.label, "h", 1))

        for i in self.example_states_data2:
            endcap_genSys.addAffinity(uc.AffinityRule(endcap_door_west_active.label, i.label, "h", 1))
            endcap_genSys.addAffinity(uc.AffinityRule(i.label, endcap_door_west_active.label, "h", 1))
            if i != end_state:
                endcap_genSys.addTransitionRule(uc.TransitionRule(    endcap_door_west_active.label, i.label, i.label, endcap_door_west_active.label, "h"))
            else:
                endcap_genSys.addTransitionRule(uc.TransitionRule(    endcap_door_west_active.label, i.label, i.label, endcap_door_west_stop.label, "h"))

        endcap_genSys.addTransitionRule(uc.TransitionRule(endcap_door_west_inactive.label, north_prefix.label, endcap_door_west_active.label, north_prefix.label, "h"))

        endcap_genSys.addTransitionRule(uc.TransitionRule(westWire.label, endcap_door_west_stop.label, endcap_door_west_stop.label, westWire.label, "h"))
        self.all_sys["endCapBasic"] = endcap_genSys
        return endcap_genSys
    def wireGeneratorWithEndcapDoorSignalGadget(self):
        endcap_no_signal_sys = self.wireGeneratorWithEndcapDoorNoSignalGadget()

        endcap_gadget_seed_states = [endcap_door_west_handle_inactive] + endcap_no_signal_sys.returnSeedStates()
        endcap_gadget_states = [endcap_door_west_handle_inactive, endcap_door_west_handle_active, endcap_door_west_handle_stop] + endcap_no_signal_sys.returnStates()
        endcap_horizontal_transitions = endcap_no_signal_sys.returnHorizontalTransitionList()
        endcap_horizontal_affinities = endcap_no_signal_sys.returnHorizontalAffinityList()
        endcap_asb = endcap_no_signal_sys.returnSeedAssembly()

        endcap_asb.setTiles([uc.Tile(endcap_door_west_handle_inactive, -1, 1)])
        #System takes in temp, states, initial states, seed states, vertical_affinitys, horizontal_affinitys, vert transitions, horiz transitions, tile vertical transitions, tile horizontal transitions, seed assembly
        endcap_signal_genSys = uc.System(1, endcap_gadget_states, [], endcap_gadget_seed_states,  [], endcap_horizontal_affinities, [], endcap_horizontal_transitions, [],  [], endcap_asb)

        endcap_signal_genSys.addAffinity(uc.AffinityRule(endcap_door_west_handle_inactive.label, endcap_door_west_inactive.label, "v", 1))
        endcap_signal_genSys.addAffinity(uc.AffinityRule(endcap_door_west_handle_inactive.label, endcap_door_west_active.label, "v", 1))
        endcap_signal_genSys.addAffinity(uc.AffinityRule(endcap_door_west_handle_active.label, endcap_door_west_active.label, "v", 1))
        endcap_signal_genSys.addAffinity(uc.AffinityRule(endcap_door_west_handle_inactive.label, endcap_door_west_stop.label, "v", 1))
        return endcap_signal_genSys

    def wireGeneratorWithEndcapDoorSignalGadget2(self):
        endcap_no_signal_sys = self.wireGeneratorWithEndcapDoorNoSignalGadget2()

        endcap_gadget_seed_states = [
            endcap_door_west_handle_inactive] + endcap_no_signal_sys.returnSeedStates()
        endcap_gadget_states = [endcap_door_west_handle_inactive, endcap_door_west_handle_active,
                                endcap_door_west_handle_stop] + endcap_no_signal_sys.returnStates()
        endcap_horizontal_transitions = endcap_no_signal_sys.returnHorizontalTransitionList()
        endcap_horizontal_affinities = endcap_no_signal_sys.returnHorizontalAffinityList()
        endcap_asb = endcap_no_signal_sys.returnSeedAssembly()

        endcap_asb.setTiles([uc.Tile(endcap_door_west_handle_inactive, -1, 1)])
        #System takes in temp, states, initial states, seed states, vertical_affinitys, horizontal_affinitys, vert transitions, horiz transitions, tile vertical transitions, tile horizontal transitions, seed assembly
        endcap_signal_genSys = uc.System(1, endcap_gadget_states, [], endcap_gadget_seed_states,  [
        ], endcap_horizontal_affinities, [], endcap_horizontal_transitions, [],  [], endcap_asb)

        endcap_signal_genSys.addAffinity(uc.AffinityRule(endcap_door_west_handle_inactive.label, endcap_door_west_inactive.label, "v", 1))
        endcap_signal_genSys.addAffinity(uc.AffinityRule(endcap_door_west_handle_inactive.label, endcap_door_west_active.label, "v", 1))
        endcap_signal_genSys.addAffinity(uc.AffinityRule(endcap_door_west_handle_active.label, endcap_door_west_active.label, "v", 1))
        endcap_signal_genSys.addAffinity(uc.AffinityRule(endcap_door_west_handle_inactive.label, endcap_door_west_stop.label, "v", 1))
        return endcap_signal_genSys

    def EqualityGadgetGenerator(self):
        #equality_gadget_seed_states = [equality_gadget_inactive, equality_gadget_active]
        #equality_gadget_states = [equality_gadget_inactive, equality_gadget_active, equality_gadget_stop]
        endcap_signal_sys = self.wireGeneratorWithEndcapDoorSignalGadget()
        endcap_asb = endcap_signal_sys.returnSeedAssembly()

        equality_gadget_seed_states = [check_equal_S_start_state_inactive, check_equal_S_end_state_inactive,
                                       check_equal_S_any_num_state_inactive, row_signal_positive_inactive, trap_door_inactive, row_signal_positive_start_inactive, signal_transmitter_turn_down_inactive] + endcap_signal_sys.returnSeedStates()
        equality_gadget_states = [check_equal_S_start_state_inactive, check_equal_S_end_state_inactive, check_equal_S_any_num_state_inactive, row_signal_positive_inactive, check_equal_S_any_num_state,
                                  check_equal_S_end_state, check_equal_S_start_state, trap_door_inactive, signal_transmitter_turn_up_active, endcap_door_west_handle_active, signal_transmitter_turn_up_inactive, row_signal_positive_start_inactive, row_signal_positive_waiting, row_signal_positive_start_waiting, signal_transmitter_turn_down_inactive, row_signal_positive_full_accept, signal_transmitter_turn_down_active, confirm_equal_S_start_state, confirm_equal_S_end_state, confirm_equal_S_any_state, row_signal_intermediate_accept, signal_door_handle_open, signal_door_open] + endcap_signal_sys.returnStates()

        equality_gadget_seed_tiles = []
        eq_t = uc.Tile(signal_transmitter_turn_up_inactive, -1, 2)
        equality_gadget_seed_tiles.append(eq_t)
        for i in range(-2, -7, -1):
            if i == -2:
                r1t = uc.Tile(check_equal_S_end_state_inactive, i, 1)
                equality_gadget_seed_tiles.append(r1t)

            elif i < -2 and i > -6:
                r1t = uc.Tile(check_equal_S_any_num_state_inactive, i, 1)
                equality_gadget_seed_tiles.append(r1t)
            elif i == -6:
                r1t = uc.Tile(check_equal_S_start_state_inactive, i, 1)
                equality_gadget_seed_tiles.append(r1t)

            if i == -2:
                t = uc.Tile(row_signal_positive_start_inactive, i, 2)
                equality_gadget_seed_tiles.append(t)
            else:
                r2t = uc.Tile(row_signal_positive_inactive, i, 2)
                equality_gadget_seed_tiles.append(r2t)

        eq_t = uc.Tile(signal_transmitter_turn_down_inactive, -7, 2)
        equality_gadget_seed_tiles.append(eq_t)

        eq_t = uc.Tile(signal_door_handle_inactive, -7, 1)
        equality_gadget_seed_tiles.append(eq_t)

        eq_t = uc.Tile(signal_door_inactive, -7, 0)
        equality_gadget_seed_tiles.append(eq_t)

        eq_t = uc.Tile(trap_door_inactive, -6, -1)
        equality_gadget_seed_tiles.append(eq_t)

        for i in range(-8, -14, -1):
            temp_tile = uc.Tile(westWire, i, 0)
            equality_gadget_seed_tiles.append(temp_tile)

        endcap_asb.setTiles(equality_gadget_seed_tiles)
        endcap_horizontal_affinities = endcap_signal_sys.returnHorizontalAffinityList()
        endcap_vertical_affinities = endcap_signal_sys.returnVerticalAffinityList()
        endcap_horizontal_transitions = endcap_signal_sys.returnHorizontalTransitionList()
        endcap_equality_gadget_sys = uc.System(1, equality_gadget_states, [], equality_gadget_seed_states,  endcap_vertical_affinities, endcap_horizontal_affinities, [], endcap_horizontal_transitions, [], [], endcap_asb)



        ## Add -1 column affinities
        aff = uc.AffinityRule(signal_transmitter_turn_up_inactive.label,
                              endcap_door_west_handle_inactive.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(signal_transmitter_turn_up_inactive.label,
                              endcap_door_west_handle_active.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(signal_transmitter_turn_up_active.label,
                              endcap_door_west_handle_active.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        ## Add -1 column transitions
        tr = uc.TransitionRule(endcap_door_west_handle_inactive.label, endcap_door_west_stop.label,
                               endcap_door_west_handle_active.label, endcap_door_west_stop.label, "v")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        tr = uc.TransitionRule(signal_transmitter_turn_up_inactive.label, endcap_door_west_handle_active.label,
                               signal_transmitter_turn_up_active.label, endcap_door_west_handle_active.label, "v")
        endcap_equality_gadget_sys.addTransitionRule(tr)


        ## Signal Row Affinities
        aff = uc.AffinityRule(row_signal_positive_start_inactive.label, signal_transmitter_turn_up_inactive.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(row_signal_positive_start_inactive.label, signal_transmitter_turn_up_active.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(row_signal_positive_start_waiting.label, signal_transmitter_turn_up_active.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(row_signal_positive_inactive.label, row_signal_positive_start_inactive.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(row_signal_positive_inactive.label, row_signal_positive_start_waiting.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(row_signal_positive_waiting.label, row_signal_positive_start_waiting.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(row_signal_positive_waiting.label, row_signal_positive_waiting.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(signal_transmitter_turn_down_inactive.label, row_signal_positive_waiting.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(signal_transmitter_turn_down_active.label,
                              row_signal_positive_full_accept.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        ### Transitions with row_signal
        tr = uc.TransitionRule(signal_transmitter_turn_down_inactive.label, row_signal_positive_full_accept.label,
                               signal_transmitter_turn_down_active.label, row_signal_positive_full_accept.label, "h")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        tr = uc.TransitionRule(row_signal_positive_start_inactive.label, signal_transmitter_turn_up_active.label, row_signal_positive_start_waiting.label, signal_transmitter_turn_up_active.label, "h")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        tr = uc.TransitionRule(row_signal_positive_inactive.label, row_signal_positive_start_waiting.label,
                               row_signal_positive_waiting.label, row_signal_positive_start_waiting.label, "h")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        tr = uc.TransitionRule(row_signal_positive_inactive.label, row_signal_positive_waiting.label,
                               row_signal_positive_waiting.label, row_signal_positive_waiting.label, "h")
        endcap_equality_gadget_sys.addTransitionRule(tr)



        #Vertical Affinities between equality signal and equality tiles
        aff = uc.AffinityRule(row_signal_positive_start_inactive.label,
                              check_equal_S_end_state_inactive.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(row_signal_positive_start_inactive.label, check_equal_S_end_state.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(row_signal_positive_waiting.label,
                              check_equal_S_any_num_state_inactive.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(row_signal_positive_waiting.label,
                              check_equal_S_any_num_state.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(row_signal_positive_start_waiting.label,
                              check_equal_S_end_state.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        ### Transitions with equality signal
        tr = uc.TransitionRule(row_signal_positive_waiting.label, check_equal_S_any_num_state_inactive.label, row_signal_positive_waiting.label, check_equal_S_any_num_state.label, "v")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        tr = uc.TransitionRule(row_signal_positive_waiting.label, check_equal_S_start_state_inactive.label,
                               row_signal_positive_waiting.label, check_equal_S_start_state.label, "v")
        endcap_equality_gadget_sys.addTransitionRule(tr)


        tr = uc.TransitionRule(row_signal_positive_start_waiting.label, check_equal_S_end_state_inactive.label,
                               row_signal_positive_start_waiting.label, check_equal_S_end_state.label, "v")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        ### Equality Tiles Test Data String
        aff = uc.AffinityRule(confirm_equal_S_end_state.label, end_state.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        tr = uc.TransitionRule(check_equal_S_end_state.label, end_state.label,
                               confirm_equal_S_end_state.label, end_state.label, "v")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        aff = uc.AffinityRule(row_signal_positive_start_waiting.label, confirm_equal_S_end_state.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(row_signal_positive_full_accept.label, confirm_equal_S_end_state.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        tr = uc.TransitionRule(row_signal_positive_start_waiting.label, confirm_equal_S_end_state.label,
                               row_signal_positive_full_accept.label, confirm_equal_S_end_state.label, "v")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        ### Equality Tiles Any Number Equality
        aff = uc.AffinityRule(check_equal_S_any_num_state.label, ds_0.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(check_equal_S_any_num_state.label, ds_1.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(check_equal_S_any_num_state.label, ds_2.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(check_equal_S_any_num_state.label, ds_3.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(check_equal_S_any_num_state.label, ds_4.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(check_equal_S_any_num_state.label, ds_5.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(check_equal_S_any_num_state.label, ds_6.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(check_equal_S_any_num_state.label, ds_7.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(check_equal_S_any_num_state.label, ds_8.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(check_equal_S_any_num_state.label, ds_9.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        ### Confirm Equality Aff with Data String
        aff = uc.AffinityRule(confirm_equal_S_any_state.label, ds_0.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(confirm_equal_S_any_state.label, ds_1.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(confirm_equal_S_any_state.label, ds_2.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(confirm_equal_S_any_state.label, ds_3.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(confirm_equal_S_any_state.label, ds_4.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(confirm_equal_S_any_state.label, ds_5.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(confirm_equal_S_any_state.label, ds_6.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(confirm_equal_S_any_state.label, ds_7.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(confirm_equal_S_any_state.label, ds_8.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(confirm_equal_S_any_state.label, ds_9.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        ### Equality Tiles Start State Check Equality
        aff = uc.AffinityRule(check_equal_S_start_state.label, start_state.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(confirm_equal_S_start_state.label, start_state.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        tr = uc.TransitionRule(check_equal_S_start_state.label, start_state.label,
                               confirm_equal_S_start_state.label, start_state.label, "v")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        tr = uc.TransitionRule(row_signal_positive_waiting.label, confirm_equal_S_start_state.label,
                               row_signal_intermediate_accept.label, confirm_equal_S_start_state.label, "v")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        ### Equality Tiles Transitions with Data String
        for i in data_states_list_nums_only:
            tr = uc.TransitionRule(check_equal_S_any_num_state.label, i.label, confirm_equal_S_any_state.label, i.label, "v")
            endcap_equality_gadget_sys.addTransitionRule(tr)


        ### Row Signal Positive Start Waiting Affinity
        aff = uc.AffinityRule(row_signal_intermediate_accept.label, confirm_equal_S_any_state.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(row_signal_positive_waiting.label, confirm_equal_S_any_state.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        tr = uc.TransitionRule(row_signal_positive_waiting.label, confirm_equal_S_any_state.label,
                               row_signal_intermediate_accept.label, confirm_equal_S_any_state.label, "v")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        aff = uc.AffinityRule(row_signal_intermediate_accept.label, confirm_equal_S_start_state.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(row_signal_positive_waiting.label, confirm_equal_S_start_state.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        tr = uc.TransitionRule(row_signal_positive_waiting.label, confirm_equal_S_start_state.label,
                               row_signal_intermediate_accept.label, confirm_equal_S_start_state.label, "v")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        aff = uc.AffinityRule(row_signal_positive_waiting.label, row_signal_positive_full_accept.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(row_signal_intermediate_accept.label, row_signal_positive_full_accept.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        tr = uc.TransitionRule(row_signal_intermediate_accept.label, row_signal_positive_full_accept.label,
                               row_signal_positive_full_accept.label, row_signal_positive_full_accept.label, "h")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        ### If inactive meets full accept transition to waiting
        aff = uc.AffinityRule(row_signal_positive_inactive.label, row_signal_positive_full_accept.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        tr = uc.TransitionRule(row_signal_positive_inactive.label, row_signal_positive_full_accept.label,
                               row_signal_positive_waiting.label, row_signal_positive_full_accept.label, "h")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        ### Turndown Key Affinity and Transition
        aff = uc.AffinityRule(signal_transmitter_turn_down_active.label, signal_door_handle_inactive.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(signal_transmitter_turn_down_active.label, signal_door_handle_open.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        tr = uc.TransitionRule(signal_transmitter_turn_down_active.label, signal_door_handle_inactive.label, signal_transmitter_turn_down_active.label, signal_door_handle_open.label, "v")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        aff = uc.AffinityRule(signal_door_handle_open.label, signal_door_inactive.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(signal_door_handle_open.label,
                              signal_door_open.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        tr = uc.TransitionRule(signal_door_handle_open.label, signal_door_inactive.label, signal_door_handle_open.label, signal_door_open.label, "v")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        for i in data_states_list_all:
            aff = uc.AffinityRule(signal_door_open.label, i.label, "h", 1)
            endcap_equality_gadget_sys.addAffinity(aff)

            tr = uc.TransitionRule(signal_door_open.label, i.label, i.label, signal_door_open.label, "h")
            endcap_equality_gadget_sys.addTransitionRule(tr)

        """ tr = uc.TransitionRule(westWire.label, signal_door_open.label, i.label, signal_door_open.label, "h")
        endcap_equality_gadget_sys.addTransitionRule(tr) """

        ### Resetting the Gadget
        endcap_equality_gadget_sys.addState(endcap_door_west_reset)
        endcap_equality_gadget_sys.addState(endcap_door_west_handle_reset)
        endcap_equality_gadget_sys.addState(signal_door_reset)
        endcap_equality_gadget_sys.addState(signal_door_reset_walk)
        endcap_equality_gadget_sys.addState(endcap_door_west_reset_waiting)
        endcap_equality_gadget_sys.addState(signal_transmitter_turn_down_reset)
        endcap_equality_gadget_sys.addState(signal_transmitter_turn_up_reset)
        endcap_equality_gadget_sys.addState(endcap_door_west_handle_reset_waiting)
        endcap_equality_gadget_sys.addState(row_signal_positive_reset)
        endcap_equality_gadget_sys.addState(signal_door_handle_reset)
        endcap_equality_gadget_sys.addState(signal_door_send_confirmed_transmission)
        endcap_equality_gadget_sys.addState(reset_confirmed_transmission_westWire)
        endcap_equality_gadget_sys.addState(signal_door_handle_inactive)
        endcap_equality_gadget_sys.addState(signal_door_inactive)


        aff = uc.AffinityRule(signal_door_open.label, endcap_door_west_stop.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff)
        aff = uc.AffinityRule(signal_door_reset.label, endcap_door_west_reset.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        tr = uc.TransitionRule(signal_door_open.label, endcap_door_west_stop.label, signal_door_reset.label, endcap_door_west_reset.label, "h")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        aff = uc.AffinityRule(endcap_door_west_handle_active.label, endcap_door_west_reset.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(endcap_door_west_handle_reset.label, endcap_door_west_reset.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        tr = uc.TransitionRule(endcap_door_west_handle_active.label, endcap_door_west_reset.label,
                               endcap_door_west_handle_reset.label, endcap_door_west_reset_waiting.label, "v")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        aff1 = uc.AffinityRule(signal_transmitter_turn_up_active.label, endcap_door_west_handle_reset.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff1)

        aff2 = uc.AffinityRule(signal_transmitter_turn_up_reset.label, endcap_door_west_handle_inactive.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff2)

        endcap_equality_gadget_sys.addTransitionRule(self.combine_affs_for_tr(aff1, aff2, "v"))

        aff1 = uc.AffinityRule(row_signal_positive_full_accept.label, signal_transmitter_turn_up_reset.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff1)

        aff2 = uc.AffinityRule(row_signal_positive_reset.label, signal_transmitter_turn_up_inactive.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff2)

        endcap_equality_gadget_sys.addTransitionRule(self.combine_affs_for_tr(aff1, aff2, "h"))

        aff1 = uc.AffinityRule(row_signal_positive_full_accept.label, row_signal_positive_reset.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff1)

        aff2 = uc.AffinityRule(row_signal_positive_reset.label, row_signal_positive_inactive.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff2)

        endcap_equality_gadget_sys.addTransitionRule(self.combine_affs_for_tr(aff1, aff2, "h"))

        aff1 = uc.AffinityRule(signal_transmitter_turn_down_active.label, row_signal_positive_reset.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff1)

        aff2 = uc.AffinityRule(signal_transmitter_turn_down_reset.label, row_signal_positive_inactive.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff2)

        endcap_equality_gadget_sys.addTransitionRule(self.combine_affs_for_tr(aff1, aff2, "h"))

        aff1 = uc.AffinityRule(signal_transmitter_turn_down_reset.label, signal_door_handle_open.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff1)

        aff2 = uc.AffinityRule(signal_transmitter_turn_down_inactive.label, signal_door_handle_reset.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff2)

        endcap_equality_gadget_sys.addTransitionRule(self.combine_affs_for_tr(aff1, aff2, "v"))

        ### Signal Door Walk Reset
        aff1 = uc.AffinityRule(confirm_equal_S_end_state.label, signal_door_reset.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff1)

        aff2 = uc.AffinityRule(check_equal_S_end_state_inactive.label, signal_door_reset_walk.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff2)

        endcap_equality_gadget_sys.addTransitionRule(self.combine_affs_for_tr(aff1, aff2, "v"))

        aff1 = uc.AffinityRule(westWire.label, signal_door_reset_walk.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff1)

        aff2 = uc.AffinityRule(signal_door_reset.label, westWire.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff2)

        endcap_equality_gadget_sys.addTransitionRule(self.combine_affs_for_tr(aff1, aff2, "h"))

        aff1 = uc.AffinityRule(confirm_equal_S_any_state.label, signal_door_reset.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff1)

        aff2 = uc.AffinityRule(check_equal_S_any_num_state_inactive.label, signal_door_reset_walk.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff2)

        endcap_equality_gadget_sys.addTransitionRule(self.combine_affs_for_tr(aff1, aff2, "v"))

        aff1 = uc.AffinityRule(confirm_equal_S_start_state.label, signal_door_reset.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff1)

        aff2 = uc.AffinityRule(check_equal_S_start_state_inactive.label, signal_door_reset_walk.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff2)

        endcap_equality_gadget_sys.addTransitionRule(self.combine_affs_for_tr(aff1, aff2, "v"))

        aff1 = uc.AffinityRule(signal_door_handle_reset.label, signal_door_reset.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff1)

        aff2 = uc.AffinityRule(signal_door_handle_inactive.label,
                               signal_door_send_confirmed_transmission.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff2)

        endcap_equality_gadget_sys.addTransitionRule(self.combine_affs_for_tr(aff1, aff2, "v"))

        aff1 = uc.AffinityRule(signal_door_send_confirmed_transmission.label, westWire.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff1)

        aff2 = uc.AffinityRule(signal_door_inactive.label,
                               reset_confirmed_transmission_westWire.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff2)

        endcap_equality_gadget_sys.addTransitionRule(self.combine_affs_for_tr(aff1, aff2, "h"))

        aff1 = uc.AffinityRule(reset_confirmed_transmission_westWire.label, westWire.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff1)

        aff2 = uc.AffinityRule(westWire.label, reset_confirmed_transmission_westWire.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff2)

        endcap_equality_gadget_sys.addTransitionRule(self.combine_affs_for_tr(aff1, aff2, "h"))

        aff1 = uc.AffinityRule(reset_confirmed_transmission_westWire.label,
                               endcap_door_west_reset_waiting.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff1)

        aff2 = uc.AffinityRule(westWire.label, endcap_door_west_inactive.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff2)

        endcap_equality_gadget_sys.addTransitionRule(self.combine_affs_for_tr(aff1, aff2, "h"))

        print("Endcap Equality Gadget System States Number: " + str(len(endcap_equality_gadget_sys.states)))

        return endcap_equality_gadget_sys


    def equality_gadget_with_prefixes(self):
        endcap_signal_sys = self.wireGeneratorWithEndcapDoorSignalGadget2()
        endcap_asb = endcap_signal_sys.returnSeedAssembly()

        equality_gadget_seed_states = [check_equal_S_start_state_inactive, check_equal_S_end_state_inactive,
                                       check_equal_S_any_num_state_inactive, row_signal_positive_inactive, trap_door_inactive, row_signal_positive_start_inactive, signal_transmitter_turn_down_inactive, signal_transmitter_turn_up_inactive] + endcap_signal_sys.returnSeedStates()
        equality_gadget_states = [check_equal_S_start_state_inactive, check_equal_S_end_state_inactive, check_equal_S_any_num_state_inactive, row_signal_positive_inactive, check_equal_S_any_num_state,
                                  check_equal_S_end_state, check_equal_S_start_state, trap_door_inactive, signal_transmitter_turn_up_active, endcap_door_west_handle_active, signal_transmitter_turn_up_inactive, row_signal_positive_start_inactive, row_signal_positive_waiting, row_signal_positive_start_waiting, signal_transmitter_turn_down_inactive, row_signal_positive_full_accept, signal_transmitter_turn_down_active, confirm_equal_S_start_state, confirm_equal_S_end_state, confirm_equal_S_any_state, row_signal_intermediate_accept, signal_door_handle_open, signal_door_open] + endcap_signal_sys.returnStates()
        ## Prefix Additions
        for i in data_states_list_all_with_north_prefixes:
            equality_gadget_seed_states.append(i)
            equality_gadget_states.append(i)

        equality_gadget_seed_states.append(check_equal_S_NorthPrefix_inactive)
        equality_gadget_states.append(check_equal_S_NorthPrefix_inactive)


        equality_gadget_states.append(check_equal_S_NorthPrefix)





        ### Back to regular code
        equality_gadget_seed_tiles = []
        eq_t = uc.Tile(signal_transmitter_turn_up_inactive, -1, 2)
        equality_gadget_seed_tiles.append(eq_t)
        for i in range(-2, -8, -1):
            if i == -2:
                r1t = uc.Tile(check_equal_S_end_state_inactive, i, 1)
                equality_gadget_seed_tiles.append(r1t)

            elif i < -2 and i > -7:
                r1t = uc.Tile(check_equal_S_any_num_state_inactive, i, 1)
                equality_gadget_seed_tiles.append(r1t)
            elif i == -6:
                r1t = uc.Tile(check_equal_S_start_state_inactive, i, 1)
                equality_gadget_seed_tiles.append(r1t)
            elif i == -7:
                r1t = uc.Tile(check_equal_S_NorthPrefix_inactive, i, 1)
                equality_gadget_seed_tiles.append(r1t)
            if i == -2:
                t = uc.Tile(row_signal_positive_start_inactive, i, 2)
                equality_gadget_seed_tiles.append(t)
            else:
                r2t = uc.Tile(row_signal_positive_inactive, i, 2)
                equality_gadget_seed_tiles.append(r2t)

        eq_t = uc.Tile(signal_transmitter_turn_down_inactive, -8, 2)
        equality_gadget_seed_tiles.append(eq_t)

        eq_t = uc.Tile(signal_door_handle_inactive, -8, 1)
        equality_gadget_seed_tiles.append(eq_t)

        eq_t = uc.Tile(signal_door_inactive, -8, 0)
        equality_gadget_seed_tiles.append(eq_t)

        eq_t = uc.Tile(trap_door_inactive, -7, -1)
        equality_gadget_seed_tiles.append(eq_t)

        for i in range(-9, -14, -1):
            temp_tile = uc.Tile(westWire, i, 0)
            equality_gadget_seed_tiles.append(temp_tile)

        for i in range(-2, -7, -1):
            temp_tile = uc.Tile(southWire, -7, i)
            equality_gadget_seed_tiles.append(temp_tile)

        ### Added Tiles
        endcap_asb.setTiles(equality_gadget_seed_tiles)
        endcap_horizontal_affinities = endcap_signal_sys.returnHorizontalAffinityList()
        endcap_vertical_affinities = endcap_signal_sys.returnVerticalAffinityList()
        endcap_horizontal_transitions = endcap_signal_sys.returnHorizontalTransitionList()
        endcap_equality_gadget_sys = uc.System(1, equality_gadget_states, [], equality_gadget_seed_states,
                                               endcap_vertical_affinities, endcap_horizontal_affinities, [], endcap_horizontal_transitions, [], [], endcap_asb)

        equality_gadget_states.append(south_prefix)
        equality_gadget_states.append(east_prefix)
        equality_gadget_states.append(west_prefix)
        equality_gadget_seed_states.append(check_equal_S_NorthPrefix_inactive)
        equality_gadget_states.append(check_equal_S_NorthPrefix_inactive)
        equality_gadget_states.append(confirm_equal_S_prefixN_state)
        equality_gadget_states.append(southWire)
        equality_gadget_seed_states.append(southWire)
        endcap_equality_gadget_sys.addState(endcap_door_west_reset)
        endcap_equality_gadget_sys.addState(endcap_door_west_handle_reset)
        endcap_equality_gadget_sys.addState(signal_door_reset)
        endcap_equality_gadget_sys.addState(signal_door_reset_walk)
        endcap_equality_gadget_sys.addState(endcap_door_west_reset_waiting)
        endcap_equality_gadget_sys.addState(signal_transmitter_turn_down_reset)
        endcap_equality_gadget_sys.addState(signal_transmitter_turn_up_reset)
        endcap_equality_gadget_sys.addState(endcap_door_west_handle_reset_waiting)
        endcap_equality_gadget_sys.addState(row_signal_positive_reset)
        endcap_equality_gadget_sys.addState(signal_door_handle_reset)
        endcap_equality_gadget_sys.addState(signal_door_send_confirmed_transmission)
        endcap_equality_gadget_sys.addState(reset_confirmed_transmission_westWire)
        endcap_equality_gadget_sys.addState(signal_door_handle_inactive)
        endcap_equality_gadget_sys.addState(signal_door_inactive)
    ### Purely Signal Arc
        ## Add -1 column affinities
        aff = uc.AffinityRule(signal_transmitter_turn_up_inactive.label,
                              endcap_door_west_handle_inactive.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(signal_transmitter_turn_up_inactive.label,
                              endcap_door_west_handle_active.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(signal_transmitter_turn_up_active.label,
                              endcap_door_west_handle_active.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        ## Add -1 column transitions
        tr = uc.TransitionRule(endcap_door_west_handle_inactive.label, endcap_door_west_stop.label,
                               endcap_door_west_handle_active.label, endcap_door_west_stop.label, "v")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        tr = uc.TransitionRule(signal_transmitter_turn_up_inactive.label, endcap_door_west_handle_active.label,
                               signal_transmitter_turn_up_active.label, endcap_door_west_handle_active.label, "v")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        ## Signal Row Affinities
        aff = uc.AffinityRule(row_signal_positive_start_inactive.label,
                              signal_transmitter_turn_up_inactive.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(row_signal_positive_start_inactive.label,
                              signal_transmitter_turn_up_active.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(row_signal_positive_start_waiting.label,
                              signal_transmitter_turn_up_active.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(row_signal_positive_inactive.label,
                              row_signal_positive_start_inactive.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(row_signal_positive_inactive.label,
                              row_signal_positive_start_waiting.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(row_signal_positive_waiting.label,
                              row_signal_positive_start_waiting.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(row_signal_positive_waiting.label,
                              row_signal_positive_waiting.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(signal_transmitter_turn_down_inactive.label,
                              row_signal_positive_waiting.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(signal_transmitter_turn_down_active.label,
                              row_signal_positive_full_accept.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        ### Transitions with row_signal
        tr = uc.TransitionRule(signal_transmitter_turn_down_inactive.label, row_signal_positive_full_accept.label,
                               signal_transmitter_turn_down_active.label, row_signal_positive_full_accept.label, "h")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        tr = uc.TransitionRule(row_signal_positive_start_inactive.label, signal_transmitter_turn_up_active.label, row_signal_positive_start_waiting.label, signal_transmitter_turn_up_active.label, "h")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        tr = uc.TransitionRule(row_signal_positive_inactive.label, row_signal_positive_start_waiting.label,
                               row_signal_positive_waiting.label, row_signal_positive_start_waiting.label, "h")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        tr = uc.TransitionRule(row_signal_positive_inactive.label, row_signal_positive_waiting.label,
                               row_signal_positive_waiting.label, row_signal_positive_waiting.label, "h")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        ## End Signal Arc

        ### Start Eqality Signal Arc Interaction

        #Vertical Affinities between equality signal and equality tiles
        aff = uc.AffinityRule(row_signal_positive_start_inactive.label,
                              check_equal_S_end_state_inactive.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(row_signal_positive_start_waiting.label,
                              check_equal_S_end_state.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(row_signal_positive_start_inactive.label, check_equal_S_end_state.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)



        aff = uc.AffinityRule(row_signal_positive_waiting.label,
                              check_equal_S_any_num_state_inactive.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(row_signal_positive_waiting.label,
                              check_equal_S_any_num_state.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(row_signal_positive_waiting.label,
                              check_equal_S_NorthPrefix_inactive.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(row_signal_positive_waiting.label, check_equal_S_NorthPrefix.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)


        ### Transitions with equality signal
        tr = uc.TransitionRule(row_signal_positive_waiting.label, check_equal_S_any_num_state_inactive.label,
                               row_signal_positive_waiting.label, check_equal_S_any_num_state.label, "v")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        tr = uc.TransitionRule(row_signal_positive_waiting.label, check_equal_S_start_state_inactive.label,
                               row_signal_positive_waiting.label, check_equal_S_start_state.label, "v")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        tr = uc.TransitionRule(row_signal_positive_start_waiting.label, check_equal_S_end_state_inactive.label,
                               row_signal_positive_start_waiting.label, check_equal_S_end_state.label, "v")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        tr = uc.TransitionRule(row_signal_positive_waiting.label, check_equal_S_NorthPrefix_inactive.label,
                               row_signal_positive_waiting.label, check_equal_S_NorthPrefix.label, "v")
        endcap_equality_gadget_sys.addTransitionRule(tr)

    ### End Equality Signal Arc Interaction
        ### Equality Tiles Test Data String
        aff = uc.AffinityRule(confirm_equal_S_end_state.label, end_state.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        tr = uc.TransitionRule(check_equal_S_end_state.label, end_state.label,
                               confirm_equal_S_end_state.label, end_state.label, "v")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        aff = uc.AffinityRule(row_signal_positive_start_waiting.label, confirm_equal_S_end_state.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(row_signal_positive_full_accept.label, confirm_equal_S_end_state.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        tr = uc.TransitionRule(row_signal_positive_start_waiting.label, confirm_equal_S_end_state.label,
                               row_signal_positive_full_accept.label, confirm_equal_S_end_state.label, "v")
        endcap_equality_gadget_sys.addTransitionRule(tr)



        ### Equality Tiles Any Number Equality

        aff = uc.AffinityRule(check_equal_S_any_num_state.label, ds_0.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(check_equal_S_any_num_state.label, ds_1.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(check_equal_S_any_num_state.label, ds_2.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(check_equal_S_any_num_state.label, ds_3.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(check_equal_S_any_num_state.label, ds_4.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(check_equal_S_any_num_state.label, ds_5.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(check_equal_S_any_num_state.label, ds_6.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(check_equal_S_any_num_state.label, ds_7.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(check_equal_S_any_num_state.label, ds_8.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(check_equal_S_any_num_state.label, ds_9.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        ### Added Prefix Equality
        aff = uc.AffinityRule(check_equal_S_NorthPrefix_inactive.label, north_prefix.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(check_equal_S_NorthPrefix.label, north_prefix.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)



        ### Confirm Equality Aff with Data String
        aff = uc.AffinityRule(confirm_equal_S_any_state.label, ds_0.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(confirm_equal_S_any_state.label, ds_1.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(confirm_equal_S_any_state.label, ds_2.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(confirm_equal_S_any_state.label, ds_3.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(confirm_equal_S_any_state.label, ds_4.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(confirm_equal_S_any_state.label, ds_5.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(confirm_equal_S_any_state.label, ds_6.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(confirm_equal_S_any_state.label, ds_7.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(confirm_equal_S_any_state.label, ds_8.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(confirm_equal_S_any_state.label, ds_9.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(confirm_equal_S_prefixN_state.label, north_prefix.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)


        ### Equality Tiles Start State Check Equality
        aff = uc.AffinityRule(check_equal_S_start_state.label, start_state.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = uc.AffinityRule(confirm_equal_S_start_state.label, start_state.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        tr = uc.TransitionRule(check_equal_S_start_state.label, start_state.label,
                               confirm_equal_S_start_state.label, start_state.label, "v")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        tr = uc.TransitionRule(row_signal_positive_waiting.label, confirm_equal_S_start_state.label,
                               row_signal_intermediate_accept.label, confirm_equal_S_start_state.label, "v")
        endcap_equality_gadget_sys.addTransitionRule(tr)



        ### North Prefix Equality
        tr = uc.TransitionRule(check_equal_S_NorthPrefix.label, north_prefix.label,
                               confirm_equal_S_prefixN_state.label, north_prefix.label, "v")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        tr = uc.TransitionRule(row_signal_positive_waiting.label, check_equal_S_NorthPrefix.label,
                               row_signal_intermediate_accept.label, confirm_equal_S_prefixN_state.label, "v")
        endcap_equality_gadget_sys.addTransitionRule(tr)


        ### Equality Tiles Transitions with Data String
        for i in data_states_list_nums_only:
            tr = uc.TransitionRule(check_equal_S_any_num_state.label,
                                   i.label, confirm_equal_S_any_state.label, i.label, "v")
            endcap_equality_gadget_sys.addTransitionRule(tr)





    ### End
    ### Start Data String Transitions

        print("Equality Gadget with Prefixes")


        return endcap_equality_gadget_sys


    def macrocell(self):


        pass



    def combine_affs_for_tr(self, aff1, aff2, direction):

        a1t1 = aff1.label1
        a1t2 = aff1.label2
        a2t1 = aff2.label1
        a2t2 = aff2.label2
        tr = uc.TransitionRule(a1t1, a1t2, a2t1, a2t2, direction)
        return tr

    def test_rotate(self):
        r_check_equal_S_start_state_inactive = uc.State("IN_Check=S(Inactive", grey_pink, "↧=₍")
        aff = uc.AffinityRule(check_equal_S_start_state_inactive.label, ds_0.label, "v", 1)
        tempSys = uc.System(1, [r_check_equal_S_start_state_inactive, ds_0], [r_check_equal_S_start_state_inactive, ds_0], [r_check_equal_S_start_state_inactive], [], [], [], [], [], [])
        tempSys.addAffinity(aff)





        return tempSys



class IU_Gadget_Generator:
    all_gadgets = []

    def __init__(self, name):
        self.seed_states = []
        self.seed_tiles = []
        self.test_data_list = []
        self.seed_assembly = None
        self.genSys = None

    def generateSeedAssembly(self):
        tile_list = []
        tr0 = []
        tr1 = []
        tr2 = []
        tr3 = []
        for i in range(0, 15):
            ## Row 0 22 ## Compromised of 5 west wire tiles, 1 locked door, 5 west wire tiles, 1 endcap door, 5 west wire tiles, test data
            if i < 5:
                r0t = uc.Tile(westWire.label, i, 0)
                tr0.append(r0t)
                temp_br_tile_r1 = uc.Tile(border_state.label, i, 1)
                tr1.append(temp_br_tile_r1)
                temp_br_tile_r2 = uc.Tile(border_state.label, i, 2)
                tr2.append(temp_br_tile_r2)

            elif i == 5:
                r0t = uc.Tile(signal_door_inactive.label, i, 0)
                tr0.append(r0t)
                r1t = uc.Tile(signal_door_handle_inactive.label, i, 1)
                tr1.append(r1t)
                r2t = uc.Tile(signal_transmitter_turn_down_inactive.label, i, 2)
                tr2.append(r2t)

            elif i > 5 and i < 11:
                r0t = uc.Tile(westWire.label, i, 0)
                tr0.append(r0t)
                if i == 6:
                    r1t = uc.Tile(check_equal_S_start_state_inactive.label, i, 1)
                    tr1.append(r1t)
                elif i > 6 and i < 10:
                    r1t = uc.Tile(check_equal_S_any_num_state_inactive.label, i, 1)
                    tr1.append(r1t)
                elif i == 10:
                    r1t = uc.Tile(check_equal_S_end_state_inactive.label, i, 1)
                    tr1.append(r1t)
                r2t = uc.Tile(row_signal_positive_inactive.label, i, 2)
                tr2.append(r2t)
            ## Row 1 ## 5 Border, 1 key accept, 5 check in active eq states, 1 startcheck, 5 border

            ## Row 2 ## 5 Border, 1 copy signal transmitter turn down, 5 check wait, 1 start check extender


            ## Row 3 ## 14 Border
            temp_br_tile = uc.Tile(border_state.label, i, 3)
            tr3.append(temp_br_tile)


    def generateSystem(self):
        pass

    def createEqualityCheck(self):
        pass

    def createWire(self):
        pass

# Wire Gadget Generator

class MultiGadgetGenerator:
    def __init__(self, name="Unnamed"):
        self.name = name
        self.gadget_list = []
        self.gadget_list.append(IU_Gadget_Generator())

    def generateGadgets(self):
        for gadget in self.gadget_list:
            gadget.generateSeedAssembly()
            gadget.generateSystem()

    def createGadgets(self):
        pass

    def addWireGadget(self):
        pass

    def appendWireToAssembly(self):
        pass

class Gadget:
    def __init__(self, name="Unnamed", description="No Description", parent_gadget=None):
        self.name = name
        self.description = description
        self.parent_gadget = parent_gadget
        self.up_most = 0
        self.down_most = 0
        self.right_most = 0
        self.left_most = 0

    def generateGadget(self):
        for gadget in self.gadget_list:
            gadget.generateSeedAssembly()
            gadget.generateSystem()

    def createGadget(self):
        pass

    def updateGadget(self):
        pass

    def notifyParent(self):
        pass

    def returnCurrentConfiguration(self):
        pass

# List of all states
## Make a door that activates when open state is detected and locks when closed state is detected
# What do I need to do for eq gadget?
## 1. Create a list of all states
### Border
border_state = uc.State("Border", outer_space_crayola, " ")

### Wires
northWire = uc.State("NorthWire", Blue_Sapphire, "🡹")
southWire = uc.State("SouthWire", Blue_Sapphire, "🡻")
westWire = uc.State("WestWire", Blue_Sapphire, "🡸")
eastWire = uc.State("EastWire", Blue_Sapphire, "🡺")

northCopyWire = uc.State("NorthCopyWire", light_blue, "⇈")
southCopyWire = uc.State("SouthCopyWire", light_blue, "⇊")
westCopyWire = uc.State("WestCopyWire", light_blue, "⇇")
eastCopyWire = uc.State("EastCopyWire", light_blue, "⇉")

wireWriterSouth_Inactive = uc.State("WireWriterSouth_Inactive5", Air_Superiority_Blue, "5🡻ⁱ")
wireWriterSouth = uc.State("WireWriterSouth5", Air_Superiority_Blue, "5🡻")
wireWriterSouth4 = uc.State("WireWriterSouth4", Air_Superiority_Blue, "4🡻")
wireWriterSouth3 = uc.State("WireWriterSouth3", Air_Superiority_Blue, "3🡻")
wireWriterSouth2 = uc.State("WireWriterSouth2", Air_Superiority_Blue, "2🡻")
wireWriterSouth1 = uc.State("WireWriterSouth1", Air_Superiority_Blue, "1🡻")
wireWriterSouth0 = uc.State("WireWriterSouth0", Air_Superiority_Blue, "0🡻")


### Check Equality
check_equal_S_start_state = uc.State("Check=S(", mid_pink, "↧=₍")
check_equal_S_end_state = uc.State("Check=S)", mid_pink, "↧=₎")
check_equal_S_any_num_state = uc.State("Check=S*", mid_pink, "↧=*")
check_equal_S_NorthPrefix = uc.State("Check=S_NorthPrefix", mid_pink, "↧=N")

check_equal_S_start_state_inactive = uc.State("IN_Check=S(Inactive", grey_pink, "↧=₍")
check_equal_S_end_state_inactive = uc.State("Check=S)Inactive", grey_pink, "↧=₎")
check_equal_S_any_num_state_inactive = uc.State("IN_Check=S*Inactive", grey_pink, "↧=*")
check_equal_S_NorthPrefix_inactive = uc.State("Check=S_NorthPrefix_Inactive", grey_pink, "↧=N")

confirm_equal_S_start_state = uc.State("(=S(", mid_pink, "↧₍=₍")
confirm_equal_S_end_state = uc.State(")=S)", mid_pink, "↧₎=₎")
confirm_equal_S_any_state = uc.State("*=S*", mid_pink, "↧*=*")
confirm_equal_S_any_0_state = uc.State("0=S*", mid_pink, "↧0=*")
confirm_equal_S_any_1_state = uc.State("1=S*", mid_pink, "↧1=*")
confirm_equal_S_any_2_state = uc.State("2=S*", mid_pink, "↧2=*")
confirm_equal_S_any_3_state = uc.State("3=S*", mid_pink, "↧3=*")
confirm_equal_S_any_4_state = uc.State("4=S*", mid_pink, "↧4=*")
confirm_equal_S_any_5_state = uc.State("5=S*", mid_pink, "↧5=*")
confirm_equal_S_any_6_state = uc.State("6=S*", mid_pink, "↧6=*")
confirm_equal_S_any_7_state = uc.State("7=S*", mid_pink, "↧7=*")
confirm_equal_S_any_8_state = uc.State("8=S*", mid_pink, "↧8=*")
confirm_equal_S_any_9_state = uc.State("9=S*", mid_pink, "↧9=*")
confirm_equal_S_prefixN_state = uc.State("N=SP", mid_pink, "↧N=N")

### Doors
endcap_door_west_inactive = uc.State("EndcapDoorWestInactive", grey, "◨")
endcap_door_west_handle_inactive = uc.State("EndCapDoorHandleWestInactive", grey, "◨🔒")
endcap_door_west_active = uc.State("EndcapDoorWestActive", persian_green, "◨")
endcap_door_west_handle_active = uc.State("EndCapDoorHandleWestActive", persian_green, "◨🔓")
endcap_door_west_stop = uc.State("EndcapDoorWestStop", Venetian_Red, "◨")
endcap_door_west_handle_stop = uc.State("EndCapDoorWestHandleStop", Venetian_Red, "◨🔒")
endcap_door_west_reset = uc.State("EndcapDoorWestReset", mango_tango, "↺◨")
endcap_door_west_handle_reset = uc.State("EndCapDoorHandleWestReset", mango_tango, "↺◨🔒")
endcap_door_west_handle_reset_waiting = uc.State("EndCapDoorHandleWestResetWaiting", mango_tango, "↺⏱◨🔒")
endcap_door_west_reset_waiting = uc.State("EndcapDoorWestResetWaiting", mango_tango, "↺⏱◨")

signal_door_inactive = uc.State("LockedSignalDoorInactive", grey, "🔒▦")
signal_door_handle_inactive = uc.State("LockedSignalDoorHandleInactive", grey, "🗝")
signal_door_handle_reset = uc.State("SignalDoorHandleReset", mango_tango, "↺🗝")
signal_door_open = uc.State("SignalDoorOpen", persian_green, "🔓▦")
signal_door_handle_open = uc.State("SignalDoorHandleOpen", persian_green, "🗝")

signal_door_propped_open = uc.State("SignalDoorProppedOpen", persian_green, "🔓")
signal_door_reset = uc.State("SignalDoorReset", mango_tango, "↺▦")
signal_door_reset_walk = uc.State("SignalDoorResetWalk", mango_tango, "↺▦◃")
signal_door_send_confirmed_transmission = uc.State("SignalDoorSendConfirmedTransmission", mango_tango, "▦⇉✅")
reset_confirmed_transmission_westWire = uc.State("ResetConfirmedTransmissionWest", mango_tango, "↺✅⇉")


### Signal Checks
closed_endcap_door_check_signal = uc.State("ClosedEndcapDoorCheckSignal", grey, "✔")
closed_endcap_door_check_signal_inactive = uc.State("ClosedEndcapDoorCheckSignalInactive", grey, "❌")

signal_transmitter_turn_down_inactive = uc.State("SignalTransmitterTurnDownInactive", grey, "⮮")
signal_transmitter_turn_down_active = uc.State("SignalTransmitterTurnDownActive", persian_green, "⮮")
signal_transmitter_turn_down_open = uc.State("SignalTransmitterTurnDownOpen", persian_green, "⮮")
signal_transmitter_turn_down_reset = uc.State("SignalTransmitterTurnDownReset", mango_tango, "↺⮮")

signal_transmitter_turn_up_inactive = uc.State("SignalTransmitterTurnUpInactive", grey, "⮲")
signal_transmitter_turn_up_active = uc.State("SignalTransmitterTurnUpActive", persian_green, "⮲")
signal_transmitter_turn_up_reset = uc.State("SignalTransmitterTurnUpReset", mango_tango, "↺⮲")

row_signal_positive_inactive = uc.State("RowSignalPositiveInactive", grey, "⊝")

row_signal_positive_start_inactive = uc.State("RowSignalPositiveStartInactive", green_yellow_crayola, "⊝")

row_signal_positive_start_waiting = uc.State("RowSignalPositiveStartWaiting", green_yellow_crayola, "⊝⏱")

row_signal_positive_waiting = uc.State("RowSignalPositiveWaiting", green_yellow_crayola, "⏱")
row_signal_positive_full_accept = uc.State("RowSignalPositiveFullAccept", Viridian_Green, "✅")
row_signal_intermediate_accept = uc.State("RowSignalPositiveInterimAccept", pistachio, "✔")
row_signal_positive_reset = uc.State("RowSignalPositiveReset", mango_tango, "↺")




### Check For Prefixes
check_equality_inactive = uc.State("CheckEqualityInactive", grey_pink, "=")
check_for_any_prefix_inactive = uc.State("CheckForAnyPrefix", grey_pink, "=*ₚ")
check_for_N_prefix_inactive = uc.State("CheckForNPrefixInactive", grey_pink, "=Nₚ")
check_for_S_prefix_inactive = uc.State("CheckForSPrefixInactive", grey_pink, "=Sₚ")
check_for_E_prefix_inactive = uc.State("CheckForEPrefixInactive", grey_pink, "=Eₚ")
check_for_W_prefix_inactive = uc.State("CheckForWPrefixInactive", grey_pink, "=Wₚ")
check_for_P_prefix_inactive = uc.State("CheckForProgramPrefixInactive", grey_pink, "=Pₚ")
check_for_C_prefix_inactive = uc.State("CheckForCustomPrefixInactive", grey_pink, "=Cₚ")

check_for_any_prefix = uc.State("CheckForAnyPrefix", mid_pink, "=*ₚ")
check_for_N_prefix = uc.State("CheckForNPrefix", mid_pink, "=Nₚ")
check_for_S_prefix = uc.State("CheckForSPrefix", mid_pink, "=Sₚ")
check_for_E_prefix = uc.State("CheckForEPrefix", mid_pink, "=Eₚ")
check_for_W_prefix = uc.State("CheckForWPrefix", mid_pink, "=Wₚ")
check_for_P_prefix = uc.State("CheckForProgramPrefix", mid_pink, "=Pₚ")
check_for_C_prefix = uc.State("CheckForCustomPrefix", mid_pink, "=Cₚ")

confirm_equal_any_prefix = uc.State("ConfirmEqualAnyPrefix", tea_green, "=*ₚ")
confirm_equal_N_prefix = uc.State("ConfirmEqualNPrefix", tea_green, "=Nₚ")
confirm_equal_S_prefix = uc.State("ConfirmEqualSPrefix", tea_green, "=Sₚ")
confirm_equal_E_prefix = uc.State("ConfirmEqualEPrefix", tea_green, "=Eₚ")
confirm_equal_W_prefix = uc.State("ConfirmEqualWPrefix", tea_green, "=Wₚ")
confirm_equal_C_prefix = uc.State("ConfirmEqualCustomPrefix", tea_green, "=Cₚ")
confirm_equal_P_prefix = uc.State("ConfirmEqualProgramPrefix", tea_green, "=Pₚ")

### Check For Caps
confirm_for_any_cap = uc.State("ConfirmForAnyCap", tea_green, "=*₍₎")
confirm_for_any_start_cap = uc.State("ConfirmForStartCap", tea_green, "=*ᵦ₍")
confirm_for_any_end_cap = uc.State("ConfirmForEndCap", tea_green, "=*ₔ₎")
confirm_for_start_state_cap = uc.State("ConfirmForStartStateCap", tea_green, "=(ᵦ")
confirm_for_end_state_cap = uc.State("ConfirmForEndStateCap", tea_green, "=)ₔ")
confirm_for_end_string_cap = uc.State("ConfirmForEndStringCap", tea_green, "=]ₔ")
confirm_for_start_string_cap = uc.State("ConfirmForStartStringCap", tea_green, "=[ᵦ")

check_for_any_cap = uc.State("CheckForAnyCap", mid_pink, "=*₍₎")
check_for_any_start_cap = uc.State("CheckForStartCap", mid_pink, "=*ᵦ₍")
check_for_any_end_cap = uc.State("CheckForEndCap", mid_pink, "=*ₔ₎")
check_for_start_state_cap = uc.State("CheckForStartStateCap", mid_pink, "=(ᵦ")
check_for_end_state_cap = uc.State("CheckForEndStateCap", mid_pink, "=)ₔ")
check_for_end_string_cap = uc.State("CheckForEndStringCap", mid_pink, "=]ₔ")
check_for_start_string_cap = uc.State("CheckForStartStringCap", mid_pink, "=[ᵦ")

check_for_any_cap_inactive = uc.State("CheckForAnyCapInactive", grey_pink, "=*₍₎")
check_for_any_start_cap_inactive = uc.State("CheckForStartCapInactive", grey_pink, "=*ᵦ₍")
check_for_any_end_cap_inactive = uc.State("CheckForEndCapInactive", grey_pink, "=*ₔ₎")
check_for_start_state_cap_inactive = uc.State("CheckForStartStateCapInactive", grey_pink, "=(ᵦ")
check_for_end_state_cap_inactive = uc.State("CheckForEndStateCapInactive", grey_pink, "=)ₔ")
check_for_start_string_cap_inactive = uc.State("CheckForStartStringCapInactive", grey_pink, "=[ᵦ")
check_for_end_string_cap_inactive = uc.State("CheckForEndStringCapInactive", grey_pink, "=]ₔ")

### Check For Num Equality
confirm_for_any_num = uc.State("ConfirmForEqualityAnyNum", tea_green, "=*")
confirm_for_equality_zero = uc.State("ConfirmForEqualityZero", tea_green, "=0")
confirm_for_equality_one = uc.State("ConfirmForEqualityOne", tea_green, "=1")
confirm_for_equality_two = uc.State("ConfirmForEqualityTwo", tea_green, "=2")
confirm_for_equality_three = uc.State("ConfirmForEqualityThree", tea_green, "=3")
confirm_for_equality_four = uc.State("ConfirmForEqualityFour", tea_green, "=4")
confirm_for_equality_five = uc.State("ConfirmForEqualityFive", tea_green, "=5")
confirm_for_equality_six = uc.State("ConfirmEqualityForSix", tea_green, "=6")
confirm_for_equality_seven = uc.State("ConfirmForEqualitySeven", tea_green, "=7")
confirm_for_equality_eight = uc.State("ConfirmForEqualityEight", tea_green, "=8")
confirm_for_equality_nine = uc.State("ConfirmForEqualityNine", tea_green, "=9")

check_for_any_num = uc.State("CheckForEqualityAnyNum", mid_pink, "=*")
check_for_equality_zero = uc.State("CheckForEqualityZero", mid_pink, "=0")
check_for_equality_one = uc.State("CheckForEqualityOne", mid_pink, "=1")
check_for_equality_two = uc.State("CheckForEqualityTwo", mid_pink, "=2")
check_for_equality_three = uc.State("CheckForEqualityThree", mid_pink, "=3")
check_for_equality_four = uc.State("CheckForEqualityFour", mid_pink, "=4")
check_for_equality_five = uc.State("CheckForEqualityFive", mid_pink, "=5")
check_for_equality_six = uc.State("CheckEqualityForSix", mid_pink, "=6")
check_for_equality_seven = uc.State("CheckForEqualitySeven", mid_pink, "=7")
check_for_equality_eight = uc.State("CheckForEqualityEight", mid_pink, "=8")
check_for_equality_nine = uc.State("CheckForEqualityNine", mid_pink, "=9")

check_for_any_num_inactive = uc.State("CheckForEqualityAnyNum_Inactive", grey_pink, "=*")
check_for_equality_zero_inactive = uc.State("CheckForEqualityZero_Inactive", grey_pink, "=0")
check_for_equality_one_inactive = uc.State("CheckForEqualityOne_Inactive", grey_pink, "=1")
check_for_equality_two_inactive = uc.State("CheckForEqualityTwo_Inactive", grey_pink, "=2")
check_for_equality_three_inactive = uc.State("CheckForEqualityThree_Inactive", grey_pink, "=3")
check_for_equality_four_inactive = uc.State("CheckForEqualityFour_Inactive", grey_pink, "=4")
check_for_equality_five_inactive = uc.State("CheckForEqualityFive_Inactive", grey_pink, "=5")
check_for_equality_six_inactive = uc.State("CheckEqualityForSix_Inactive", grey_pink, "=6")
check_for_equality_seven_inactive = uc.State("CheckForEqualitySeven_Inactive", grey_pink, "=7")
check_for_equality_eight_inactive = uc.State("CheckForEqualityEight_Inactive", grey_pink, "=8")
check_for_equality_nine_inactive = uc.State("CheckForEqualityNine_Inactive", grey_pink, "=9")

### Trap Doors
trap_door_inactive = uc.State("TrapDoorInactive", Barn_Red, "TD")
### Data States
ds_1 = uc.State("1", Papaya_Whip, "①")
ds_2 = uc.State("2", Papaya_Whip, "②")
ds_3 = uc.State("3", Papaya_Whip, "③")
ds_4 = uc.State("4", Papaya_Whip, "④")
ds_5 = uc.State("5", Papaya_Whip, "⑤")
ds_6 = uc.State("6", Papaya_Whip, "⑥")
ds_7 = uc.State("7", Papaya_Whip, "⑦")
ds_8 = uc.State("8", Papaya_Whip, "⑧")
ds_9 = uc.State("9", Papaya_Whip, "⑨")
ds_0 = uc.State("0", Papaya_Whip, "⓪")
data_states_list_nums_only = [ds_0, ds_1, ds_2, ds_3, ds_4, ds_5, ds_6, ds_7, ds_8, ds_9]

start_state = uc.State("EndcapDSOpen", Papaya_Whip, "(")
end_state = uc.State("EndcapDSClosed", Papaya_Whip, ")")
data_states_list_all = [start_state] + data_states_list_nums_only + [end_state]

north_prefix = uc.State("NorthPrefix", Papaya_Whip, "𝗡")
south_prefix = uc.State("SouthPrefix", Papaya_Whip, "𝗦")
east_prefix = uc.State("EastPrefix", Papaya_Whip, "𝗘")
west_prefix = uc.State("WestPrefix", Papaya_Whip, "𝗪")
program_prefix = uc.State("ProgramPrefix", Papaya_Whip, "</>")
reset_prefix = uc.State("ResetPrefix", Papaya_Whip, "⭯")

data_states_list_prefixes = [north_prefix, south_prefix, east_prefix, west_prefix, program_prefix, reset_prefix]
data_states_list_all_with_prefixes_no_order = data_states_list_prefixes + data_states_list_all
data_states_list_all_with_north_prefixes = [north_prefix] + data_states_list_all
#data_state = uc.State("1", Papaya_Whip, "1")
## Reprograamming Equality Gadget by sending a reset start cap then a data string and flip the equlities
reprogram_verifier_eq_gadget = uc.State("ReprogramEqGadgetVerifier", Papaya_Whip, "")
### Transition Rules
#transition = uc.TransitionRule("WestWire", ds.label, ds.label, "WestWire", "h")


## 2. Make a wire load as seed assembly
## 3. Make a door that activates when open state is detected and locks when closed state is detected
## Various Symbols ⚿⚾⚽⚰⚱⚲⚳⚴⚵⚶⚷⚸⚹⚺⚻⚼⚽⚾⛀⛁⛂⛃⛄⛅⛆⛇⛈⛉⛊⛋⛌⛍⛎⛏⛐⛑⛒⛓⛔⛕⛖⛗⛘⛙⛚⛛⛜⛝⛞⛟⛠⛡⛢⛣⛤⛥⛦⛧⛨⛩⛪⛫⛬⛭⛮⛯⛰⛱⛲⛳⛴⛵⛶⛷⛸⛹⛺⛻⛼⛽⛾⛿✀✁✂✃✄✅✆✇✈✉✊✋✌✍✎✏✐✑✒✔✕✖✗✘✙✚✛✜✝✞✟✠✡✢✣✤✥✦✧✨✩✪✫✬✭✮✯✰✱✲✳✴✵✶✷✸✹✺✻✼✽✾✿❀❁❂❃❄❅❆❇❈❉❊❋❌❍❎❏❐❑❒❓❔❕❖❗❘❙❚❛❜❝❞❟❠❡❢❣❤❥❦❧❨❩❪❫❬❭❮❯❰❱❲❳❴❵❶❷❸❹❺❻❼❽❾❿➀🔏⊟
#🯰🯱🯲🯳🯴🯵🯶🯷🯸🯹🢀🢁🢂🢃🞴🞺🙹🆗🆔𝗡𝗘𝗦𝗪﹝﹞﹪﹦﹜﹛︽︾︹︺︵︶﹟﹢﹣﹙﹚︷︸︵︶﹇﹈《》〔〕〚〛〓⹗⹘⩐⨷⨸⨶⨹⨺⨻⨀⨁⨂⧪⧬⧮⧰⧯⧱⧧⧟⧞⧛⧚⧙⧘⧗⧖⧈⧉⧊⧆⦍⦎⦏⦐⦛⦜⧃⦴⦳⦲⦱⦰⦷⥿⥾⥽⥼⥱⥲⥴⥵⥶⥸⥹⥮⥯

#Other stuff
##Colors
## Various Symbols
# Circled Equals: ⊜
# Subscripted Equals: ₌ (U+208C)
# Questioned Equals: ≟ (U+225F)

# Equals with Asterisk: ⩮ (U+2A6E)
"""
Arrows
    East: 🡺, ⮚
    West: 🡸, ⮘
    North: 🡹, ⮙, ⥉
    South: 🡻, ⮛
    Curved: ⮮, ⮯, ⮰, ⮱

"""
