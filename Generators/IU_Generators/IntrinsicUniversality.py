import UniversalClasses as uc
from UniversalClasses import State, TransitionRule, AffinityRule, System, Tile, Assembly
from Assets.colors import *
from Generators.IU_Generators.binaryStates import *
import sys


class IUSystem:
    unit_states = []
    unit_vertical_affinities = {}
    unit_horizontal_affinities = {}
    unit_vertical_transitions = {}
    unit_horizontal_transitions = {}
    all_gadgets = []

    def __init__(self, source_system=None):
        self.source_system = source_system
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

    def add_gadget(self, gadget):
        self.all_gadgets.append(gadget)


class DataString:  # Takes in a list of data objects and
    def __init__(self, data, color):
        self.data = data


class MacroCell:
    def __init__(self, x, y, column_num, row_num, cell_len=6, transition_num=None, column_state_sim=None, row_state_sim=None, dir=None):
        # Starts at the neg door and ends at the pos door
        self.door_start_x = x
        self.door_start_y = y
        self.column_state = column_num
        self.row_state = row_num
        self.transition_num = transition_num
        self.cell_len = cell_len
        self.simulated_column_state = column_state_sim
        self.simulated_row_state = row_state_sim
        self.dir = dir

        self.mc_states = [punch_down_ds_neg_active, punch_down_ds_active, punch_down_ds_neg_inactive,
                          punch_down_ds_inactive, punch_down_ds_neg_end_found, punch_down_ds_end_found]
        self.mc_seed_states = [punch_down_ds_neg_active, punch_down_ds_active, eastWire, mc_door_east_negative_inactive,
                               mc_door_east_positive_inactive, mc_door_handle_east_negative_inactive, mc_door_handle_east_positive_inactive]
        self.mc_seed_assembly, self.mc_seed_tiles = self.makeSeedAssembly()

        self.mc_horizontal_affinities, self.mc_horizontal_transitions, self.mc_vertical_affinities, self.mc_vertical_transitions = self.makeHorizontalAffinitiesTransitions()

    def makeSeedAssembly(self):
        mc_tiles = []
        for i in range(1, self.cell_len - 1):
            #wire
            mc_tiles.append(Tile(eastWire, self.door_start_x + i, self.door_start_y))

        mc_tiles.append(Tile(punch_down_ds_neg_active,
                        self.door_start_x + 1, self.door_start_y + 1))
        mc_tiles.append(Tile(punch_down_ds_active, self.door_start_x +
                        self.cell_len - 2, self.door_start_y + 1))
        mc_tiles.append(Tile(mc_door_east_negative_inactive,
                        self.door_start_x - 1, self.door_start_y))
        mc_tiles.append(Tile(mc_door_handle_east_negative_inactive,
                        self.door_start_x - 1, self.door_start_y + 1))
        mc_tiles.append(Tile(mc_door_east_positive_inactive,
                        self.door_start_x + self.cell_len, self.door_start_y))
        mc_tiles.append(Tile(mc_door_handle_east_positive_inactive,
                        self.door_start_x + self.cell_len, self.door_start_y + 1))

        seed_assembly = Assembly()
        seed_assembly.setTiles(mc_tiles)

        return seed_assembly, mc_tiles










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


class Table(Gadget):
    def __init__(self, name="TableGadget", description="No Description", parent_gadget=None, iu_sys=None):
        super().__init__(name, description, parent_gadget)
        self.gadget_list = []






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


#data_state = State("1", Papaya_Whip, "1")
## Reprograamming Equality Gadget by sending a reset start cap then a data string and flip the equlities

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
