import math
from UniversalClasses import Tile, toCoords

def checkStartEndXY(start_coords, end_coords):
    mismatch = False
    if start_coords[0] > end_coords[0]:
        start_x = end_coords[0]
        end_x = start_coords[0]
        start_y = end_coords[1]
        end_y = start_coords[1]
        if start_coords[1] < end_coords[1]:
            mismatch = True

    else:
        start_x = start_coords[0]
        end_x = end_coords[0]
        start_y = start_coords[1]
        end_y = end_coords[1]

        if start_coords[1] > end_coords[1]:
            mismatch = True

    return start_x, start_y, end_x, end_y, mismatch


def adjustCoordsDict(initiation_location_xy, adjusted_location_xy, coordsDict, tiles, allowOverlap=False):

    move_x = math.dist(initiation_location_xy[0], adjusted_location_xy[0])
    if initiation_location_xy[0] > adjusted_location_xy[0]:
        move_x = -move_x

    move_y = math.dist(initiation_location_xy[1], adjusted_location_xy[1])
    if initiation_location_xy[1] > adjusted_location_xy[1]:
        move_y = -move_y

    newTiles = []
    newCoordsDict = {}
    allowOverlap = False
    overlapFlag = False
    overLapsDict = {(int, int): []}

    for tile in tiles:
        newTile = Tile(tile.state, tile.x + move_x, tile.y + move_y)
        newTiles.append(newTile)
        if toCoords(tile.x + move_x, tile.y + move_y) in newCoordsDict.keys():
            overLapsDict[toCoords(tile.x + move_x, tile.y + move_y)].append(newTile)
            if allowOverlap == False:
                continue
            else:
                newCoordsDict[toCoords(tile.x + move_x, tile.y + move_y)] = newTile
        else:
            newCoordsDict[toCoords(tile.x + move_x, tile.y + move_y)] = newTile
