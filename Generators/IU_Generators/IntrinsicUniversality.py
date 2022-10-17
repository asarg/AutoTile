import UniversalClasses as uc
from UniversalClasses import State, TransitionRule, AffinityRule, System, Tile, Assembly
from Assets.colors import *
import sys


class IUSystem:
    unit_states = []
    unit_vertical_affinities = {}
    unit_horizontal_affinities = {}
    unit_vertical_transitions = {}
    unit_horizontal_transitions = {}
    all_gadgets = []

    def __init__(self):
        self.source_system = None
        self.states = []
        self.initial_states = []
        self.seed_states = []
        self.unit_vertical_affinities = {}
        self.unit_horizontal_affinities = {}

    def add_unit_state(self, state):
        self.states.append(state)
        self.unit_states.append(state)

    def add_unit_transition(self, transition):
        if transition.dir == 'h':
            self.add_unit_horizontal_transition(transition)
        else:
            self.add_unit_vertical_transition(transition)
    def add_unit_affinity(self, affinity):
        if affinity.dir == 'h':
            self.add_unit_horizontal_affinity(affinity)
        else:
            self.add_unit_vertical_affinity(affinity)

    def add_unit_vertical_affinity(self, affinity):
        self.unit_vertical_affinities[(affinity.state1, affinity.state2)] = affinity.strength

    def add_unit_horizontal_affinity(self, affinity):
        self.unit_horizontal_affinities[(affinity.state1, affinity.state2)] = affinity.strength

    def add_unit_vertical_transition(self, transition):
        self.unit_vertical_transitions[(transition.state1, transition.state2)] = transition

    def add_unit_horizontal_transition(self, transition):
        self.unit_horizontal_transitions[(transition.state1, transition.state2)] = transition

class MacroCell:
    def __init__(self, v_aff=False, h_aff=False):
        self.states_used = []
        self.initial_states_used = []
        self.seed_states_used = []
        self.vertical_affinity_status = v_aff
        self.horizontal_affinity_status = h_aff








class DataString:  # Takes in a list of data objects and
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
        self.example_states_data = [start_state, ds_1, ds_2, ds_3, end_state]
        self.aff_list = []

    def basicWireSeedAssembly(self):
        seed_states = [westWire]
        seed_tiles = []
        for i in self.example_states_data:
            seed_states.append(i)

        for i in range(4):
            temp_tile = Tile(westWire, i, 0)
            seed_tiles.append(temp_tile)

        c = 4
        for i in self.example_states_data:
            temp_tile = Tile(i, c, 0)
            seed_tiles.append(temp_tile)
            c = c + 1

        asb = Assembly()
        asb.setTiles(seed_tiles)
        return asb, seed_states, seed_tiles

    def basicWireGenerator(self):
        asb, seed_states, seed_tiles = self.basicWireSeedAssembly()

        #System takes in temp, states, initial states, seed states, vertical_affinitys, horizontal_affinitys, vert transitions, horiz transitions, tile vertical transitions, tile horizontal transitions, seed assembly
        self.genSys = System(
            1, seed_states, [], seed_states,  [], [], [], [], [], [], asb)

        for i in self.example_states_data:
            aff = AffinityRule(westWire.label, i.label, "h", 1)
            self.all_aff.append(aff)
            self.genSys.addAffinity(aff)
            aff = AffinityRule(i.label, westWire.label, "h", 1)
            self.genSys.addAffinity(aff)
            self.all_aff.append(aff)
            tr = TransitionRule(westWire.label, i.label, i.label, westWire.label, "h")
            self.genSys.addTransitionRule(tr)
            self.all_tr.append(tr)

        aff = AffinityRule(westWire.label, westWire.label, "h", 1)
        self.genSys.addAffinity(aff)
        self.all_aff.append(aff)
        self.all_sys["basicWire"] = self.genSys

        return self.genSys

    def wireGeneratorWithEndcapDoorNoSignalGadget(self):

        wire_sys = self.basicWireGenerator()
        end_cap_asb = wire_sys.returnSeedAssembly()
        endcap_door_tile = Tile(endcap_door_west_inactive, -1, 0)
        ec_seed_tiles = [endcap_door_tile]
        for i in range(-2, -7, -1):
            temp_tile = Tile(westWire, i, 0)
            ec_seed_tiles.append(temp_tile)

        endcap_seed_states = [endcap_door_west_inactive]

        end_cap_asb.setTiles(ec_seed_tiles)
        endcap_states = [endcap_door_west_inactive, endcap_door_west_active,
                         endcap_door_west_stop] + wire_sys.returnStates()
        endcap_all_seed_states = endcap_seed_states + wire_sys.returnSeedStates()
        horizontal_transitions = wire_sys.returnHorizontalTransitionList()
        horizontal_affinities = wire_sys.returnHorizontalAffinityList()
        endcap_genSys = System(1, endcap_states, [], endcap_all_seed_states, [
        ], horizontal_affinities, [], horizontal_transitions, [], [], end_cap_asb)
        endcap_genSys.addAffinity(AffinityRule(
            endcap_door_west_inactive.label, westWire.label, "h", 1))

        endcap_genSys.addAffinity(AffinityRule(
            endcap_door_west_inactive.label, start_state.label, "h", 1))

        endcap_genSys.addAffinity(AffinityRule(
            endcap_door_west_stop.label, end_state.label, "h", 1))

        endcap_genSys.addAffinity(AffinityRule(
            endcap_door_west_stop.label, westWire.label, "h", 1))
        endcap_genSys.addAffinity(AffinityRule(
            westWire.label, endcap_door_west_stop.label, "h", 1))

        for i in self.example_states_data:
            endcap_genSys.addAffinity(AffinityRule(
                endcap_door_west_active.label, i.label, "h", 1))
            endcap_genSys.addAffinity(AffinityRule(
                i.label, endcap_door_west_active.label, "h", 1))
            if i != end_state:
                endcap_genSys.addTransitionRule(TransitionRule(
                    endcap_door_west_active.label, i.label, i.label, endcap_door_west_active.label, "h"))
            else:
                endcap_genSys.addTransitionRule(TransitionRule(
                    endcap_door_west_active.label, i.label, i.label, endcap_door_west_stop.label, "h"))

        endcap_genSys.addTransitionRule(TransitionRule(
            endcap_door_west_inactive.label, start_state.label, endcap_door_west_active.label, start_state.label, "h"))

        endcap_genSys.addTransitionRule(TransitionRule(
            westWire.label, endcap_door_west_stop.label, endcap_door_west_stop.label, westWire.label, "h"))
        self.all_sys["endCapBasic"] = endcap_genSys
        return endcap_genSys

    def wireGeneratorWithEndcapDoorSignalGadget(self):
        endcap_no_signal_sys = self.wireGeneratorWithEndcapDoorNoSignalGadget()

        endcap_gadget_seed_states = [
            endcap_door_west_handle_inactive] + endcap_no_signal_sys.returnSeedStates()
        endcap_gadget_states = [endcap_door_west_handle_inactive, endcap_door_west_handle_active,
                                endcap_door_west_handle_stop] + endcap_no_signal_sys.returnStates()
        endcap_horizontal_transitions = endcap_no_signal_sys.returnHorizontalTransitionList()
        endcap_horizontal_affinities = endcap_no_signal_sys.returnHorizontalAffinityList()
        endcap_asb = endcap_no_signal_sys.returnSeedAssembly()

        endcap_asb.setTiles(
            [Tile(endcap_door_west_handle_inactive, -1, 1)])
        #System takes in temp, states, initial states, seed states, vertical_affinitys, horizontal_affinitys, vert transitions, horiz transitions, tile vertical transitions, tile horizontal transitions, seed assembly
        endcap_signal_genSys = System(1, endcap_gadget_states, [], endcap_gadget_seed_states,  [
        ], endcap_horizontal_affinities, [], endcap_horizontal_transitions, [],  [], endcap_asb)

        endcap_signal_genSys.addAffinity(AffinityRule(
            endcap_door_west_handle_inactive.label, endcap_door_west_inactive.label, "v", 1))
        endcap_signal_genSys.addAffinity(AffinityRule(
            endcap_door_west_handle_inactive.label, endcap_door_west_active.label, "v", 1))
        endcap_signal_genSys.addAffinity(AffinityRule(
            endcap_door_west_handle_active.label, endcap_door_west_active.label, "v", 1))
        endcap_signal_genSys.addAffinity(AffinityRule(
            endcap_door_west_handle_inactive.label, endcap_door_west_stop.label, "v", 1))
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
        eq_t = Tile(signal_transmitter_turn_up_inactive, -1, 2)
        equality_gadget_seed_tiles.append(eq_t)
        for i in range(-2, -7, -1):
            if i == -2:
                r1t = Tile(check_equal_S_end_state_inactive, i, 1)
                equality_gadget_seed_tiles.append(r1t)

            elif i < -2 and i > -6:
                r1t = Tile(check_equal_S_any_num_state_inactive, i, 1)
                equality_gadget_seed_tiles.append(r1t)
            elif i == -6:
                r1t = Tile(check_equal_S_start_state_inactive, i, 1)
                equality_gadget_seed_tiles.append(r1t)

            if i == -2:
                t = Tile(row_signal_positive_start_inactive, i, 2)
                equality_gadget_seed_tiles.append(t)
            else:
                r2t = Tile(row_signal_positive_inactive, i, 2)
                equality_gadget_seed_tiles.append(r2t)

        eq_t = Tile(signal_transmitter_turn_down_inactive, -7, 2)
        equality_gadget_seed_tiles.append(eq_t)

        eq_t = Tile(signal_door_handle_inactive, -7, 1)
        equality_gadget_seed_tiles.append(eq_t)

        eq_t = Tile(signal_door_inactive, -7, 0)
        equality_gadget_seed_tiles.append(eq_t)

        eq_t = Tile(trap_door_inactive, -6, -1)
        equality_gadget_seed_tiles.append(eq_t)

        for i in range(-8, -14, -1):
            temp_tile = Tile(westWire, i, 0)
            equality_gadget_seed_tiles.append(temp_tile)

        endcap_asb.setTiles(equality_gadget_seed_tiles)
        endcap_horizontal_affinities = endcap_signal_sys.returnHorizontalAffinityList()
        endcap_vertical_affinities = endcap_signal_sys.returnVerticalAffinityList()
        endcap_horizontal_transitions = endcap_signal_sys.returnHorizontalTransitionList()
        endcap_equality_gadget_sys = System(1, equality_gadget_states, [], equality_gadget_seed_states,
                                               endcap_vertical_affinities, endcap_horizontal_affinities, [], endcap_horizontal_transitions, [], [], endcap_asb)

        ## Add -1 column affinities
        aff = AffinityRule(signal_transmitter_turn_up_inactive.label,
                              endcap_door_west_handle_inactive.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = AffinityRule(signal_transmitter_turn_up_inactive.label,
                              endcap_door_west_handle_active.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = AffinityRule(signal_transmitter_turn_up_active.label,
                              endcap_door_west_handle_active.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        ## Add -1 column transitions
        tr = TransitionRule(endcap_door_west_handle_inactive.label, endcap_door_west_stop.label,
                               endcap_door_west_handle_active.label, endcap_door_west_stop.label, "v")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        tr = TransitionRule(signal_transmitter_turn_up_inactive.label, endcap_door_west_handle_active.label,
                               signal_transmitter_turn_up_active.label, endcap_door_west_handle_active.label, "v")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        ## Signal Row Affinities
        aff = AffinityRule(row_signal_positive_start_inactive.label,
                              signal_transmitter_turn_up_inactive.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = AffinityRule(row_signal_positive_start_inactive.label,
                              signal_transmitter_turn_up_active.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = AffinityRule(row_signal_positive_start_waiting.label,
                              signal_transmitter_turn_up_active.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = AffinityRule(row_signal_positive_inactive.label,
                              row_signal_positive_start_inactive.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = AffinityRule(row_signal_positive_inactive.label,
                              row_signal_positive_start_waiting.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = AffinityRule(row_signal_positive_waiting.label,
                              row_signal_positive_start_waiting.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = AffinityRule(row_signal_positive_waiting.label,
                              row_signal_positive_waiting.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = AffinityRule(signal_transmitter_turn_down_inactive.label,
                              row_signal_positive_waiting.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = AffinityRule(signal_transmitter_turn_down_active.label,
                              row_signal_positive_full_accept.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        ### Transitions with row_signal
        tr = TransitionRule(signal_transmitter_turn_down_inactive.label, row_signal_positive_full_accept.label,
                               signal_transmitter_turn_down_active.label, row_signal_positive_full_accept.label, "h")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        tr = TransitionRule(
            row_signal_positive_start_inactive.label, signal_transmitter_turn_up_active.label, row_signal_positive_start_waiting.label, signal_transmitter_turn_up_active.label, "h")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        tr = TransitionRule(row_signal_positive_inactive.label, row_signal_positive_start_waiting.label,
                               row_signal_positive_waiting.label, row_signal_positive_start_waiting.label, "h")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        tr = TransitionRule(row_signal_positive_inactive.label, row_signal_positive_waiting.label,
                               row_signal_positive_waiting.label, row_signal_positive_waiting.label, "h")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        #Vertical Affinities between equality signal and equality tiles
        aff = AffinityRule(row_signal_positive_start_inactive.label,
                              check_equal_S_end_state_inactive.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = AffinityRule(
            row_signal_positive_start_inactive.label, check_equal_S_end_state.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = AffinityRule(row_signal_positive_waiting.label,
                              check_equal_S_any_num_state_inactive.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = AffinityRule(row_signal_positive_waiting.label,
                              check_equal_S_any_num_state.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = AffinityRule(row_signal_positive_start_waiting.label,
                              check_equal_S_end_state.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        ### Transitions with equality signal
        tr = TransitionRule(row_signal_positive_waiting.label, check_equal_S_any_num_state_inactive.label,
                               row_signal_positive_waiting.label, check_equal_S_any_num_state.label, "v")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        tr = TransitionRule(row_signal_positive_waiting.label, check_equal_S_start_state_inactive.label,
                               row_signal_positive_waiting.label, check_equal_S_start_state.label, "v")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        tr = TransitionRule(row_signal_positive_start_waiting.label, check_equal_S_end_state_inactive.label,
                               row_signal_positive_start_waiting.label, check_equal_S_end_state.label, "v")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        ### Equality Tiles Test Data String
        aff = AffinityRule(
            confirm_equal_S_end_state.label, end_state.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        tr = TransitionRule(check_equal_S_end_state.label, end_state.label,
                               confirm_equal_S_end_state.label, end_state.label, "v")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        aff = AffinityRule(
            row_signal_positive_start_waiting.label, confirm_equal_S_end_state.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = AffinityRule(
            row_signal_positive_full_accept.label, confirm_equal_S_end_state.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        tr = TransitionRule(row_signal_positive_start_waiting.label, confirm_equal_S_end_state.label,
                               row_signal_positive_full_accept.label, confirm_equal_S_end_state.label, "v")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        ### Equality Tiles Any Number Equality
        aff = AffinityRule(
            check_equal_S_any_num_state.label, ds_0.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = AffinityRule(
            check_equal_S_any_num_state.label, ds_1.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = AffinityRule(
            check_equal_S_any_num_state.label, ds_2.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = AffinityRule(
            check_equal_S_any_num_state.label, ds_3.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = AffinityRule(
            check_equal_S_any_num_state.label, ds_4.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = AffinityRule(
            check_equal_S_any_num_state.label, ds_5.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = AffinityRule(
            check_equal_S_any_num_state.label, ds_6.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = AffinityRule(
            check_equal_S_any_num_state.label, ds_7.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = AffinityRule(
            check_equal_S_any_num_state.label, ds_8.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = AffinityRule(
            check_equal_S_any_num_state.label, ds_9.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        ### Confirm Equality Aff with Data String
        aff = AffinityRule(
            confirm_equal_S_any_state.label, ds_0.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = AffinityRule(
            confirm_equal_S_any_state.label, ds_1.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = AffinityRule(
            confirm_equal_S_any_state.label, ds_2.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = AffinityRule(
            confirm_equal_S_any_state.label, ds_3.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = AffinityRule(
            confirm_equal_S_any_state.label, ds_4.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = AffinityRule(
            confirm_equal_S_any_state.label, ds_5.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = AffinityRule(
            confirm_equal_S_any_state.label, ds_6.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = AffinityRule(
            confirm_equal_S_any_state.label, ds_7.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = AffinityRule(
            confirm_equal_S_any_state.label, ds_8.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = AffinityRule(
            confirm_equal_S_any_state.label, ds_9.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        ### Equality Tiles Start State Check Equality
        aff = AffinityRule(
            check_equal_S_start_state.label, start_state.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = AffinityRule(
            confirm_equal_S_start_state.label, start_state.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        tr = TransitionRule(check_equal_S_start_state.label, start_state.label,
                               confirm_equal_S_start_state.label, start_state.label, "v")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        tr = TransitionRule(row_signal_positive_waiting.label, confirm_equal_S_start_state.label,
                               row_signal_intermediate_accept.label, confirm_equal_S_start_state.label, "v")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        ### Equality Tiles Transitions with Data String
        for i in data_states_list_nums_only:
            tr = TransitionRule(check_equal_S_any_num_state.label,
                                   i.label, confirm_equal_S_any_state.label, i.label, "v")
            endcap_equality_gadget_sys.addTransitionRule(tr)

        ### Row Signal Positive Start Waiting Affinity
        aff = AffinityRule(
            row_signal_intermediate_accept.label, confirm_equal_S_any_state.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = AffinityRule(row_signal_positive_waiting.label,
                              confirm_equal_S_any_state.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        tr = TransitionRule(row_signal_positive_waiting.label, confirm_equal_S_any_state.label,
                               row_signal_intermediate_accept.label, confirm_equal_S_any_state.label, "v")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        aff = AffinityRule(row_signal_intermediate_accept.label,
                              confirm_equal_S_start_state.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = AffinityRule(row_signal_positive_waiting.label,
                              confirm_equal_S_start_state.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        tr = TransitionRule(row_signal_positive_waiting.label, confirm_equal_S_start_state.label,
                               row_signal_intermediate_accept.label, confirm_equal_S_start_state.label, "v")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        aff = AffinityRule(row_signal_positive_waiting.label,
                              row_signal_positive_full_accept.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = AffinityRule(row_signal_intermediate_accept.label,
                              row_signal_positive_full_accept.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        tr = TransitionRule(row_signal_intermediate_accept.label, row_signal_positive_full_accept.label,
                               row_signal_positive_full_accept.label, row_signal_positive_full_accept.label, "h")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        ### If inactive meets full accept transition to waiting
        aff = AffinityRule(row_signal_positive_inactive.label,
                              row_signal_positive_full_accept.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        tr = TransitionRule(row_signal_positive_inactive.label, row_signal_positive_full_accept.label,
                               row_signal_positive_waiting.label, row_signal_positive_full_accept.label, "h")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        ### Turndown Key Affinity and Transition
        aff = AffinityRule(signal_transmitter_turn_down_active.label,
                              signal_door_handle_inactive.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = AffinityRule(
            signal_transmitter_turn_down_active.label, signal_door_handle_open.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        tr = TransitionRule(signal_transmitter_turn_down_active.label, signal_door_handle_inactive.label,
                               signal_transmitter_turn_down_active.label, signal_door_handle_open.label, "v")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        aff = AffinityRule(signal_door_handle_open.label,
                              signal_door_inactive.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = AffinityRule(signal_door_handle_open.label,
                              signal_door_open.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        tr = TransitionRule(signal_door_handle_open.label, signal_door_inactive.label,
                               signal_door_handle_open.label, signal_door_open.label, "v")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        for i in data_states_list_all:
            aff = AffinityRule(signal_door_open.label, i.label, "h", 1)
            endcap_equality_gadget_sys.addAffinity(aff)

            tr = TransitionRule(
                signal_door_open.label, i.label, i.label, signal_door_open.label, "h")
            endcap_equality_gadget_sys.addTransitionRule(tr)

        """ tr = TransitionRule(westWire.label, signal_door_open.label, i.label, signal_door_open.label, "h")
        endcap_equality_gadget_sys.addTransitionRule(tr) """

        ### Resetting the Gadget
        endcap_equality_gadget_sys.addState(endcap_door_west_reset)
        endcap_equality_gadget_sys.addState(endcap_door_west_handle_reset)
        endcap_equality_gadget_sys.addState(signal_door_reset)
        endcap_equality_gadget_sys.addState(signal_door_reset_walk)
        endcap_equality_gadget_sys.addState(endcap_door_west_reset_waiting)
        endcap_equality_gadget_sys.addState(signal_transmitter_turn_down_reset)
        endcap_equality_gadget_sys.addState(signal_transmitter_turn_up_reset)
        endcap_equality_gadget_sys.addState(
            endcap_door_west_handle_reset_waiting)
        endcap_equality_gadget_sys.addState(row_signal_positive_reset)
        endcap_equality_gadget_sys.addState(signal_door_handle_reset)
        endcap_equality_gadget_sys.addState(
            signal_door_send_confirmed_transmission)
        endcap_equality_gadget_sys.addState(
            reset_confirmed_transmission_westWire)
        endcap_equality_gadget_sys.addState(signal_door_handle_inactive)
        endcap_equality_gadget_sys.addState(signal_door_inactive)

        aff = AffinityRule(signal_door_open.label,
                              endcap_door_west_stop.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff)
        aff = AffinityRule(signal_door_reset.label,
                              endcap_door_west_reset.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        tr = TransitionRule(signal_door_open.label, endcap_door_west_stop.label,
                               signal_door_reset.label, endcap_door_west_reset.label, "h")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        aff = AffinityRule(
            endcap_door_west_handle_active.label, endcap_door_west_reset.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        aff = AffinityRule(
            endcap_door_west_handle_reset.label, endcap_door_west_reset.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff)

        tr = TransitionRule(endcap_door_west_handle_active.label, endcap_door_west_reset.label,
                               endcap_door_west_handle_reset.label, endcap_door_west_reset_waiting.label, "v")
        endcap_equality_gadget_sys.addTransitionRule(tr)

        aff1 = AffinityRule(signal_transmitter_turn_up_active.label,
                               endcap_door_west_handle_reset.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff1)

        aff2 = AffinityRule(signal_transmitter_turn_up_reset.label,
                               endcap_door_west_handle_inactive.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff2)

        endcap_equality_gadget_sys.addTransitionRule(
            self.combine_affs_for_tr(aff1, aff2, "v"))

        aff1 = AffinityRule(row_signal_positive_full_accept.label,
                               signal_transmitter_turn_up_reset.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff1)

        aff2 = AffinityRule(row_signal_positive_reset.label,
                               signal_transmitter_turn_up_inactive.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff2)

        endcap_equality_gadget_sys.addTransitionRule(
            self.combine_affs_for_tr(aff1, aff2, "h"))

        aff1 = AffinityRule(
            row_signal_positive_full_accept.label, row_signal_positive_reset.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff1)

        aff2 = AffinityRule(
            row_signal_positive_reset.label, row_signal_positive_inactive.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff2)

        endcap_equality_gadget_sys.addTransitionRule(
            self.combine_affs_for_tr(aff1, aff2, "h"))

        aff1 = AffinityRule(
            signal_transmitter_turn_down_active.label, row_signal_positive_reset.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff1)

        aff2 = AffinityRule(signal_transmitter_turn_down_reset.label,
                               row_signal_positive_inactive.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff2)

        endcap_equality_gadget_sys.addTransitionRule(
            self.combine_affs_for_tr(aff1, aff2, "h"))

        aff1 = AffinityRule(
            signal_transmitter_turn_down_reset.label, signal_door_handle_open.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff1)

        aff2 = AffinityRule(
            signal_transmitter_turn_down_inactive.label, signal_door_handle_reset.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff2)

        endcap_equality_gadget_sys.addTransitionRule(
            self.combine_affs_for_tr(aff1, aff2, "v"))

        ### Signal Door Walk Reset
        aff1 = AffinityRule(
            confirm_equal_S_end_state.label, signal_door_reset.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff1)

        aff2 = AffinityRule(
            check_equal_S_end_state_inactive.label, signal_door_reset_walk.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff2)

        endcap_equality_gadget_sys.addTransitionRule(
            self.combine_affs_for_tr(aff1, aff2, "v"))

        aff1 = AffinityRule(
            westWire.label, signal_door_reset_walk.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff1)

        aff2 = AffinityRule(signal_door_reset.label, westWire.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff2)

        endcap_equality_gadget_sys.addTransitionRule(
            self.combine_affs_for_tr(aff1, aff2, "h"))

        aff1 = AffinityRule(
            confirm_equal_S_any_state.label, signal_door_reset.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff1)

        aff2 = AffinityRule(
            check_equal_S_any_num_state_inactive.label, signal_door_reset_walk.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff2)

        endcap_equality_gadget_sys.addTransitionRule(
            self.combine_affs_for_tr(aff1, aff2, "v"))

        aff1 = AffinityRule(
            confirm_equal_S_start_state.label, signal_door_reset.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff1)

        aff2 = AffinityRule(
            check_equal_S_start_state_inactive.label, signal_door_reset_walk.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff2)

        endcap_equality_gadget_sys.addTransitionRule(
            self.combine_affs_for_tr(aff1, aff2, "v"))

        aff1 = AffinityRule(
            signal_door_handle_reset.label, signal_door_reset.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff1)

        aff2 = AffinityRule(signal_door_handle_inactive.label,
                               signal_door_send_confirmed_transmission.label, "v", 1)
        endcap_equality_gadget_sys.addAffinity(aff2)

        endcap_equality_gadget_sys.addTransitionRule(
            self.combine_affs_for_tr(aff1, aff2, "v"))

        aff1 = AffinityRule(
            signal_door_send_confirmed_transmission.label, westWire.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff1)

        aff2 = AffinityRule(signal_door_inactive.label,
                               reset_confirmed_transmission_westWire.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff2)

        endcap_equality_gadget_sys.addTransitionRule(
            self.combine_affs_for_tr(aff1, aff2, "h"))

        aff1 = AffinityRule(
            reset_confirmed_transmission_westWire.label, westWire.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff1)

        aff2 = AffinityRule(
            westWire.label, reset_confirmed_transmission_westWire.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff2)

        endcap_equality_gadget_sys.addTransitionRule(
            self.combine_affs_for_tr(aff1, aff2, "h"))

        aff1 = AffinityRule(reset_confirmed_transmission_westWire.label,
                               endcap_door_west_reset_waiting.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff1)

        aff2 = AffinityRule(
            westWire.label, endcap_door_west_inactive.label, "h", 1)
        endcap_equality_gadget_sys.addAffinity(aff2)

        endcap_equality_gadget_sys.addTransitionRule(
            self.combine_affs_for_tr(aff1, aff2, "h"))

        return endcap_equality_gadget_sys

    def combine_affs_for_tr(self, aff1, aff2, direction):

        a1t1 = aff1.label1
        a1t2 = aff1.label2
        a2t1 = aff2.label1
        a2t2 = aff2.label2
        tr = TransitionRule(a1t1, a1t2, a2t1, a2t2, direction)
        return tr


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
                r0t = Tile(westWire.label, i, 0)
                tr0.append(r0t)
                temp_br_tile_r1 = Tile(border_state.label, i, 1)
                tr1.append(temp_br_tile_r1)
                temp_br_tile_r2 = Tile(border_state.label, i, 2)
                tr2.append(temp_br_tile_r2)

            elif i == 5:
                r0t = Tile(signal_door_inactive.label, i, 0)
                tr0.append(r0t)
                r1t = Tile(signal_door_handle_inactive.label, i, 1)
                tr1.append(r1t)
                r2t = Tile(
                    signal_transmitter_turn_down_inactive.label, i, 2)
                tr2.append(r2t)

            elif i > 5 and i < 11:
                r0t = Tile(westWire.label, i, 0)
                tr0.append(r0t)
                if i == 6:
                    r1t = Tile(
                        check_equal_S_start_state_inactive.label, i, 1)
                    tr1.append(r1t)
                elif i > 6 and i < 10:
                    r1t = Tile(
                        check_equal_S_any_num_state_inactive.label, i, 1)
                    tr1.append(r1t)
                elif i == 10:
                    r1t = Tile(check_equal_S_end_state_inactive.label, i, 1)
                    tr1.append(r1t)
                r2t = Tile(row_signal_positive_inactive.label, i, 2)
                tr2.append(r2t)
            ## Row 1 ## 5 Border, 1 key accept, 5 check in active eq states, 1 startcheck, 5 border

            ## Row 2 ## 5 Border, 1 copy signal transmitter turn down, 5 check wait, 1 start check extender

            ## Row 3 ## 14 Border
            temp_br_tile = Tile(border_state.label, i, 3)
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

class WireGadget(Gadget):
    def __init__(self, dir, start_x, start_y, end_x, end_y, parent_gadget=None, name="Unnamed", description="No Description"):
        super().__init__()
        self.wire_list = []
        self.dir = dir
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.makeWireFromCoords()

    def __init__(self, dir, start_x, start_y, len):
        super().__init__()
        self.wire_list = []
        self.dir = dir
        self.start_x = start_x
        self.start_y = start_y
        self.len = len
        self.makeWireFromLen()

    def makeWireFromCoords(self):
        if dir == "W" or "West":
            for i in range(self.start_x, self.end_x + 1):
                self.wire_list.append(Tile(westWire, i, self.start_y))
        if dir == "E" or "East":
            for i in range(self.start_x, self.end_x + 1):
                self.wire_list.append(Tile(eastWire, i, self.start_y))
        if dir == "N" or "North":
            for i in range(self.start_y, self.end_y + 1):
                self.wire_list.append(Tile(northWire, self.start_x, i))
        if dir == "S" or "South":
            for i in range(self.start_y, self.end_y + 1):
                self.wire_list.append(Tile(southWire, self.start_x, i))
        return self.wire_list

    def makeWireFromLen(self):
        for i in range(0, self.len):
            if dir == "W" or "West":
                self.wire_list.append(Tile(westWire, self.start_x + i, self.start_y))
            if dir == "E" or "East":
                self.wire_list.append(Tile(eastWire, self.start_x + i, self.start_y))
            if dir == "N" or "North":
                self.wire_list.append(Tile(northWire, self.start_x, self.start_y + i))
            if dir == "S" or "South":
                self.wire_list.append(Tile(southWire, self.start_x, self.start_y + i))
        return self.wire_list


# List of all states
## Make a door that activates when open state is detected and locks when closed state is detected
# What do I need to do for eq gadget?
## 1. Create a list of all states
### Border
border_state = State("Border", outer_space_crayola, " ", "black")

### Wires
northWire = State("NorthWire", Blue_Sapphire, "🡹")
southWire = State("SouthWire", Blue_Sapphire, "🡻")
westWire = State("WestWire", Blue_Sapphire, "🡸")
eastWire = State("EastWire", Blue_Sapphire, "🡺")

northCopyWire = State("NorthCopyWire", light_blue, "⇈")
southCopyWire = State("SouthCopyWire", light_blue, "⇊")
westCopyWire = State("WestCopyWire", light_blue, "⇇")
eastCopyWire = State("EastCopyWire", light_blue, "⇉")

wireWriterSouth_Inavtive = State("WireWriterSouth_Inactive", light_blue, "🡻")
### Check Equality
check_equal_S_start_state = State("Check=S(", mid_pink, "↧=₍", "black")
check_equal_S_end_state = State("Check=S)", mid_pink, "↧=₎", "black")
check_equal_S_any_num_state = State("Check=S*", mid_pink, "↧⩮", "black")

check_equal_S_start_state_inactive = State(
    "IN_Check=S(Inactive", grey_pink, "↧=₍", "black")
check_equal_S_end_state_inactive = State(
    "Check=S)Inactive", grey_pink, "↧=₎", "black")
check_equal_S_any_num_state_inactive = State(
    "IN_Check=S*Inactive", grey_pink, "↧⩮", "black")

confirm_equal_S_start_state = State("(=S(", mid_pink, "↧₍=₍", "black")
confirm_equal_S_end_state = State(")=S)", mid_pink, "↧₎=₎", "black")
confirm_equal_S_any_state = State("*=S*", mid_pink, "↧*⩮", "black")
confirm_equal_S_any_0_state = State("0=S*", mid_pink, "↧0⩮", "black")
confirm_equal_S_any_1_state = State("1=S*", mid_pink, "↧1⩮", "black")
confirm_equal_S_any_2_state = State("2=S*", mid_pink, "↧2⩮", "black")
confirm_equal_S_any_3_state = State("3=S*", mid_pink, "↧3⩮", "black")
confirm_equal_S_any_4_state = State("4=S*", mid_pink, "↧4⩮", "black")
confirm_equal_S_any_5_state = State("5=S*", mid_pink, "↧5⩮", "black")
confirm_equal_S_any_6_state = State("6=S*", mid_pink, "↧6⩮", "black")
confirm_equal_S_any_7_state = State("7=S*", mid_pink, "↧7⩮", "black")
confirm_equal_S_any_8_state = State("8=S*", mid_pink, "↧8⩮", "black")
confirm_equal_S_any_9_state = State("9=S*", mid_pink, "↧9⩮", "black")

### Doors
endcap_door_west_inactive = State(
    "EndcapDoorWestInactive", grey, "◨", "black")
endcap_door_west_handle_inactive = State(
    "EndCapDoorHandleWestInactive", grey, "◨🔒", "black")
endcap_door_west_active = State(
    "EndcapDoorWestActive", persian_green, "◨", "black")
endcap_door_west_handle_active = State(
    "EndCapDoorHandleWestActive", persian_green, "◨🔓", "black")
endcap_door_west_stop = State(
    "EndcapDoorWestStop", Venetian_Red, "◨", "black")
endcap_door_west_handle_stop = State(
    "EndCapDoorWestHandleStop", Venetian_Red, "◨🔒", "black")
endcap_door_west_reset = State(
    "EndcapDoorWestReset", mango_tango, "↺◨", "black")
endcap_door_west_handle_reset = State(
    "EndCapDoorHandleWestReset", mango_tango, "↺◨🔒", "black")
endcap_door_west_handle_reset_waiting = State(
    "EndCapDoorHandleWestResetWaiting", mango_tango, "↺⏱◨🔒", "black")
endcap_door_west_reset_waiting = State(
    "EndcapDoorWestResetWaiting", mango_tango, "↺⏱◨", "black")

signal_door_inactive = State(
    "LockedSignalDoorInactive", grey, "🔒▦", "black")
signal_door_handle_inactive = State(
    "LockedSignalDoorHandleInactive", grey, "🗝", "black")
signal_door_handle_reset = State(
    "SignalDoorHandleReset", mango_tango, "↺🗝", "black")
signal_door_open = State("SignalDoorOpen", persian_green, "🔓▦", "black")
signal_door_handle_open = State(
    "SignalDoorHandleOpen", persian_green, "🗝", "black")

signal_door_propped_open = State(
    "SignalDoorProppedOpen", persian_green, "🔓", "black")
signal_door_reset = State("SignalDoorReset", mango_tango, "↺▦", "black")
signal_door_reset_walk = State(
    "SignalDoorResetWalk", mango_tango, "↺▦◃", "black")
signal_door_send_confirmed_transmission = State(
    "SignalDoorSendConfirmedTransmission", mango_tango, "▦⇉✅", "black")
reset_confirmed_transmission_westWire = State(
    "ResetConfirmedTransmissionWest", mango_tango, "↺✅⇉", "black")


### Signal Checks
closed_endcap_door_check_signal = State(
    "ClosedEndcapDoorCheckSignal", grey, "✅", "black")
closed_endcap_door_check_signal_inactive = State(
    "ClosedEndcapDoorCheckSignalInactive", grey, "❌", "black")

signal_transmitter_turn_down_inactive = State(
    "SignalTransmitterTurnDownInactive", grey, "⮮", "black")
signal_transmitter_turn_down_active = State(
    "SignalTransmitterTurnDownActive", persian_green, "⮮", "black")
signal_transmitter_turn_down_open = State(
    "SignalTransmitterTurnDownOpen", persian_green, "⮮", "black")
signal_transmitter_turn_down_reset = State(
    "SignalTransmitterTurnDownReset", mango_tango, "↺⮮", "black")

signal_transmitter_turn_up_inactive = State(
    "SignalTransmitterTurnUpInactive", grey, "⮲", "black")
signal_transmitter_turn_up_active = State(
    "SignalTransmitterTurnUpActive", persian_green, "⮲", "black")
signal_transmitter_turn_up_reset = State(
    "SignalTransmitterTurnUpReset", mango_tango, "↺⮲", "black")

row_signal_positive_inactive = State(
    "RowSignalPositiveInactive", grey, "⊝", "black")

row_signal_positive_start_inactive = State(
    "RowSignalPositiveStartInactive", green_yellow_crayola, "⊝", "black")

row_signal_positive_start_waiting = State(
    "RowSignalPositiveStartWaiting", green_yellow_crayola, "⊝⏱", "black")

row_signal_positive_waiting = State(
    "RowSignalPositiveWaiting", green_yellow_crayola, "⏱", "black")
row_signal_positive_full_accept = State(
    "RowSignalPositiveFullAccept", Viridian_Green, "✅")
row_signal_intermediate_accept = State(
    "RowSignalPositiveInterimAccept", pistachio, "✅")
row_signal_positive_reset = State(
    "RowSignalPositiveReset", mango_tango, "↺", "black")


### Trap Doors
trap_door_inactive = State("TrapDoorInactive", Barn_Red, "TD", "black")
### Data States
ds_1 = State("1", Papaya_Whip, "①")
ds_2 = State("2", Papaya_Whip, "②")
ds_3 = State("3", Papaya_Whip, "③")
ds_4 = State("4", Papaya_Whip, "④")
ds_5 = State("5", Papaya_Whip, "⑤")
ds_6 = State("6", Papaya_Whip, "⑥")
ds_7 = State("7", Papaya_Whip, "⑦")
ds_8 = State("8", Papaya_Whip, "⑧")
ds_9 = State("9", Papaya_Whip, "⑨")
ds_0 = State("0", Papaya_Whip, "⓪")
data_states_list_nums_only = [ds_0, ds_1, ds_2,
                              ds_3, ds_4, ds_5, ds_6, ds_7, ds_8, ds_9]

start_state = State("EndcapDSOpen", Papaya_Whip, "(", "black")
end_state = State("EndcapDSClosed", Papaya_Whip, ")", "black")
data_states_list_all = [start_state] + data_states_list_nums_only + [end_state]

#data_state = State("1", Papaya_Whip, "1")
## Reprograamming Equality Gadget by sending a reset start cap then a data string and flip the equlities
reprogram_verifier_eq_gadget = State(
    "ReprogramEqGadgetVerifier", Papaya_Whip, "", "black")
### Transition Rules
#transition = TransitionRule("WestWire", ds.label, ds.label, "WestWire", "h")


## 2. Make a wire load as seed assembly
## 3. Make a door that activates when open state is detected and locks when closed state is detected


#Other stuff
##Colors
## Various Symbols ⚿⚾⚽⚰⚱⚲⚳⚴⚵⚶⚷⚸⚹⚺⚻⚼⚽⚾⛀⛁⛂⛃⛄⛅⛆⛇⛈⛉⛊⛋⛌⛍⛎⛏⛐⛑⛒⛓⛔⛕⛖⛗⛘⛙⛚⛛⛜⛝⛞⛟⛠⛡⛢⛣⛤⛥⛦⛧⛨⛩⛪⛫⛬⛭⛮⛯⛰⛱⛲⛳⛴⛵⛶⛷⛸⛹⛺⛻⛼⛽⛾⛿✀✁✂✃✄✅✆✇✈✉✊✋✌✍✎✏✐✑✒✔✕✖✗✘✙✚✛✜✝✞✟✠✡✢✣✤✥✦✧✨✩✪✫✬✭✮✯✰✱✲✳✴✵✶✷✸✹✺✻✼✽✾✿❀❁❂❃❄❅❆❇❈❉❊❋❌❍❎❏❐❑❒❓❔❕❖❗❘❙❚❛❜❝❞❟❠❡❢❣❤❥❦❧❨❩❪❫❬❭❮❯❰❱❲❳❴❵❶❷❸❹❺❻❼❽❾❿➀🔏

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

IUSys = IUSystem()
