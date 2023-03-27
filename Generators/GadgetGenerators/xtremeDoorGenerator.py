from UniversalClasses import *
import Assets.colors as colors
from Generators.IU_Generators.binaryStates import border_state, eastWire, signal_door_east_inactive, signal_door_handle_east_inactive, trap_door_inactive, toggle_lock_door_handle_north_active, toggle_lock_door_handle_north_inactive, toggle_lock_door_handle_north_trigger_south, toggle_lock_door_handle_south_active, agent_state, toggle_lock_door_handle_south_inactive, toggle_lock_door_handle_south_trigger_north, trap_door_inactive, trap_door_active, trap_door_used, signal_door_east_active, signal_door_pass_toggle_south, signal_door_pass_toggle_north, signal_door_east_open, signal_door_east_reset_walk, signal_door_east_reset_walk_border, northEastWire, southEastWire


class Door:
    def __init__(self):
        states = []
        initial_states = []
        seed_states = []
        tiles = []

    def makeAffinitiesTransitions(self):
        h_aff = [AffinityRule(agent_state.label, eastWire.label, 1),
                 AffinityRule(eastWire.label, agent_state.label, 1),
                 AffinityRule(agent_state.label, signal_door_east_inactive.label, 1),
                 AffinityRule(agent_state.label, signal_door_east_active.label, 1),
                 AffinityRule(agent_state.label, signal_door_east_open.label, 1)]
        v_aff = [AffinityRule(toggle_lock_door_handle_north_active.label, signal_door_east_active.label, 1),
                 AffinityRule(toggle_lock_door_handle_north_active.label, signal_door_east_open.label, 1),
                 AffinityRule(signal_door_east_reset_walk_border.label, border_state.label, 1),
                 AffinityRule(agent_state.label, trap_door_active.label, 1),
                 AffinityRule(trap_door_active.label, agent_state.label,  1),
                 ]
        h_tr = [TransitionRule(agent_state.label, eastWire.label, eastWire.label, agent_state.label, "h"),
                TransitionRule(agent_state.label, signal_door_east_inactive.label, agent_state.label, signal_door_east_active.label, "h"),
                TransitionRule(agent_state.label, signal_door_east_open.label, signal_door_east_reset_walk_border.label, agent_state.label, "h"),
                TransitionRule(signal_door_east_reset_walk.label, eastWire.label, eastWire.label, signal_door_east_reset_walk_border.label, "h"),
                TransitionRule(toggle_lock_door_handle_north_active.label, trap_door_used.label, toggle_lock_door_handle_north_trigger_south.label, trap_door_inactive.label, "h"),
                TransitionRule( toggle_lock_door_handle_south_active.label, trap_door_inactive.label,
                                toggle_lock_door_handle_south_active.label, trap_door_active.label, "h"),
                TransitionRule(toggle_lock_door_handle_south_active.label, trap_door_used.label,
                               toggle_lock_door_handle_south_trigger_north.label,  trap_door_inactive.label, "h"),
                TransitionRule(toggle_lock_door_handle_north_active.label, trap_door_inactive.label,
                               toggle_lock_door_handle_north_active.label, trap_door_active.label, "h"),
                ]

        v_tr = [TransitionRule(toggle_lock_door_handle_north_active.label, signal_door_east_active.label,  toggle_lock_door_handle_north_active.label, signal_door_east_open.label,  "v"),
                TransitionRule(signal_door_east_reset_walk_border.label, border_state.label, signal_door_east_reset_walk.label, border_state.label, "v"),
                TransitionRule(trap_door_active.label, agent_state.label, agent_state.label, trap_door_used.label, "v"),
                TransitionRule(agent_state.label, trap_door_active.label, trap_door_used.label, agent_state.label,  "v"),
                TransitionRule(northEastWire.label, agent_state.label,
                               agent_state.label, northEastWire.label, "v"),
                TransitionRule(eastWire.label, northEastWire.label,
                               northEastWire.label, eastWire.label, "v"),
                TransitionRule(eastWire.label, trap_door_used.label,
                               trap_door_used.label, eastWire.label, "v"),
                TransitionRule(toggle_lock_door_handle_north_trigger_south.label, signal_door_east_reset_walk_border.label, toggle_lock_door_handle_north_inactive.label, signal_door_pass_toggle_south.label, "v"),
                TransitionRule(signal_door_pass_toggle_south.label, toggle_lock_door_handle_south_inactive.label, signal_door_east_inactive.label, toggle_lock_door_handle_south_active.label, "v"),
                TransitionRule(signal_door_east_active.label,  toggle_lock_door_handle_south_active.label,
                               signal_door_east_open.label, toggle_lock_door_handle_south_active.label,   "v"),
                TransitionRule(agent_state.label, southEastWire.label, southEastWire.label, agent_state.label, "v"),
                TransitionRule(southEastWire.label, eastWire.label, eastWire.label, southEastWire.label, "v"),
                TransitionRule(trap_door_used.label, eastWire.label,
                               eastWire.label, trap_door_used.label, "v"),
                TransitionRule(signal_door_east_reset_walk_border.label, toggle_lock_door_handle_south_trigger_north.label,
                               signal_door_pass_toggle_north.label, toggle_lock_door_handle_south_inactive.label, "v"),
                TransitionRule(toggle_lock_door_handle_north_inactive.label, signal_door_pass_toggle_north.label,
                               toggle_lock_door_handle_north_active.label, signal_door_east_inactive.label, "v"),







        ]

        return h_aff, v_aff, h_tr, v_tr



    def makeSeedAssembly(self):
        seed = Assembly()
        t = []
        t.append(Tile(agent_state, -1, 0))
        t.append(Tile(agent_state, -2, 0))
        t.append(Tile(agent_state, -3, 0))

        for i in range(0, 4):
            t.append(Tile(border_state, i, 1))
            t.append(Tile(eastWire, i, 0))
            t.append(Tile(border_state, i, -1))

        t.append(Tile(signal_door_east_inactive, 4, 0))
        t.append(Tile(toggle_lock_door_handle_north_active, 4, 1))
        t.append(Tile(toggle_lock_door_handle_south_inactive, 4, -1))
        t.append(Tile(eastWire, 5, 0))
        t.append(Tile(trap_door_active, 5, 1))
        t.append(Tile(trap_door_inactive, 5, -1))
        t.append(Tile(northEastWire, 5, 2))
        t.append(Tile(southEastWire, 5, -2))

        for i in range(6, 10):
            t.append(Tile(eastWire, i, 2))
            t.append(Tile(eastWire, i, -2))


        seed.setTiles(t)
        return seed

    def makeSys(self):
        seed = self.makeSeedAssembly()
        seed_states = seed.returnStates()
        h_aff, v_aff, h_tr, v_tr = self.makeAffinitiesTransitions()
        states = seed_states + [toggle_lock_door_handle_north_inactive,
                                toggle_lock_door_handle_north_trigger_south, toggle_lock_door_handle_south_active, toggle_lock_door_handle_south_trigger_north, trap_door_used, signal_door_pass_toggle_south, signal_door_pass_toggle_north, signal_door_east_reset_walk, border_state, signal_door_east_reset_walk_border, signal_door_east_active, signal_door_east_open]


        sys = System(1, states, [], seed_states, v_aff, h_aff, v_tr, h_tr, [], [], seed)

        return sys