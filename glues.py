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
# {Glue Name} {Interger Strength}
# \\ comment with "#"


def loadTilesFromText(filename):
    with open (filename) as f:
        temp = 0

        tiles = []

        for line in f:
            if line[0] == "#":
                continue

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
            if line[0] == "#":
                continue

            try: 
                [glue, str] = line.split()
            except:
                print("Line: (", line, " not read")
            if str != 0:
                glueStrengths[glue] = str

    return glueStrengths



def buildSystem(temp, tiles, glueStrengths):

    # States
    states = []
    initial_st = []
    northGlues = {}
    eastGlues = {}
    southGlues = {}
    westGlues = {}
    seed = 0

    for t in tiles:
        [label, color, northG, eastG, southG, westG] = t

        states.append(State(label, color))

        if seed == 0:
            seed = State(label, color)
        else:
            initial_st.append(State(label, color))
        
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


    sys = System(temp, states, initial_st, [seed])

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


def toffSys():
    #[temp, tiles] = loadTilesFromText("XML Files/aTAM/tilesToff.txt")
    #glueStrs = loadGluesFromText("XML Files/aTAM/glueToff.txt")

    # Get Circuit
    input = "010"
    gates = [4, 3, 4]
    bits = 4


    # Make Tile set and glues
    tiles = []
    glueStrs = []

    glueStrs["s0"] = 1
    glueStrs["s1"] = 1
    glueStrs["t0"] = 1
    glueStrs["t1"] = 1
    glueStrs["dec0"] = 1
    glueStrs["dec1"] = 1
    glueStrs["inc0"] = 1
    glueStrs["inc1"] = 1

    # Red Tiles
    for i in range((2 * len(gates)) + 5):
        if i == 0:
            glueStrs["r" + str(i)] = 1
        else:
            glueStrs["r" + str(i)] = 2


    #  r0
    r0 = ["r0", "9d5c63", "S0", "r1", "NULL", "r0"]
    tiles.append(r0)

    for i in range(bits):
        # S tiles
        # Si is vertical glue
        sTile0 = ["s" + "0_" + str(i), "ececec", "S" + str(i + 1), "s0", "S" + str(i), "dec0"]
        sTile1 = ["s" + "1_" + str(i), "b3b3b3", "S" + str(i + 1), "s1", "S" + str(i), "dec1"]
        tiles.append(sTile0)
        tiles.append(sTile1)

        glueStrs["S" + str(i)] = 1
        glueStrs["S" + str(i)] = 1

        # T tiles is the reversed version
        tTile0 = ["t" + "0_" + str(i), "ececec", "T" + str(i + 1), "dec0", "T" + str(i), "t0"]
        tTile1 = ["t" + "1_" + str(i), "b3b3b3", "T" + str(i + 1), "dec1", "T" + str(i), "t1"]
        tiles.append(tTile0)
        tiles.append(tTile1)

        glueStrs["T" + str(i)] = 1
        glueStrs["T" + str(i)] = 1

        # Input tiles - Connection between S and circuit
        iTile0 = ["i" + "0_" + str(i), "93e1d8", "I" + str(i + 1), "0_" + str(i), "I" + str(i), "s0"]
        iTile1 = ["i" + "1_" + str(i), "ef8354", "I" + str(i + 1), "1_" + str(i), "I" + str(i), "s1"]
        tiles.append(iTile0)
        tiles.append(iTile1)

        glueStrs["I" + str(i)] = 1
        glueStrs["I" + str(i)] = 1
        
        # "jinput" reversed input
        jTile0 = ["j" + "0_" + str(i), "93e1d8", "J" + str(i + 1), "t0", "J" + str(i), "0" + str(i)]
        jTile1 = ["j" + "1_" + str(i), "ef8354", "J" + str(i + 1), "t1", "J" + str(i), "1" + str(i)]
        tiles.append(jTile0)
        tiles.append(jTile1)

        glueStrs["J" + str(i)] = 1
        glueStrs["J" + str(i)] = 1

        # Circuit Glues
        glueStrs["0_" + str(i)] = 1
        glueStrs["1_" + str(i)] = 1



    sys = buildSystem(2, tiles, glueStrs)

    seedTiles = []

    seedTiles.append(Tile(sys.get_state("r0"), 0, 0))
    seedTiles.append(Tile(sys.get_state("r1"), 1, 0))
    seedTiles.append(Tile(sys.get_state("r2"), 2, 0))
    seedTiles.append(Tile(sys.get_state("S0A"), 0, 1))
    seedTiles.append(Tile(sys.get_state("S1B"), 0, 2))
    seedTiles.append(Tile(sys.get_state("S0C"), 0, 3))
    seedTiles.append(Tile(sys.get_state("i0A"), 1, 1))
    seedTiles.append(Tile(sys.get_state("i1B"), 1, 2))
    seedTiles.append(Tile(sys.get_state("i0C"), 1, 3))

    for seedT in seedTiles:
        print(seedT.get_label())

    seedAssembly = Assembly()
    seedAssembly.set_tiles(seedTiles)
    sys.set_Seed_Assembly(seedAssembly)

    return sys

if __name__ == "__main__":
    [temp, tiles] = loadTilesFromText("XML Files/aTAM/tilesToff.txt")
    glueStrs = loadGluesFromText("XML Files/aTAM/glueToff.txt")

    sys = buildSystem(temp, tiles, glueStrs)

    SaveFile.main(sys, ["XML Files/aTAM/toffSystem.xml"])