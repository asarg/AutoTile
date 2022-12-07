import LoadFile
import SaveFile
import util.loaders.assemblyLoader as assemblyLoader
from UniversalClasses import *
import math

def shift_tiles(tiles, amount_x=0, amount_y=0):
    for tile in tiles:
        tile.y += amount_y
        tile.x += amount_x
    return tiles


def verify_no_overlap(a1, a2):
    overlaps_list = []
    no_overlaps_bool = True
    a1_tiles = a1.returnTiles()
    a2_tiles = a2.returnTiles()
    for tile1 in a1_tiles:
        for tile2 in a2_tiles:
            if tile1.x == tile2.x and tile1.y == tile2.y:
                overlapping_tile_pair = (tile1, tile2)
                overlaps_list.append(overlapping_tile_pair)
                no_overlaps_bool = False
    return no_overlaps_bool, overlaps_list

def double_assembly(a1, dir):
    a1_tiles = a1.returnTiles()
    height = abs(a1.upMost) + abs(a1.downMost) + 1
    width = abs(a1.leftMost) + abs(a1.rightMost) + 1
    a2 = Assembly()
    a2_tiles = []
    if dir == "above":
        a2_tiles = shift_tiles(a1_tiles, 0, height + 1)
    elif dir == "below":
        a2_tiles = shift_tiles(a1_tiles, 0, -height - 1)
    elif dir == "left":
        a2_tiles = shift_tiles(a1_tiles, -width - 1, 0)
    elif dir == "right":
        a2_tiles = shift_tiles(a1_tiles, width + 1, 0)


    a2.setTiles(a2_tiles)
    no_ol_bool, ol_list = verify_no_overlap(a1, a2)
    if no_ol_bool:
        a2.setTiles(a2_tiles)
        return a2
    else:
        print("Overlapping tiles: ", ol_list)
        return None


def returnLoadedSystem(file):
    seed = assemblyLoader.returnSystemLoadXML(file)
    seed_assembly = system_dict["seedAssembly"]
    double_assembly = seed_assembly
    return double_assembly



if __name__ == "__main__":
    #system_dict = LoadFile.readxml("uniaryPunchTwoCells.xml")
    system_dict = assemblyLoader.returnSystemLoadXML("uniaryPunchTwoCells.xml")
    seed_assembly = system_dict["seedAssembly"]

    #double_assembly = seed_assembly
