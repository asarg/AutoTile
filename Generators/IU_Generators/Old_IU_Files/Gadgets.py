from Generators.IU_Generators.Old_IU_Files.GadgetComponents import add_affinities_vertical
from UniversalClasses import State, AffinityRule, System, TransitionRule, Tile, Assembly
from Assets.colors import *
from binaryStates import *
from gadget_states import *
from GadgetComponents import add_affinity_all_dirs
from binaryStates import write_data_states, write_data_states_dirs, write_data_states_caps

class Gadget:
    def __init__(self):
        self.name = None
        self.seed_states = None
        self.seed_assembly = None
        self.states = None
        self.initial_states = []
        self.available_edges = []
        self.state_affinities = {}
        self.state_transitions = {}


class SignalTransmitter:
    def __init__(self, signal_recived, signal_sent):
        self.signal_recived = signal_recived
        self.signal_sent = signal_sent





class SignalArc:
    def __init__(self):
        self.example = True
        self.initial_states = []
        self.seed_states = [signal_enter_inactive, signal_exit_inactive, signal_checkpoint_inactive, signal_conditional_inactive]
        self.states = [signal_enter_active, signal_checkpoint_active, signal_conditional_waiting, signal_conditional_intermediate_accept, signal_conditional_reject, signal_conditional_reset, signal_conditional_full_accept, signal_exit_accept] + self.seed_states
        self.affinity_rules = {}
        self.transition_rules = {}
        self.tiles = []

    def makeSeedAssembly(self, direction, start_x_y, end_x_y):
        t = Tile(signal_enter_inactive, start_x_y[0], start_x_y[1])
        self.tiles.append(t)

        t2 = Tile(signal_exit_inactive, end_x_y[0], end_x_y[1])
        self.tiles.append(t2)

        big_y = max(start_x_y[1], end_x_y[1])
        big_x = max(start_x_y[0], end_x_y[0])
        little_y = min(start_x_y[1], end_x_y[1])
        little_x = min(start_x_y[0], end_x_y[0])

        if direction == "NH":  # The signal arc is north of a horizontal wire
            check1 = Tile(signal_checkpoint_inactive,start_x_y[0], start_x_y[1] + 1)
            check2 = Tile(signal_checkpoint_inactive, end_x_y[0], end_x_y[1] + 1)

            for i in range(little_x + 1, big_x):
                t = Tile(signal_conditional_inactive, i, start_x_y[1] + 1)
                self.tiles.append(t)

        elif direction == "SH": # The signal arc is south of a horizontal wire
            check1 = Tile(signal_checkpoint_inactive, start_x_y[0], start_x_y[1] - 1)
            check2 = Tile(signal_checkpoint_inactive, end_x_y[0], end_x_y[1] - 1)

            for i in range(little_x + 1, big_x):
                t = Tile(signal_conditional_inactive, i, start_x_y[1] - 1)
                self.tiles.append(t)

        elif direction == "EV": # East of a vertical wire
            check1 = Tile(signal_checkpoint_inactive, start_x_y[0] - 1, start_x_y[1])
            check2 = Tile(signal_checkpoint_inactive, end_x_y[0] - 1, end_x_y[1])

            for i in range(little_y + 1, big_y):
                t = Tile(signal_conditional_inactive, start_x_y[0] - 1, i)
                self.tiles.append(t)

        elif direction == "WV":
            check1 = Tile(signal_checkpoint_inactive, start_x_y[0] + 1, start_x_y[1])
            check2 = Tile(signal_checkpoint_inactive, end_x_y[0] + 1, end_x_y[1])

            for i in range(little_y + 1, big_y):
                t = Tile(signal_conditional_inactive, start_x_y[0] + 1, i)
                self.tiles.append(t)


        self.tiles.append(check1)
        self.tiles.append(check2)

        a = Assembly()
        a.setTiles(self.tiles)

        return a

    def makeArcAffinities(self):
        for t in self.tiles:
            if t.x == 0 and t.y == 0:
                self.affinity_rules[t] = [signal_enter_inactive, signal_enter_active]
        return False

    def makeArcAffs(self):
        all_affs = []

        for sc in signal_checkpoint_states:
            for st in signal_enter_states:
                affs = add_affinity_all_dirs(sc, st)
                all_affs = all_affs + affs

            for stx in signal_exit_states:
                affs = add_affinity_all_dirs(sc, stx)
                all_affs = all_affs + affs

            for scs in signal_conditional_states:
                affs = add_affinity_all_dirs(sc, scs)
                all_affs = all_affs + affs

            for i in writeStatesAll:
                affs = add_affinity_all_dirs(sc, i)
                all_affs = all_affs + affs

        for i in writeStatesAll:
            affs = add_affinities_vertical(i, westWire)
            all_affs = all_affs + affs








    """ def __init__(self, startState, endState, startCoords, endCoords, length=5, input_gadget=None, output=None):
        self.startState = startState
        self.endState = endState


    def arcStatesInactive(self):
        return self.startState.active == False and self.endState.active == False """

    def buildArc(self):
        if self.arcStatesInactive():
            return None
        else:
            return self.buildArc()

    def makeSeedAssembly(self):

        return Assembly()