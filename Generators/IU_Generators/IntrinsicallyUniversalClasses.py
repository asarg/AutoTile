from UniversalClasses import State, AffinityRule, System, TransitionRule, Tile, Assembly
from Assets.colors import *


class StateTypeBuilder:
    # This class is used to build states
    # A state has not just the Attributes of a State, but also the Attributes of a Unit State
    # It has several attributes that are not in the State class
    def __init__(self):
        # Is the state active?
        #
        pass

class UnitState(State):
    def __init__(self):
        self.short_name
    def __init__(self, label, color, display_label=None):
        State.__init__(self, label, color, display_label)
        self.short_name
        self.category


class StateConstructor:
    def __init__(self):
        self.canTravelOnWire = None # True, False, or With Special Rules

    def wireTravelRules(self, canTravelOnWire=False, canTravelOnWireWithSpecialRules=False):

        self.canTravelOnWire = canTravelOnWire
        self.canTravelOnWireWithSpecialRules = canTravelOnWireWithSpecialRules


        pass


def WireInteractions():
    # State Can Have Affinities With Wire(s) in every direction
    # Wires have a direction and they have available affinity directions
    pass

def LabelConstructor():
    pass

def DisplayLabelConstructor():
    pass

# Things a Unit State Has:
    """
    1. A Label
    2. A Category
    """
# State Categories:

"""
1. Wire
2. Direction
3. Status (Inactive, Active, Complete, Reject, Accept, Intermediate Accept, Passing Signal, Reset, Reprogram)
4. Signal
5. Data State
6. Gate
7. Door

"""