from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPainter, QBrush, QPen

from PyQt5.QtCore import Qt
from random import randrange

from assemblyEngine import Engine
from UniversalClasses import System, Assembly, Tile
import TAMainWindow
import LoadFile
import SaveFile
import Assembler_Proto

import sys

# Global Variables
currentSystem = None
currentAssemblyHistory = []
# General Seeded TA Simulator


# Takes in:
# Seed State
# Set of States
# Set of Transition Rules
# Set of Affinities
# Creates
# A list of events based on transition rules states and affinities
# Add a tile or tiles
# Transition a tile(s)
# Make new assembly
# Attach assemblies
# An Assembly
# Outputs:
#
# GUI showing step by step growth starting with seed state
# Step button
# Keep growing until their are no more rules that apply

class Ui_MainWindow(QMainWindow, TAMainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #self.label = QtWidgets.QLabel()
        self.time = 0
        self.delay = 0
        self.seedX = 25
        self.seedY = 550

        self.textX = self.seedX + 10
        self.textY = self.seedY + 25

        self.tileSize = 6

        self.Engine = None
        self.SysLoaded = False
        self.play = True
        canvas = QtGui.QPixmap(1000, 600)
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)

        self.label_2.setText("")

        # this is "Load" on the "File" menu
        self.actionLoad.triggered.connect(self.Click_FileSearch)

        # "Save" from the "File" menu
        self.actionSave.triggered.connect(self.Click_SaveFile)

        self.actionFirst.triggered.connect(self.first_step)

        self.actionPrevious.triggered.connect(self.prev_step)

        self.actionStop.triggered.connect(self.stop_sequence)

        self.actionPlay.triggered.connect(self.play_sequence)

        self.actionNext.triggered.connect(self.next_step)

        self.actionLast.triggered.connect(self.last_step)

    def draw_tiles(self, assembly):
        painter = QPainter(self.label.pixmap())
        pen = QtGui.QPen()
        brush = QtGui.QBrush()
        font = QtGui.QFont()

        pen.setWidth(3)

        brush.setStyle(Qt.SolidPattern)

        pen.setColor(QtGui.QColor("white"))
        brush.setColor(QtGui.QColor("white"))
        painter.setPen(pen)
        painter.setBrush(brush)
        # this block is drawing a big white rectangle across the screen to "clear" it
        painter.drawRect(0, 0, 1000, 1000)

        font.setFamily("Times")
        font.setBold(True)
        painter.setFont(font)
        for tile in assembly.tiles:
            # print(tile[0].color)
            pen.setColor(QtGui.QColor("black"))
            brush.setColor(QtGui.QColor("#" + tile.get_color()))

            painter.setPen(pen)
            painter.setBrush(brush)
            painter.drawRect((tile.x * self.tileSize) + self.seedX, (tile.y * -
                             self.tileSize) + self.seedY, self.tileSize, self.tileSize)
            #painter.drawText((tile.x * self.tileSize) + self.textX,
                             #(tile.y * -self.tileSize) + self.textY, tile.state.label)

        painter.end()

        if self.Engine.currentIndex != 0:
            self.label_2.setText("Time elapsed: " +
                                 str(self.time) + " seconds")
            self.label_3.setText("Current step time: " +
                                 str(self.Engine.timeTaken()) + " seconds")
        else:
            self.label_2.setText("Time elapsed: 0 seconds")
            self.label_3.setText("Current step time: 0 seconds")

        print(self.Engine.currentIndex)
        self.update()

    def Click_Run_Simulation(self):  # Run application if everythings good
        err_flag = False

        if(err_flag == False):
            self.step = 0
            self.time = 0
            # Assembler_Proto.Main()
            self.draw_tiles(Assembler_Proto.CompleteAssemblyHistory[self.step])

    def Click_FileSearch(self, id):
        self.stop_sequence()
        self.SysLoaded = False
        file = QFileDialog.getOpenFileName(
            self, "Select XML Document", "", "XML Files (*.xml)")
        if file[0] != '':
            # Simulator must clear all of LoadFile's global variables when the user attempts to load something.
            LoadFile.HorizontalAffinityRules.clear()
            LoadFile.VerticalAffinityRules.clear()
            LoadFile.HorizontalTransitionRules.clear()
            LoadFile.VerticalTransitionRules.clear()
            LoadFile.SeedStateSet.clear()
            LoadFile.InitialStateSet.clear()
            LoadFile.CompleteStateSet.clear()

            LoadFile.readxml(file[0])

            # Creating global variables
            global temp
            global states
            global inital_states
            global seed_assembly
            global seed_states
            global vertical_affinities
            global horizontal_affinities
            global vertical_transitions
            global horizontal_transitions

            # Creating a System object from data read.
            temp = LoadFile.Temp
            states = LoadFile.CompleteStateSet
            inital_states = LoadFile.InitialStateSet
            seed_states = LoadFile.SeedStateSet
            vertical_affinities = LoadFile.VerticalAffinityRules
            horizontal_affinities = LoadFile.HorizontalAffinityRules
            vertical_transitions = LoadFile.VerticalTransitionRules
            horizontal_transitions = LoadFile.HorizontalTransitionRules

            self.SysLoaded = True

            # Establish the current system we're working with
            currentSystem = System(temp, states, inital_states, seed_states, vertical_affinities,
                                   horizontal_affinities, vertical_transitions, horizontal_transitions)
            print("\nSystem Dictionaries:")
            print("Vertical Affinities:")
            currentSystem.displayVerticalAffinityDict()
            print("Horizontal Affinities:")
            currentSystem.displayHorizontalAffinityDict()
            print("Vertical Transitions:")
            currentSystem.displayVerticalTransitionDict()
            print("Horizontal Transitions:")
            currentSystem.displayHorizontalTransitionDict()

            self.time = 0
            self.Engine = Engine(currentSystem)
            #a = Assembly()
            #t = Tile(currentSystem.returnSeedStates(), 0, 0)
            # a.tiles.append(t)
            # currentAssemblyHistory.append(a)
            # Assembler_Proto.Main()
            self.draw_tiles(self.Engine.getCurrentAssembly())

    def Click_SaveFile(self):
        # Creating a System object from data read.
        if(self.SysLoaded == True):
            temp = LoadFile.Temp
            states = LoadFile.CompleteStateSet
            inital_states = LoadFile.InitialStateSet
            seed_states = LoadFile.SeedStateSet
            vertical_affinities = LoadFile.VerticalAffinityRules
            horizontal_affinities = LoadFile.HorizontalAffinityRules
            vertical_transitions = LoadFile.VerticalTransitionRules
            horizontal_transitions = LoadFile.HorizontalTransitionRules

            # Establish the current system we're working with
            currentSystem = System(temp, states, inital_states, seed_states, vertical_affinities,
                                   horizontal_affinities, vertical_transitions, horizontal_transitions)

            fileName = QFileDialog.getSaveFileName(
                self, "QFileDialog.getSaveFileName()", "", "XML Files (*.xml)")

            if(fileName[0] != ''):
                SaveFile.main(currentSystem, fileName)

    # self.draw_tiles(LoadFile.) #starting assembly goes here

    def first_step(self):
        if self.SysLoaded == True:
            self.stop_sequence()
            self.Engine.first()
            self.time = 0
            # print(self.Engine.currentIndex)
            self.draw_tiles(self.Engine.getCurrentAssembly())

    def prev_step(self):
        self.stop_sequence()
        if self.SysLoaded == True:
            if self.Engine.currentIndex > 0:
                self.Engine.back()
                # Might need to go below
                self.time = self.time - (self.Engine.timeTaken())
                self.draw_tiles(self.Engine.getCurrentAssembly())

    def next_step(self):
        self.stop_sequence()
        if self.SysLoaded == True:
            if self.Engine.step() != -1:
                # Might need to go above
                self.time = self.time + (self.Engine.timeTaken())
                self.draw_tiles(self.Engine.getCurrentAssembly())

    def last_step(self):
        self.stop_sequence()
        if self.SysLoaded == True:
            while (self.Engine.build() != -1):
                self.time = self.time + (self.Engine.timeTaken())

            self.draw_tiles(self.Engine.getCurrentAssembly())

    def play_sequence(self):
        if self.SysLoaded == True:
            self.play = True
            while((self.Engine.build() != -1) and self.play == True):
                print(self.Engine.currentIndex)
                self.time = self.time + (self.Engine.timeTaken())

                loop = QtCore.QEventLoop()
                if self.Engine.currentIndex != 0:
                    QtCore.QTimer.singleShot(
                        int(self.delay * self.Engine.timeTaken()), loop.quit)
                else:
                    QtCore.QTimer.singleShot(self.delay, loop.quit)
                loop.exec_()

                self.draw_tiles(self.Engine.getCurrentAssembly())
                # if self.Engine.currentIndex != 0: #and self.Engine.currentIndex < self.Engine.lastIndex:

            # self.step = len(self.Engine.assemblyList) - 1 #this line is here to prevent a crash that happens if you click last after play finishes
            self.stop_sequence()

    def stop_sequence(self):
        self.play = False


if __name__ == "__main__":

    # App Stuff
    app = QApplication(sys.argv)
    w = Ui_MainWindow()
    w.show()

    sys.exit(app.exec_())
#
