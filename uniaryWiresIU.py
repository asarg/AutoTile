from UniversalClasses import State, AffinityRule, TransitionRule, System, Tile, Assembly
from Generators.IU_Generators.binaryStates import eastWire, end_data_string, ds_1, endcap_doors_west_list, endcap_doors_east_list, endcap_door_east_inactive
import SaveFile
import LoadFile
import sys



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
                      AffinityRule(eastWire.label, eastWire.label, "h", 1), AffinityRule(ds_1.label, ds_1.label, "h", 1), AffinityRule(
                          eastWire.label, end_data_string.label, "h", 1), AffinityRule(end_data_string.label, eastWire.label, "h", 1),
                      AffinityRule(end_data_string.label, ds_1.label, "h", 1), AffinityRule(ds_1.label, endcap_door_east_inactive.label, "h", 1)]
    transition_rules = [TransitionRule(ds_1.label, eastWire.label, eastWire.label, ds_1.label, "h")]
    return System(1, states_list, [], states_list, [], affinity_rules, [], transition_rules, [], [], seed_a)


class UniaryTable:
    def __init__(self, sys_dict):
        self.sys_dictionary = sys_dict


if __name__ == "__main__":
    system = make_system()
    SaveFile.main(system, ["uniaryWiresIUTest.xml"])
