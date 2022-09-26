from LoadFile import InitialStateSet
import xml.etree.ElementTree as ET

from AutoTile import System
from UniversalClasses import State

from UniversalClasses import AffinityRule
from UniversalClasses import TransitionRule


def main(system, fileName):
    # The following variables are lists from the system
    temp = str(system.returnTemp())
    states = system.returnStates()
    initial_states = system.returnInitialStates()
    seed_assembly = system.returnSeedStates()
    seed_states = system.returnSeedStates()
    # The following variables are dictionaries from the system
    vertical_affinities = system.returnVerticalAffinityDict()
    horizontal_affinities = system.returnHorizontalAffinityDict()
    vertical_transitions = system.returnVerticalTransitionDict()
    horizontal_transitions = system.returnHorizontalTransitionDict()
    tiles = system.returnTiles()


    # Establish root and add temperature value
    root = ET.Element("System")
    root.set('Temp', temp)

    # Add all states used in the system
    all_states_tag = ET.Element("AllStates")
    root.append(all_states_tag)
    for state in states:
        label = state.returnLabel()
        color = state.returnColor()
        display_label = state.returnDisplayLabel()
        display_label_color = state.returnDisplayLabelColor()
        display_label_font = state.returnDisplayLabelFont()

        state_tag = ET.SubElement(all_states_tag, "State")
        state_tag.set('Label', label)
        state_tag.set('Color', color)
        state_tag.set('DisplayLabel', display_label)
        state_tag.set('DisplayLabelFont', display_label_font)
        state_tag.set('DisplayLabelColor', display_label_color)

    # Add all inital states
    initial_states_tag = ET.Element("InitialStates")
    root.append(initial_states_tag)
    for state in initial_states:
        label = state.returnLabel()
        color = state.returnColor()
        display_label = state.returnDisplayLabel()
        display_label_color = state.returnDisplayLabelColor()
        display_label_font = state.returnDisplayLabelFont()

        state_tag = ET.SubElement(initial_states_tag, "State")
        state_tag.set('Label', label)
        state_tag.set('Color', color)
        state_tag.set('DisplayLabel', display_label)
        state_tag.set('DisplayLabelFont', display_label_font)
        state_tag.set('DisplayLabelColor', display_label_color)

    # Add all seed states
    seed_states_tag = ET.Element("SeedStates")
    root.append(seed_states_tag)
    for state in seed_states:
        label = state.returnLabel()
        color = state.returnColor()
        x = str(state.getX())
        y = str(state.getY())
        display_label = state.returnDisplayLabel()
        display_label_color = state.returnDisplayLabelColor()
        display_label_font = state.returnDisplayLabelFont()

        state_tag = ET.SubElement(seed_states_tag, "State")
        state_tag.set('Label', label)
        state_tag.set('Color', color)
        state_tag.set('x', x)
        state_tag.set('y', y)
        state_tag.set('DisplayLabel', display_label)
        state_tag.set('DisplayLabelFont', display_label_font)
        state_tag.set('DisplayLabelColor', display_label_color)
    
    # Add all Tiles
    tiles_tag = ET.Element("Tiles")
    root.append(tiles_tag)
    for tile in tiles:
        label = tile.returnLabel()
        color = tile.returnColor()
        x = str(tile.getX())
        y = str(tile.getY())
        display_label = tile.returnDisplayLabel()
        display_label_color = tile.returnDisplayLabelColor()
        display_label_font = tile.returnDisplayLabelFont()

        state_tag = ET.SubElement(tiles_tag, "Tile")
        state_tag.set('Label', label)
        state_tag.set('Color', color)
        state_tag.set('x', x)
        state_tag.set('y', y)
        state_tag.set('DisplayLabel', display_label)
        state_tag.set('DisplayLabelFont', display_label_font)
        state_tag.set('DisplayLabelColor', display_label_color)
        

    # Add vertical transition rules
    vertical_transitions_tag = ET.Element("VerticalTransitions")
    root.append(vertical_transitions_tag)
    for key, value in vertical_transitions.items():
        label1 = key[0]
        label2 = key[1]
        for i in range(0, len(value), 2):
            label1Final = value[i]
            label2Final = value[i + 1]

            rule_tag = ET.SubElement(vertical_transitions_tag, "Rule")
            rule_tag.set('Label1', label1)
            rule_tag.set('Label2', label2)
            rule_tag.set('Label1Final', label1Final)
            rule_tag.set('Label2Final', label2Final)

    # Add horizontal transition rules
    horizontal_transitions_tag = ET.Element("HorizontalTransitions")
    root.append(horizontal_transitions_tag)
    for key, value in horizontal_transitions.items():
        label1 = key[0]
        label2 = key[1]
        for i in range(0, len(value), 2):
            label1Final = value[i]
            label2Final = value[i + 1]

            rule_tag = ET.SubElement(horizontal_transitions_tag, "Rule")
            rule_tag.set('Label1', label1)
            rule_tag.set('Label2', label2)
            rule_tag.set('Label1Final', label1Final)
            rule_tag.set('Label2Final', label2Final)

    # Add vertical affinity rules
    vertical_affinities_tag = ET.Element("VerticalAffinities")
    root.append(vertical_affinities_tag)
    for key, value in vertical_affinities.items():
        label1 = key[0]
        label2 = key[1]
        strength = str(value)

        rule_tag = ET.SubElement(vertical_affinities_tag, "Rule")
        rule_tag.set('Label1', label1)
        rule_tag.set('Label2', label2)
        rule_tag.set("Strength", strength)

    # Add horizontal affinity rules
    horizontal_affinities_tag = ET.Element("HorizontalAffinities")
    root.append(horizontal_affinities_tag)
    for key, value in horizontal_affinities.items():
        label1 = key[0]
        label2 = key[1]
        strength = str(value)

        rule_tag = ET.SubElement(horizontal_affinities_tag, "Rule")
        rule_tag.set('Label1', label1)
        rule_tag.set('Label2', label2)
        rule_tag.set("Strength", strength)

    tree = ET.ElementTree(root)
    with open(fileName[0], "wb") as file:
        tree.write(file, encoding='utf-8', xml_declaration=True)
