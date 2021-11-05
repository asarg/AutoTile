import xml.etree.ElementTree as ET

from UniversalClasses import State
from UniversalClasses import AffinityRule
from UniversalClasses import TransitionRule

from UniversalClasses import System, AffinityRule, TransitionRule


def main(currentSystem, file):
    # Retrieve currentSystem's lists
    # currentSystem's Affinity Rules
    current_VerticalAffinityRules = currentSystem.returnVerticalAffinityList()
    current_HorizontalAffinityRules = currentSystem.returnHorizontalAffinityList()
    # currentSystem's Transition Rules
    current_VerticalTransitionRules = currentSystem.returnVerticalTransitionList()
    current_HorizontalTransitionRules = currentSystem.returnHorizontalTransitionList()
    # currentSystem's States
    current_SeedStateSet = currentSystem.returnSeedStates()
    current_InitialStateSet = currentSystem.returnInitialStates()
    current_CompleteStateSet = currentSystem.returnStates()  # All states in the system

    # Does the new state in secondSystem already exist in currentSystem?
    state_duplicated = False
    # Does the new rule in secondSystem alread exist in currentSystem?
    rule_duplicated = False

    tree = ET.parse(file)
    treeroot = tree.getroot()

    # Attach secondSystem's All States to currentSystem
    for state_tag in treeroot.findall('AllStates/State'):
        label = state_tag.get("Label")
        # If the label is the pot (X), don't append a "$".
        if(label != "X"):
            label = label + "$"
        color = state_tag.get("Color")
        for state in current_CompleteStateSet:
            if(state.returnLabel() == label):
                state_duplicated = True
                break
        if(not state_duplicated):
            tempState = State(label, color)
            current_CompleteStateSet.append(tempState)
        state_duplicated = False

    # Attach secondSystem's Initial States
    for state_tag in treeroot.findall("InitialStates/State"):
        label = state_tag.get("Label")
        # If the label is the pot (X), don't append a "$".
        if(label != "X"):
            label = label + "$"
        color = state_tag.get("Color")
        for state in current_InitialStateSet:
            if(state.returnLabel() == label):
                state_duplicated = True
                break
        if(not state_duplicated):
            tempState = State(label, color)
            current_InitialStateSet.append(tempState)
        state_duplicated = False

    # Seed States
    for state_tag in treeroot.findall("SeedStates/State"):
        label = state_tag.get("Label")
        # If the label is the pot (X), don't append a "$".
        if(label != "X"):
            label = label + "$"
        color = state_tag.get("Color")

        for state in current_SeedStateSet:
            if(state.returnLabel() == label):
                state_duplicated = True
                break
        if(not state_duplicated):
            tempState = State(label, color)
            current_SeedStateSet.append(tempState)
        state_duplicated = False

    # Vertical Transitions
    for rule_tag in treeroot.findall("VerticalTransitions/Rule"):
        label1 = rule_tag.get("Label1")
        label2 = rule_tag.get("Label2")
        label1Final = rule_tag.get("Label1Final")
        label2Final = rule_tag.get("Label2Final")

        # If the label is the pot (X), don't append a "$".
        if(label1 != "X"):
            label1 = label1 + "$"
        if(label2 != "X"):
            label2 = label2 + "$"
        if(label1Final != "X"):
            label1Final = label1Final + "$"
        if(label2Final != "X"):
            label2Final = label2Final + "$"

        # Attach secondSystem's Vertical Transitions if they don't already exist in currentSystem
        for rule in current_VerticalTransitionRules:
            if(rule.returnLabel1() == label1 and rule.returnLabel2() == label2 and rule.returnLabel1Final() == label1Final and rule.returnLabel2Final() == label2Final):
                rule_duplicated = True
                break
        if(not rule_duplicated):
            tempRule = TransitionRule(
                label1, label2, label1Final, label2Final, "v")
            current_VerticalTransitionRules.append(tempRule)
        rule_duplicated = False

    # Horizontal Transitions
    for rule_tag in treeroot.findall("HorizontalTransitions/Rule"):
        label1 = rule_tag.get("Label1")
        label2 = rule_tag.get("Label2")
        label1Final = rule_tag.get("Label1Final")
        label2Final = rule_tag.get("Label2Final")

        # If the label is the pot (X), don't append a "$".
        if(label1 != "X"):
            label1 = label1 + "$"
        if(label2 != "X"):
            label2 = label2 + "$"
        if(label1Final != "X"):
            label1Final = label1Final + "$"
        if(label2Final != "X"):
            label2Final = label2Final + "$"

        # Attach secondSystem's Horizontal Transitions if they don't already exist in currentSystem
        for rule in current_HorizontalTransitionRules:
            if(rule.returnLabel1() == label1 and rule.returnLabel2() == label2 and rule.returnLabel1Final() == label1Final and rule.returnLabel2Final() == label2Final):
                rule_duplicated = True
                break
        if(not rule_duplicated):
            tempRule = TransitionRule(
                label1, label2, label1Final, label2Final, "v")
            current_HorizontalTransitionRules.append(tempRule)
        rule_duplicated = False

    # Vertical Affinities
    for rule_tag in treeroot.findall("VerticalAffinities/Rule"):
        label1 = rule_tag.get("Label1")
        label2 = rule_tag.get("Label2")
        strength = rule_tag.get("Strength")

        if(label1 != "X"):
            label1 = label1 + "$"
        if(label2 != "X"):
            label2 = label2 + "$"

        # Attach secondSystem's Vertical Affinities if they don't already exist in currentSystem
        for rule in current_VerticalAffinityRules:
            if(rule.returnLabel1() == label1 and rule.returnLabel2() == label2):
                rule_duplicated = True
                break
        if(not rule_duplicated):
            tempRule = AffinityRule(label1, label2, "h", strength)
            current_VerticalAffinityRules.append(tempRule)
        rule_duplicated = False

    # Horizontal Affinities
    for rule_tag in treeroot.findall("HorizontalAffinities/Rule"):
        label1 = rule_tag.get("Label1")
        label2 = rule_tag.get("Label2")
        strength = rule_tag.get("Strength")

        if(label1 != "X"):
            label1 = label1 + "$"
        if(label2 != "X"):
            label2 = label2 + "$"

        # Attach secondSystem's Vertical Affinities if they don't already exist in currentSystem
        for rule in current_HorizontalAffinityRules:
            if(rule.returnLabel1() == label1 and rule.returnLabel2() == label2):
                rule_duplicated = True
                break
        if(not rule_duplicated):
            tempRule = AffinityRule(label1, label2, "h", strength)
            current_HorizontalAffinityRules.append(tempRule)
        rule_duplicated = False
