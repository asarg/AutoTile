from UniversalClasses import *
from Generators.IU_Generators.binaryStates import *
from Generators.IU_Generators.General_IU_Helper_Functions import *


def makeRectangleOutline(top_left_coords, bottom_right_coords, type="outerMostBorder"):
    a = Assembly()
    tiles = []
    if type == "outerMostBorder":
        little_x, big_y = top_left_coords
        big_x, little_y = bottom_right_coords
        tiles = addCorners(top_left_coords, (big_x, big_y), (little_x, little_y), bottom_right_coords, type)

        a.setTiles(tiles)
        state = border_state

        for i in range(little_x, big_x + 1):
            t = []
            if not a.checkInCoords(i, big_y):
                t.append(Tile(state, i, big_y))

            if not a.checkInCoords(i, little_y):
                t.append(Tile(state, i, little_y))
            a.setTiles(t)

        for j in range(little_y, big_y + 1):
            t = []
            if not a.checkInCoords(little_x, j):
                t.append(Tile(state, little_x, j))
            if not a.checkInCoords(big_x, j):
                t.append(Tile(state, big_x, j))
            a.setTiles(t)

    return a


def addCorners(NW_coords, NE_coords, SW_coords, SE_coords, type="outerMostBorder"):
    tiles = []
    if type == "outerMostBorder":

        tiles.append(Tile(northEastCorner, NE_coords[0], NE_coords[1]))
        tiles.append(Tile(northWestCorner, NW_coords[0], NW_coords[1]))
        tiles.append(Tile(southEastCorner, SE_coords[0], SE_coords[1]))
        tiles.append(Tile(southWestCorner, SW_coords[0], SW_coords[1]))



    return tiles