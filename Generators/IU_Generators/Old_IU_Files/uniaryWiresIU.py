from .UniversalClasses import State, AffinityRule, TransitionRule, System, Tile, Assembly
from Generators.IU_Generators.binaryStates import eastWire, end_data_string, ds_1, endcap_doors_west_list, endcap_doors_east_list, endcap_door_east_inactive
import SaveFile
import LoadFile
import sys
import re
import Generators.IU_Generators.Old_IU_Files.IntrinsicUniversality as IU
from util.loaders.assemblyLoader import returnSystemLoadXML_load_edit_py_file
from Assets.colors import waiting_color, inactive_color, inactive_waiting_color, active_color, active_waiting_color
from Assets.colors import reset_color, intermediate_accept_color, reject_color, complete_color
from Assets.colors import door_color, wire_color, writing_color, writing_inactive_color, border_color
import Generators.IU_Generators.binary_symbols_colors as symbols
from Generators.IU_Generators.Old_IU_Files.load_edit import writeToFile, makeColorsList



def make_east_wires():
    """Makes the east wires in table"""
    east_wires = []
    for i in range(0, 36):
        for j in range(0, 60, 4):
            east_wires.append(Tile(eastWire, i, j))
    return east_wires

def make_system():
    """Makes the system with the east wires"""
    east_wires = make_east_wires()
    seed_a = Assembly()
    seed_a.tiles = east_wires
    states_list = [eastWire, ds_1] + endcap_doors_east_list
    affinity_rules = [AffinityRule(eastWire.label, ds_1.label, "h", 1), AffinityRule(ds_1.label, eastWire.label, "h", 1),
                      AffinityRule(eastWire.label, eastWire.label, "h", 1), AffinityRule(ds_1.label, ds_1.label, "h", 1), AffinityRule(  eastWire.label, end_data_string.label, "h", 1), AffinityRule(end_data_string.label, eastWire.label, "h", 1),
                      AffinityRule(end_data_string.label, ds_1.label, "h", 1), AffinityRule(ds_1.label, endcap_door_east_inactive.label, "h", 1)]
    transition_rules = [TransitionRule(ds_1.label, eastWire.label, eastWire.label, ds_1.label, "h")]
    return System(1, states_list, [], states_list, [], affinity_rules, [], transition_rules, [], [], seed_a)


class UniaryTable:
    def __init__(self, sys_dict):
        self.sys_dictionary = sys_dict

class MacroCell:
    def __init__(self, sys_dict):
        self.sys_dictionary = sys_dict

















if __name__ == "__main__":
    #file = "Generators/IU_Generators/SpecGadgetGenerators/Xmls/UniaryPunchTwoCells.xml"

    #sysdict = returnSystemLoadXML_load_edit_py_file(file)
    """ states_dict = sysdict["States"]
    initial_states_dict = sysdict["InitialStates"]
    seed_states_dict = sysdict["SeedStates"]
    vert_aff_rules_dict = sysdict["VerticalAffinities"]
    hori_aff_rules_dict = sysdict["HorizontalAffinities"]
    vert_tr_rules_dict = sysdict["VerticalTransitions"]
    hori_tr_rules_dict = sysdict["HorizontalTransitions"]
    seed_assembly_dict = sysdict["SeedAssembly"]
    temp = sysdict["Temp"]
    system = System(temp, states_dict, initial_states_dict, seed_states_dict, vert_aff_rules_dict, hori_aff_rules_dict, vert_tr_rules_dict, hori_tr_rules_dict, seed_assembly = seed_assembly_dict)
    states_write_file = "Generators/IU_Generators/write_states.txt"
    writeToFile(sysdict, states_write_file, system).writeStatesToFile(states_write_file) """

    eq_class = IU.IUGenerators("EqualityGadgets")
    eq_sys = eq_class.EqualityGadgetGenerator()

    states_write_file = "Generators/IU_Generators/all_states.txt"
    writeToFile(None, states_write_file, eq_sys).writeStatesToFile(states_write_file)
