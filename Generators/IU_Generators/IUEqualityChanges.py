import UniversalClasses as uc
from components import *
import sys
from Generators.IU_Generators.states import *

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

        if "W" in dir_len_dict.keys():
            wireState = westWire
            k = "W"
        elif "S" in dir_len_dict.keys():
            wireState = southWire
            k = "S"
        elif "E" in dir_len_dict.keys():
            wireState = eastWire
            k = "E"
        elif "N" in dir_len_dict.keys():
            wireState = northWire
            k = "N"

        start_end_coords = dir_len_dict[k]

        start_x = start_end_coords[0][0]
        start_y = start_end_coords[0][1]
        end_x = start_end_coords[1][0]
        end_y = start_end_coords[1][1]

        wa_seed_states = [wireState]
        wa_seed_tiles = []

        if start_x == end_x:
            for i in range(start_y, end_y + 1):
                wa_seed_tiles.append(uc.Tile(wireState, start_x, i))
            example_tiles = self.setSampleDataStartCoords(end_x, end_y + 1, "V")
        elif start_y == end_y:
            for i in range(start_x, end_x + 1):
                wa_seed_tiles.append(uc.Tile(wireState, i, start_y))
            example_tiles = self.setSampleDataStartCoords(end_x + 1, end_y, "H")

        wa_seed_tiles = wa_seed_tiles + example_tiles

        asb = uc.Assembly()
        asb.setTilesFromList(wa_seed_tiles)
        return asb, wa_seed_states, wa_seed_tiles

    def basicWireGenerator(self):
        asb, wa_seed_states, wa_seed_tiles = self.basicWireSeedAssembly()

        #System takes in temp, states, initial states, seed states, vertical_affinitys, horizontal_affinitys, vert transitions, horiz transitions, tile vertical transitions, tile horizontal transitions, seed assembly
        genSys = uc.System(1, wa_seed_states, [], wa_seed_states,  [], [], [], [], [], [], asb)
        wire_stuff = self.wireAffinities()

        wire_tr = wire_stuff[0]
        wire_affs = wire_stuff[1]
        if len(wire_stuff) == 3:
            wire_st = wire_stuff[2]
            for i in wire_st:
                self.addSeedStateToIUSys(i)
                genSys.addSeedState(i)

        print("Wire TR length: ", len(wire_tr))
        print("Wire Affs length: ", len(wire_affs))

        for i in wire_tr:
            self.addToAllTr(i)
            genSys.addTransitionRule(i)



        for a in wire_affs:
            self.addToAllAff(a)
            genSys.addAffinity(a)




        self.all_sys["basicWire"] = genSys

        return genSys

    def wireAffinities(self):
        wire_affs = []
        wire_tr = []
        wire_st = []
        if self.genSys is not None:
            for ds in data_states_list_all_with_prefixes_no_order:
                self.genSys.addSeedState(ds)
                for i in wire_states:
                    self.genSys.addSeedState(i)

                    if i.label == "westWire" or i.label == "westProtectedWire":
                        aff = uc.AffinityRule(i.label, i.label, "h", 1)
                        wire_affs.append(aff)
                        self.genSys.addAffinity(aff)
                        aff = uc.AffinityRule(i.label, ds.label, "h", 1)
                        wire_affs.append(aff)
                        self.genSys.addAffinity(aff)
                        aff = uc.AffinityRule(ds.label, i.label, "h", 1)
                        wire_affs.append(aff)
                        self.genSys.addAffinity(aff)
                        tr = uc.TransitionRule(i.label, ds.label, ds.label, i.label, "h")
                        wire_tr.append(tr)
                        self.genSys.addTransitionRule(tr)
                        if "Protected" in i.label:
                            aff = uc.AffinityRule(
                                i.label, border_state.label, "v", 1)
                            wire_affs.append(aff)
                            self.genSys.addAffinity(aff)
                            aff = uc.AffinityRule(
                                border_state.label, i.label,  "v", 1)
                            wire_affs.append(aff)
                            self.genSys.addAffinity(aff)
                    elif i.label == "eastWire" or i.label == "eastProtectedWire":
                        aff = uc.AffinityRule(i.label, i.label, "h", 1)
                        wire_affs.append(aff)
                        self.genSys.addAffinity(aff)
                        aff = uc.AffinityRule(i.label, ds.label, "h", 1)
                        wire_affs.append(aff)
                        self.genSys.addAffinity(aff)
                        aff = uc.AffinityRule(ds.label, i.label, "h", 1)
                        wire_affs.append(aff)
                        self.genSys.addAffinity(aff)
                        tr = uc.TransitionRule(ds.label, i.label, i.label, ds.label, "h")
                        wire_tr.append(tr)
                        self.genSys.addTransitionRule(tr)

                        if "Protected" in i.label:
                            aff = uc.AffinityRule(
                                i.label, border_state.label, "v", 1)
                            wire_affs.append(aff)
                            self.genSys.addAffinity(aff)
                            aff = uc.AffinityRule(
                                border_state.label, i.label,  "v", 1)
                            wire_affs.append(aff)
                            self.genSys.addAffinity(aff)
                    elif i.label == "northWire" or i.label == "northProtectedWire":
                        aff = uc.AffinityRule(i.label, i.label, "v", 1)
                        wire_affs.append(aff)
                        self.genSys.addAffinity(aff)
                        aff = uc.AffinityRule(i.label, ds.label, "v", 1)
                        wire_affs.append(aff)
                        self.genSys.addAffinity(aff)
                        aff = uc.AffinityRule(ds.label, i.label, "v", 1)
                        wire_affs.append(aff)
                        self.genSys.addAffinity(aff)
                        tr = uc.TransitionRule(i.label, ds.label, ds.label, i.label, "v")
                        wire_tr.append(tr)
                        self.genSys.addTransitionRule(tr)

                        if "Protected" in i.label:
                            aff = uc.AffinityRule(
                                i.label, border_state.label, "h", 1)
                            wire_affs.append(aff)
                            self.genSys.addAffinity(aff)
                            aff = uc.AffinityRule(
                                border_state.label, i.label,  "h", 1)
                            wire_affs.append(aff)
                            self.genSys.addAffinity(aff)

                    elif i.label == "southWire" or i.label == "southProtectedWire":
                        aff = uc.AffinityRule(i.label, i.label, "v", 1)
                        wire_affs.append(aff)
                        self.genSys.addAffinity(aff)
                        aff = uc.AffinityRule(i.label, ds.label, "v", 1)
                        wire_affs.append(aff)
                        aff = uc.AffinityRule(ds.label, i.label, "v", 1)
                        wire_affs.append(aff)
                        tr = uc.TransitionRule(ds.label, i.label, i.label, ds.label, "v")
                        wire_tr.append(tr)
                        self.genSys.addTransitionRule(tr)

                        if "Protected" in i.label:
                            aff = uc.AffinityRule(i.label, border_state.label, "h", 1)
                            wire_affs.append(aff)
                            self.genSys.addAffinity(aff)
                            aff = uc.AffinityRule(border_state.label, i.label,  "h", 1)
                            wire_affs.append(aff)
                            self.genSys.addAffinity(aff)

                    elif i.label == "northEastWire" or i.label == "northEastProtectedWire":
                        aff = uc.AffinityRule(i.label, northWire.label, "v", 1)
                        wire_affs.append(aff)
                        self.genSys.addAffinity(aff)

                        aff = uc.AffinityRule(i.label, eastWire.label, "h", 1)
                        wire_affs.append(aff)
                        self.genSys.addAffinity(aff)

                        aff = uc.AffinityRule(i.label, ds.label, "v", 1)
                        wire_affs.append(aff)
                        self.genSys.addAffinity(aff)

                        aff = uc.AffinityRule(i.label, ds.label, "h", 1)
                        wire_affs.append(aff)
                        self.genSys.addAffinity(aff)

                        aff = uc.AffinityRule(eastWire.label, i.label, "v", 1)
                        wire_affs.append(aff)
                        self.genSys.addAffinity(aff)

                        tr = uc.TransitionRule(eastWire.label, i.label, i.label, northWire.label, "v")
                        wire_tr.append(tr)
                        self.genSys.addTransitionRule(tr)

                        if "Protected" in i.label:
                            aff = uc.AffinityRule(border_state.label, i.label,  "h", 1)
                            wire_affs.append(aff)
                            self.genSys.addAffinity(aff)
                            aff = uc.AffinityRule(border_state.label, i.label,  "v", 1)
                            wire_affs.append(aff)
                            self.genSys.addAffinity(aff)

                    elif i.label == "northWestWire" or i.label == "northWestProtectedWire":
                        aff = uc.AffinityRule(i.label, northWire.label, "v", 1)
                        wire_affs.append(aff)
                        self.genSys.addAffinity(aff)

                        aff = uc.AffinityRule(westWire.label, i.label, "h", 1)
                        wire_affs.append(aff)
                        self.genSys.addAffinity(aff)

                        aff = uc.AffinityRule(i.label, ds.label, "v", 1)
                        wire_affs.append(aff)
                        self.genSys.addAffinity(aff)

                        aff = uc.AffinityRule(ds.label, i.label, "h", 1)
                        wire_affs.append(aff)
                        self.genSys.addAffinity(aff)

                        aff = uc.AffinityRule(westWire.label, i.label, "v", 1)
                        wire_affs.append(aff)
                        self.genSys.addAffinity(aff)

                        tr = uc.TransitionRule(westWire.label, i.label, i.label, northWire.label, "v")
                        wire_tr.append(tr)
                        self.genSys.addTransitionRule(tr)

                        """ tr = uc.TransitionRule(i.label, westWire.label, i.label, northWire.label, "v")
                        wire_tr.append(tr)
                        self.genSys.addTransitionRule(tr) """

                        if "Protected" in i.label:
                            aff = uc.AffinityRule(i.label, border_state.label, "h", 1)
                            wire_affs.append(aff)
                            self.genSys.addAffinity(aff)
                            aff = uc.AffinityRule(border_state.label, i.label,  "v", 1)
                            wire_affs.append(aff)
                            self.genSys.addAffinity(aff)

        else:
            wire_st.append(border_state)

            for ds in data_states_list_all_with_prefixes_no_order:
                if ds not in wire_st:
                    wire_st.append(ds)

                for i in wire_states:
                    if i not in wire_st:
                        wire_st.append(i)

                    print(i.label)
                    if i.label == "WestWire" or i.label == "WestProtectedWire":
                        print("This Works")
                        aff = uc.AffinityRule(i.label, i.label, "h", 1)
                        wire_affs.append(aff)

                        aff = uc.AffinityRule(i.label, ds.label, "h", 1)
                        wire_affs.append(aff)

                        aff = uc.AffinityRule(ds.label, i.label, "h", 1)
                        wire_affs.append(aff)

                        tr = uc.TransitionRule(i.label, ds.label, ds.label, i.label, "h")
                        wire_tr.append(tr)

                        if "Protected" in i.label:
                            aff = uc.AffinityRule(i.label, border_state.label, "v", 1)
                            wire_affs.append(aff)

                            aff = uc.AffinityRule(border_state.label, i.label,  "v", 1)
                            wire_affs.append(aff)

                    elif i.label == "EastWire" or i.label == "EastProtectedWire":
                        aff = uc.AffinityRule(i.label, i.label, "h", 1)
                        wire_affs.append(aff)

                        aff = uc.AffinityRule(i.label, ds.label, "h", 1)
                        wire_affs.append(aff)

                        aff = uc.AffinityRule(ds.label, i.label, "h", 1)
                        wire_affs.append(aff)

                        tr = uc.TransitionRule(
                            ds.label, i.label, i.label, ds.label, "h")
                        wire_tr.append(tr)


                        if "Protected" in i.label:
                            aff = uc.AffinityRule(
                                i.label, border_state.label, "v", 1)
                            wire_affs.append(aff)

                            aff = uc.AffinityRule(
                                border_state.label, i.label,  "v", 1)
                            wire_affs.append(aff)

                    elif i.label == "NorthWire" or i.label == "NorthProtectedWire":
                        aff = uc.AffinityRule(i.label, i.label, "v", 1)
                        wire_affs.append(aff)

                        aff = uc.AffinityRule(i.label, ds.label, "v", 1)
                        wire_affs.append(aff)

                        aff = uc.AffinityRule(ds.label, i.label, "v", 1)
                        wire_affs.append(aff)

                        tr = uc.TransitionRule(
                            i.label, ds.label, ds.label, i.label, "v")
                        wire_tr.append(tr)


                        if "Protected" in i.label:
                            aff = uc.AffinityRule(
                                i.label, border_state.label, "h", 1)
                            wire_affs.append(aff)

                            aff = uc.AffinityRule(
                                border_state.label, i.label,  "h", 1)
                            wire_affs.append(aff)


                    elif i.label == "SouthWire" or i.label == "SouthProtectedWire":
                        aff = uc.AffinityRule(i.label, i.label, "v", 1)
                        wire_affs.append(aff)

                        aff = uc.AffinityRule(i.label, ds.label, "v", 1)
                        wire_affs.append(aff)
                        aff = uc.AffinityRule(ds.label, i.label, "v", 1)
                        wire_affs.append(aff)
                        tr = uc.TransitionRule(
                            ds.label, i.label, i.label, ds.label, "v")
                        wire_tr.append(tr)


                        if "Protected" in i.label:
                            aff = uc.AffinityRule(
                                i.label, border_state.label, "h", 1)
                            wire_affs.append(aff)

                            aff = uc.AffinityRule(
                                border_state.label, i.label,  "h", 1)
                            wire_affs.append(aff)


                    """ elif i.label == "NorthEastWire" or i.label == "NorthEastProtectedWire":
                        aff = uc.AffinityRule(i.label, northWire.label, "v", 1)
                        wire_affs.append(aff)


                        aff = uc.AffinityRule(i.label, eastWire.label, "h", 1)
                        wire_affs.append(aff)


                        aff = uc.AffinityRule(i.label, ds.label, "v", 1)
                        wire_affs.append(aff)


                        aff = uc.AffinityRule(i.label, ds.label, "h", 1)
                        wire_affs.append(aff)


                        aff = uc.AffinityRule(eastWire.label, i.label, "v", 1)
                        wire_affs.append(aff)


                        tr = uc.TransitionRule(
                            eastWire.label, i.label, i.label, northWire.label, "v")
                        wire_tr.append(tr)


                        if "Protected" in i.label:
                            aff = uc.AffinityRule(
                                border_state.label, i.label,  "h", 1)
                            wire_affs.append(aff)

                            aff = uc.AffinityRule(
                                border_state.label, i.label,  "v", 1)
                            wire_affs.append(aff)
 """

                    """ elif i.label == "NorthWestWire" or i.label == "NorthWestProtectedWire":
                        aff = uc.AffinityRule(i.label, northWire.label, "v", 1)
                        wire_affs.append(aff)


                        aff = uc.AffinityRule(westWire.label, i.label, "h", 1)
                        wire_affs.append(aff)


                        aff = uc.AffinityRule(i.label, ds.label, "v", 1)
                        wire_affs.append(aff)

                        aff = uc.AffinityRule(ds.label, i.label, "h", 1)
                        wire_affs.append(aff)


                        aff = uc.AffinityRule(westWire.label, i.label, "v", 1)
                        wire_affs.append(aff)


                        tr = uc.TransitionRule(
                            westWire.label, i.label, i.label, northWire.label, "v")
                        wire_tr.append(tr)




                        if "Protected" in i.label:
                            aff = uc.AffinityRule(
                                i.label, border_state.label, "h", 1)
                            wire_affs.append(aff)

                            aff = uc.AffinityRule(
                                border_state.label, i.label,  "v", 1)
                            wire_affs.append(aff) """

            print("Wires Other")
        return [wire_tr, wire_affs, wire_st]

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

    def equalityEndCap(self):
        bw_gs = self.basicWireGenerator()




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

wire_states = [westWire, eastWire, northWire, southWire, northEastWire, northWestWire, southEastWire, southWestWire, westProtectedWire, eastProtectedWire, northProtectedWire, southProtectedWire]
data_states_list_prefixes = [north_prefix, south_prefix, east_prefix, west_prefix, program_prefix, reset_prefix]
data_states_list_all_with_prefixes_no_order = data_states_list_prefixes + data_states_list_all
