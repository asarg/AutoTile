import random
import UniversalClasses
import copy


# Debugging Functions
def printMove(move):
    if move["type"] == "a":
        print("Attach: ", move["state1"].get_label(),
              " at ", move["x"], ", ", move["y"])
    if move["type"] == "t":
        print("Transition ", move["state1"].get_label(), ", ", move["state2"].get_label(
        ), " to ", move["state1Final"].get_label(), ", ", move["state2Final"].get_label())
        print(" at ", move["x"], ", ", move["y"])


class Engine:
    def __init__(self, currentSystem):
        self.reset_engine(currentSystem)

    def reset_engine(self, currentSystem):
        self.system = currentSystem
        self.moveList = []
        self.TimeTaken = []
        self.currentIndex = 0
        self.lastIndex = 0

        # Get seed
        print(self.system.returnSeedStates())

        seedState = random.choice(self.system.returnSeedStates())
        seed = UniversalClasses.Tile(seedState, 0, 0)
        self.seedAssembly = UniversalClasses.Assembly()
        self.seedAssembly.set_tiles([seed])
        # Changed from adding to list to setting it as the current assembly
        # self.assemblyList.append(seedAssembly)
        # self.currentAssembly = self.seedAssembly
        self.currentAssembly = copy.deepcopy(self.seedAssembly)

        self.validMoves = self.currentAssembly.getMoves(self.system)

    def step(self, nextMove=None):

        # we are in our history, but they did NOT give us a new move
        if nextMove == None and self.currentIndex < self.lastIndex:
            move = self.moveList[self.currentIndex]
            res = self.build(move)
            if res == -1:
                return res
            else:
                # added a duplicate inside of build, remove it
                self.moveList.pop()
                self.currentIndex += 1
                return 0

        # we are in our history, and they gave us a new move to use instead
        if nextMove != None and self.currentIndex < self.lastIndex:
            # remove move list entries that are ahead of us
            while self.currentIndex != self.lastIndex:
                self.moveList.pop()
                self.lastIndex -= 1

            # now we can act like this is just a normal step
            # fall out the if statement into the normal step case

        # No history to worry about, just call build
        res = self.build(nextMove)
        if res == -1:
            return res
        else:
            self.lastIndex += 1
            self.currentIndex += 1
            return 0

    def back(self):
        if(self.currentIndex > 0):
            self.currentIndex = self.currentIndex - 1
            move = self.moveList[self.currentIndex]
            self.build(move, False)

    def first(self):
        self.currentIndex = 0
        self.currentAssembly = copy.deepcopy(self.seedAssembly)
        self.validMoves = self.currentAssembly.getMoves(self.system)

    def last(self):
        while self.currentIndex < self.lastIndex:
            # Will update current assembly, break if terminal
            if self.step() == -1:
                break

    def getCurrentAssembly(self):
        return self.currentAssembly

    def getCurrentIndex(self):
        return self.currentIndex

    def getCurrentMove(self):
        if len(self.moveList) != 0:
            return self.moveList[self.getCurrentIndex() - 1]

    def getLastMove(self):
        if len(self.moveList) != 0:
            return self.moveList[self.getCurrentIndex()]

    def getCurrentBorders(self):
        return self.currentAssembly.get_borders()

    def build(self, nextMove=None, forwards=True):

        # Check if assembly is terminal
        if(len(self.validMoves) == 0 and forwards):
            print("Terminal")
            self.currentAssembly.print_size()
            return -1

        # Add or Update only if we going forwards
        if forwards:
            if len(self.TimeTaken) <= self.currentIndex:
                self.TimeTaken.append(len(self.validMoves))
            else:
                self.TimeTaken[self.currentIndex] = len(self.validMoves)

        # Get next assembly and add to list
        # If given a move, choose that one, otherwise do random move
        move = None
        if nextMove == None:
            move = random.choice(self.validMoves)
        else:
            move = nextMove

        moveX = move["x"]
        moveY = move["y"]

        # get all moves that need to be removed

        # If Attachment
        if move["type"] == "a":
            # Remove other moves for self
            attOldMoves = self.currentAssembly.getAttat(
                self.system, moveX, moveY)
            self.removeMoves(attOldMoves)

            # remove Attachments for neighbors
            nAtts = self.currentAssembly.getAttat(
                self.system, moveX, moveY + 1)
            self.removeMoves(nAtts)

            sAtts = self.currentAssembly.getAttat(
                self.system, moveX, moveY - 1)
            self.removeMoves(sAtts)

            wAtts = self.currentAssembly.getAttat(
                self.system, moveX - 1, moveY)
            self.removeMoves(wAtts)

            eAtts = self.currentAssembly.getAttat(
                self.system, moveX + 1, moveY)
            self.removeMoves(eAtts)

            # remove transitions when going backwards
            if not forwards:
                # remove other move for self
                trOldMoves = self.currentAssembly.getTRat(
                    self.system, moveX, moveY)
                self.removeMoves(trOldMoves)

                # remove "v" TR moves from N neighbor
                vOldMoves = self.currentAssembly.getTRat(
                    self.system, moveX, moveY + 1, "v")
                self.removeMoves(vOldMoves)

                # remove "h" TR moves from W Neighbor
                hOldMoves = self.currentAssembly.getTRat(
                    self.system, moveX - 1, moveY, "h")
                self.removeMoves(hOldMoves)

        elif move["type"] == "t":
            # Removing Moves
            # remove other move for self
            trOldMoves = self.currentAssembly.getTRat(
                self.system, moveX, moveY)
            self.removeMoves(trOldMoves)

            # remove "v" TR moves from N neighbor
            vOldMoves = self.currentAssembly.getTRat(
                self.system, moveX, moveY + 1, "v")
            self.removeMoves(vOldMoves)

            # remove "h" TR moves from W Neighbor
            hOldMoves = self.currentAssembly.getTRat(
                self.system, moveX - 1, moveY, "h")
            self.removeMoves(hOldMoves)

            # remove attachment rules from neighbors
            nAtts = self.currentAssembly.getAttat(
                self.system, moveX, moveY + 1)
            self.removeMoves(nAtts)

            sAtts = self.currentAssembly.getAttat(
                self.system, moveX, moveY - 1)
            self.removeMoves(sAtts)

            wAtts = self.currentAssembly.getAttat(
                self.system, moveX - 1, moveY)
            self.removeMoves(wAtts)

            eAtts = self.currentAssembly.getAttat(
                self.system, moveX + 1, moveY)
            self.removeMoves(eAtts)

            # Update tile 2
            # If V rule
            if move["dir"] == "v":
                # Removing moves
                # remove TR from self
                vOldMoves = self.currentAssembly.getTRat(
                    self.system, moveX, moveY - 1)
                self.removeMoves(vOldMoves)

                # Remove "h" rules for SW
                swMoves = self.currentAssembly.getTRat(
                    self.system, moveX - 1, moveY - 1, "h")
                self.removeMoves(swMoves)

                # Remove attachments from neighbors
                s2Atts = self.currentAssembly.getAttat(
                    self.system, moveX, moveY - 2)
                self.removeMoves(s2Atts)

                swAtts = self.currentAssembly.getAttat(
                    self.system, moveX - 1, moveY - 1)
                self.removeMoves(swAtts)

                seAtts = self.currentAssembly.getAttat(
                    self.system, moveX + 1, moveY - 1)
                self.removeMoves(seAtts)

            # If H rule
            if move["dir"] == "h":
                # remove TR from self
                vOldMoves = self.currentAssembly.getTRat(
                    self.system, moveX + 1, moveY)
                self.removeMoves(vOldMoves)

                # Remove "v" rules for NE
                neMoves = self.currentAssembly.getTRat(
                    self.system, moveX + 1, moveY + 1, "v")
                self.removeMoves(neMoves)

                # remove attachments from neighbors
                e2Atts = self.currentAssembly.getAttat(
                    self.system, moveX + 2, moveY)
                self.removeMoves(e2Atts)

                neAtts = self.currentAssembly.getAttat(
                    self.system, moveX + 1, moveY + 1)
                self.removeMoves(neAtts)

                seAtts = self.currentAssembly.getAttat(
                    self.system, moveX + 1, moveY - 1)
                self.removeMoves(seAtts)

        # perform move
        if forwards:
            self.currentAssembly.performMove(move)
            self.moveList.append(move)
        else:
            self.currentAssembly = self.currentAssembly.undoMove(move)

        # add all moves that need to be added

        # If Attachment
        if move["type"] == "a":

            # Add Attachments for neighbors
            nAtts = self.currentAssembly.getAttat(
                self.system, moveX, moveY + 1)
            self.addMoves(nAtts)

            sAtts = self.currentAssembly.getAttat(
                self.system, moveX, moveY - 1)
            self.addMoves(sAtts)

            wAtts = self.currentAssembly.getAttat(
                self.system, moveX - 1, moveY)
            self.addMoves(wAtts)

            eAtts = self.currentAssembly.getAttat(
                self.system, moveX + 1, moveY)
            self.addMoves(eAtts)

            # Add attachments for the current x,y when going backwards
            if not forwards:
                backwardMoves = self.currentAssembly.getAttat(
                    self.system, moveX, moveY)
                self.addMoves(backwardMoves)

            # Add transitions for self
            newTR = self.currentAssembly.getTRat(self.system, moveX, moveY)
            self.addMoves(newTR)

            # Add "v" transitions for North Neighbor (New assembly)
            vTR = self.currentAssembly.getTRat(
                self.system, moveX, moveY + 1, "v")
            self.addMoves(vTR)

            # Add "h" transitions for W Neighbor (New Assembly)
            hTR = self.currentAssembly.getTRat(
                self.system, moveX - 1, moveY, "h")
            self.addMoves(hTR)

        elif move["type"] == "t":

            # Adding Moves
            # add new transitions rules for self
            newTR = self.currentAssembly.getTRat(self.system, moveX, moveY)
            self.addMoves(newTR)

            # Add "v" transitions for North Neighbor (New assembly)
            vTR = self.currentAssembly.getTRat(
                self.system, moveX, moveY + 1, "v")
            self.addMoves(vTR)

            # Add "h" transitions for W Neighbor (New Assembly)
            hTR = self.currentAssembly.getTRat(
                self.system, moveX - 1, moveY, "h")
            self.addMoves(hTR)

            # remove attachment rules from neighbors
            nAtts = self.currentAssembly.getAttat(
                self.system, moveX, moveY + 1)
            self.addMoves(nAtts)

            sAtts = self.currentAssembly.getAttat(
                self.system, moveX, moveY - 1)
            self.addMoves(sAtts)

            wAtts = self.currentAssembly.getAttat(
                self.system, moveX - 1, moveY)
            self.addMoves(wAtts)

            eAtts = self.currentAssembly.getAttat(
                self.system, moveX + 1, moveY)
            self.addMoves(eAtts)

            # Update tile 2
            # If V rule
            if move["dir"] == "v":

                # Adding Moves
                # Add TR to self
                vNewMoves = self.currentAssembly.getTRat(
                    self.system, moveX, moveY - 1)
                self.addMoves(vNewMoves)

                # Add "h" rules for SW
                swNewMoves = self.currentAssembly.getTRat(
                    self.system, moveX - 1, moveY - 1, "h")
                self.addMoves(swNewMoves)

                # Add attachments from neighbors
                s2Atts = self.currentAssembly.getAttat(
                    self.system, moveX, moveY - 2)
                self.addMoves(s2Atts)

                swAtts = self.currentAssembly.getAttat(
                    self.system, moveX - 1, moveY - 1)
                self.addMoves(swAtts)

                seAtts = self.currentAssembly.getAttat(
                    self.system, moveX + 1, moveY - 1)
                self.addMoves(seAtts)

            # If H rule
            if move["dir"] == "h":

                # add TR from self
                vNewMoves = self.currentAssembly.getTRat(
                    self.system, moveX + 1, moveY)
                self.addMoves(vNewMoves)

                # add "v" rules for ne
                neMoves = self.currentAssembly.getTRat(
                    self.system, moveX + 1, moveY + 1, "v")
                self.addMoves(neMoves)

                # add attachments from neighbors
                e2Atts = self.currentAssembly.getAttat(
                    self.system, moveX + 2, moveY)
                self.addMoves(e2Atts)

                neAtts = self.currentAssembly.getAttat(
                    self.system, moveX + 1, moveY + 1)
                self.addMoves(neAtts)

                seAtts = self.currentAssembly.getAttat(
                    self.system, moveX + 1, moveY - 1)
                self.addMoves(seAtts)

        return 0

    def removeMoves(self, oldMoves):
        if oldMoves == None:
            return

        if not isinstance(oldMoves, list):
            oldMoves = [oldMoves]

        for oMove in oldMoves:
            self.validMoves.remove(oMove)

    def addMoves(self, newMoves):
        if newMoves == None:
            return

        if not isinstance(newMoves, list):
            newMoves = [newMoves]

        for nMove in newMoves:
            self.validMoves.append(nMove)

    def timeTaken(self):
        if len(self.TimeTaken) > 0:
            return 1 / self.TimeTaken[self.currentIndex - 1]
        else:
            return 0
