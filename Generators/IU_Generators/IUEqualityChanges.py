import UniversalClasses as uc
from components import *
import sys
from states import *

gsc = GeneratedStates()
gsd = gsc.states_dict

class IUGenerators:
    all_states_dict = {}
    all_initial_states_dict = {}
    all_states_list = []
    all_seed_states_list = []
    all_seed_states_dict = {}
    all_aff_list = []
    all_aff_dict = {}
    all_tr_list = []
    all_tr_dict = {}
    all_sys = {}

    def __init__(self, exampleSysName=""):
        self.exampleSysName = exampleSysName
        self.genSys = None

        self.example_states_data = [north_prefix, start_state, ds_1, ds_2, ds_5, end_state]
        self.aff_list = []

    #To Do
    def setExampleData(self, data_string):
        self.example_states_data = data_string
    def setSampleDataStartCoords(self, x, y, dir):
        self.sampleTiles = []

        for i in range(0, len(self.example_states_data)):
            if dir == "V" or dir == "N" or dir == "S":
                self.sampleTiles.append(uc.Tile(self.example_states_data[i], x, y + i))
            else:
                self.sampleTiles.append(uc.Tile(self.example_states_data[i], x + i, y))

        return self.sampleTiles

    def basicWireSeedAssembly(self, dir_len_dict={"W": ((1, 0), (4, 0))}):
        # , "S": ((-7, -2), (-7, -6))

        if dir_len_dict.key() == "W":
            wireState = westWire
        elif dir_len_dict.key() == "S":
            wireState = southWire
        elif dir_len_dict.key() == "E":
            wireState = eastWire
        elif dir_len_dict.key() == "N":
            wireState = northWire

        start_end_coords = dir_len_dict[dir_len_dict.key()]

        start_x = start_end_coords[0][0]
        start_y = start_end_coords[0][1]
        end_x = start_end_coords[1][0]
        end_y = start_end_coords[1][1]

        wa_seed_states = [wireState]
        wa_seed_tiles = []

        for i in range(start_x, end_x + 1):
            for j in range(start_y, end_y + 1):
                wa_seed_tiles.append(uc.Tile(wireState, i, j))

        example_tiles = self.setSampleDataStartCoords(end_x + 1, end_y + 1, dir_len_dict.key())
        wa_seed_tiles = wa_seed_tiles + example_tiles

        asb = uc.Assembly()
        asb.setTilesFromList(wa_seed_tiles)
        return asb, wa_seed_states, wa_seed_tiles

    def basicWireGenerator(self):
        asb, wa_seed_states, wa_seed_tiles = self.basicWireSeedAssembly()

        #System takes in temp, states, initial states, seed states, vertical_affinitys, horizontal_affinitys, vert transitions, horiz transitions, tile vertical transitions, tile horizontal transitions, seed assembly
        self.genSys = uc.System(1, wa_seed_states, [], wa_seed_states,  [], [], [], [], [], [], asb)


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

    def addStateToIUSys(self, state):
        if state.label not in self.all_states_dict.keys():
            self.all_states_dict[state.label] = state

    def addSeedStateToIUSys(self, state):
        if state.label not in self.all_seed_states_dict.keys():
            self.all_seed_states_dict[state.label] = state
            self.addStateToIUSys(state)

        else:
            print("Seed State already exists in system")

    def addToAllAff(self, aff):
        if aff not in self.all_aff:
            self.all_aff_list.append(aff)

    def addToAllTr(self, tr):
        if tr not in self.all_tr:
            self.all_tr_list.append(tr)

    def addToAllStates(self, state):
        if state not in self.all_states_list:
            self.all_states_list.append(state)

    def addToAllSeedStates(self, state):
        if state not in self.all_seed_states_list:
            self.all_seed_states_list.append(state)

## Basic Requirements for Boolean Circuit Simulation
### 1. Wires
        """
        This is done
        """
### 2.Turn and Delay

### 3. Signal Crossing
### 4. Gates
### 5. Fan-out






data_states_list_nums_only = [ds_0, ds_1, ds_2, ds_3, ds_4, ds_5, ds_6, ds_7, ds_8, ds_9]
data_states_list_all = [start_state] + data_states_list_nums_only + [end_state]


data_states_list_prefixes = [north_prefix, south_prefix, east_prefix, west_prefix, program_prefix, reset_prefix]
data_states_list_all_with_prefixes_no_order = data_states_list_prefixes + data_states_list_all
