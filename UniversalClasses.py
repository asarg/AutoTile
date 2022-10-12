from cgitb import lookup
import unicodedata as ud
import random
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor, QFont, QFontDatabase
# These classes are used for Loading and Saving Files and Communicating with general_TA_simulator.


def toCoords(x, y):
    return "(" + str(x) + "," + str(y) + ")"
class State:
    def __init__(self, label, color, display_label=None, display_label_font="Fira Code Regular Nerd Font Complete Mono", display_label_color ="black", xCoordinate = 0, yCoordinate = 0):
        self.label = label
        self.color = color
        self.display_label = display_label

        if display_label is None:
            self.display_label = label
            #self.display_label = label.encode('utf-8')

        else:
            #self.display_label = display_label.encode('utf-8')
            self.display_label = display_label

        if display_label_font is str:
            self.display_label_font = QFont(display_label_font)

        else:
            self.display_label_font = display_label_font

        if display_label_color is str:
            self.display_label_color = QColor(display_label_color)

        else: self.display_label_color = display_label_color

    # Getters
    def returnLabel(self):
        return self.label

    def returnColor(self):
        return self.color

    def returnDisplayLabel(self):
        if self.display_label is str:
            return self.display_label
        else:
            return self.returnLabel()
            

    def returnDisplayLabelColor(self):
        if self.display_label_color is str:
            return self.display_label_color
        else:
            return self.returnColor()

    def returnDisplayLabelFont(self):
        return self.display_label_font

    def setDisplayLabel(self, display_label):
        self.display_label = display_label
        #self.display_label = display_label.encode('utf-8')

    def setDisplayLabelFont(self, display_label_font):
        if display_label_font is str:
            self.display_label_font = QFont(display_label_font)
        else:
            self.display_label_font = display_label_font

    def setDisplayLabelColor(self, display_label_color):
        if display_label_color is str:
            self.display_label_color = QColor(display_label_color)
        else:
            self.display_label_color = display_label_color

    def __eq__(self, other):
        if isinstance(other, State):
            return self.label == other.label and self.color == other.color





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
        s = self.state.label + " (" + str(self.x) + ", " + str(self.y) + ")"
        return s
    def setState(self, s):
        self.state = s
    def setLabel(self, l):
        self.state.label = l

    def setDisplayLabel(self, display_label):
        try:
            self.state.setDisplayLabel(display_label)
        except Exception as e:
            raise e

    def setDisplayLabelFont(self, display_label_font):
        try:
            self.state.setDisplayLabelFont(display_label_font)
        except Exception as e:
            raise e

    def setDisplayLabelColor(self, display_label_color):
        try:
            self.state.setDisplayLabelColor(display_label_color)
        except Exception as e:
            raise e
    def returnColor(self):
        return self.state.returnColor()
    def returnLabel(self):
        return self.state.returnLabel()
    def returnState(self):
        return self.state
    def returnDisplayLabel(self):
        return self.state.returnDisplayLabel()
    def returnDisplayLabelColor(self):
        return self.state.returnDisplayLabelColor()
    def returnDisplayLabelFont(self):
        return self.state.returnDisplayLabelFont()

    def getX(self):
        return self.x
    def getY(self):
        return self.y

    def returnPosition(self):
        return "({self.x}, {self.y})".format(self=self)


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

    def returnBorders(self):
        borders_list = [self.leftMost, self.rightMost, self.upMost, self.downMost]
        return borders_list

    def returnLabel(self):
        return self.label

    def returnTiles(self):
        return self.tiles

    def returnAttachments(self, sy):  # takes in a system
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
                            (neighborN.returnLabel(), iTile.returnLabel()))
                        if(stren != None):
                            attStr += int(stren)
                    if(neighborS != None):
                        stren = v_rules.get(
                            (iTile.returnLabel(), neighborS.returnLabel()))
                        if(stren != None):
                            attStr += int(stren)
                    if(neighborE != None):
                        stren = h_rules.get(
                            (iTile.returnLabel(), neighborE.returnLabel()))
                        if(stren != None):
                            attStr += int(stren)
                    # else:
                    #    print("East of "+ str(iX) + " : " + str(iY) + " is empty")
                    if(neighborW != None):
                        stren = h_rules.get(
                            (neighborW.returnLabel(), iTile.returnLabel()))
                        if(stren != None):
                            attStr += int(stren)
                    # else:
                    #    print("West of "+ str(iX) + " : " + str(iY) + " is empty")

                    #print(iTile.returnLabel(), ": ", attStr)
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
        # print(len(attachments_list), " Attachments")

        return attachments_list
        # ORIGINAL tuple of ((coord pair), (current labels), (transition labels))

    def returnTransitions(self, sy):  # takes in a system
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
        #sys_h_tiles = sy.returnTileHorizontalTransitions()
        #sys_v_tiles = sy.returnTileVerticalTransitions()

        # Check each tile in the assembly
        for iTile in self.tiles:
           # print(sys_h_tiles[iTile.returnLabel()])
            # if isinstance(sys_h_tiles[iTile.returnLabel()], tuple):

            #iHTranRules = None
            #iVTranRules = None

            # if sys_h_tiles != None:
            # if sys_h_tiles.get(iTile.returnLabel()) != None:
            #iHTranRules = sys_h_tr[sys_h_tiles[iTile.returnLabel()]]
            # else:
            # for tiles in sys_h_tiles[iTile.returnLabel()]:
            #iHTranRules = sys_h_tr[tiles]

            # if isinstance(sys_v_tiles[iTile.returnLabel()], tuple):
            # if sys_v_tiles != None:
            # if sys_v_tiles.get(iTile.returnLabel()):
            #iVTranRules = sys_v_tr[sys_v_tiles[iTile.returnLabel()]]
            # else:
            # for tiles in sys_v_tiles[iTile.returnLabel()]:
            #iVTranRules = sys_v_tr[tiles]

            # Get only the south and east neighbors of iTile
            neighborS = self.coords.get(toCoords(iTile.x, iTile.y - 1))
            neighborE = self.coords.get(toCoords(iTile.x + 1, iTile.y))

            if(neighborS != None):
                # second dictionary
                # rules = iVTranRules.get(neighborS.returnLabel())
                rules = sys_v_tr.get(
                    (iTile.returnLabel(), neighborS.returnLabel()))
                # rules.append(iVTranRules)
                if rules != None:
                    for i in range(0, len(rules), 2):
                        move = {"type": "t"}
                        move["x"] = iTile.x
                        move["y"] = iTile.y
                        move["dir"] = "v"
                        move["state1"] = iTile.returnState()
                        move["state2"] = neighborS.returnState()

                        move["state1Final"] = sy.returnState(
                            rules[i])  # .returnLabel1Final()
                        move["state2Final"] = sy.returnState(
                            rules[i + 1])  # .returnLabel2Final()
                        transitions_list.append(move)

            if(neighborE != None):
                #rules = iHTranRules[neighborE.returnLabel()]
                rules = sys_h_tr.get(
                    (iTile.returnLabel(), neighborE.returnLabel()))
                # print(sys_h_tr)
                # rules.append(iHTranRules)

                if rules != None:
                    #print(iTile.returnLabel() + " : " + str(len(rules)))
                    for i in range(0, len(rules), 2):
                        move = {"type": "t"}
                        move["x"] = iTile.x
                        move["y"] = iTile.y
                        move["dir"] = "h"
                        move["state1"] = iTile.returnState()
                        move["state2"] = neighborE.returnState()

                        move["state1Final"] = sy.returnState(
                            rules[i])  # .returnLabel1Final()
                        move["state2Final"] = sy.returnState(
                            rules[i + 1])  # .returnLabel2Final()
                        transitions_list.append(move)

        return transitions_list
        # ORIGINAL ((type: ), (current labels), (transition labels))

    def returnMoves(self, sy):
        #print("attachments: " + str(len(self.returnAttachments(sy))) + " transitions: " + str(len(self.returnTransitions(sy))))
        return self.returnAttachments(sy) + self.returnTransitions(sy)

    def setLabel(self, l):
        self.label = l
    def setTiles(self, t):
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

    def setTilesFromList(self, t):
        #takes in a list of tile objects
        for tile in t:
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
    def setAttachments(self, att):  # tuple of ((type: ), (x: ), (y: ), (state1: ))
        # a = Assembly()
        #a.label = self.label + "A " + att["state1"]
        # a.setTiles(self.tiles.copy())
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

    # tuple of {'type': 't', 'x': 0, 'y': 0, 'state1': 'S', 'state2': 'A', 'state1Final': 'S', 'state2Final': 'A'}
    def setTransition(self, trans):
        # a = Assembly()
        # originally trans[2][0] + trans[2][1]
        self.label = self.label + "T " + \
            trans["state1Final"].returnLabel() + trans["state2Final"].returnLabel()
        # self.setTiles(self.tiles.copy())
        #change = trans["type"]

        # print(a.tiles[change])
        #print(trans["state2Final"].returnLabel())
        #print(trans["type"])
        self.coords[toCoords(trans["x"], trans["y"])].setState(
            trans["state1Final"])
        # a.tiles[trans["x"]][trans["y"]].setState(trans["state1Final"])
        if(trans["dir"] == "v"):
            self.coords[toCoords(trans["x"], trans["y"] - 1)].setState(trans["state2Final"])
        if(trans["dir"] == "h"):
            self.coords[toCoords(trans["x"] + 1, trans["y"])].setState(trans["state2Final"])
        #print("New Assembly Tiles: ", a.tiles)

    def performMove(self, move):
        if(move["type"] == "a"):
            self.setAttachments(move)
        if(move["type"] == "t"):
            self.setTransition(move)

    def undoMove(self, move):
        a = Assembly()
        a.setTiles(self.tiles.copy())

        x = move["x"]
        y = move["y"]

        if(move["type"] == "t"):
            a.coords[toCoords(x, y)].setState(move["state1"])
            # a.tiles[trans["x"]][trans["y"]].setState(trans["state1Final"])
            if(move["dir"] == "v"):
                a.coords[toCoords(move["x"], move["y"] - 1)
                        ].setState(move["state2"])
            if(move["dir"] == "h"):
                a.coords[toCoords(move["x"] + 1, move["y"])
                        ].setState(move["state2"])



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
                    (neighborN.returnLabel(), iTile.returnLabel()))
                if(stren != None):
                    attStr += int(stren)
            if(neighborS != None):
                stren = v_rules.get(
                    (iTile.returnLabel(), neighborS.returnLabel()))
                if(stren != None):
                    attStr += int(stren)
            if(neighborE != None):
                stren = h_rules.get(
                    (iTile.returnLabel(), neighborE.returnLabel()))
                if(stren != None):
                    attStr += int(stren)
            # else:
            #    print("East of "+ str(iX) + " : " + str(iY) + " is empty")
            if(neighborW != None):
                stren = h_rules.get(
                    (neighborW.returnLabel(), iTile.returnLabel()))
                if(stren != None):
                    attStr += int(stren)
            # else:
            #    print("West of "+ str(iX) + " : " + str(iY) + " is empty")

            #print(iTile.returnLabel(), ": ", attStr)
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
                    # rules = iVTranRules.get(neighborS.returnLabel())
                    rules = sys_v_tr.get(
                        (iTile.returnLabel(), neighborS.returnLabel()))
                    # rules.append(iVTranRules)
                    if rules != None:
                        for i in range(0, len(rules), 2):
                            move = {"type": "t"}
                            move["x"] = iTile.x
                            move["y"] = iTile.y
                            move["dir"] = "v"
                            move["state1"] = iTile.returnState()
                            move["state2"] = neighborS.returnState()

                            move["state1Final"] = sy.returnState(
                                rules[i])  # .returnLabel1Final()
                            move["state2Final"] = sy.returnState(
                                rules[i + 1])  # .returnLabel2Final()
                            transitions_list.append(move)


        if dir == None or dir == "h":
            if(neighborE != None):
                    # second dictionary
                    # rules = iVTranRules.get(neighborS.returnLabel())
                    rules = sys_h_tr.get(
                        (iTile.returnLabel(), neighborE.returnLabel()))
                    # rules.append(iVTranRules)
                    if rules != None:
                        for i in range(0, len(rules), 2):
                            move = {"type": "t"}
                            move["x"] = iTile.x
                            move["y"] = iTile.y
                            move["dir"] = "h"
                            move["state1"] = iTile.returnState()
                            move["state2"] = neighborE.returnState()

                            move["state1Final"] = sy.returnState(
                                rules[i])  # .returnLabel1Final()
                            move["state2Final"] = sy.returnState(
                                rules[i + 1])  # .returnLabel2Final()
                            transitions_list.append(move)

        return transitions_list

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
    def __init__(self, temp, states, initial_states, seed_states=None, vertical_affinities_list=[], horizontal_affinities_list=[], vertical_transitions_list=[], horizontal_transitions_list=[], tile_vertical_transitions=[], tile_horizontal_transitions=[], seed_assembly = Assembly(), empty=False):
        self.temp = temp
        self.states = states
        self.initial_states = initial_states
        self.seed_states = seed_states
        self.seed_assembly = seed_assembly

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


    def add_values_in_dict(self, dict, key, list_of_values):
        if key not in dict:
            dict[key] = list()
        dict[key].extend(list_of_values)

    # Getters
    def returnState(self, label):
        for state in self.states:
            if state.returnLabel() == label:
                return state
        print("State: ", label, "not found")
        return None


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

    def returnTileVerticalTransitions(self):
        return self.tile_vertical_transitions

    def returnTileHorizontalTransitions(self):
        return self.tile_horizontal_transitions

    def returnSeedAssembly(self):
        return self.seed_assembly
    
    def returnTiles(self):
        return self.seed_assembly.returnTiles()

    def returnStateLabelList(self):
        st = []
        cst = self.returnStates()
        for s in cst:
            st.append(s.returnLabel())

        return st

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

    def setTileVerticalTransitions(self, tile_vt):
        self.tile_vertical_transitions = tile_vt

    def setTileHorizontalTransitions(self, tile_ht):
        self.tile_horizontal_transitions = tile_ht

    def setSeedAssembly(self, assembly):
        self.seed_assembly = assembly
    # each of these: add a remove functions to UC to call
    def addState(self, state):
        if isinstance(state, list):
            for s in state:
                self.states.append(s)
        elif isinstance(state, State):
            self.states.append(state)
        else:
            print("Attempted to add a state that is not a state object")

    def addInitialState(self, state):
        self.initial_states.append(state)

    # idk if this will work
    def addSeedState(self, state):
        self.seed_states.append(state)

    # start here
    def addTransitionRule(self, tr):
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

    def addAffinity(self, a):
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

    #if there is no preset assembly, pick a random seed state
    #do nothing if there is a preset assembly
    def makeSeedAssembly(self):
        if len(self.seed_assembly.tiles) == 0:
            try:
                seed = random.choice(self.seed_states)
                self.seed_assembly.setTiles([Tile(seed, 0, 0)])
            except:
                "There are no states set as seeds for this assembly."


    def removeState(self, state):
        # if
        if isinstance(state, list):
            for s in state:
                self.states.remove(s)
        elif isinstance(state, State):
            self.states.remove(state)