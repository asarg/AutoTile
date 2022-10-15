from UniversalClasses import State, AffinityRule, System, TransitionRule, Tile, Assembly
from Assets.colors import *
from binaryStates import *

class Gadget:
    def __init__(self):
        self.name = None
        self.seed_states = None
        self.seed_assembly = None
        self.states = None
        self.initial_states = []
        self.available_edges = []
        self.state_affinities = {}
        self.state_transitions = {}


class SignalTransmitter:
    def __init__(self, signal_recived, signal_sent):
        self.signal_recived = signal_recived
        self.signal_sent = signal_sent





class SignalArc:
    def __init__(self):
        self.example = True
        self.initial_states = []
        self.seed_states = []
        self.states = []
        self.affinity_rules = {}
        self.transition_rules = {}
        self.tiles = []


    """ def __init__(self, startState, endState, startCoords, endCoords, length=5, input_gadget=None, output=None):
        self.startState = startState
        self.endState = endState


    def arcStatesInactive(self):
        return self.startState.active == False and self.endState.active == False """

    def buildArc(self):
        if self.arcStatesInactive():
            return None
        else:
            return self.buildArc()

    def makeSeedAssembly(self):

        return Assembly()