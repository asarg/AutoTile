from UniversalClasses import State, AffinityRule, TransitionRule, System, Assembly, Tile


def seed_states_label_change(states_list, symbol):
    new_states_list = []
    for state in states_list:
        state.label += symbol
        new_states_list.append(state)
    return new_states_list


def seed_assembly_shift_tiles(starting_assembly, old_x, old_y, new_x, new_y, symbol=None):
    assembly_tiles = starting_assembly.tiles
    new_assembly_tiles = []

    offset_x = new_x - old_x
    offset_y = new_y - old_y

    for tile in assembly_tiles:
        tile.x += offset_x
        tile.y += offset_y
        if symbol is not None:
            tile.state.label += symbol
        new_assembly_tiles.append(tile)

    return new_assembly_tiles


def combineSeedAssemblies(sys1, sys1_comboPointPair, sys2, sys2_comboPointPair, comboPointOffsetPair, symbol=None):
    sys1_seed_assembly = sys1.seed_assembly
    sys2_seed_assembly = sys2.seed_assembly
    new_assembly = Assembly()

    sys1_x, sys1_y = sys1_comboPointPair
    sys2_x, sys2_y = sys2_comboPointPair

    given_offset_x, given_offset_y = comboPointOffsetPair

    sys2_new_x = sys1_x + given_offset_x
    sys2_new_y = sys1_y + given_offset_y

    sys2_new_tiles = seed_assembly_shift_tiles(
        sys2_seed_assembly, sys2_x, sys2_y, sys2_new_x, sys2_new_y)
    combined_tiles = sys1_seed_assembly.tiles + sys2_new_tiles

    new_assembly.setTiles(combined_tiles)

    return new_assembly


def combineSystemsAndSeedAssemblies(sys1, sys1_comboPointPair, sys2, sys2_comboPointPair, comboPointOffsetPair, symbol=None):
    new_sys = main(sys1, sys2, symbol)
    new_seed_assembly = combineSeedAssemblies(
        sys1, sys1_comboPointPair, sys2, sys2_comboPointPair, comboPointOffsetPair, symbol)
    new_sys.setSeedAssembly(new_seed_assembly)
    new_seed_states = sys1.seed_states + \
        seed_states_label_change(sys2.seed_states, symbol)
    new_sys.setSeedStates(new_seed_states)
    return new_sys


def main(currentSystem, secondSystem, symbol=None):
    # Does the new state in secondSystem already exist in currentSystem?
    state_duplicated = False
    # Does the new rule in secondSystem alread exist in currentSystem?
    rule_duplicated = False

    if(symbol == None):
        symbol = input("Enter the symbol marker for System #2: ")

    # Gather currentSystem's lists
    current_CompleteStateSet = currentSystem.returnStates()
    current_InitialStateSet = currentSystem.returnInitialStates()
    current_SeedStateSet = currentSystem.returnSeedStates()
    current_VerticalAffinityRules = currentSystem.returnVerticalAffinityList()
    current_HorizontalAffinityRules = currentSystem.returnHorizontalAffinityList()
    current_VerticalTransitionRules = currentSystem.returnVerticalTransitionList()
    current_HorizontalTransitionRules = currentSystem.returnHorizontalTransitionList()

    current_temp = currentSystem.returnTemp()

    # Gather secondSystem's lists
    second_CompleteStateSet = secondSystem.returnStates()
    second_InitialStateSet = secondSystem.returnInitialStates()
    second_SeedStateSet = secondSystem.returnSeedStates()
    second_VerticalAffinityRules = secondSystem.returnVerticalAffinityList()
    second_HorizontalAffinityRules = secondSystem.returnHorizontalAffinityList()
    second_VerticalTransitionRules = secondSystem.returnVerticalTransitionList()
    second_HorizontalTransitionRules = secondSystem.returnHorizontalTransitionList()

    # Attach secondSystem's All States (with symbol marker) to currentSystem
    # All States
    for new_state in second_CompleteStateSet:
        second_label = new_state.returnLabel() + symbol
        second_color = new_state.returnColor()

        for original_state in current_CompleteStateSet:
            if(original_state.returnLabel() == second_label):
                state_duplicated = True
                break
        if(not state_duplicated):
            tempState = State(second_label, second_color)
            current_CompleteStateSet.append(tempState)
        state_duplicated = False

    # Initial States
    for new_state in second_InitialStateSet:
        second_label = new_state.returnLabel() + symbol
        second_color = new_state.returnColor()

        for original_state in current_InitialStateSet:
            if(original_state.returnLabel() == second_label):
                state_duplicated = True
                break
        if(not state_duplicated):
            tempState = State(second_label, second_color)
            current_InitialStateSet.append(tempState)
        state_duplicated = False

    # Ignoring secondSystem's seed list because currentSystem has priority

    # Vertical Transitions
    for new_rule in second_VerticalTransitionRules:
        second_label1 = new_rule.returnLabel1() + symbol
        second_label2 = new_rule.returnLabel2() + symbol
        second_label1Final = new_rule.returnLabel1Final() + symbol
        second_label2Final = new_rule.returnLabel2Final() + symbol

        for original_rule in current_VerticalTransitionRules:
            if(original_rule.returnLabel1() == second_label1 and original_rule.returnLabel2() == second_label2 and original_rule.returnLabel1Final() == second_label1Final and original_rule.returnLabel2Final() == second_label2Final):
                rule_duplicated = True
                break
        if(not rule_duplicated):
            tempRule = TransitionRule(second_label1, second_label2, second_label1Final, second_label2Final, "v")
            current_VerticalTransitionRules.append(tempRule)
        rule_duplicated = False

    # Horizontal Transitions
    for new_rule in second_HorizontalTransitionRules:
        second_label1 = new_rule.returnLabel1() + symbol
        second_label2 = new_rule.returnLabel2() + symbol
        second_label1Final = new_rule.returnLabel1Final() + symbol
        second_label2Final = new_rule.returnLabel2Final() + symbol

        for original_rule in current_HorizontalTransitionRules:
            if(original_rule.returnLabel1() == second_label1 and original_rule.returnLabel2() == second_label2 and original_rule.returnLabel1Final() == second_label1Final and original_rule.returnLabel2Final() == second_label2Final):
                rule_duplicated = True
                break
        if(not rule_duplicated):
            tempRule = TransitionRule(second_label1, second_label2, second_label1Final, second_label2Final, "h")
            current_HorizontalTransitionRules.append(tempRule)
        rule_duplicated = False

    # Vertical Affinities
    for new_rule in second_VerticalAffinityRules:
        second_label1 = new_rule.returnLabel1() + symbol
        second_label2 = new_rule.returnLabel2() + symbol
        second_strength = new_rule.returnStr()

        for original_rule in current_VerticalAffinityRules:
            if(original_rule.returnLabel1() == second_label1 and original_rule.returnLabel2() == second_label2):
                rule_duplicated = True
                break
        if(not rule_duplicated):
            tempRule = AffinityRule(second_label1, second_label2, "v", second_strength)
            current_VerticalAffinityRules.append(tempRule)

    # Horizontal Affinities
    for new_rule in second_HorizontalAffinityRules:
        second_label1 = new_rule.returnLabel1() + symbol
        second_label2 = new_rule.returnLabel2() + symbol
        second_strength = new_rule.returnStr()

        for original_rule in current_HorizontalAffinityRules:
            if(original_rule.returnLabel1() == second_label1 and original_rule.returnLabel2() == second_label2):
                rule_duplicated = True
                break
        if(not rule_duplicated):
            tempRule = AffinityRule(second_label1, second_label2, "h", second_strength)
            current_HorizontalAffinityRules.append(tempRule)

    return System(current_temp, current_CompleteStateSet, current_InitialStateSet, current_SeedStateSet, current_VerticalAffinityRules, current_HorizontalAffinityRules, current_VerticalTransitionRules, current_HorizontalTransitionRules)
