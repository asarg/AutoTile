import os
import sys

parent = os.path.abspath('...')
sys.path.insert(1, parent)

from UniversalClasses import *
from IntrinsicUniversality import IU_System

# getting the name of the directory
# where the this file is present.
# current = os.path.dirname(os.path.realpath(__file__))

# # Getting the parent directory name
# # where the current directory is present.
# parent = os.path.dirname(current)

# # adding the parent directory to
# # the sys.path.
# sys.path.append(parent)



genSys = IU_System().returnIUsystem()
h = 10
w = 10
tiles_list = genSys.returnTiles()
curr_x = 100
curr_y = 100
with open("util/inkscape_scripts/iu_script.py", "w") as script_file:
    for t in tiles_list:
        tile_start_x = t.x*10 + curr_x
        tile_start_y = t.y*-10 + curr_y
        tile_end_x = tile_start_x + w
        tile_end_y = tile_start_y - h
        script_file.write(f"rect(({tile_start_x}, {tile_start_y}), ({tile_end_x}, {tile_end_y}), fill=\'#{t.state.color}\', stroke='black')")
        script_file.write("\n")
