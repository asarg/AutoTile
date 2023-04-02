from UniversalClasses import *
from Assets.colors import *
from Generators.IU_Generators.binaryStates import *


def makeTableInOutWire(in_wire_start_coords, in_wire_end_coords, out_wire_start_coords, out_wire_end_coords,
                        incoming_tile_direction, direction_label_coords, state_label, state_label_start_coords,
                        reverse=False, in_wire_direction=None):
    tiles = []
    # in_wire_coords = (x, y)
    if in_wire_direction == None:
        if incoming_tile_direction == "N" or incoming_tile_direction == "S":
            in_wire_direction = "E"
        else:
            in_wire_direction = "W"


    if in_wire_direction == "E":
        out_wire_direction = "W"
    else:
        out_wire_direction = "E"


    in_wire_tiles = makeWire(in_wire_start_coords, in_wire_end_coords, in_wire_direction)
    out_wire_tiles = makeWire(out_wire_start_coords, out_wire_end_coords, out_wire_direction)
    label_tiles = makeStateDirectionLabel(state_label, state_label_start_coords, incoming_tile_direction,
                                          direction_label_coords, reverse)

    tiles = in_wire_tiles + out_wire_tiles + label_tiles
    return tiles

def makeStateDirectionLabel(state_label, state_label_start_coords, incoming_tile_direction, direction_label_coords, reverse=False):
    tiles = []

    if incoming_tile_direction == "N":
        incoming_tile_direction_state = north_prefix
    elif incoming_tile_direction == "S":
        incoming_tile_direction_state = south_prefix
    elif incoming_tile_direction == "E":
        incoming_tile_direction_state = east_prefix
    else:
        incoming_tile_direction_state = west_prefix

    tiles.append(Tile(incoming_tile_direction_state, direction_label_coords[0], direction_label_coords[1]))


    if reverse:
        if state_label_start_coords[0] - direction_label_coords[0] > 0:
           for i in range(direction_label_coords[0] + 1, state_label_start_coords[0]):
               tiles.append(Tile(border_state, i, state_label_start_coords[1]))


        for i in range(0, len(state_label)):
            if state_label[i] == "0":
                tiles.append(Tile(ds_0, state_label_start_coords[0] + i, state_label_start_coords[1]))
            elif state_label[i] == "1":
                tiles.append(Tile(ds_1, state_label_start_coords[0] + i, state_label_start_coords[1]))
            elif state_label[i] == start_data_string.label:
                tiles.append(Tile(start_data_string, state_label_start_coords[0] + i, state_label_start_coords[1]))
            elif state_label[i] == end_data_string.label:
                tiles.append(Tile(end_data_string, state_label_start_coords[0] + i, state_label_start_coords[1]))
    else:
        if direction_label_coords[0] - state_label_start_coords[0] > 0:
            for i in range(state_label_start_coords[0] + 1, direction_label_coords[0]):
                tiles.append(Tile(border_state, i, state_label_start_coords[1]))

        for i in range(len(state_label), 0, -1):
            if state_label[i] == "0":
                tiles.append(Tile(ds_0, state_label_start_coords[0] - i, state_label_start_coords[1]))
            elif state_label[i] == "1":
                tiles.append(Tile(ds_1, state_label_start_coords[0] - i, state_label_start_coords[1]))
            elif state_label[i] == start_data_string.label:
                tiles.append(Tile(start_data_string, state_label_start_coords[0] - i, state_label_start_coords[1]))
            elif state_label[i] == end_data_string.label:
                tiles.append(Tile(end_data_string, state_label_start_coords[0] - i, state_label_start_coords[1]))


    return tiles


def makeWire(start_coords, end_coords, wire_direction):
    tiles = []

    if wire_direction == "N": wire_state = northWire
    elif wire_direction == "S": wire_state = southWire
    elif wire_direction == "E": wire_state = eastWire
    else: wire_state = westWire

    if start_coords[0] == end_coords[0]:
        # vertical wire
        if start_coords[1] > end_coords[1]:
            # wire goes up
            for y in range(end_coords[1], start_coords[1] + 1):
                tiles.append(Tile(wire_state, start_coords[0], y))
        else:
            # wire goes down
            for y in range(start_coords[1], end_coords[1] + 1):
                tiles.append(Tile(wire_state, start_coords[0], y))

    elif start_coords[1] == end_coords[1]:
        # horizontal wire

        if start_coords[1] > end_coords[1]:
            # wire goes left
            for i in range(end_coords[0], start_coords[0] + 1):
                tiles.append(Tile(wire_state, i, start_coords[1]))
        else:
            # wire goes right
            for i in range(start_coords[0], end_coords[0] + 1):
                tiles.append(Tile(wire_state, i, start_coords[1]))
    return tiles