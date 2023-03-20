from UniversalClasses import *
import Assets.colors as colors
from Generators.IU_Generators.binaryStates import border_state, eastWire, signal_door_east_inactive, signal_door_handle_east_inactive, trap_door_inactive, toggle_lock_door_handle_north_active, toggle_lock_door_handle_north_inactive, toggle_lock_door_handle_north_trigger_south, toggle_lock_door_handle_south_active, toggle_lock_door_handle_south_inactive,toggle_lock_door_handle_south_trigger_north, trap_door_inactive, trap_door_active, trap_door_used


class Door:
    def __init__(self):
        states = []
        initial_states = []
        seed_states = []
        tiles = []

    def makeSeedAssembly(self):
        seed = Assembly()
        t = []
        for i in range(0, 4):
            t.append(Tile(eastWire, i, 0))

        t.append(Tile(signal_door_east_inactive, 4, 0))
        t.append(Tile(toggle_lock_door_handle_north_active, 4, 1))
        t.append(Tile(toggle_lock_door_handle_south_inactive, 4, -1))
        t.append(Tile(eastWire, 5, 0))
        t.append(Tile(trap_door_active, 5, 1))
        t.append(Tile(trap_door_inactive, 5, -1))

        for i in range(5, 10):
            t.append(Tile(eastWire, i, 2))
            t.append(Tile(eastWire, i, -2))

        seed.setTiles(t)
        return seed

    def makeSys(self):
        seed = self.makeSeedAssembly()
        seed_states = seed.returnStates()
        states = seed_states + [toggle_lock_door_handle_north_inactive,
                                toggle_lock_door_handle_north_trigger_south, toggle_lock_door_handle_south_active, toggle_lock_door_handle_south_trigger_north, trap_door_used]

        sys = System(1, states, [], seed_states, [], [], [], [], [], [], seed)

        return sys