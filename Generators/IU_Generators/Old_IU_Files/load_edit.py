import sys
sys.path.insert(0, '.../..')
from .UniversalClasses import *

from util.loaders.assemblyLoader import returnSystemLoadXML_load_edit_py_file
from Assets.colors import waiting_color, inactive_color, inactive_waiting_color, active_color, active_waiting_color
from Assets.colors import reset_color, intermediate_accept_color, reject_color, complete_color
from Assets.colors import door_color, wire_color, writing_color, writing_inactive_color, border_color
colors_list = [waiting_color, inactive_color, inactive_waiting_color, active_color, active_waiting_color,
               reset_color, intermediate_accept_color, reject_color, complete_color, door_color, wire_color,
               writing_color, writing_inactive_color, border_color]

color_replacement_dict = {"waiting_color": waiting_color, "inactive_color": inactive_color, "inactive_waiting_color": inactive_waiting_color,
                          "active_color": active_color, "active_waiting_color": active_waiting_color, "reset_color": reset_color,
                          "intermediate_accept_color": intermediate_accept_color, "reject_color": reject_color, "complete_color": complete_color,
                          "door_color": door_color, "wire_color": wire_color, "writing_color": writing_color, "writing_inactive_color": writing_inactive_color,
                          "border_color": border_color}

""" symbol_replacement_dict = {"waiting_symbol": symbols.waiting_symbol, "inactive_symbol": symbols.inactive_symbol, "inactive_waiting_symbol": symbols.inactive_waiting_symbol,
                    "active_symbol": symbols.active_symbol, "active_waiting_symbol": symbols.active_waiting_symbol, "reset_symbol": symbols.reset_symbol,
                    "intermediate_accept_symbol": symbols.intermediate_accept_symbol, "reject_symbol": symbols.reject_symbol, "complete_symbol": symbols.complete_symbol,
                    "door_symbol": symbols.door_symbol, "wire_symbol": symbols.wire_symbol, "writing_symbol": symbols.writing_symbol,"writing_inactive_symbol": symbols.writing_inactive_symbol,
                    "border_symbol": symbols.border_symbol} """

var_char_replacement_dict = {"-": 'Neg', '=': "Eq", ")": "EndState", "*": "Any", "(": "StartState", " ": "Space", ",": "Comma", ".": "Period", "!": "Exclamation", "?": "Question", ":": "Colon", ";": "Semicolon",
                             "'": "Apostrophe", '"': "Quotation", "/": "Slash", "\\": "Backslash", "|": "Pipe", "+": "Add", "<": "LessThan", ">": "GreaterThan", "@": "At",
                             "#": "Pound", "$": "Dollar", "%": "Percent", "^": "Caret", "&": "And", "~": "Tilde", "`": "Backtick", "[": "LeftBracket", "]": "RightBracket",
                             "{": "StartDataString", "}": "EndDataString", "_": "_"}
def shift_tiles(tiles, amount_x=0, amount_y=0):
    for tile in tiles:
        tile.y += amount_y
        tile.x += amount_x
    return tiles


def verify_no_overlap(a1, a2):
    overlaps_list = []
    no_overlaps_bool = True
    a1_tiles = a1.returnTiles()
    a2_tiles = a2.returnTiles()
    for tile1 in a1_tiles:
        for tile2 in a2_tiles:
            if tile1.x == tile2.x and tile1.y == tile2.y:
                overlapping_tile_pair = (tile1, tile2)
                overlaps_list.append(overlapping_tile_pair)
                no_overlaps_bool = False
    return no_overlaps_bool, overlaps_list

def double_assembly(a1, dir):
    a1_tiles = a1.returnTiles()
    height = abs(a1.upMost) + abs(a1.downMost) + 1
    width = abs(a1.leftMost) + abs(a1.rightMost) + 1
    a2 = Assembly()
    a2_tiles = []
    if dir == "above":
        a2_tiles = shift_tiles(a1_tiles, 0, height + 1)
    elif dir == "below":
        a2_tiles = shift_tiles(a1_tiles, 0, -height - 1)
    elif dir == "left":
        a2_tiles = shift_tiles(a1_tiles, -width - 1, 0)
    elif dir == "right":
        a2_tiles = shift_tiles(a1_tiles, width + 1, 0)


    a2.setTiles(a2_tiles)
    no_ol_bool, ol_list = verify_no_overlap(a1, a2)
    if no_ol_bool:
        a2.setTiles(a2_tiles)
        return a2
    else:
        print("Overlapping tiles: ", ol_list)
        return None


def returnLoadedSystem(file):
    seed = returnSystemLoadXML_load_edit_py_file(file)
    seed_assembly = seed["seedAssembly"]
    double_assembly = seed_assembly
    return double_assembly


def makeColorsList(colors_write_file=None):
    """Writes the colors to the file"""
    if colors_write_file is None:
        colors_write_file = "Assets/Colors.txt"
    f_py = open("Assets/Colors.py", "r", encoding="utf-8")
    f = open(colors_write_file, "w", encoding="utf-8")
    colors_all_in_file_hex_key = {}
    colors_all_in_file_name_key = {}
    for line in f_py.readlines():
        if "=" in line:
            l_split = line.split("=")
            color_name = l_split[0].strip()
            l1 = l_split[1]
            if "#" in l_split[1]:
                l1 = l_split[1].split("#")[0]
                ch = '"'
                color_hex = l1.strip(ch).strip()

            colors_all_in_file_hex_key[color_hex] = color_name
            colors_all_in_file_name_key[color_name] = color_hex

    return colors_all_in_file_hex_key, colors_all_in_file_name_key


class writeToFile:
    def __init__(self, sys_dict=None, write_file_name=None, system=None):
        self.system = system
        if sys_dict is None:
            sys_dict = {"States": system.returnStates(), "InitialStates": system.returnInitialStates(), "SeedStates": system.returnSeedStates(),
                        "VerticalAffinities": system.returnVerticalAffinityList(), "HorizontalAffinities": system.returnHorizontalAffinityList(),
                        "VerticalTransitions": system.returnVerticalTransitionList(), "HorizontalTransitions": system.returnHorizontalTransitionList(),
                        "SeedAssembly": system.returnSeedAssembly()}

        self.states = sys_dict["States"]
        self.initial_states = sys_dict["InitialStates"]
        self.seed_states = sys_dict["SeedStates"]
        self.vertical_affinities = sys_dict["VerticalAffinities"]
        self.horizontal_affinities = sys_dict["HorizontalAffinities"]
        self.horizontal_transition_rules = sys_dict["HorizontalTransitions"]
        self.vertical_transition_rules = sys_dict["VerticalTransitions"]
        self.seed_assembly = sys_dict["SeedAssembly"]
        self.tiles = self.seed_assembly.returnTiles()
        self.write_file_name = write_file_name
        self.new_state_vars_dict = {}
        self.transition_rules_dict = {}
        self.affinities_dict = {}

    def writeStatesToFile(self, states_write_file=None):
        """Writes the states to the file"""
        states_lines_list = []

        if states_write_file is None:
            states_write_file = self.write_file_name

        f = open(states_write_file, "w", encoding="utf-8")
        # Format: label, color, display_label
        # f'{stateVarName} = State("{label}", "{color}", "{display_label}")/n'
        f.write("from UniversalClasses import State, Tile, Assembly, AffinityRule, TransitionRule, System \n")
        colors_all_hex, colors_all_names = makeColorsList()

        for state in self.states:
            c = None

            c = {i for i in color_replacement_dict if color_replacement_dict[i] == state.color}
            print(c)
            if c == None:
                c = state.color
                c = colors_all_hex.get(c, c)
                print(c)
            elif c == set():
                c = state.color

                c = colors_all_hex.get(c, c)
                print("Set: ", c, "State: ", state.label)
                #== "list":
                #c = c[0]
            else:
                c = c.pop()

            try:
                l = state.label
                if not (l.isalnum()):
                    for i in l:
                        if i.isalnum():
                            continue
                        else:
                            l = l.replace(i, var_char_replacement_dict.get(i, "_x_"))
                f_line = f'  {l} = State("{state.label}", {c}, "{state.display_label}") '
                states_lines_list.append(f_line)
                self.new_state_vars_dict[state.label] = l
                f.write(f'  {l} = State("{state.label}", {c}, "{state.display_label}") \n ')
            except:
                print("Char failure")

        f.close()
        print("States written to file")
        return states_lines_list, self.new_state_vars_dict

    def writeAffinityRulesToFile(self, affinity_rules_write_file=None, var_pairs_dict=None):
        """Writes the affinity rules to the file"""
        if affinity_rules_write_file is None:
            file = "Generators/IU_Generators/SpecGadgetGenerators/Xmls/Written_Affinities.xml"
            affinity_rules_write_file = file

        f = open(affinity_rules_write_file, "a", encoding="utf-8")
        # Format: label, color, display_label
        # f'{stateVarName} = State("{label}", "{color}", "{display_label}")/n'
        f.write("\n")
        affinity_rule_vars = []
        affinity_rules_vars_dict = {}
        affs = self.vertical_affinities + self.horizontal_affinities

        if var_pairs_dict is None:
            var_pairs_dict = self.new_state_vars_dict

        for affinity_rule in affs:
            aff_var_name = ""
            if var_pairs_dict is not None:
                if affinity_rule.label1 in var_pairs_dict.keys():
                    aff_var_name = var_pairs_dict[affinity_rule.label1] + "_"
                else:
                    aff_var_name = affinity_rule.label1 + "_"
                if affinity_rule.label2 in var_pairs_dict.keys():
                    aff_var_name = aff_var_name + var_pairs_dict[affinity_rule.label2] + "_" + affinity_rule.direction + "_" + affinity_rule.strength + "_" + "aff"
                else:
                    aff_var_name = aff_var_name + affinity_rule.label2 + "_" + affinity_rule.direction + "_" + affinity_rule.strength + "_" + "aff"

            else:
                aff_var_name = affinity_rule.label1 + "_" + affinity_rule.label2 + "_" + affinity_rule.direction + "_" + affinity_rule.strength + "_" + "aff"

            f.write(f'  {aff_var_name} = AffinityRule("{affinity_rule.label1}", "{affinity_rule.label2}", "{affinity_rule.direction}", {affinity_rule.strength}) \n ')
            affinity_rule_vars.append(aff_var_name)
            affinity_rules_vars_dict[(affinity_rule.label1, affinity_rule.label2, affinity_rule.dir, affinity_rule.strength)] = (aff_var_name, affinity_rule)

        f.close()
        print("Affinity rules written to file")
        return affinity_rule_vars, affinity_rules_vars_dict
    def writeTransitionRulesToFile(self, transition_rules_write_file=None, var_pairs_dict=None):
        """Writes the transition rules to the file"""
        if transition_rules_write_file is None:
            file = "Generators/IU_Generators/SpecGadgetGenerators/Xmls/Written_Transitions.xml"
            transition_rules_write_file = file

        f = open(transition_rules_write_file, "a", encoding="utf-8")
        # Format: label, color, display_label
        # f'{stateVarName} = State("{label}", "{color}", "{display_label}")/n'
        f.write("\n")
        transition_rule_vars = []
        transition_rule_vars_dict = {}
        trs = self.vertical_transition_rules + self.horizontal_transition_rules
        for transition_rule in trs:
            tr_var_name = ""
            if var_pairs_dict is not None:
                if transition_rule.label1 in var_pairs_dict.keys():
                    tr_var_name = var_pairs_dict[transition_rule.label1] + "_"
                else:
                    tr_var_name = transition_rule.label1 + "_"
                if transition_rule.label2 in var_pairs_dict.keys():
                    tr_var_name = tr_var_name + var_pairs_dict[transition_rule.label2]
                else:
                    tr_var_name = tr_var_name + transition_rule.label2
            else:
                tr_var_name = transition_rule.label1 + "_" + transition_rule.label2

            tr_var_name = tr_var_name + "_" + transition_rule.direction + "_tr"


            f.write(f'  {tr_var_name} = TransitionRule("{transition_rule.label1}", "{transition_rule.label2}", "{transition_rule.direction}") \n ')
            transition_rule_vars.append(tr_var_name)
            transition_rule_vars_dict[(transition_rule.label1, transition_rule.label2, transition_rule.dir)] = (tr_var_name, transition_rule)

            return transition_rule_vars, transition_rule_vars_dict









if __name__ == "__main__":
    #system_dict = LoadFile.readxml("uniaryPunchTwoCells.xml")
    #system_dict = assemblyLoader.returnSystemLoadXML("uniaryPunchTwoCells.xml")
    #seed_assembly = system_dict["seedAssembly"]
    print("Loaded")
    print(makeColorsList()[0])

    #double_assembly = seed_assembly
