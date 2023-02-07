from Generators.IU_Generators.binaryStates import *
from UniversalClasses import State, TransitionRule, AffinityRule, System, Tile, Assembly
from Assets.colors import *
import sys

exSt = [State("A", active_color), State("B", inactive_color), State("C", wire_color)]
xISt = [State("A", active_color), State("B", inactive_color), State("C", wire_color)]
xSSt = [State("A", active_color)]
vaff = [AffinityRule("A", "B", "v", 1), AffinityRule("C", "A", "v", 1), AffinityRule("C", "B", "v", 1)]
hAff = [AffinityRule("B", "B", "h", 1), AffinityRule("C", "C", "h", 1), AffinityRule("A", "C", "h", 1)]
vtr = [TransitionRule("A", "B", "A", "A", "v"), TransitionRule("B", "C", "A", "C", "v")]
htr = [TransitionRule("C", "C", "B", "A", "h"), TransitionRule("A", "C", "B", "C", "h")]
exampleSystem = System(1, exSt, xISt, xSSt, vaff, hAff, vtr, htr)  # seed assm)

class Wire:
    def __init__(self, start_x, start_y, end_x, end_y, start_direction, label=None, input_state=None, input_state_dir=None):

        if label is None:
            if input_state is None:
                label = "wire|({},{}), ({},{})| {}".format(start_x, start_y, end_x, end_y, start_direction)
            else:
                if input_state_dir is None:
                    label = "wire{}|({},{}), ({},{})| {}".format(input_state.label, start_x, start_y, end_x, end_y, start_direction)
                else:
                    label = "wire{}_{}|({},{}), ({},{})| {}".format(input_state.label, input_state_dir, start_x, start_y, end_x, end_y, start_direction)

        self.label = label
        start_direction = start_direction.lower()
        self.start_direction = start_direction
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.input_state = input_state
        self.input_state_dir = input_state_dir
        self.tiles = self.addWireTiles()
    def returnTiles(self):
        return self.tiles

    def addWireTiles(self):
        t = []
        dir_state = westWire
        sd = self.start_direction
        if sd == "w":
            dir_state = westWire
        elif sd == "n":
            dir_state = northWire
        elif sd == "s":
            dir_state = southWire
        elif sd == "e":
            dir_state = eastWire
        for i in range(self.start_x, self.end_x):
            t.append(Tile(dir_state, i, self.start_y))
        return t

class Row:
    def __init__(self, input_state, direction, start_x, start_y, row_width):
        self.input_state = input_state
        self.input_wire_direction = direction
        self.start_x = start_x
        self.start_y = start_y
        self.row_width = row_width
        self.wire = Wire(start_x - 3, start_y, start_x + row_width, start_y, "e", label=None, input_state=input_state, input_state_dir=direction)
        self.wire_tiles = self.addWireTiles()

        self.enter_door = self.addDoorTiles()
        self.border_tiles = self.addBorderTiles()
        self.tiles = self.addWireTiles() + self.addBorderTiles() + self.addDoorTiles()



    def addWireTiles(self):
        t = self.wire.returnTiles()
        print(len(t))
        return t

    def addDoorTiles(self):
        t = [Tile(signal_door_inactive_east, self.start_x, self.start_y), Tile(signal_door_handle_inactive, self.start_x, self.start_y + 1), Tile(signal_transmitter_inactive, self.start_x, self.start_y + 2), Tile(signal_receiver_inactive, self.start_x, self.start_y -1), Tile(row_border, self.start_x, self.start_y - 2)]
        return t

    def addBorderTiles(self):
        t = []
        for i in range(self.start_x + 1, self.start_x + self.row_width):
            t.append(Tile(row_border, i, self.start_y - 2))
        return t

    def returnTiles(self):
        return self.tiles

class Table:
    def __init__(self, inputSystem, start_x=0, start_y=0):
        self.input_system = inputSystem
        self.input_states_to_cols_dict, self.cols_to_input_states_dict = self.map_input_states_to_cols()
        self.input_states_dirs_to_rows_dict, self.rows_to_input_states_dirs_dict = self.map_input_states_to_rows()
        self.num_input_states = len(self.input_system.returnStates())
        self.start_x = start_x
        self.start_y = start_y
        self.row_size = 6
        self.column_size = len(self.input_system.returnStates()) + 2 + 3
        self.table_tiles = []#self.create_table_tiles()
        self.coords = {}
        self.num_rows = self.num_input_states * 4
        self.num_cols = self.num_input_states

        self.columns = []#self.create_columns()
        self.width = (self.column_size * self.num_cols) + 2
        self.height = (self.row_size * self.num_rows) + 2
        self.rows = self.createRows()
        self.end_x = start_x + self.width
        self.end_y = start_y - self.height
        self.TableAssembly, self.table_tiles = self.createTable(self.width, self.height, self.start_x, self.start_y)

    def createTable(self, w, h, n_x, n_y):
        outlineTiles = self.createOutline(w, h, n_x, n_y)
        r = self.rows
        row_tiles = []
        for i in r:
            row_tiles += i.returnTiles()

        #self.columns = self.create_columns()
        tableAssem = Assembly()
        table_tiles = outlineTiles + row_tiles
        tableAssem.setTiles(outlineTiles)
        tableAssem.setTiles(row_tiles)

        return tableAssem, table_tiles

    def returnSeedAssemblyTableTiles(self):
        return self.TableAssembly, self.table_tiles



    def createOutline(self, w, h, n_x, n_y):
        tiles = []
        end_x = n_x + w
        end_y = n_y - h
        start_x = n_x
        start_y = n_y

        tiles.append(Tile(northWestCorner, start_x, start_y))
        tiles.append(Tile(northEastCorner, end_x, start_y))
        tiles.append(Tile(southWestCorner, start_x, end_y))
        tiles.append(Tile(southEastCorner, end_x, end_y))

        for i in range(start_x + 1, end_x):
            tiles.append(Tile(border_state, i, start_y))
            tiles.append(Tile(border_state, i, end_y))

        for i in range(start_y -1 , end_y, -1):
            tiles.append(Tile(border_state, start_x, i))
            tiles.append(Tile(border_state, end_x, i))

        return tiles

    def createRows(self):
        r = []
        s = self.input_system.returnStates()
        row_num = 0
        x = self.start_x
        y = self.start_y - 4
        for i in s:
            for j in ["n", "s", "e", "w"]:
                r.append(Row(i, j, x, y, self.width))
                row_num += 1
                y -= 5
        return r

    def create_table_tiles(self):
        table_tiles = []
        for row in self.rows:
            for tile in row:
                table_tiles.append(tile)
        return table_tiles

    def map_input_states_to_cols(self):
        col_num = 0
        input_states_to_cols = {}
        cols_to_input_states = {}
        for state in self.input_system.states:
            input_states_to_cols[state.label] = col_num
            cols_to_input_states[col_num] = state.label
            col_num += 1
        return input_states_to_cols, cols_to_input_states

    def map_input_states_to_rows(self):
        row_num = 0
        input_states_dirs_to_rows = {}
        rows_to_input_states_dirs = {}
        for state in self.input_system.states:
            for direction in ["n", "e", "s", "w"]:
                input_states_dirs_to_rows[(state.label, direction)] = row_num
                rows_to_input_states_dirs[row_num] = (state.label, direction)
                row_num += 1
        return input_states_dirs_to_rows, rows_to_input_states_dirs

class IU_System:
    def __init__(self, name="Example", input_sys=exampleSystem):
        self.name = name
        self.input_system = input_sys
        self.table = Table(self.input_system)
        self.states = [northEastCorner, northWestCorner, southEastCorner, southWestCorner, border_state]
        self.seed_states = [northEastCorner, northWestCorner, southEastCorner, southWestCorner, border_state]
        self.initial_states =[]
        self.vaffinities = []
        self.haffinities = []
        self.vtransitions = []
        self.htransitions = []
        self.seed_assembly = Assembly()

    def returnIUsystem(self):
        table_seed_assembly, table_seed_tiles = self.table.returnSeedAssemblyTableTiles()
        self.seed_assembly.setTiles(table_seed_tiles)
        iuSys = System(1, self.states, [], self.seed_states, self.vaffinities, self.haffinities,
                       self.vtransitions, self.htransitions, [], [], table_seed_assembly)
        return iuSys

if __name__ == "__main__":
    iu_sys = IU_System(exampleSystem)
