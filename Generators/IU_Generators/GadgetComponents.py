from components import *
from UniversalClasses import *
from states import *

class WireGadget:
    def __init__(self, dir, len, start_x, start_y):
        self.wire_name = ""
        self.wire_list = []
        self.wire = Assembly()
        self.states_used = []
        self.direction = dir
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = None
        self.end_y = None
        self.wire_length = len
        self.makeWire()

    def __init__(self, dir, start_coords, end_coords):
        self.wire_name = ""

    def makeWire(self):

        for i in range(self.wire_length):
            if self.direction == "N":
                self.wire_list.append(Tile(northWire, self.start_x, self.start_y + i))
                self.end_y = self.start_y + i
                self.end_x = self.start_x
                if northWire not in self.states_used:
                    self.states_used.append(northWire)
            elif self.direction == "S":
                self.wire_list.append(Tile(southWire, self.start_x, self.start_y + i))
                self.end_y = self.start_y + i
                self.end_x = self.start_x
                if southWire not in self.states_used:
                    self.states_used.append(southWire)
            elif self.direction == "W":
                self.wire_list.append(
                    Tile(westWire, self.start_x + i, self.start_y))
                self.end_x = self.start_x + i
                self.end_y = self.start_y
                if westWire not in self.states_used:
                    self.states_used.append(westWire)
            elif self.direction == "E":
                self.wire_list.append(
                    Tile(eastWire, self.start_x + i, self.start_y))
                self.end_x = self.start_x + i
                self.end_y = self.start_y
                if eastWire not in self.states_used:
                    self.states_used.append(eastWire)

        self.wire.setTilesFromList(self.wire_list)
        print("Wire made from ({},{}) to {}".format(
            self.start_x, self.start_y, self.wire_list[-1].returnPosition()))

    def returnWireTileList(self):
        return self.wire_list

    def returnWireAssembly(self):
        return self.wire

    def returnStatesUsed(self):
        return self.states_used

    def appendTestDataString(self, data_string):
        self.test_data_tile_list = []
        self.test_data_states_list = []
        curr_borders = self.wire.returnBorders()

        for i in range(len(data_string)):
            if self.direction == "N":
                temptile = uc.Tile(
                    data_string[i].state, self.end_x, self.end_y - i)
            elif self.direction == "S":
                temptile = uc.Tile(
                    data_string[i].state, self.end_x, self.end_y + i)
            elif self.direction == "W":
                temptile = uc.Tile(
                    data_string[i].state, self.end_x + i, self.end_y)
            elif self.direction == "E":
                temptile = uc.Tile(
                    data_string[i].state, self.end_x + i, self.end_y)
            self.test_data_tile_list.append(temptile)
            if data_string[i].state not in self.states_used:
                self.states_used.append(data_string[i].state)
            if temptile is not None:
                self.test_data_states_list.append(data_string[i].state)

        self.wire.setTilesFromList(self.test_data_tile_list)

    def appendTestDataRawString(self, raw_string):
        pass
