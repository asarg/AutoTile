from UniversalClasses import AffinityRule, System, Assembly, Tile, State
import SaveFile

##############################
# aTAM tile set text file format
# {Interger temperature}
# 
# %  \\ This is the stop signal. List tiles after.
# {Tile Name} {Color} {North Glue} {East Glue} {South Glue} West Glue}
#
# \\ First Tile is assumed to be seed tile

########################
# Glues File format
#
#


def loadTilesFromText(filename):
    with open (filename) as f:
        temp = 0

        tiles = []

        for line in f:
            if temp == 0:
                # First line states only temperature 
                temp = int(line)
            else:
                # Splits the line into an array and appends to the list of tiles
                tiles.append(line.split()) 

    return [temp, tiles]

def loadGluesFromText(filename):
    glueStrengths = {}

    with open (filename) as f:
        for line in f:
            [glue, str] = line.split()
            glueStrengths[glue] = str

    return glueStrengths



def buildSystem(temp, tiles, glueStrengths):

    # States
    states = []
    northGlues = {}
    eastGlues = {}
    southGlues = {}
    westGlues = {}

    for t in tiles:
        [label, color, northG, eastG, southG, westG] = t

        states.append(State(label, color))
        
        if northG in northGlues:
            northGlues[northG].append(label)
        else:
            northGlues[northG] = [label]

        if eastG in eastGlues:
            eastGlues[eastG].append(label)
        else:
            eastGlues[eastG] = [label]

        if southG in southGlues:
            southGlues[southG].append(label)
        else:
            southGlues[southG] = [label]

        if westG in westGlues:
            westGlues[westG].append(label)
        else:
            westGlues[westG] = [label]

    sys = System(temp, states, states, [states[0]])

    # For each north glue
    for glue in glueStrengths.keys():
        # Reason for name change: The tiles with a glue on the north attach on the south.  
        # The tiles with a glue on the east attach on the west.
        southTiles = northGlues.get(glue)
        northTiles = southGlues.get(glue)
        westTiles = eastGlues.get(glue)
        eastTiles = westGlues.get(glue)

        if southTiles != None: 
            for sTile in southTiles:
                if northTiles != None:
                    for nTile in northTiles:
                        sys.add_affinity(AffinityRule(nTile, sTile, "v", glueStrengths[glue]))

        if eastTiles != None:
            for eTile in eastTiles:
                if westTiles != None:
                    for wTile in westTiles:
                        sys.add_affinity(AffinityRule(wTile, eTile, "h", glueStrengths[glue]))


    return sys


if __name__ == "__main__":
    [temp, tiles] = loadTilesFromText("XML Files/aTAM/testTiles.txt")
    glueStrs = loadGluesFromText("XML Files/aTAM/testGlues.txt")

    sys = buildSystem(temp, tiles, glueStrs)

    SaveFile.main(sys, ["XML Files/aTAM/testSystem.xml"])