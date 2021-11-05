import copy

from UniversalClasses import System, AffinityRule, TransitionRule


def reflect_across_x(currentSystem):
    global tempSystem
    tempSystem = copy.deepcopy(currentSystem)

    # Note: Since this is a reflection across the X-axis...
    # then only vertical affinities and transitions change.

    # Still have to reset tempSystem's dictionaries
    tempSystem.clearVerticalAffinityDict()
    tempSystem.clearHorizontalAffinityDict()
    tempSystem.clearVerticalTransitionDict()
    tempSystem.clearHorizontalTransitionDict()

    # But only reset tempSystem's vertical lists
    tempSystem.clearVerticalAffinityList()
    tempSystem.clearVerticalTransitionList()

    # Shallow copies of currentSystem's vertical lists
    currentVAffinityList = currentSystem.returnVerticalAffinityList()
    currentVTransitionList = currentSystem.returnVerticalTransitionList()

    # Shallow copies of the tempSystem's vertical lists
    tempVAffinityList = tempSystem.returnVerticalAffinityList()
    tempVTransitionList = tempSystem.returnVerticalTransitionList()

    # Reflect Vertical Affinities for tempSystem
    for rule in currentVAffinityList:
        label1 = rule.returnLabel1()
        label2 = rule.returnLabel2()
        dir = "v"
        strength = rule.returnStr()

        tempRule = AffinityRule(label2, label1, dir, strength)
        tempVAffinityList.append(tempRule)

    # Reflect Vertical Transitions for tempSystem
    for rule in currentVTransitionList:
        label1 = rule.returnLabel1()
        label2 = rule.returnLabel2()
        label1Final = rule.returnLabel1Final()
        label2Final = rule.returnLabel2Final()
        dir = "v"

        tempRule = TransitionRule(
            label2, label1, label2Final, label1Final, dir)
        tempVTransitionList.append(tempRule)

    # Translate tempSystem's lists into dictionaries
    tempSystem.translateListsToDicts()


def reflect_across_y(currentSystem):
    global tempSystem
    tempSystem = copy.deepcopy(currentSystem)

    # Note: Since this is a reflection across the Y-axis...
    # then only horizontal affinities and transitions change.

    # Still have to reset tempSystem's dictionaries
    tempSystem.clearVerticalAffinityDict()
    tempSystem.clearHorizontalAffinityDict()
    tempSystem.clearVerticalTransitionDict()
    tempSystem.clearHorizontalTransitionDict()

    # But only reset tempSystem's horizontal lists
    tempSystem.clearHorizontalAffinityList()
    tempSystem.clearHorizontalTransitionList()

    # Shallow copies of currentSystem's horizontal lists
    currentHAffinityList = currentSystem.returnHorizontalAffinityList()
    currentHTransitionList = currentSystem.returnHorizontalTransitionList()

    # Shallow copies of the tempSystem's horizontal lists
    tempHAffinityList = tempSystem.returnHorizontalAffinityList()
    tempHTransitionList = tempSystem.returnHorizontalTransitionList()

    # Reflect Horizontal Affinities for tempSystem
    for rule in currentHAffinityList:
        label1 = rule.returnLabel1()
        label2 = rule.returnLabel2()
        dir = "h"
        strength = rule.returnStr()

        tempRule = AffinityRule(label2, label1, dir, strength)
        tempHAffinityList.append(tempRule)

    # Reflect Horizontal Transitions for tempSystem
    for rule in currentHTransitionList:
        label1 = rule.returnLabel1()
        label2 = rule.returnLabel2()
        label1Final = rule.returnLabel1Final()
        label2Final = rule.returnLabel2Final()
        dir = "h"

        tempRule = TransitionRule(
            label2, label1, label2Final, label1Final, dir)
        tempHTransitionList.append(tempRule)

    # Translate tempSystem's lists into dictionaries
    tempSystem.translateListsToDicts()
