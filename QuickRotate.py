import copy

from UniversalClasses import System, AffinityRule, TransitionRule

# Major Note: Currently rotates a system by 90 degrees CW


def main(currentSystem):
    global tempSystem

    tempSystem = rotate(currentSystem)




def rotate(currentSystem):
    tempSystem = copy.deepcopy(currentSystem)

    # Reset tempSystem's dictionaries
    tempSystem.clearVerticalAffinityDict()
    tempSystem.clearHorizontalAffinityDict()
    tempSystem.clearVerticalTransitionDict()
    tempSystem.clearHorizontalTransitionDict()

    # Reset tempSystem's lists
    tempSystem.clearVerticalAffinityList()
    tempSystem.clearHorizontalAffinityList()
    tempSystem.clearVerticalTransitionList()
    tempSystem.clearHorizontalTransitionList()

    # Shallow copies of the currentSystem's lists
    currentVAffinityList = currentSystem.returnVerticalAffinityList()
    currentHAffinityList = currentSystem.returnHorizontalAffinityList()
    currentVTransitionList = currentSystem.returnVerticalTransitionList()
    currentHTransitionList = currentSystem.returnHorizontalTransitionList()

    # Shallow copies of the tempSystem's lists
    tempVAffinityList = tempSystem.returnVerticalAffinityList()
    tempHAffinityList = tempSystem.returnHorizontalAffinityList()
    tempVTransitionList = tempSystem.returnVerticalTransitionList()
    tempHTransitionList = tempSystem.returnHorizontalTransitionList()

    # If the current rule is a vertical affinity, swap label1's and label2's positions and change dir to horizontal.
    for rule in currentVAffinityList:
        label1 = rule.returnLabel1()
        label2 = rule.returnLabel2()
        dir = "v"
        strength = rule.returnStr()

        tempRule = AffinityRule(label2, label1, dir, strength)
        tempHAffinityList.append(tempRule)

    # If the current rule is a horizontal affinity, don't touch label1 and label2, but change dir to horizontal.
    for rule in currentHAffinityList:
        label1 = rule.returnLabel1()
        label2 = rule.returnLabel2()
        dir = "h"
        strength = rule.returnStr()

        tempRule = AffinityRule(label1, label2, dir, strength)
        tempVAffinityList.append(tempRule)

    # Apply the same principles we used in vertical affinities for vertical transitions.
    for rule in currentVTransitionList:
        label1 = rule.returnLabel1()
        label2 = rule.returnLabel2()
        label1Final = rule.returnLabel1Final()
        label2Final = rule.returnLabel2Final()
        dir = "v"

        tempRule = TransitionRule(
            label2, label1, label2Final, label1Final, dir)
        tempHTransitionList.append(tempRule)

    # And the same thing for horizontal transitions.
    for rule in currentHTransitionList:
        label1 = rule.returnLabel1()
        label2 = rule.returnLabel2()
        label1Final = rule.returnLabel1Final()
        label2Final = rule.returnLabel2Final()
        dir = "h"

        tempRule = TransitionRule(
            label1, label2, label1Final, label2Final, dir)
        tempVTransitionList.append(tempRule)

    # Translate tempSystem's lists into dictionaries
    tempSystem.translateListsToDicts()

    return tempSystem
