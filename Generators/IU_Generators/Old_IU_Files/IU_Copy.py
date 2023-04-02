
import UniversalClasses as uc
import sys
from components import *
from Assets.colors import *
#Colors



class IUGenerator:
    def __init__(self):
        pass

    def makeSeedAssembly(self, states):
        pass

    def makeAffinities(self, states):
        pass

    def makeTransitions(self, states):
        pass


class SeedAssemblyEqualityWire:
    def __init__(self):
        self.seed = None

        self.wire_gadget = WireGadget(9, "W", 0, 0)
        test_data = ["1", "1", "0", "2"]
        self.wire_assembly = self.wire_gadget.returnWireAssembly()
        self.wire_gadget_states = self.wire_gadget.returnStatesUsed()
        self.wire_assembly_tiles = self.wire_assembly.returnTiles()
        self.test_data_generator(test_data)

        self.wire_transitions = self.createWireTransitions(self.test_data_states)

    def returnWireAssembly(self):
        return self.wire_assembly

    def returnWireGadget(self):
        return self.wire_gadget

    def returnStatesUsed(self):
        return self.wire_gadget_states

    def test_data_generator(self, td):
        self.test_data_states = []
        self.test_data_tiles = []
        for count, ele in enumerate(td):
            print("count: {}, element: {}".format(count, ele))
            temp_state = uc.State(ele, Barn_Red, ele)

            if temp_state not in self.test_data_states:
                self.test_data_states.append(temp_state)

            temp_tile = uc.Tile(temp_state, count, 0)
            self.test_data_tiles.append(temp_tile)

        self.wire_gadget.appendTestDataString(self.test_data_tiles)

        """ self.wire_gadget_states = self.wire_gadget.returnStatesUsed()
        self.wire_assembly_tiles = self.wire_assembly.returnTiles()
        self.wire_assembly = self.wire_gadget.returnWireAssembly() """
        self.wire_assembly = self.wire_gadget.returnWireAssembly()
        print("Test Data Added")

    def createWireTransitions(self, test_data_states):
        wire_transitions = []
        for ds in test_data_states:
            transition = uc.TransitionRule("WestWire", ds.label, ds.label, "WestWire", "h")
            wire_transitions.append(transition)
        return wire_transitions


class IUSeedAssemblyGenerator:
    def __init__(self):

        self.seedA = uc.Assembly()
        self.st = []
        self.border_state = uc.State("Border", Papaya_Whip, " ", "black", "Arial")
        self.st.append(self.border_state)
        self.equalityGadget(self)

        if self.seedA.returnTiles() == []:
            print("Seed Assembly is empty")
        else:
            self.genSys = uc.System(1, [], [], [self.st], [], [], [], [], [
            ], [], self.returnSeedAssembly(), False)
            print("Seed Assembly Generated")

    def equalityGadget(self):
        check_equal_S_para = uc.State("CheckEqualS(", pink, "=(", "black", "Arial")
        self.st.append(check_equal_S_para)
        check_equal_S_any = uc.State("CheckEqualS*", pink, "=*", "black", "Arial")
        self.st.append(check_equal_S_any)
        check_equal_S_rpara = uc.State("CheckEqualS)", pink, "=)", "black", "Arial")
        self.st.append(check_equal_S_rpara)

        eq_list = []
        EqT = uc.Tile(check_equal_S_any, 0, 0)
        eq_list.append(EqT)
        EqT = uc.Tile(check_equal_S_any, 1, 0)
        eq_list.append(EqT)
        EqT = uc.Tile(check_equal_S_any, -1, 0)
        eq_list.append(EqT)
        EqT = uc.Tile(check_equal_S_para, -2, 0)
        eq_list.append(EqT)
        EqT = uc.Tile(check_equal_S_rpara, 2, 0)

        for i in range(-2, 3):
            EqT = uc.Tile(self.border_state, 1, i)
            eq_list.append(EqT)

        EqT = uc.Tile(self.border_state, 3, 0)
        eq_list.append(EqT)

        self.seedA.addTilesFromList(eq_list)

    def returnSeedAssembly(self):
        return self.seedA

    def returnStatesInSeedAssembly(self):
        return self.st

    def returnGenSys(self):
        return self.genSys

    """ def makeWire(self, len, dir, start_x, start_y):
        wire = uc.Assembly()
        wire_list = []
        northWire = uc.State("NorthWire", blue, "⮙")
        southWire = uc.State("SouthWire", blue, "⮛")
        westWire = uc.State("WestWire", blue, "⮘")
        eastWire = uc.State("EastWire", blue, "⮚")
        for i in range(len):
            if dir == "N":
                wire_list.append(uc.Tile(self.border_state, start_x, start_y + i))

        wire.addTilesFromList(wire_list)
        return wire """


class SuperState:
    def __init__(self, data_string, source_state):
        self.data_string = data_string
        self.source_state_label = source_state.returnLabel()
        self.data_string_identifier = None  # List of data string states

    def __str__(self):
        return self.data_string_identifier

    def makeIdentifierPair(self):

        for i in self.data_string:
            self.data_string_identifier.append(i.returnLabel())


class DataString:
    def __init__(self, data, parent=None):
        self.alt_identifier = ""
        if type(data[0]) == uc.Tile:
            self.data = data
            self.parent = parent
        self.data = data  # List of tiles in order of appearance
        self.value = " ".join(t.label for t in self.data)

    def __str__(self):
        return self.value

    def returnData(self):
        return self.data

    def returnAltIdentifier(self):
        return self.alt_identifier


class Gadget:
    def __init__(self, name="", description="", states=[], intitial_config=uc.Assembly()):
        self.gadget_name = name
        self.gadget_description = description
        self.gadget_states = states  # list of states in the gadget
        self.initial_config = intitial_config  # Assembly
        self.demensions = None  # tuple of (x, y) demensions of the gadget


class TestGadget:
    def __init__(self, gadget_to_test, test_name):
        self.test_name = test_name
        self.test_gadget = gadget_to_test


class MultiGadget:
    def __init__(self, multi_gadget_name, start_assembly=uc.Assembly()):
        self.gadget_states = []
        self.multi_assembly = start_assembly
        self.gadgets_added = []
        self.multi_gadget_name = multi_gadget_name

    def appendAssembly(self, assembly, location):
        self.multi_assembly.addAssembly(assembly, location)

    def addAssembly(self, assembly, location):
        current_borders = self.multi_assembly.returnBorders()
        new_assembly_borders = assembly.returnBorders()
        self.gadgets_added.append(assembly)

        if location == "SW":
            self.multi_assembly

    def addGadget(self, gadget, location):
        self.gadget_states.append(gadget.gadget_states)
        self.gadgets_added.append(gadget)
        self.addAssembly(gadget.initial_config, location)

    def addWireGadget(self, wire):
        self.gadget_states.append(wire.states_used)

    def addNewWire(self, len, dir, start_x, start_y):
        wire = WireGadget()
        if "({},{})".format(start_x, start_y) in self.multi_assembly.returnTiles():
            print("Wire cannot be placed here")
        else:
            wire.makeWire(len, dir, start_x, start_y)

            self.addWireGadget(wire)

    def makeEqualityWire(self):
        wire = WireGadget()
        equality_gadget = EqualityGadget()
        wire.makeWire(9, "W", 0, 0)
        self.addWireGadget(wire)


class GadgetBlock:
    pass


class SuperBlock:
    def __init__(self, source_state, sim_state, architecture, position):
        self.superblock_source_state = source_state
        self.sim_state = []  # data string
        #self.gadgets = gadgets
        #self.gSystem = IU_System


class SourceSystem:
    pass


class IUSystem:
    unit_states = []


class WireGadget:
    northWire = uc.State("NorthWire", blue, "⥉")
    southWire = uc.State("SouthWire", blue, "⮛")
    westWire = uc.State("WestWire", blue, "🡸")
    eastWire = uc.State("EastWire", blue, "⮚")

    def __init__(self, len, dir, start_x, start_y):
        self.wire_name = ""
        self.wire_list = []
        self.wire = uc.Assembly()
        self.states_used = []
        self.direction = dir
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = None
        self.end_y = None
        self.wire_length = len
        self.makeWire()

    def makeWire(self):

        for i in range(self.wire_length):
            if self.direction == "N":
                self.wire_list.append(    uc.Tile(self.northWire, self.start_x, self.start_y + i))
                self.end_y = self.start_y + i
                self.end_x = self.start_x
                if self.northWire not in self.states_used:
                    self.states_used.append(self.northWire)
            elif self.direction == "S":
                self.wire_list.append(    uc.Tile(self.southWire, self.start_x, self.start_y + i))
                self.end_y = self.start_y + i
                self.end_x = self.start_x
                if self.southWire not in self.states_used:
                    self.states_used.append(self.southWire)
            elif self.direction == "W":
                self.wire_list.append(    uc.Tile(self.westWire, self.start_x + i, self.start_y))
                self.end_x = self.start_x + i
                self.end_y = self.start_y
                if self.westWire not in self.states_used:
                    self.states_used.append(self.westWire)
            elif self.direction == "E":
                self.wire_list.append(    uc.Tile(self.eastWire, self.start_x + i, self.start_y))
                self.end_x = self.start_x + i
                self.end_y = self.start_y
                if self.eastWire not in self.states_used:
                    self.states_used.append(self.eastWire)

        self.wire.setTiles(self.wire_list)
        print("Wire made from ({},{}) to {}".format(self.start_x, self.start_y, self.wire_list[-1].returnPosition()))

    def returnWireTileList(self):
        return self.wire_list

    def returnWireAssembly(self):
        return self.wire

    def returnStatesUsed(self):
        return self.states_used

    def appendTestDataString(self, data_string):
        self.test_data_tile_list = []
        self.test_data_states_list = []
        curr_borders = self.wire.returnBorders()

        for i in range(len(data_string)):
            if self.direction == "N":
                temptile = uc.Tile(    data_string[i].state, self.end_x, self.end_y - i)
            elif self.direction == "S":
                temptile = uc.Tile(    data_string[i].state, self.end_x, self.end_y + i)
            elif self.direction == "W":
                temptile = uc.Tile(    data_string[i].state, self.end_x + i, self.end_y)
            elif self.direction == "E":
                temptile = uc.Tile(    data_string[i].state, self.end_x + i, self.end_y)
            self.test_data_tile_list.append(temptile)
            if data_string[i].state not in self.states_used:
                self.states_used.append(data_string[i].state)
            if temptile is not None:
                self.test_data_states_list.append(data_string[i].state)

        self.wire.setTiles(self.test_data_tile_list)

    def appendTestDataRawString(self, raw_string):
        pass


class EqualityGadget:
    check_equal_S_start_state = uc.State("CheckEqualS(", pink, "↧=₍")
    check_equal_S_end_state = uc.State("CheckEqualS)", pink, "↧=₎")
    check_equal_S_any_num_state = uc.State("CheckEqualS*", pink, "↧⩮")

    def __init__(self):
        self.eq_list = []
        self.eq = uc.Assembly()
        self.states_used = []

    def make_equality_any_gadget(self, start_x, start_y, len_to_check):
        self.eq_list.append(uc.Tile(self.check_equal_S_start_state, start_x, start_y))
        self.states_used.append(self.check_equal_S_start_state)
        for i in range(1, len_to_check - 2):
            self.eq_list.append(uc.Tile(self.check_equal_S_any_num_state, start_x + i, start_y))
        self.states_used.append(self.check_equal_S_any_num_state)
        self.eq_list.append(uc.Tile(self.check_equal_S_end_state, start_x + 2, start_y))
        self.states_used.append(self.check_equal_S_end_state)
        self.eq.addTilesFromList(self.eq_list)
        print("Equality Gadget Generated")

    def returnEqualityAssembly(self):
        return self.eq

    def returnEqualityTileList(self):
        return self.eq_list

    def returnEqualityStatesUsed(self):
        return self.states_used

# Notes
## At edge of a superbloc data strings pick up a directional signature depending on the direction they are moving in
    """northCopyWire = uc.State("NorthWire", blue, "⇈")
    southCopyWire = uc.State("SouthWire", blue, "⇊")
    westCopyWire = uc.State("WestWire", blue, "⇇")
    eastCopyWire = uc.State("EastWire", blue, "⇉")
    northWire = uc.State("NorthWire", blue, "⮙")
    southWire = uc.State("SouthWire", blue, "⮛")
    westWire = uc.State("WestWire", blue, "⮘")
    eastWire = uc.State("EastWire", blue, "⮚")
    """

    # Circled Equals: ⊜
    # Subscripted Equals: ₌ (U+208C)
    # Questioned Equals: ≟ (U+225F)
    # Combining Equals:
    # Equals with Asterisk: ⩮ (U+2A6E)


def test_data_generator(td, d):
    test_data_states = []
    test_data_tiles = []
    for count, ele in enumerate(td):
        temp_state = uc.State(str(ele), Barn_Red, str(ele))

        if temp_state not in test_data_states:
            test_data_states.append(temp_state)

        temp_tile = uc.Tile(temp_state, count, 0)
        test_data_tiles.append(temp_tile)

        return test_data_states, test_data_tiles


if __name__ == "__main__":
    test_data = [1, 1, 0, 2]
    test_data_generator(test_data, "W")
