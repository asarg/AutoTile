from random import randrange
# These classes are used for Loading and Saving Files and Communicating with general_TA_simulator.


class State:
    def __init__(self, label, color):
        self.label = label
        self.color = color

    # Getters
    def returnLabel(self):
        return self.label

    def get_label(self):  # NOTICE: LEAVE THIS HERE FOR THE ASSEMBLER
        return self.label

    def returnColor(self):
        return self.color
    
    def __eq__(self, other):
        if isinstance(other, State):
            return self.label == other.label and self.color == other.color
        

    def get_color(self):      # for editor window
        return self.color


def toCoords(x, y):
    return "(" + str(x) + "," + str(y) + ")"


class Tile:
    # label
    # # changes or list of changes (start num)
    # maybe list of affinities pairs (state, direction)
    # boolean can_change

    def __init__(self, s, _x, _y):
        self.state = s
        self.x = _x
        self.y = _y

    def __str__(self):
        s = self.state.label + " (" + self.x + ", " + self.y + ")"
        return s

    def get_state(self):
        return self.state

    def set_state(self, s):
        self.state = s

    def get_label(self):
        return self.state.label

    def set_label(self, l):
        self.state.label = l

    def get_color(self):
        return self.state.returnColor()


class Assembly:
    def __init__(self):
        self.label = ""
        self.tiles = []  # tuple of (label, x, y)
        self.coords = {}  # mapping of strings (x, y) to tiles
        self.leftMost = 0
        self.rightMost = 0
        self.upMost = 0
        self.downMost = 0

    def print_size(self):
        print("Left Boundary: ", self.leftMost)
        print("Right Boundary: ", self.rightMost)
        print("North Boundary: ", self.upMost)
        print("South Boundary: ", self.downMost)
        print("Size: ", len(self.tiles))

    def get_borders(self):
        borders_list = [self.leftMost, self.rightMost, self.upMost, self.downMost]
        return borders_list

    def get_label(self):
        return self.label

    def set_label(self, l):
        self.label = l

    def get_tiles(self):
        return self.tiles

    def set_tiles(self, t):
        for tileI in t:
            tile = Tile(tileI.state, tileI.x, tileI.y)
            self.tiles.append(tile)
            self.coords["(" + str(tile.x) + "," + str(tile.y) + ")"] = tile
            # update boundaries
            if(tile.y > self.upMost):
                self.upMost = tile.y
            if(tile.y < self.downMost):
                self.downMost = tile.y
            if(tile.x > self.rightMost):
                self.rightMost = tile.x
            if(tile.x < self.leftMost):
                self.leftMost = tile.x

    # Sonya on attachments
    def get_attachments(self, sy):  # takes in a system
        attachments_list = []
        # sys_attachments = sy.get_initial_states()
        # sys_v_transition_rules = sy.get_vertical_transition_rules

        v_rules = sy.returnVerticalAffinityDict()
        h_rules = sy.returnHorizontalAffinityDict()

        for iX in range(self.leftMost - 1, self.rightMost + 2):
            for iY in range(self.downMost - 1, self.upMost + 2):

                # Check if position is empty
                if self.coords.get(toCoords(iX, iY)) != None:
                    continue
                #print("Testing ", iX, ", ", iY)

                # Get each neighbor
                neighborN = self.coords.get(toCoords(iX, iY + 1))
                neighborS = self.coords.get(toCoords(iX, iY - 1))
                neighborE = self.coords.get(toCoords(iX + 1, iY))
                neighborW = self.coords.get(toCoords(iX - 1, iY))

                # Calcuate the str of each tile attaching at this position
                for iTile in sy.returnInitialStates():
                    attStr = 0

                    if(neighborN != None):
                        stren = v_rules.get(
                            (neighborN.get_label(), iTile.get_label()))
                        if(stren != None):
                            attStr += int(stren)
                    if(neighborS != None):
                        stren = v_rules.get(
                            (iTile.get_label(), neighborS.get_label()))
                        if(stren != None):
                            attStr += int(stren)
                    if(neighborE != None):
                        stren = h_rules.get(
                            (iTile.get_label(), neighborE.get_label()))
                        if(stren != None):
                            attStr += int(stren)
                    # else:
                    #    print("East of "+ str(iX) + " : " + str(iY) + " is empty")
                    if(neighborW != None):
                        stren = h_rules.get(
                            (neighborW.get_label(), iTile.get_label()))
                        if(stren != None):
                            attStr += int(stren)
                    # else:
                    #    print("West of "+ str(iX) + " : " + str(iY) + " is empty")

                    #print(iTile.get_label(), ": ", attStr)
                    if attStr >= sy.returnTemp():
                        attMove = {"type": "a"}

                        attMove["x"] = iX
                        attMove["y"] = iY
                        attMove["state1"] = iTile

                        attachments_list.append(attMove)

            #ttc = (i-1, i)
            #ttl = (t1, t2)
            # print(ttl)
            # if ttl in sys_attachments:
                #attachments_list.append((ttc, ttl, sys_attachments[ttl]))
        print(len(attachments_list), " Attachments")

        return attachments_list
        # ORIGINAL tuple of ((coord pair), (current labels), (transition labels))

    def set_attachments(self, att):  # tuple of ((type: ), (x: ), (y: ), (state1: ))
        # a = Assembly()
        #a.label = self.label + "A " + att["state1"]
        # a.set_tiles(self.tiles.copy())
        #change = trans[0][0]
       # print(a.tiles[change][0])
        # print(trans[2][1])
       # print(trans[0])
        #a.tiles[change] = trans[2][1]
        #print("attaching at " + str(att["x"]) + " : " + str(att["y"]))
        #print("New Assembly Tiles: ", a.tiles)

        att_tile = Tile(att["state1"], att["x"], att["y"])
        self.tiles.append(att_tile)
        self.coords[toCoords(att["x"], att["y"])] = att_tile

        # Update Boundaries
        if(int(att["y"]) > self.upMost):
            self.upMost = att["y"]
        else:
            self.upMost = self.upMost
        if(int(att["y"]) < self.downMost):
            self.downMost = att["y"]
        else:
            self.downMost = self.downMost
        if(int(att["x"]) > self.rightMost):
            self.rightMost = att["x"]
        else:
            self.rightMost = self.rightMost
        if(int(att["x"]) < self.leftMost):
            self.leftMost = att["x"]
        else:
            self.leftMost = self.leftMost


    # Elise on transitions
    def get_transitions(self, sy):  # takes in a system
        #t1 = (self.tiles[i-1][0])
        #t2 = (self.tiles[i][0])
        #ttc = (i-1, i)
        #ttl = (t1, t2)

        # print(ttl)
        # if ttl in sys_h_tr:
        #transitions_list.append((ttc, ttl, sys_h_transition_rules[ttl]))

        transitions_list = []
        sys_h_tr = sy.returnHorizontalTransitionDict()
        sys_v_tr = sy.returnVerticalTransitionDict()
        #sys_h_tiles = sy.get_tile_horizontal_transitions()
        #sys_v_tiles = sy.get_tile_vertical_transitions()

        # Check each tile in the assembly
        for iTile in self.tiles:
           # print(sys_h_tiles[iTile.get_label()])
            # if isinstance(sys_h_tiles[iTile.get_label()], tuple):

            #iHTranRules = None
            #iVTranRules = None

            # if sys_h_tiles != None:
            # if sys_h_tiles.get(iTile.get_label()) != None:
            #iHTranRules = sys_h_tr[sys_h_tiles[iTile.get_label()]]
            # else:
            # for tiles in sys_h_tiles[iTile.get_label()]:
            #iHTranRules = sys_h_tr[tiles]

            # if isinstance(sys_v_tiles[iTile.get_label()], tuple):
            # if sys_v_tiles != None:
            # if sys_v_tiles.get(iTile.get_label()):
            #iVTranRules = sys_v_tr[sys_v_tiles[iTile.get_label()]]
            # else:
            # for tiles in sys_v_tiles[iTile.get_label()]:
            #iVTranRules = sys_v_tr[tiles]

            # Get only the south and east neighbors of iTile
            neighborS = self.coords.get(toCoords(iTile.x, iTile.y - 1))
            neighborE = self.coords.get(toCoords(iTile.x + 1, iTile.y))

            if(neighborS != None):
                # second dictionary
                # rules = iVTranRules.get(neighborS.get_label())
                rules = sys_v_tr.get(
                    (iTile.get_label(), neighborS.get_label()))
                # rules.append(iVTranRules)
                if rules != None:
                    for i in range(0, len(rules), 2):
                        move = {"type": "t"}
                        move["x"] = iTile.x
                        move["y"] = iTile.y
                        move["dir"] = "v"
                        move["state1"] = iTile.get_state()
                        move["state2"] = neighborS.get_state()

                   
                        move["state1Final"] = sy.get_state(
                            rules[i])  # .returnLabel1Final()
                        move["state2Final"] = sy.get_state(
                            rules[i + 1])  # .returnLabel2Final()
                        transitions_list.append(move)

            if(neighborE != None):
                #rules = iHTranRules[neighborE.get_label()]
                rules = sys_h_tr.get(
                    (iTile.get_label(), neighborE.get_label()))
                # print(sys_h_tr)
                # rules.append(iHTranRules)

                if rules != None:
                    #print(iTile.get_label() + " : " + str(len(rules)))
                    for i in range(0, len(rules), 2):
                        move = {"type": "t"}
                        move["x"] = iTile.x
                        move["y"] = iTile.y
                        move["dir"] = "h"
                        move["state1"] = iTile.get_state()
                        move["state2"] = neighborE.get_state()

                    
                        move["state1Final"] = sy.get_state(
                            rules[i])  # .returnLabel1Final()
                        move["state2Final"] = sy.get_state(
                            rules[i + 1])  # .returnLabel2Final()
                        transitions_list.append(move)

        return transitions_list
        # ORIGINAL ((type: ), (current labels), (transition labels))

    # tuple of {'type': 't', 'x': 0, 'y': 0, 'state1': 'S', 'state2': 'A', 'state1Final': 'S', 'state2Final': 'A'}
    def set_transition(self, trans):
        # a = Assembly()
        # originally trans[2][0] + trans[2][1]
        self.label = self.label + "T " + \
            trans["state1Final"].get_label() + trans["state2Final"].get_label()
        # self.set_tiles(self.tiles.copy())
        #change = trans["type"]

        # print(a.tiles[change])
        #print(trans["state2Final"].get_label())
        #print(trans["type"])
        self.coords[toCoords(trans["x"], trans["y"])].set_state(
            trans["state1Final"])
        # a.tiles[trans["x"]][trans["y"]].setState(trans["state1Final"])
        if(trans["dir"] == "v"):
            self.coords[toCoords(trans["x"], trans["y"] - 1)
                     ].set_state(trans["state2Final"])
        if(trans["dir"] == "h"):
            self.coords[toCoords(trans["x"] + 1, trans["y"])
                     ].set_state(trans["state2Final"])
        #print("New Assembly Tiles: ", a.tiles)

    def getMoves(self, sy):
        #print("attachments: " + str(len(self.get_attachments(sy))) + " transitions: " + str(len(self.get_transitions(sy))))
        return self.get_attachments(sy) + self.get_transitions(sy)

    def performMove(self, move):
        if(move["type"] == "a"):
            self.set_attachments(move)
        if(move["type"] == "t"):
            self.set_transition(move)

    def undoMove(self, move):
        a = Assembly()
        a.set_tiles(self.tiles.copy())

        x = move["x"]
        y = move["y"]

        if(move["type"] == "t"):
            a.coords[toCoords(x, y)].set_state(move["state1"])
            # a.tiles[trans["x"]][trans["y"]].setState(trans["state1Final"])
            if(move["dir"] == "v"):
                a.coords[toCoords(move["x"], move["y"] - 1)
                        ].set_state(move["state2"])
            if(move["dir"] == "h"):
                a.coords[toCoords(move["x"] + 1, move["y"])
                        ].set_state(move["state2"])



            return a
        if(move["type"] == "a"):
            print("Removing state", move["state1"], "from ", move["x"], ", ", move["y"])
            tile = a.coords[toCoords(x, y)]
            del a.coords[toCoords(x, y)]

            a.tiles.remove(tile)

            return a

    def getAttat(self, sy, x, y):
        attachments_list = []
        # sys_attachments = sy.get_initial_states()
        # sys_v_transition_rules = sy.get_vertical_transition_rules

        v_rules = sy.returnVerticalAffinityDict()
        h_rules = sy.returnHorizontalAffinityDict()

        # Check if position is empty
        if self.coords.get(toCoords(x, y)) != None:
            return attachments_list
        #print("Testing ", iX, ", ", iY)

        # Get each neighbor
        neighborN = self.coords.get(toCoords(x, y + 1))
        neighborS = self.coords.get(toCoords(x, y - 1))
        neighborE = self.coords.get(toCoords(x + 1, y))
        neighborW = self.coords.get(toCoords(x - 1, y))

        # Calcuate the str of each tile attaching at this position
        for iTile in sy.returnInitialStates():
            attStr = 0

            if(neighborN != None):
                stren = v_rules.get(
                    (neighborN.get_label(), iTile.get_label()))
                if(stren != None):
                    attStr += int(stren)
            if(neighborS != None):
                stren = v_rules.get(
                    (iTile.get_label(), neighborS.get_label()))
                if(stren != None):
                    attStr += int(stren)
            if(neighborE != None):
                stren = h_rules.get(
                    (iTile.get_label(), neighborE.get_label()))
                if(stren != None):
                    attStr += int(stren)
            # else:
            #    print("East of "+ str(iX) + " : " + str(iY) + " is empty")
            if(neighborW != None):
                stren = h_rules.get(
                    (neighborW.get_label(), iTile.get_label()))
                if(stren != None):
                    attStr += int(stren)
            # else:
            #    print("West of "+ str(iX) + " : " + str(iY) + " is empty")

            #print(iTile.get_label(), ": ", attStr)
            if attStr >= sy.returnTemp():
                attMove = {"type": "a"}

                attMove["x"] = x
                attMove["y"] = y
                attMove["state1"] = iTile

                attachments_list.append(attMove)
        return attachments_list


    def getTRat(self, sy, x, y, dir=None):
        transitions_list = []
        sys_h_tr = sy.returnHorizontalTransitionDict()
        sys_v_tr = sy.returnVerticalTransitionDict()

        iTile = self.coords.get(toCoords(x, y))
        
        if iTile == None:
            return transitions_list

                # Get only the south and east neighbors of iTile
        neighborS = self.coords.get(toCoords(x, y - 1))
        neighborE = self.coords.get(toCoords(x + 1, y))

        if dir == None or dir == "v":
            if(neighborS != None):
                    # second dictionary
                    # rules = iVTranRules.get(neighborS.get_label())
                    rules = sys_v_tr.get(
                        (iTile.get_label(), neighborS.get_label()))
                    # rules.append(iVTranRules)
                    if rules != None:
                        for i in range(0, len(rules), 2):     
                            move = {"type": "t"}
                            move["x"] = iTile.x
                            move["y"] = iTile.y
                            move["dir"] = "v"
                            move["state1"] = iTile.get_state()
                            move["state2"] = neighborS.get_state()
                          
                            move["state1Final"] = sy.get_state(
                                rules[i])  # .returnLabel1Final()
                            move["state2Final"] = sy.get_state(
                                rules[i + 1])  # .returnLabel2Final()
                            transitions_list.append(move)


        if dir == None or dir == "h":
            if(neighborE != None):
                    # second dictionary
                    # rules = iVTranRules.get(neighborS.get_label())
                    rules = sys_h_tr.get(
                        (iTile.get_label(), neighborE.get_label()))
                    # rules.append(iVTranRules)
                    if rules != None:
                        for i in range(0, len(rules), 2): 
                            move = {"type": "t"}
                            move["x"] = iTile.x
                            move["y"] = iTile.y
                            move["dir"] = "h"
                            move["state1"] = iTile.get_state()
                            move["state2"] = neighborE.get_state()
  
                            move["state1Final"] = sy.get_state(
                                rules[i])  # .returnLabel1Final()
                            move["state2Final"] = sy.get_state(
                                rules[i + 1])  # .returnLabel2Final()
                            transitions_list.append(move)

        return transitions_list




                    
            

# Not in use right now.


class SeedAssemblyTile:
    def __init__(self, label, x, y):
        self.label = label
        self.x = x
        self.y = y


class AffinityRule:
    def __init__(self, label1, label2, dir, strength=None):
        self.label1 = label1  # Left/Upper label
        self.label2 = label2  # Right/Bottom label
        if strength == None:
            self.strength = 1
        else:
            self.strength = strength  # Bond Strength (as a string)
        self.dir = dir

    # Getters
    def returnLabel1(self):
        return self.label1

    def returnLabel2(self):
        return self.label2

    def returnStr(self):
        return self.strength

    def returnDir(self):
        return self.dir


class TransitionRule:
    def __init__(self, label1, label2, label1Final, label2Final, dir):
        self.label1 = label1
        self.label2 = label2
        self.label1Final = label1Final
        self.label2Final = label2Final
        self.dir = dir

    # Getters
    def returnLabel1(self):
        return self.label1

    def returnLabel2(self):
        return self.label2

    def returnLabel1Final(self):
        return self.label1Final

    def returnLabel2Final(self):
        return self.label2Final

    def returnDir(self):
        return self.dir


# System is used for the assembler; represents the data in the XML
class System:
    # Horizontal Hash Rule
    # Vertical Hash Rules
    # Horizontal Transition Rules
    # Vertical Transition Rules
    # Temp int
    # Initial List of States
    # Seed Assembly Object
    def __init__(self, temp, states, initial_states, seed_states=None, vertical_affinities_list=None, horizontal_affinities_list=None, vertical_transitions_list=None, horizontal_transitions_list=None, tile_vertical_transitions=None, tile_horizontal_transitions=None, empty=False):
        self.temp = temp
        self.states = states
        self.initial_states = initial_states
        self.seed_states = seed_states

        # List versions of rules
        # Takes 2 tiles [N][S] and returns the glue strength between them as an int
        self.vertical_affinities_list = vertical_affinities_list
        # Takes 2 tiles [W][E] and returns the glue strength between them as an int
        self.horizontal_affinities_list = horizontal_affinities_list
        # Takes 2 tiles [N][S] and and returns the transition pair
        self.vertical_transitions_list = vertical_transitions_list
        # Takes 2 tiles [W][E] and returns the transition pair
        self.horizontal_transitions_list = horizontal_transitions_list

        # Takes tile and returns vertical transition pairs
        self.tile_vertical_transitions = tile_vertical_transitions
        # Takes tile and returns horizontal transition pairs
        self.tile_horizontal_transitions = tile_horizontal_transitions

        # Establish dictionaries
        self.vertical_affinities_dict = {}
        self.horizontal_affinities_dict = {}
        self.vertical_transitions_dict = {}
        self.horizontal_transitions_dict = {}

        # Translate list versions into dictionary versions
        if not empty:
            self.translateListsToDicts()

    def get_state(self, label):
        for state in self.states:
            if state.get_label() == label:
                return state
    # Utility
    # if tr remove dont work and still in system look here
    def translateListsToDicts(self):
        for rule in self.vertical_affinities_list:
            label1 = rule.returnLabel1()
            label2 = rule.returnLabel2()
            str = rule.returnStr()

            self.vertical_affinities_dict[label1, label2] = str
        for rule in self.horizontal_affinities_list:
            label1 = rule.returnLabel1()
            label2 = rule.returnLabel2()
            str = rule.returnStr()

            self.horizontal_affinities_dict[label1, label2] = str
        for rule in self.vertical_transitions_list:
            label1 = rule.returnLabel1()
            label2 = rule.returnLabel2()
            label1Final = rule.returnLabel1Final()
            label2Final = rule.returnLabel2Final()

            key = (label1, label2)
            transition = (label1Final, label2Final)

            self.add_values_in_dict(
                self.vertical_transitions_dict, key, transition)

            # self.vertical_transitions_dict[label1, label2] = (
            #    label1Final, label2Final)
        for rule in self.horizontal_transitions_list:
            label1 = rule.returnLabel1()
            label2 = rule.returnLabel2()
            label1Final = rule.returnLabel1Final()
            label2Final = rule.returnLabel2Final()

            key = (label1, label2)
            transition = (label1Final, label2Final)

            self.add_values_in_dict(
                self.horizontal_transitions_dict, key, transition)
            # self.horizontal_transitions_dict[label1, label2] = (
            #    label1Final, label2Final)

    def get_state(self, label):
        for state in self.states:
            if state.get_label() == label:
                return state
        print("State: ", label, "not found")
        return None

    def add_values_in_dict(self, dict, key, list_of_values):
        if key not in dict:
            dict[key] = list()
        dict[key].extend(list_of_values)

    # Getters

    def returnTemp(self):
        return int(self.temp)

    def returnStates(self):
        return self.states

    def returnInitialStates(self):
        return self.initial_states

    def returnSeedStates(self):
        return self.seed_states

    def returnVerticalAffinityList(self):
        return self.vertical_affinities_list

    def returnHorizontalAffinityList(self):
        return self.horizontal_affinities_list

    def returnVerticalTransitionList(self):
        return self.vertical_transitions_list

    def returnHorizontalTransitionList(self):
        return self.horizontal_transitions_list

    def returnVerticalAffinityDict(self):
        return self.vertical_affinities_dict

    def returnHorizontalAffinityDict(self):
        return self.horizontal_affinities_dict

    def returnVerticalTransitionDict(self):
        return self.vertical_transitions_dict

    def returnHorizontalTransitionDict(self):
        return self.horizontal_transitions_dict

    def get_tile_vertical_transitions(self):
        return self.tile_vertical_transitions

    def get_tile_horizontal_transitions(self):
        return self.tile_horizontal_transitions

    # Displayers

    def displayVerticalAffinityDict(self):
        print(self.vertical_affinities_dict)

    def displayHorizontalAffinityDict(self):
        print(self.horizontal_affinities_dict)

    def displayVerticalTransitionDict(self):
        print(self.vertical_transitions_dict)

    def displayHorizontalTransitionDict(self):
        print(self.horizontal_transitions_dict)

    # Clearers
    def clearVerticalAffinityList(self):
        self.vertical_affinities_list.clear()

    def clearHorizontalAffinityList(self):
        self.horizontal_affinities_list.clear()

    def clearVerticalTransitionList(self):
        self.vertical_transitions_list.clear()

    def clearHorizontalTransitionList(self):
        self.horizontal_transitions_list.clear()

    def clearVerticalAffinityDict(self):
        self.vertical_affinities_dict.clear()

    def clearHorizontalAffinityDict(self):
        self.horizontal_affinities_dict.clear()

    def clearVerticalTransitionDict(self):
        self.vertical_transitions_dict.clear()

    def clearHorizontalTransitionDict(self):
        self.horizontal_transitions_dict.clear()

    # Dictionary Appenders
    # Note: Value = Bond Strength
    def appendVerticalAffinityDict(self, label1, label2, value):
        self.vertical_affinities_dict[label1, label2] = value

    def appendHorizontalAffinityDict(self, label1, label2, value):
        self.horizontal_affinities_dict[label1, label2] = value

    def appendVerticalTransitionDict(self, label1, label2, label1Final, label2Final):
        self.vertical_transitions_dict[label1, label2] = (
            label1Final, label2Final)

    def appendHorizontalTransitionDict(self, label1, label2, label1Final, label2Final):
        self.horizontal_transitions_dict[label1, label2] = (
            label1Final, label2Final)

    # TO DO Update these to write to a dictionary, and to use lists of objects from universalClasses.py

    def set_tile_vertical_transitions(self, tile_vt):
        self.tile_vertical_transitions = tile_vt

    def set_tile_horizontal_transitions(self, tile_ht):
        self.tile_horizontal_transitions = tile_ht
    # each of these: add a remove functions to UC to call
    def add_State(self, state):
        if isinstance(state, list):
            for s in state:
                self.states.append(s)
        elif isinstance(state, State):
            self.states.append(state)
        else:
            print("Attempted to add a state that is not a state object")
            
    def return_list_of_state_labels(self):
        st = []
        cst = self.returnStates()
        for s in cst:
            st.append(s.get_label())
            
        return st    
        
    def add_Initial_State(self, state):
        self.initial_states.append(state)

    # idk if this will work
    def add_Seed_State(self, state):
        self.seed_states.append(state)

    def remove_state(self, state):
        # if 
        if isinstance(state, list):
            for s in state:
                self.states.remove(s)
        elif isinstance(state, State):
            self.states.remove(state)

    # start here 
    def add_transition_rule(self, tr):
        label1 = tr.returnLabel1()
        label2 = tr.returnLabel2()
        label1Final = tr.returnLabel1Final()
        label2Final = tr.returnLabel2Final()
        direct = tr.returnDir()

        if direct == "v":
            self.vertical_transitions_list.append(tr)

            oldList = self.vertical_transitions_dict.get((label1, label2))

            if oldList == None:
                oldList = [label1Final, label2Final]
            else:
                oldList.append(label1Final)
                oldList.append(label2Final)

            self.vertical_transitions_dict[label1, label2] = oldList
        else:
            self.horizontal_transitions_list.append(tr)

            oldList = self.horizontal_transitions_dict.get((label1, label2))

            if oldList == None:
                oldList = [label1Final, label2Final]
            else:
                oldList.append(label1Final)
                oldList.append(label2Final)

            

            self.horizontal_transitions_dict[label1, label2] = oldList

    def add_affinity(self, a):
        label1 = a.returnLabel1()
        label2 = a.returnLabel2()
        direct = a.returnDir()
        stren = a.returnStr()

        if direct == "v":
            self.vertical_affinities_list.append(a)
            self.vertical_affinities_dict[(label1, label2)] = stren
        else:
            self.horizontal_affinities_list.append(a)
            self.horizontal_affinities_dict[(label1, label2)] = stren
