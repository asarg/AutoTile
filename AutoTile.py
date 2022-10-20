from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QFileDialog, QPushButton, QWidget, QVBoxLayout, QTableWidgetItem, QCheckBox, QMessageBox, QButtonGroup
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor, QFont, QFontDatabase
from PyQt5.QtCore import QObject, QThread, Qt, pyqtSignal

from unicodedata import *
from random import randrange
import math, sys

from Player import ComputeLast, Player
from SeedEditor import SeedScene, TableScene
from Historian import Historian
from assemblyEngine import Engine
from UniversalClasses import AffinityRule, System, Assembly, Tile, State, TransitionRule, SingleTransitionRule
import TAMainWindow, EditorWindow, sCRNEditorWindow, LoadFile, SaveFile, QuickCombine, QuickRotate, QuickReflect, FreezingCheck, sampleGen
#import Generators.IU_Generators.IntrinsicUniversality as IU
#import Generators.IU_Generators.IU2 as IU2
#from Generators.IU_Generators import IUSampleGen

from util.loaders import assemblyLoader


# Global Variables
# Note: currentSystem is still global but had to be moved into the loading method
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

        ###Remove Window title bar ####
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        ###Set main background to transparent####
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ###Shadow effect #####
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(0, 92, 157, 550))

        ####Apply shadow to central widget####
        self.centralwidget.setGraphicsEffect(self.shadow)

        ###Set window title and Icon####
        self.setWindowIcon(QtGui.QIcon('Icons/Logo.png'))
        self.setWindowTitle("AutoTile")
        pixmap = QtGui.QPixmap('Icons/Logo.png')

        self.Logo_label.setPixmap(pixmap)

        ### Minimize window ######
        self.minimize_button.clicked.connect(lambda: self.showMinimized())
        self.minimize_button.setIcon(QtGui.QIcon(
            'Icons/Programming-Minimize-Window-icon.png'))

        ### Close window ####
        self.close_button.clicked.connect(lambda: self.close())
        self.close_button.setIcon(QtGui.QIcon('Icons/X-icon.jpg'))

        ### Restore/Maximize window ####
        self.maximize_button.clicked.connect(
            lambda: self.restore_or_maximize_window())
        self.maximize_button.setIcon(QtGui.QIcon(
            'Icons/Programming-Maximize-Window-icon.png'))

        ### Window Size grip to resize window ###
        QtWidgets.QSizeGrip(self.sizeDrag_Button)
        self.sizeDrag_Button.setIcon(
            QtGui.QIcon('Icons/tabler-icon-resize.png'))

        # Left Menu toggle button
        self.Menu_button.clicked.connect(lambda: self.slideLeftMenu())
        self.Menu_button.setIcon(QtGui.QIcon('Icons/menu_icon.png'))
        self.New_button.clicked.connect(self.Click_newButton)

        # "New" on the File menu
        self.New_button.setIcon(QtGui.QIcon('Icons/tabler-icon-file.png'))

        # this is "Load" on the "File" menu
        self.Load_button.clicked.connect(self.Click_FileSearch)
        self.Load_button.setIcon(QtGui.QIcon('Icons/tabler-icon-folder.png'))

        # this is "Load Assembly" on the "File" menu
        self.seededLoadButton.clicked.connect(self.Click_FileSearchSeeded)
        self.seededLoadButton.setIcon(QtGui.QIcon('Icons/tabler-icon-folder.png'))

        # "Save" from the "File" menu
        self.SaveAs_button.clicked.connect(self.Click_SaveFile)
        self.SaveAs_button.setIcon(QtGui.QIcon('Icons/save-icon.png'))

        self.First_button.clicked.connect(self.first_step)
        self.First_button.setIcon(QtGui.QIcon(
            'Icons/tabler-icon-player-skip-back.png'))

        self.Prev_button.clicked.connect(self.prev_step)
        self.Prev_button.setIcon(QtGui.QIcon(
            'Icons/tabler-icon-player-track-prev.png'))

        self.Play_button.clicked.connect(self.play_sequence)
        self.Play_button.setIcon(QtGui.QIcon(
            'Icons/tabler-icon-player-play.png'))

        self.Next_button.clicked.connect(self.next_step)
        self.Next_button.setIcon(QtGui.QIcon(
            'Icons/tabler-icon-player-track-next.png'))

        self.Last_button.clicked.connect(self.last_step)
        self.Last_button.setIcon(QtGui.QIcon(
            'Icons/tabler-icon-player-skip-forward.png'))

        self.Edit_button.clicked.connect(self.Click_EditFile)
        # "Quick Rotate"
        self.Rotate_button.clicked.connect(self.Click_QuickRotate)

        # "Quick Combine"
        self.Combine_button.clicked.connect(self.Click_QuickCombine)

        # "Quick Reflect-X."
        self.X_reflect_button.clicked.connect(self.Click_XReflect)

        # "Quick Reflect-Y"
        self.Y_reflect_button.clicked.connect(self.Click_YReflect)


        # Group for the radio buttons, this is so they can be checked independently.
        self.group = QButtonGroup()
        self.group.setExclusive(False)
        self.group.addButton(self.SlowMode_button)
        self.group.addButton(self.sCRN_button)

        self.SlowMode_button.clicked.connect(self.slowMode_toggle)

        # Available moves layout to place available moves
        self.movesLayout = QVBoxLayout(self.page_3)
        self.movesLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        # List of Move Widgets
        self.moveWidgets = []

        # Assembly History
        self.historian = Historian()
        self.historian.set_ui_parent(self)
        font = QtGui.QFont()
        font.setPointSize(10)

        self.SaveHistory_Button.clicked.connect(self.historian.dump)
        self.LoadHistory_Button.clicked.connect(self.historian.load)
        self.move_status = QLabel("No Available Moves")
        self.movesLayout.addWidget(self.move_status)

        self.next_moves_button = QPushButton()
        self.next_moves_button.setText("Next")
        self.next_moves_button.clicked.connect(self.next_set_of_moves)
        self.next_moves_button.setFont(font)
        self.next_moves_button.setStyleSheet("QPushButton::hover"
                                             "{"
                                             "background-color : lightblue;"
                                             "}")
        self.prev_moves_button = QPushButton()
        self.prev_moves_button.setText("Prev")
        self.prev_moves_button.clicked.connect(self.prev_set_of_moves)
        self.prev_moves_button.setFont(font)
        self.prev_moves_button.setStyleSheet("QPushButton::hover"
                                             "{"
                                             "background-color : lightblue;"
                                             "}")

        self.moves_page = 0
        self.moves_per_page = 8

        # updating combobox
        self.movesLayout.addWidget(self.next_moves_button)
        self.movesLayout.addWidget(self.prev_moves_button)

        # Add 10 Move widgets that we overwrite
        for i in range(self.moves_per_page):
            mGUI = Move(None, self, self.centralwidget)
            mGUI.setFixedHeight(40)
            self.moveWidgets.append(mGUI)
            self.movesLayout.addWidget(mGUI)

        # Add fonts to database
        # TODO :: add whole font folder here
        fontdatabase = QtGui.QFontDatabase()
        fontdatabase.addApplicationFont("fonts/Fira Code Regular Nerd Font Complete.tff")
        fontdatabase.addApplicationFont("fonts/Fira Code Bold Nerd Font Complete.tff")
        fontdatabase.addApplicationFont("fonts/MaterialIcons-Regular.tff")
        fontdatabase.addApplicationFont("fonts/MaterialIcons-Outlined.tff")
        #QFont("Fira Code", )

        paper_options = ["SAND22", "IU"]
        self.GenPaper_Box.addItems(paper_options)

        shape_options = ["Strings", "Rectangle", "Squares"]
        self.GenShape_Box.addItems(shape_options)

        model_options = ["Deterministic", "Non-Deterministic", "Single-Transition"]
        self.GenModel_Box.addItems(model_options)

        self.InputLabel.setText("Enter a binary string.")

        self.GenShape_Box.currentIndexChanged.connect(self.exampleTextChange)
        self.GenPaper_Box.currentIndexChanged.connect(self.paperTextChange)

        self.ExampleButton.clicked.connect(self.Begin_example)

        # Function to Move window on mouse drag event on the title bar
        def moveWindow(e):
            # Detect if the window is  normal size
            if self.isMaximized() == False:  # Not maximized
                # Move window only when window is normal size
                # if left mouse button is clicked (Only accept left mouse button clicks)
                if e.buttons() == Qt.LeftButton:
                    # Move window
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        # Add click event/Mouse move event/drag event to the top header to move the window
        self.header.mouseMoveEvent = moveWindow
        self.slide_menu.mouseMoveEvent = moveWindow

        self.time = 0
        self.delay = 0
        # 0 is red, 1 is blue, and 2 is black. Nums correspond with forward/backward highlight
        self.color_flag = 2
        self.seedX = self.geometry().width() / 2
        self.seedY = self.geometry().height() / 2
        self.clickPosition = QtCore.QPoint(
            self.geometry().x(), self.geometry().y())

        self.tileSize = 40
        self.textSize = int(self.tileSize / 3)

        self.textX_offset = self.tileSize / 3.9
        self.textY_offset = self.tileSize / 1.7

        self.textX = self.seedX + self.textX_offset
        self.textY = self.seedY + self.textY_offset

        self.Engine = None
        self.SysLoaded = False
        self.play = False

        canvas = QtGui.QPixmap(self.geometry().width(),
                               self.geometry().height())
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)

        self.label_2.setText("")

        self.frame_6.setGeometry(0, 0, 164, 463)

        self.thread = QThread()
        self.threadlast = QThread()
        #self.loadAssembly("XML Files/IUActiveState.xml")
        #self.Begin_IU_Example()

        print(len(sys.argv))
        if len(sys.argv) == 2:
            self.Load_File(sys.argv[1])
        elif len(sys.argv) == 3:
            self.loadAssembly(sys.argv[1])
        else:
            self.Load_File("XML Files/seededExample.xml")


    # Slide left menu function
    def slideLeftMenu(self):
        # Get current left menu width
        width = self.slide_menu_container.width()

        # If minimized
        if width == 0:
            # Expand menu
            newWidth = 200
            canvas = QtGui.QPixmap(
                self.geometry().width() - 200, self.geometry().height() - 45)
            canvas.fill(Qt.white)

            self.slide_menu_container.setMaximumWidth(newWidth)
            self.label.setPixmap(canvas)
        # If maximized
        else:
            # Restore menu
            newWidth = 0

            self.slide_menu_container.setMaximumWidth(newWidth)

            canvas = QtGui.QPixmap(
                self.geometry().width(), self.geometry().height() - 45)
            canvas.fill(Qt.white)
            self.label.setPixmap(canvas)

        if self.Engine != None:
            self.draw_assembly(self.Engine.getCurrentAssembly())

    # Add mouse events to the window
    def mousePressEvent(self, event):
        # Get the current position of the mouse
        super().mousePressEvent(event)
        self.clickPosition = event.globalPos()
        # We will use this value to move the window

    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def resizeEvent(self, event):
        # If left menu is closed
        if self.slide_menu_container.width() == 0:
            canvas = QtGui.QPixmap(
                self.geometry().width(), self.geometry().height() - 45)
        else:
            # prevents a bug that happens if menus open
            canvas = QtGui.QPixmap(
                self.geometry().width() - 200, self.geometry().height() - 45)

        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)
        if self.Engine != None:
            self.seedX = self.geometry().width() / 2
            self.seedY = self.geometry().height() / 2
            self.textX = self.seedX + self.textX_offset
            self.textY = self.seedY + self.textY_offset
            self.draw_assembly(self.Engine.getCurrentAssembly())

    def keyPressEvent(self, event):
        #### Moving tiles across screen functions #####

        # "up" arrow key is pressed
        if event.key() == Qt.Key_W and not self.play and event.modifiers() == Qt.ShiftModifier:
            #"CAPITAL W"
            Upborder = self.Engine.getCurrentBorders()[2]
            Downborder = self.Engine.getCurrentBorders()[3]

            distance = (self.tileSize * Upborder) - \
                (self.tileSize * Downborder)
            self.seedY = self.seedY - distance / 5
            self.textY = self.textY - distance / 5
            if self.Engine != None:
                self.draw_assembly(self.Engine.getCurrentAssembly())

        elif event.key() == Qt.Key_W and not self.play:
            self.seedY = self.seedY - 10
            self.textY = self.textY - 10
            if self.Engine != None:
                self.draw_assembly(self.Engine.getCurrentAssembly())

        # "down" arrow key is pressed
        elif event.key() == Qt.Key_S and not self.play and event.modifiers() == Qt.ShiftModifier:
            #"CAPITAL S"
            Upborder = self.Engine.getCurrentBorders()[2]
            Downborder = self.Engine.getCurrentBorders()[3]

            distance = (self.tileSize * Upborder) - \
                (self.tileSize * Downborder)
            self.seedY = self.seedY + distance / 5
            self.textY = self.textY + distance / 5
            if self.Engine != None:
                self.draw_assembly(self.Engine.getCurrentAssembly())

        elif event.key() == Qt.Key_S and not self.play:
            self.seedY = self.seedY + 10
            self.textY = self.textY + 10
            if self.Engine != None:
                self.draw_assembly(self.Engine.getCurrentAssembly())

        # "left" arrow key is pressed
        elif event.key() == Qt.Key_A and not self.play and event.modifiers() == Qt.ShiftModifier:
            # CAPITAL A
            Leftborder = self.Engine.getCurrentBorders()[0]
            Rightborder = self.Engine.getCurrentBorders()[1]

            distance = (self.tileSize * Rightborder) - \
                (self.tileSize * Leftborder)
            self.seedX = self.seedX - distance / 5
            self.textX = self.textX - distance / 5
            if self.Engine != None:
                self.draw_assembly(self.Engine.getCurrentAssembly())

        elif event.key() == Qt.Key_A and not self.play:
            self.seedX = self.seedX - 10
            self.textX = self.textX - 10
            if self.Engine != None:
                self.draw_assembly(self.Engine.getCurrentAssembly())

        # "right" arrow key is pressed
        elif event.key() == Qt.Key_D and not self.play and event.modifiers() == Qt.ShiftModifier:
            # CAPITAL D
            Leftborder = self.Engine.getCurrentBorders()[0]
            Rightborder = self.Engine.getCurrentBorders()[1]

            distance = (self.tileSize * Rightborder) - \
                (self.tileSize * Leftborder)
            self.seedX = self.seedX + distance / 5
            self.textX = self.textX + distance / 5
            if self.Engine != None:
                self.draw_assembly(self.Engine.getCurrentAssembly())

        elif event.key() == Qt.Key_D and not self.play:
            self.seedX = self.seedX + 10
            self.textX = self.textX + 10
            if self.Engine != None:
                self.draw_assembly(self.Engine.getCurrentAssembly())

        # Spacebar to center seed
        elif event.key() == Qt.Key_C and not self.play:
            self.seedX = self.geometry().width() / 2
            self.seedY = self.geometry().height() / 2

            self.textX = self.seedX + self.textX_offset
            self.textY = self.seedY + self.textY_offset
            if self.Engine != None:
                self.draw_assembly(self.Engine.getCurrentAssembly())

        # Hotkeys for the toolbar
        elif event.key() == Qt.Key_H:
            self.first_step()

        elif event.key() == Qt.Key_J:
            self.prev_step()

        elif event.key() == Qt.Key_K:
            self.play_sequence()

        elif event.key() == Qt.Key_L:
            self.next_step()

        elif event.key() == Qt.Key_Semicolon:
            self.last_step()

        # "Scroll" in and out functionality for + and - keys
        elif event.key() == Qt.Key_Plus or event.key() == Qt.Key_Equal:
            if self.Engine != None:
                x_num = 0
                y_num = 0

                tile_increase = 10

                if self.tileSize < 10:
                    tile_increase = 5

                elif self.tileSize < 30:
                    x_num = 4.2
                    y_num = 5
                else:
                    x_num = 2
                    y_num = 6

                self.update_tileSize(tile_increase, x_num, y_num)

                self.draw_assembly(self.Engine.getCurrentAssembly())

        elif event.key() == Qt.Key_Minus or event.key() == Qt.Key_Underscore:
            if self.Engine != None:
                tile_increase = 0
                x_num = 0
                y_num = 0

                if self.tileSize > 30:
                    tile_increase = -10
                    x_num = -2
                    y_num = -6

                elif self.tileSize > 10:
                    tile_increase = -10
                    x_num = -4.2
                    y_num = -5

                elif self.tileSize > 5:
                    tile_increase = -5

                self.update_tileSize(tile_increase, x_num, y_num)

                self.draw_assembly(self.Engine.getCurrentAssembly())


    def wheelEvent(self, event):
        if self.play:
            return
        tile_increase = 0
        x_num = 0
        y_num = 0
        #### Zoom in functions for the scroll wheel ####
        if event.angleDelta().y() == 120:
            tile_increase = 10

            if self.tileSize < 10:
                tile_increase = 5

            elif self.tileSize < 30:
                x_num = 3.4
                y_num = 5
            elif self.tileSize < 40:
                x_num = 4.1
                y_num = 6

            else:
                x_num = 2
                y_num = 6
        else:
            if self.tileSize > 40:
                tile_increase = -10 #keep these in here so tile_increase stays at 0 when it should
                x_num = -2
                y_num = -6

            elif self.tileSize > 30:
                tile_increase = -10
                x_num = -4.1
                y_num = -6

            elif self.tileSize > 10:
                tile_increase = -10
                x_num = -3.4
                y_num = -5

            elif self.tileSize > 5:
                tile_increase = -5

        self.update_tileSize(tile_increase, x_num, y_num)

        if self.Engine != None:
            self.draw_assembly(self.Engine.getCurrentAssembly())

    def update_tileSize(self, tile_increase, x_num, y_num):
        self.tileSize = self.tileSize + tile_increase
        self.textX_offset = self.textX_offset + x_num
        self.textY_offset = self.textY_offset + y_num

        self.textX = self.textX + x_num
        self.textY = self.textY + y_num

        self.textSize = int(self.tileSize / 3)

    def draw_move(self, move, forward, color):
        painter = QPainter(self.label.pixmap())
        pen = QtGui.QPen()
        brush = QtGui.QBrush()
        font = QtGui.QFont()

        pen.setWidth(3)

        brush.setStyle(Qt.SolidPattern)

        font.setFamily("Times")
        font.setBold(True)
        font.setPixelSize(self.textSize)
        painter.setFont(font)

        pen.setColor(QtGui.QColor(color))
        painter.setPen(pen)

        # adding attachment on screen
        try:
            if move['type'] == 'a' and forward == 1:  # (type, x, y, state1)
                if self.onScreen_check(move['x'], move['y']) != 1:
                    brush.setColor(QtGui.QColor( "#" + move['state1'].returnColor()))
                    self.draw_to_screen(move['x'], move['y'], move['state1'], painter, brush)

            # showing transition on screen
            # (type, x, y, dir, state1, state2, state1Final, state2Final)
            elif move['type'] == 't' and forward == 1:
                self.transition_draw_function(move, move['state1Final'], move['state2Final'], painter, brush)

            # getting rid of attachment on screen
            elif move['type'] == 'a' and forward == 0:  # (type, x, y, state1)
                brush.setColor(QtGui.QColor("white"))
                pen.setColor(QtGui.QColor("white"))
                painter.setPen(pen)

                if self.onScreen_check(move['x'], move['y']) != 1:
                    self.draw_to_screen(move['x'], move['y'], "", painter, brush)

                assembly = self.Engine.getCurrentAssembly()
                pen.setColor(QtGui.QColor("black"))
                painter.setPen(pen)

                neighborN = assembly.coords.get(
                    "(" + str(move['x']) + "," + str(move['y'] + 1) + ")")
                neighborS = assembly.coords.get(
                    "(" + str(move['x']) + "," + str(move['y'] - 1) + ")")
                neighborE = assembly.coords.get(
                    "(" + str(move['x'] + 1) + "," + str(move['y']) + ")")
                neighborW = assembly.coords.get(
                    "(" + str(move['x'] - 1) + "," + str(move['y']) + ")")

                if neighborN != None:
                    if self.onScreen_check(move['x'], move['y'] + 1) != 1:
                        brush.setColor(QtGui.QColor("#" + neighborN.returnColor()))
                        self.draw_to_screen(
                            move['x'], move['y'] + 1, neighborN.returnState(), painter, brush)
                if neighborS != None:
                    if self.onScreen_check(move['x'], move['y'] - 1) != 1:
                        brush.setColor(QtGui.QColor("#" + neighborS.returnColor()))
                        self.draw_to_screen(
                            move['x'], move['y'] - 1, neighborS.returnState(), painter, brush)
                if neighborE != None:
                    if self.onScreen_check(move['x'] + 1, move['y']) != 1:
                        brush.setColor(QtGui.QColor("#" + neighborE.returnColor()))
                        self.draw_to_screen(
                            move['x'] + 1, move['y'], neighborE.returnState(), painter, brush)
                if neighborW != None:
                    if self.onScreen_check(move['x'] - 1, move['y']) != 1:
                        brush.setColor(QtGui.QColor("#" + neighborW.returnColor()))
                        self.draw_to_screen(
                            move['x'] - 1, move['y'], neighborW.returnState(), painter, brush)

            # reversing transition on screen
            # (type, x, y, dir, state1, state2, state1Final, state2Final)
            elif move['type'] == 't' and forward == 0:
                self.transition_draw_function(
                    move, move['state1'], move['state2'], painter, brush)
        except:
            print("There are no valid attachments.")

        painter.end()

        self.Update_time_onScreen()
        if self.play == False:
            self.Update_available_moves()

        self.update()

    def draw_assembly(self, assembly):
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
        painter.drawRect(0, 0, self.geometry().width(),
                         self.geometry().height())

        # Font
        font.setFamily("Fira Code")
        font.setBold(True)
        font.setPixelSize(self.textSize)
        painter.setFont(font)

        pen.setColor(QtGui.QColor("black"))
        painter.setPen(pen)
        for tile in assembly.tiles:
            if self.onScreen_check(tile.x, tile.y) == 1:
                continue

            brush.setColor(QtGui.QColor("#" + tile.returnColor()))

            self.draw_to_screen(tile.x, tile.y, tile.state, painter, brush)

        if self.Engine.currentIndex > 0:
            if self.color_flag == 0 and self.play != True and self.Engine.currentIndex < self.Engine.lastIndex:
                self.highlight_move(self.Engine.getLastMove(),
                                    self.color_flag, painter, brush, pen)
            elif self.color_flag == 1:
                self.highlight_move(self.Engine.getCurrentMove(
                ), self.color_flag, painter, brush, pen)

        painter.end()

        self.update()

    def Update_time_onScreen(self):
        if self.Engine.currentIndex != 0:
            self.label_2.setText("Time elapsed: \n" +
                                 str(round(self.time, 2)) + " time steps")
            self.label_3.setText("Current step time: \n" +
                                 str(round(self.Engine.timeTaken(), 2)) + " time steps")
        else:
            self.label_2.setText("Time elapsed: \n 0 time steps")
            self.label_3.setText("Current step time: \n 0 time steps")

    def prev_set_of_moves(self):
        if not self.play:
            self.moves_page -= 1
            self.show_other_page()

    def next_set_of_moves(self):
        if not self.play:
            self.moves_page += 1
            self.show_other_page()

    def show_other_page(self):
        # Set all moves to None
        for m in self.moveWidgets:
            m.move = None
            m.hide()
        self.move_status.hide()

        # if page is negative, wrap around
        # if page is over the limit, wrap around
        if self.moves_page < 0:
            newpage = 1.0 * len(self.Engine.validMoves) / self.moves_per_page
            newpage = math.ceil(newpage)
            self.moves_page = newpage - 1
        elif self.moves_page * self.moves_per_page >= len(self.Engine.validMoves):
            self.moves_page = 0

        # If no more moves, show it
        if len(self.Engine.validMoves) == 0:
            self.move_status.show()

        # If there are moves to pick, show them
        elif not len(self.Engine.validMoves) == 0:
            # Create moves and add to layout
            i = 0
            for m_i in range(self.moves_page * self.moves_per_page, len(self.Engine.validMoves)):
                m = self.Engine.validMoves[m_i]

                if i < self.moves_per_page:
                    self.moveWidgets[i].move = m
                    self.moveWidgets[i].show()
                    i += 1

    def Update_available_moves(self):
        self.moves_page = 0

        # Set all moves to None
        for m in self.moveWidgets:
            m.move = None
            m.hide()
        self.move_status.hide()

        # If no more moves, show it
        if len(self.Engine.validMoves) == 0:
            self.move_status.show()

        # If there are moves to pick, show them
        elif not len(self.Engine.validMoves) == 0:
            # Create moves and add to layout
            i = 0
            for m in self.Engine.validMoves:
                if i < self.moves_per_page:
                    self.moveWidgets[i].move = m
                    self.moveWidgets[i].show()
                    i += 1

    def highlight_move(self, move, color_flag, painter, brush, pen):
        # attachment highlight
        if move['type'] == 'a' and color_flag == 1:  # (type, x, y, state1)
            if self.onScreen_check(move['x'], move['y']) != 1:
                brush.setColor(QtGui.QColor(
                    "#" + move['state1'].returnColor()))
                pen.setColor(QtGui.QColor("blue"))
                painter.setPen(pen)
                self.draw_to_screen(move['x'], move['y'], move['state1'], painter, brush)

        # transition highlight
        # (type, x, y, dir, state1, state2, state1Final, state2Final)
        elif move['type'] == 't' and color_flag == 1:
            pen.setColor(QtGui.QColor("blue"))
            painter.setPen(pen)
            self.transition_draw_function(move, move['state1Final'], move['state2Final'], painter, brush)

        # (type, x, y, dir, state1, state2, state1Final, state2Final)
        elif move['type'] == 't' and color_flag == 0:
            pen.setColor(QtGui.QColor("red"))
            painter.setPen(pen)
            self.transition_draw_function(
                move, move['state1'], move['state2'], painter, brush)

    def display_tile_list(self):
        curr = self.Engine.getCurrentAssembly()
        tile_list = curr.returnTiles()
        for t in tile_list:
            print(t)


    def draw_to_screen(self, x, y, state, painter, brush):
        painter.setBrush(brush)
        ts = self.tileSize
        ts_x = int(x*ts + self.seedX)
        ts_y = int((y * -ts) + self.seedY)
        rect = QtCore.QRect(ts_x, ts_y, ts, ts)

        painter.drawRect(rect)

        if state == "":
            painter.drawText(rect, Qt.AlignCenter, "")
            return
        else:
            decoded_display_label = state.display_label

        if self.tileSize > 10:
            fm = QtGui.QFontMetrics(painter.font())
            txt_width = fm.width(decoded_display_label)

            if decoded_display_label == None:
                if len(state.label) > 4:
                    painter.drawText(rect, Qt.AlignCenter, state.label[0:3])
                else:
                    painter.drawText(rect, Qt.AlignCenter, state.label)
            elif len(decoded_display_label) > 4:

                painter.drawText(rect, Qt.AlignCenter, decoded_display_label[0:3])
            else:
                painter.drawText(rect, Qt.AlignCenter, decoded_display_label)



    def transition_draw_function(self, move, state1, state2, painter, brush):
        horizontal = 0
        vertical = 0
        brush.setColor(QtGui.QColor("white"))
        if move['dir'] == 'h':
            horizontal = 1
        elif move['dir'] == 'v':
            vertical = -1

        if self.onScreen_check(move['x'], move['y']) != 1:
            self.draw_to_screen(move['x'], move['y'], "", painter, brush)
            brush.setColor(QtGui.QColor("#" + state1.returnColor()))
            self.draw_to_screen(move['x'], move['y'], state1, painter, brush)

        if self.onScreen_check(move['x'] + horizontal, move['y'] + vertical) != 1:
            brush.setColor(QtGui.QColor("white"))
            self.draw_to_screen(move['x'] + horizontal, move['y'] + vertical, "", painter, brush)
            brush.setColor(QtGui.QColor("#" + state2.returnColor()))
            self.draw_to_screen(move['x'] + horizontal, move['y'] + vertical, state2, painter, brush)

    # checks if a given tile is on screen by checking its coordinate, if not returns 1
    def onScreen_check(self, x, y):
        if((x * self.tileSize) + self.seedX > self.geometry().width() or (x * self.tileSize) + self.seedX < -self.tileSize):
            return 1
        if((y * -self.tileSize) + self.seedY > self.geometry().height() or (y * -self.tileSize) + self.seedY < -self.tileSize):
            return 1
        return 0

    def Click_newButton(self):
        global currentSystem

        currentSystem = System(1, [], [], [], [], [], [], [], [], [], seed_assembly = Assembly(), empty=True)
        seed = State("X", "ffffff")
        currentSystem.addSeedState(seed)
        currentSystem.addState(seed)
        self.Engine = Engine(currentSystem)

        if self.sCRN_button.isChecked():
            self.e = Ui_sCRNEditorWindow(self.Engine, self)
        else:
            self.e = Ui_EditorWindow(self.Engine, self)
        self.e.show()

    def Click_FileSearch(self, id):
        self.stop_sequence()
        file = QFileDialog.getOpenFileName(
            self, "Select XML Document", "", "XML Files (*.xml)")
        if file[0] != '':
            self.SysLoaded = False
            self.Load_File(file[0])

    def Click_FileSearchSeeded(self, id):
        self.stop_sequence()
        file = QFileDialog.getOpenFileName(
            self, "Select XML Document", "", "XML Files (*.xml)")
        if file[0] != '':
            self.SysLoaded = False
            self.loadAssembly(file[0])

    def Load_File(self, filename):
        # Simulator must clear all of LoadFile's global variables when the user attempts to load something.
            LoadFile.HorizontalAffinityRules.clear()
            LoadFile.VerticalAffinityRules.clear()
            LoadFile.HorizontalTransitionRules.clear()
            LoadFile.VerticalTransitionRules.clear()
            LoadFile.SeedStateSet.clear()
            LoadFile.InitialStateSet.clear()
            LoadFile.CompleteStateSet.clear()
            LoadFile.seed_assembly = Assembly()

            LoadFile.readxml(filename)

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
            seeded_assembly = LoadFile.seed_assembly

            self.SysLoaded = True
            self.stop_sequence()

            # Establish the current system we're working with
            global currentSystem
            currentSystem = System(temp, states, inital_states, seed_states,  vertical_affinities,
                                   horizontal_affinities, vertical_transitions, horizontal_transitions,seed_assembly=seeded_assembly)
            print("\nSystem Dictionaries:")
            print("Vertical Affinities:")
            currentSystem.displayVerticalAffinityDict()
            print("Horizontal Affinities:")
            currentSystem.displayHorizontalAffinityDict()
            print("Vertical Transitions:")
            currentSystem.displayVerticalTransitionDict()
            print("Horizontal Transitions:")
            currentSystem.displayHorizontalTransitionDict()

            # the -150 is to account for the slide menu
            self.seedX = (self.geometry().width() - 150) / 2
            self.seedY = self.geometry().height() / 2

            self.tileSize = 40
            self.textSize = int(self.tileSize / 3)

            self.textX_offset = self.tileSize / 3.9
            self.textY_offset = self.tileSize / 1.7

            self.textX = self.seedX + self.textX_offset
            self.textY = self.seedY + self.textY_offset

            self.time = 0
            self.Engine = Engine(currentSystem)
            self.historian.set_engine(self.Engine)

            self.draw_assembly(self.Engine.getCurrentAssembly())
            self.Update_available_moves()

    def loadAssembly(self, filename):
    # Simulator must clear all of LoadFile's global variables when the user attempts to load something.
        assemblyLoader.HorizontalAffinityRules.clear()
        assemblyLoader.VerticalAffinityRules.clear()
        assemblyLoader.HorizontalTransitionRules.clear()
        assemblyLoader.VerticalTransitionRules.clear()
        assemblyLoader.SeedStateSet.clear()
        assemblyLoader.InitialStateSet.clear()
        assemblyLoader.CompleteStateSet.clear()
        assemblyLoader.seed_assembly = Assembly()

        assemblyLoader.readxml(filename)

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
        temp = assemblyLoader.Temp
        states = assemblyLoader.CompleteStateSet
        inital_states = assemblyLoader.InitialStateSet
        seed_states = assemblyLoader.SeedStateSet
        vertical_affinities = assemblyLoader.VerticalAffinityRules
        horizontal_affinities = assemblyLoader.HorizontalAffinityRules
        vertical_transitions = assemblyLoader.VerticalTransitionRules
        horizontal_transitions = assemblyLoader.HorizontalTransitionRules
        seeded_assembly = assemblyLoader.seed_assembly

        self.SysLoaded = True
        self.stop_sequence()

        # Establish the current system we're working with
        global currentSystem
        currentSystem = System(temp, states, inital_states, seed_states, vertical_affinities,
                                horizontal_affinities, vertical_transitions, horizontal_transitions, seed_assembly=seeded_assembly)
        print("\nSystem Dictionaries:")
        print("Vertical Affinities:")
        currentSystem.displayVerticalAffinityDict()
        print("Horizontal Affinities:")
        currentSystem.displayHorizontalAffinityDict()
        print("Vertical Transitions:")
        currentSystem.displayVerticalTransitionDict()
        print("Horizontal Transitions:")
        currentSystem.displayHorizontalTransitionDict()

        # the -150 is to account for the slide menu
        self.seedX = (self.geometry().width() - 150) / 2
        self.seedY = self.geometry().height() / 2

        self.tileSize = 40
        self.textSize = int(self.tileSize / 3)

        self.textX_offset = self.tileSize / 3.9
        self.textY_offset = self.tileSize / 1.7

        self.textX = self.seedX + self.textX_offset
        self.textY = self.seedY + self.textY_offset

        self.time = 0
        self.Engine = Engine(currentSystem)
        self.historian.set_engine(self.Engine)

        self.draw_assembly(self.Engine.getCurrentAssembly())
        self.Update_available_moves()

    def Click_SaveFile(self):
        # Creating a System object from data read.
        if(self.SysLoaded == True):
            fileName = QFileDialog.getSaveFileName(
                self, "QFileDialog.getSaveFileName()", "", "XML Files (*.xml)")

            if(fileName[0] != ''):
                SaveFile.main(currentSystem, fileName)

    def Click_QuickRotate(self):
        # Make a rotated system based off the current system, and instantly load the new system.
        if(self.SysLoaded == True):
            global currentSystem
            QuickRotate.main(currentSystem)
            currentSystem = QuickRotate.tempSystem
            self.time = 0
            self.Engine = Engine(currentSystem)
            self.draw_assembly(self.Engine.getCurrentAssembly())
            self.Update_available_moves()

    def Click_QuickCombine(self):
        if(self.SysLoaded == True):
            global currentSystem
            file = QFileDialog.getOpenFileName(
                self, "Select XML Document", "", "XML Files (*.xml)")
            if file[0] != '':
                QuickCombine.main(currentSystem, file[0])
            currentSystem.clearVerticalTransitionDict()
            currentSystem.clearHorizontalTransitionDict()
            currentSystem.clearVerticalAffinityDict()
            currentSystem.clearHorizontalAffinityDict()
            currentSystem.translateListsToDicts()
            self.time = 0
            self.Engine = Engine(currentSystem)
            self.draw_assembly(self.Engine.getCurrentAssembly())
            self.Update_available_moves()

    def Click_XReflect(self):
        # Make a rotated system based off the current system, and instantly load the new system.
        if(self.SysLoaded == True):
            global currentSystem
            QuickReflect.reflect_across_x(currentSystem)
            currentSystem = QuickReflect.tempSystem
            self.time = 0
            self.Engine = Engine(currentSystem)
            self.draw_assembly(self.Engine.getCurrentAssembly())
            self.Update_available_moves()

    def Click_YReflect(self):
        # Make a rotated system based off the current system, and instantly load the new system.
        if(self.SysLoaded == True):
            global currentSystem
            QuickReflect.reflect_across_y(currentSystem)
            currentSystem = QuickReflect.tempSystem
            self.time = 0
            self.Engine = Engine(currentSystem)
            self.draw_assembly(self.Engine.getCurrentAssembly())
            self.Update_available_moves()

    # starting assembly goes here
    def slowMode_toggle(self):
        if self.SlowMode_button.isChecked():
            self.delay = 1000
        else:
            self.delay = 0

    def paperTextChange(self):
        self.GenShape_Box.clear()
        if self.GenPaper_Box.currentText() == "SAND22":
            shape_options = ["Strings", "Rectangle", "Squares"]
            self.GenShape_Box.addItems(shape_options)
        else:
            gadget_options = ["gadget1", "gadget2"]
            self.GenShape_Box.addItems(gadget_options)

    def exampleTextChange(self):
        if self.GenShape_Box.currentText() == "Strings":
            self.InputLabel.setText("Enter a binary string.")
        elif self.GenShape_Box.currentText() == "Rectangle" or self.GenShape_Box.currentText() == "Squares":
            self.InputLabel.setText("Enter an integer.")
        elif self.GenShape_Box.currentText() == "gadget1" or self.GenShape_Box.currentText() == "gadget2":
            self.InputLabel.setText("No input. Press start.")

    def Begin_example(self):
        self.stop_sequence()
        self.play = False
        global currentSystem

        if self.GenShape_Box.currentText() == "Strings":
            print("Strings " + self.lineEdit.text())
        elif self.GenShape_Box.currentText() == "Rectangle":
            print("Rectangle " + self.lineEdit.text())
        elif self.GenShape_Box.currentText() == "Squares":
            print("Squares " + self.lineEdit.text())
        elif self.GenShape_Box.currentText() == "Lines":
            print("Lines " + self.lineEdit.text())
        self.GenShape_Box.currentText()

        shape = self.GenShape_Box.currentText()
        model = self.GenModel_Box.currentText()
        value = self.lineEdit.text()

        genSystem = sampleGen.generator(shape, value, model)

        if type(genSystem) == System:
            self.SysLoaded = True
            # the -150 is to account for the slide menu
            self.seedX = (self.geometry().width() - 150) / 2
            self.seedY = self.geometry().height() / 2

            self.tileSize = 40
            self.textSize = int(self.tileSize / 3)

            self.textX_offset = self.tileSize / 3.9
            self.textY_offset = self.tileSize / 1.7

            self.textX = self.seedX + self.textX_offset
            self.textY = self.seedY + self.textY_offset

            self.time = 0
            self.Engine = Engine(genSystem)
            self.historian.set_engine(self.Engine)

            currentSystem = genSystem

            self.draw_assembly(self.Engine.getCurrentAssembly())
            self.Update_available_moves()

    """ def Begin_IU_Example(self):
        self.stop_sequence()
        self.play = False
        global currentSystem

        genS = IU2.IUGenerators()
        genSystem = genS.EqualityGadgetGenerator()


        if type(genSystem) == System:
            #current system takes in an assembly,

            self.SysLoaded = True
            # the -150 is to account for the slide menu
            self.seedX = (self.geometry().width() - 100) / 2
            self.seedY = self.geometry().height() / 2

            self.tileSize = 40
            self.textSize = int(self.tileSize / 2)

            self.time = 0
            self.Engine = Engine(genSystem)
            self.historian.set_engine(self.Engine)

            currentSystem = genSystem

            self.draw_assembly(self.Engine.getCurrentAssembly())
            self.Update_available_moves() """

    def do_move(self, move):
        if not self.play:
            # Shouldn't need all this code but copying from next_step() anyways
            self.stop_sequence()
            if self.SysLoaded == True:
                prev_move = self.Engine.getCurrentMove()
                print("prev_move: " + str(prev_move))
                if self.Engine.step(move) != -1:
                    self.color_flag = 1
                    if self.Engine.currentIndex > 1:
                        self.draw_move(prev_move, 1, "black")

                    self.time = self.time + (self.Engine.timeTaken())
                    self.draw_move(move, 1, "blue")
                else:
                    self.color_flag = 2
                    self.draw_move(move, 1, "black")

    def first_step(self):
        if self.SysLoaded == True:
            if self.play:
                self.stop_sequence()
                self.thread.finished.connect(self.first_step)
            else:
                self.Engine.first()
                self.time = 0
                self.Update_time_onScreen()
                self.draw_assembly(self.Engine.getCurrentAssembly())
                self.Update_available_moves()

    def prev_step(self):
        if self.play:
            return

        if self.SysLoaded == True:
            if self.Engine.currentIndex > 0:
                self.color_flag = 0
                if self.Engine.currentIndex < self.Engine.lastIndex:
                    prev_move = self.Engine.getLastMove()
                    self.draw_move(prev_move, 0, "black")

                self.time = self.time - (self.Engine.timeTaken())
                if self.Engine.currentIndex == 0:
                    self.time = 0

                self.Engine.back()

                self.draw_move(self.Engine.getLastMove(), 0, "red")

    def next_step(self):
        if self.play:
            return

        if self.SysLoaded == True:
            prev_move = self.Engine.getCurrentMove()
            if self.Engine.step() != -1:
                self.color_flag = 1
                if self.Engine.currentIndex > 1:
                    self.draw_move(prev_move, 1, "black")

                self.time = self.time + (self.Engine.timeTaken())
                self.draw_move(self.Engine.getCurrentMove(), 1, "blue")

            else:
                self.color_flag = 2
                self.draw_move(self.Engine.getCurrentMove(), 1, "black")

    def last_step(self):
        if self.SysLoaded == True:
            if self.play:
                self.stop_sequence()
                self.thread.finished.connect(self.last_step)
            elif not self.threadlast.isRunning():

                self.threadlast.deleteLater()
                self.threadlast = QThread()
                self.workerlast = ComputeLast()
                self.workerlast.give_ui(self)

                self.workerlast.moveToThread(self.threadlast)

                self.threadlast.started.connect(self.workerlast.run)

                self.workerlast.finished.connect(self.threadlast.quit)
                self.workerlast.finished.connect(self.workerlast.deleteLater)

                self.threadlast.finished.connect(lambda: self.draw_assembly(self.Engine.getCurrentAssembly()))
                self.threadlast.finished.connect(
                    lambda: self.Update_available_moves())

                self.threadlast.start()

    def play_sequence(self):
        if self.SysLoaded == True:
            if self.play == False:
                self.play = True

                self.Play_button.setIcon(QtGui.QIcon(
                    'Icons/tabler-icon-player-pause.png'))

                if self.color_flag == 0:
                    if self.Engine.currentIndex > 0:
                        if self.Engine.currentIndex < self.Engine.lastIndex:
                            prev_move = self.Engine.getLastMove()
                            self.draw_move(prev_move, 0, "black")
                elif self.color_flag == 1:
                    if self.Engine.currentIndex > 1:
                        prev_move = self.Engine.getCurrentMove()
                        self.draw_move(prev_move, 1, "black")
                self.color_flag = 2

                self.thread.deleteLater()
                self.thread = QThread()
                self.worker = Player()
                self.worker.give_ui(self)

                self.worker.moveToThread(self.thread)

                self.thread.started.connect(self.worker.run)

                self.worker.finished.connect(self.thread.quit)
                self.worker.finished.connect(self.worker.deleteLater)

                self.thread.finished.connect(
                    lambda: self.draw_assembly(self.Engine.getCurrentAssembly()))
                self.thread.finished.connect(
                    lambda: self.Update_available_moves())
                self.thread.finished.connect(lambda: self.Play_button.setIcon(
                    QtGui.QIcon('Icons/tabler-icon-player-play.png')))

                self.thread.start()

            elif self.play == True:
                self.stop_sequence()

    def stop_sequence(self):
        self.play = False

    # opens editor window

    # opens editor window
    def Click_EditFile(self):
        # if system loaded, open editorwindow
        if self.SysLoaded == True:
            if self.sCRN_button.isChecked():
                self.e = Ui_sCRNEditorWindow(self.Engine, self)
            else:
                self.e = Ui_EditorWindow(self.Engine, self)
            self.e.show()
        else:
            print("Please load a file to edit.")
# add self, engine - then fill the table
# engine has the system


class Ui_EditorWindow(QMainWindow, EditorWindow.Ui_EditorWindow): #the editor window class
    def __init__(self, engine, mainGUI):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('Icons/Logo.png'))
        self.mainGUI = mainGUI
        self.Engine = engine
        self.system = engine.system
        self.t = TableScene()
        self.s = SeedScene()
        # set row count state table
        self.newStateIndex = len(self.system.states)
        self.tableWidget.setRowCount(len(self.system.states))
        print(len(self.system.states))
        # set row count affinity table
        self.newAffinityIndex = (len(self.system.vertical_affinities_list)) + \
            (len(self.system.horizontal_affinities_list))
        self.tableWidget_2.setRowCount(len(
            self.system.vertical_affinities_list) + len(self.system.horizontal_affinities_list))
        print(len(self.system.vertical_affinities_list) +
              len(self.system.horizontal_affinities_list))
        # set row count transition table
        self.newTransitionIndex = (len(
            self.system.vertical_transitions_list)) + (len(self.system.horizontal_transitions_list))
        self.tableWidget_3.setRowCount(len(
            self.system.vertical_transitions_list) + len(self.system.horizontal_transitions_list))
        print(len(self.system.vertical_transitions_list) +
              len(self.system.horizontal_transitions_list))

        self.tableWidget_3.setColumnWidth(0, 100)
        self.tableWidget_3.setColumnWidth(1, 100)
        self.tableWidget_3.setColumnWidth(2, 40)
        self.tableWidget_3.setColumnWidth(3, 120)
        self.tableWidget_3.setColumnWidth(4, 120)
        self.tableWidget_3.setColumnWidth(5, 100)

        # set tempurature
        self.spinBox.setMinimum(1)
        self.spinBox.setValue(self.system.returnTemp())

        # connect the color change
        self.tableWidget.cellChanged.connect(self.cellchanged)

        # filling in table 2 with vertical affinities
        r = 0
        for af in self.system.vertical_affinities_list:
            label1 = QTableWidgetItem()
            label1.setText(af.returnLabel1())
            label1.setTextAlignment(Qt.AlignCenter)
            label2 = QTableWidgetItem()
            label2.setText(af.returnLabel2())
            label2.setTextAlignment(Qt.AlignCenter)
            self.tableWidget_2.setItem(r, 0, label1)
            self.tableWidget_2.setItem(r, 1, label2)

            direc = QTableWidgetItem()
            direc.setText(af.returnDir())
            direc.setTextAlignment(Qt.AlignCenter)
            self.tableWidget_2.setItem(r, 2, direc)
            glue = QTableWidgetItem()

            glue.setText(str(af.returnStr()))
            glue.setTextAlignment(Qt.AlignCenter)
            self.tableWidget_2.setItem(r, 3, glue)
            r += 1

        # filling in table 2 with horizontal affinities
        for afH in self.system.horizontal_affinities_list:
            label1HR = QTableWidgetItem()
            label1HR.setText(afH.returnLabel1())
            label1HR.setTextAlignment(Qt.AlignCenter)
            self.tableWidget_2.setItem(r, 0, label1HR)
            label2HR = QTableWidgetItem()
            label2HR.setText(afH.returnLabel2())
            label2HR.setTextAlignment(Qt.AlignCenter)
            self.tableWidget_2.setItem(r, 1, label2HR)
            direcHR = QTableWidgetItem()
            direcHR.setText(afH.returnDir())
            direcHR.setTextAlignment(Qt.AlignCenter)
            self.tableWidget_2.setItem(r, 2, direcHR)
            glueHR = QTableWidgetItem()
            glueHR.setText(str(afH.returnStr()))
            glueHR.setTextAlignment(Qt.AlignCenter)
            self.tableWidget_2.setItem(r, 3, glueHR)
            r += 1

        # filling in table 3 with vertical transitions
        r = 0
        for trV in self.system.vertical_transitions_list:
            stateVT1 = QTableWidgetItem()
            stateVT1.setText(trV.returnLabel1())
            stateVT1.setTextAlignment(Qt.AlignCenter)
            self.tableWidget_3.setItem(r, 0, stateVT1)
            stateVT2 = QTableWidgetItem()
            stateVT2.setText(trV.returnLabel2())
            stateVT2.setTextAlignment(Qt.AlignCenter)
            self.tableWidget_3.setItem(r, 1, stateVT2)
            finalVT1 = QTableWidgetItem()
            finalVT1.setText(trV.returnLabel1Final())
            finalVT1.setTextAlignment(Qt.AlignCenter)
            self.tableWidget_3.setItem(r, 3, finalVT1)
            finalVT2 = QTableWidgetItem()
            finalVT2.setText(trV.returnLabel2Final())
            finalVT2.setTextAlignment(Qt.AlignCenter)
            self.tableWidget_3.setItem(r, 4, finalVT2)
            direcVT = QTableWidgetItem()
            direcVT.setText(trV.returnDir())
            direcVT.setTextAlignment(Qt.AlignCenter)
            self.tableWidget_3.setItem(r, 5, direcVT)
            r += 1

        # filling in table 3 with horizontal transitions
        for trH in self.system.horizontal_transitions_list:
            stateHT1 = QTableWidgetItem()
            stateHT1.setText(trH.returnLabel1())
            stateHT1.setTextAlignment(Qt.AlignCenter)
            self.tableWidget_3.setItem(r, 0, stateHT1)
            stateHT2 = QTableWidgetItem()
            stateHT2.setText(trH.returnLabel2())
            stateHT2.setTextAlignment(Qt.AlignCenter)
            self.tableWidget_3.setItem(r, 1, stateHT2)
            finalHT1 = QTableWidgetItem()
            finalHT1.setText(trH.returnLabel1Final())
            finalHT1.setTextAlignment(Qt.AlignCenter)
            self.tableWidget_3.setItem(r, 3, finalHT1)
            finalHT2 = QTableWidgetItem()
            finalHT2.setText(trH.returnLabel2Final())
            finalHT2.setTextAlignment(Qt.AlignCenter)
            self.tableWidget_3.setItem(r, 4, finalHT2)
            direcHT = QTableWidgetItem()
            direcHT.setText(trH.returnDir())
            direcHT.setTextAlignment(Qt.AlignCenter)
            self.tableWidget_3.setItem(r, 5, direcHT)
            r += 1

        # filling in table 1 with states
        r = 0
        for s in self.system.states:
            color_cell = QTableWidgetItem()
            color_cell.setText(s.returnColor())
            color_cell.setTextAlignment(Qt.AlignCenter)
            color_cell.setForeground(QtGui.QColor("#" + s.returnColor()))
            color_cell.setBackground(QtGui.QColor("#" + s.returnColor()))
            self.tableWidget.setItem(r, 0, color_cell)

            label_cell = QTableWidgetItem()
            label_cell.setText(s.returnLabel())
            label_cell.setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(r, 1, label_cell)

            seedWidget = QtWidgets.QWidget()
            seedCheckbox = QCheckBox()
            seedChkLayout = QtWidgets.QHBoxLayout(seedWidget)
            seedChkLayout.addWidget(seedCheckbox)
            seedChkLayout.setAlignment(Qt.AlignCenter)
            seedChkLayout.setContentsMargins(0, 0, 0, 0)
            self.tableWidget.setCellWidget(r, 2, seedWidget)
            for sstate in self.system.seed_states:
                if sstate.returnLabel() == s.returnLabel():
                    seedCheckbox.setChecked(True)

            initialWidget = QtWidgets.QWidget()
            initialCheckbox = QCheckBox()
            initialChkLayout = QtWidgets.QHBoxLayout(initialWidget)
            initialChkLayout.addWidget(initialCheckbox)
            initialChkLayout.setAlignment(Qt.AlignCenter)
            initialChkLayout.setContentsMargins(0, 0, 0, 0)
            self.tableWidget.setCellWidget(r, 3, initialWidget)
            for istate in self.system.initial_states:
                if istate.returnLabel() == s.returnLabel():
                    initialCheckbox.setChecked(True)

            r += 1

     # action for 'apply' the changes made to the side edit window to the view states side
        self.pushButton.clicked.connect(self.Click_EditApply)
        # action for 'save' the changes made to the side edit window to the XML file
        self.pushButton_2.clicked.connect(self.Click_EditSaveAs)
        self.pushButton_3.clicked.connect(self.Click_AddRowStates)
        self.pushButton_4.clicked.connect(self.Click_AddRowAff)
        self.pushButton_5.clicked.connect(self.Click_AddRowTrans)

        # duplicate row
        self.pushButton_6.clicked.connect(self.click_duplicateRowState)
        self.pushButton_7.clicked.connect(self.click_duplicateRowAff)
        self.pushButton_8.clicked.connect(self.click_duplicateRowTrans)

        # user deletes state - currently only deletes state from
        # state table.
        self.pushButton_9.clicked.connect(self.click_removeRowState)
        self.pushButton_10.clicked.connect(self.click_removeRowAff)
        self.pushButton_11.clicked.connect(self.click_removeRowTran)

        self.pushButton_12.clicked.connect(self.Click_freezingCheck)

        # Seed Editor
        self.s.table = self.t

        self.t.states.clear()
        self.s.assembly = self.Engine.getCurrentAssembly()

        for st in self.Engine.system.states:
            self.t.states.append(st)

        self.t.draw_table()
        self.s.draw_assembly()

        self.tableGraphicsView.setScene(self.t)
        self.tableGraphicsView.centerOn(0, 0)
        self.graphicsView.setScene(self.s)

    # just need to fix this function
    def Click_freezingCheck(self):
        global currentSystem
        self.label2.setText(str(FreezingCheck.main(currentSystem)))

    # for 'add state'
    def cellchanged(self, row, col):
        # only do anything is we are in the color column (0)
        if col == 0:
            print("in color column")

            color_cell = self.tableWidget.item(row, col)
            color = color_cell.text()
            color_cell.setForeground(QtGui.QColor("#" + color))
            color_cell.setBackground(QtGui.QColor("#" + color))

    def Click_AddRowStates(self):
        print("Add Row in States clicked")
        newrow = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(newrow + 1)

        color_cell = QTableWidgetItem()
        color_cell.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(newrow, 0, color_cell)

        label_cell = QTableWidgetItem()
        label_cell.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(newrow, 1, label_cell)

        seedWidget = QtWidgets.QWidget()
        seedCheckbox = QCheckBox()
        seedChkLayout = QtWidgets.QHBoxLayout(seedWidget)
        seedChkLayout.addWidget(seedCheckbox)
        seedChkLayout.setAlignment(Qt.AlignCenter)
        seedChkLayout.setContentsMargins(0, 0, 0, 0)
        self.tableWidget.setCellWidget(newrow, 2, seedWidget)

        initialWidget = QtWidgets.QWidget()
        initialCheckbox = QCheckBox()
        initialChkLayout = QtWidgets.QHBoxLayout(initialWidget)
        initialChkLayout.addWidget(initialCheckbox)
        initialChkLayout.setAlignment(Qt.AlignCenter)
        initialChkLayout.setContentsMargins(0, 0, 0, 0)
        self.tableWidget.setCellWidget(newrow, 3, initialWidget)

     # To add new row entered by user as a rule
    def Click_AddRowAff(self):
        print("Add Row in Affinities clicked")
        newrow = self.tableWidget_2.rowCount()
        self.tableWidget_2.setRowCount(newrow + 1)

        label1 = QTableWidgetItem()
        label1.setTextAlignment(Qt.AlignCenter)
        self.tableWidget_2.setItem(newrow, 0, label1)

        label2 = QTableWidgetItem()
        label2.setTextAlignment(Qt.AlignCenter)
        self.tableWidget_2.setItem(newrow, 1, label2)

        direc = QTableWidgetItem()
        direc.setTextAlignment(Qt.AlignCenter)
        self.tableWidget_2.setItem(newrow, 2, direc)

        glue = QTableWidgetItem()
        glue.setTextAlignment(Qt.AlignCenter)
        self.tableWidget_2.setItem(newrow, 3, glue)

    def Click_AddRowTrans(self):
        print("Add Row in Transitions clicked")
        newrow = self.tableWidget_3.rowCount()
        self.tableWidget_3.setRowCount(newrow + 1)

        tLabel1 = QTableWidgetItem()
        tLabel1.setTextAlignment(Qt.AlignCenter)
        self.tableWidget_3.setItem(newrow, 0, tLabel1)

        tLabel2 = QTableWidgetItem()
        tLabel2.setTextAlignment(Qt.AlignCenter)
        self.tableWidget_3.setItem(newrow, 1, tLabel2)

        tFinal1 = QTableWidgetItem()
        tFinal1.setTextAlignment(Qt.AlignCenter)
        self.tableWidget_3.setItem(newrow, 3, tFinal1)

        tFinal2 = QTableWidgetItem()
        tFinal2.setTextAlignment(Qt.AlignCenter)
        self.tableWidget_3.setItem(newrow, 4, tFinal2)

        tDirec = QTableWidgetItem()
        tDirec.setTextAlignment(Qt.AlignCenter)
        self.tableWidget_3.setItem(newrow, 5, tDirec)

    # remove/delete rows from state table
    def click_removeRowState(self):

        print("remove row button clicked")

        if self.tableWidget_2.rowCount() > 0:
            currentRow = self.tableWidget_2.currentRow()
            self.tableWidget_2.removeRow(currentRow)

        # only delete if there is something in the table, and if there is something selected
        if self.tableWidget.rowCount() > 0 and len(self.tableWidget.selectedIndexes()) > 0:
            self.tableWidget.removeRow(
                self.tableWidget.selectedIndexes()[0].row())

    def click_removeRowAff(self):
        if self.tableWidget_2.rowCount() > 0 and len(self.tableWidget_2.selectedIndexes()) > 0:
            self.tableWidget_2.removeRow(
                self.tableWidget_2.selectedIndexes()[0].row())

    def click_removeRowTran(self):
        if self.tableWidget_3.rowCount() > 0 and len(self.tableWidget_3.selectedIndexes()) > 0:
            self.tableWidget_3.removeRow(
                self.tableWidget_3.selectedIndexes()[0].row())

    # new_w is not copying checked state if w is checked
    # new_w not aligned in cells

    def copy_widget(self, w):
        if isinstance(w, QtWidgets.QWidget):
            new_w = QCheckBox()
            newWidget = QtWidgets.QWidget()
            newChkLayout = QtWidgets.QHBoxLayout(newWidget)
            newChkLayout.addWidget(new_w)
            newChkLayout.setAlignment(Qt.AlignCenter)
            newChkLayout.setContentsMargins(0, 0, 0, 0)
            # copy values

            for widget in w.children():
                if isinstance(widget, QCheckBox):
                    if widget.isChecked():
                        new_w.setChecked(True)
            # else:
             #   new_w.setChecked(False)
        return newWidget

    def copy(self, cells, r):
        self.tableWidget.insertRow(r)
        for i, it in cells["items"]:
            self.tableWidget.setItem(r, i, it)
        for i, w in cells["widgets"]:
            self.tableWidget.setCellWidget(r, i, w)

    def copy_2(self, cells, r):
        self.tableWidget_2.insertRow(r)
        for i, it in cells["items"]:
            self.tableWidget_2.setItem(r, i, it)

    def copy_3(self, cells, r):
        self.tableWidget_3.insertRow(r)
        for i, it in cells["items"]:
            self.tableWidget_3.setItem(r, i, it)

    def click_duplicateRowState(self):

        currentRow = self.tableWidget.currentRow()

        if self.tableWidget.rowCount() > 0 and len(self.tableWidget.selectedIndexes()) > 0:
            cells = {"items": [], "widgets": []}
            for i in range(self.tableWidget.columnCount()):

                it = self.tableWidget.item(currentRow, i)
                if it:
                    cells["items"].append((i, it.clone()))

                w = self.tableWidget.cellWidget(currentRow, i)
                print(w)
                if w:
                    cells["widgets"].append((i, self.copy_widget(w)))
            self.copy(cells, currentRow+1)

    def click_duplicateRowAff(self):
        currentRow = self.tableWidget_2.currentRow()

        if self.tableWidget_2.rowCount() > 0 and len(self.tableWidget_2.selectedIndexes()) > 0:
            cells = {"items": []}
            for i in range(self.tableWidget_2.columnCount()):

                it = self.tableWidget_2.item(currentRow, i)
                if it:
                    cells["items"].append((i, it.clone()))
            self.copy_2(cells, currentRow+1)

    def click_duplicateRowTrans(self):
        currentRow = self.tableWidget_3.currentRow()

        if self.tableWidget_3.rowCount() > 0 and len(self.tableWidget_3.selectedIndexes()) > 0:
            cells = {"items": []}
            for i in range(self.tableWidget_3.columnCount()):

                it = self.tableWidget_3.item(currentRow, i)
                if it:
                    cells["items"].append((i, it.clone()))
            self.copy_3(cells, currentRow+1)

    def Click_EditApply(self):
        global currentSystem
        newtemp = self.spinBox.value()

        newsys = System(newtemp, [], [], [], [], [], [], [], [], [], seed_assembly = self.s.getAssembly(), empty=True)
        currentSystem = newsys

        available_states = []
        states_used = []

        self.system = newsys

        # go through new rows, create states, add states to system
        for row in range(0, self.tableWidget.rowCount()):
            color_cell = self.tableWidget.item(row, 0)
            label_cell = self.tableWidget.item(row, 1)
            initialCheckbox = self.tableWidget.cellWidget(row, 3)
            seedCheckbox = self.tableWidget.cellWidget(row, 2)
            color = color_cell.text()
            label = label_cell.text()

            # print(initialCheckbox)
            # 'apply as' works now
            initial = initialCheckbox.layout().itemAt(0).widget().isChecked()
            seed = seedCheckbox.layout().itemAt(0).widget().isChecked()
            s = State(label, color)

            self.system.addState(s)

            available_states.append(s)

            if initial:
                self.system.addInitialState(s)
            if seed:
                self.system.addSeedState(s)

        # affinity
        for row in range(0, self.tableWidget_2.rowCount()):
            label1 = self.tableWidget_2.item(row, 0)
            label2 = self.tableWidget_2.item(row, 1)

            direc = self.tableWidget_2.item(row, 2)
            glue = self.tableWidget_2.item(row, 3)

            lab1 = label1.text()
            lab2 = label2.text()
            dire = direc.text()
            glu = glue.text()

            afRule = AffinityRule(lab1, lab2, dire, glu)

            self.system.addAffinity(afRule)

        # transitions
        for row in range(0, self.tableWidget_3.rowCount()):
            tLabel1 = self.tableWidget_3.item(row, 0)
            tLabel2 = self.tableWidget_3.item(row, 1)
            tFinal1 = self.tableWidget_3.item(row, 3)
            tFinal2 = self.tableWidget_3.item(row, 4)
            tDirec = self.tableWidget_3.item(row, 5)

            tLab1 = tLabel1.text()
            tLab2 = tLabel2.text()
            tFin1 = tFinal1.text()
            tFin2 = tFinal2.text()
            tDir = tDirec.text()

            states_used.append(tFin1)
            states_used.append(tFin2)

            trRule = TransitionRule(tLab1, tLab2, tFin1, tFin2, tDir)

            self.system.addTransitionRule(trRule)

        # Check here to see if states used in transitions exist
        states_not_used = self.StatesUsed_Exist(available_states, states_used)
        if len(states_not_used) != 0:
            error_states = ""
            for state in states_not_used:
                error_states += state
                error_states += " "

            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("The following states dont exist: \n" + error_states + "\n Click Cancel to go back or Ok to apply anyway")
            msgBox.setWindowTitle("Missing states")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            #msgBox.buttonClicked.connect(self.msgButtonClick)

            returnValue = msgBox.exec()

            if returnValue == QMessageBox.Cancel:
                return

        # assumes that the user is okay with their current system (they did not say cancel above)


        # check if states were used
        s_used = []
        for t in self.s.assembly.tiles:
            s_used.append(t.state.returnLabel())

        states_not_used = self.StatesUsed_Exist(self.system.states, s_used)
        if len(states_not_used) != 0:
            error_states = ""
            for state in states_not_used:
                error_states += state
                error_states += " "

            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("The following states dont exist in the assembly: \n" + error_states + "\n Click Cancel to go back or Ok to apply anyway (generates random seed)")
            msgBox.setWindowTitle("Missing states")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

            returnValue = msgBox.exec()

            if returnValue == QMessageBox.Ok:
                self.system.setSeedAssembly(Assembly())
            elif returnValue == QMessageBox.Cancel:
                return

        # update the engine, and update the main GUI
        self.Engine.reset_engine(self.system)

        self.mainGUI.SysLoaded = True
        currentSystem = self.system

        self.mainGUI.draw_assembly(self.Engine.getCurrentAssembly())
        self.mainGUI.Update_available_moves()

        # update the seed editor
        self.t.states.clear()
        for st in self.Engine.system.states:
            self.t.states.append(st)

        self.s.assembly = self.Engine.getCurrentAssembly()

        self.t.draw_table()
        self.s.draw_assembly()



    def Click_EditSaveAs(self):
        # TODO call save as
        print("Save As button clicked")
        fileName = QFileDialog.getSaveFileName(
            self, "QFileDialog.getSaveFileName()", "", "XML Files (*.xml)")


        currentSystem.setSeedAssembly(self.s.getAssembly())
        if(fileName[0] != ''):
            SaveFile.main(currentSystem, fileName)

    #function to see if the states the user uses exist
    def StatesUsed_Exist(self, available_states, states_used):
        states_not_used = []
        for state in states_used:
            flag = 0
            for item in available_states:
                if state == item.returnLabel():
                    flag = 1                     #flag means the state exist
                    break

            for item in states_not_used:     #if state has already been added we dont need to add it again
                if item == state:
                    flag = 1
                    break

            if flag != 1:
                states_not_used.append(state)

        return states_not_used

    def msgButtonClick(self, i):
        print("Button clicked is:",i.text())


class Ui_sCRNEditorWindow(QMainWindow, sCRNEditorWindow.Ui_EditorWindow): #the sCRN editor window class
    def __init__(self, engine, mainGUI):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('Icons/Logo.png'))
        self.mainGUI = mainGUI
        self.Engine = engine
        self.system = engine.system
        self.t = TableScene()
        self.s = SeedScene()
        # set row count state table
        self.newStateIndex = len(self.system.states)
        self.tableWidget.setRowCount(len(self.system.states))

        self.tableWidget.setColumnWidth(0, 274)
        self.tableWidget.setColumnWidth(1, 274)

        print(len(self.system.states))

        # set row count transition table
        self.tableWidget_3.setRowCount((len(self.system.horizontal_transitions_list) // 2) + len(self.system.single_transition_list))

        self.tableWidget_3.setColumnWidth(0, 124)
        self.tableWidget_3.setColumnWidth(1, 125)
        self.tableWidget_3.setColumnWidth(2, 40)
        self.tableWidget_3.setColumnWidth(3, 125)
        self.tableWidget_3.setColumnWidth(4, 125)

        # connect the color change
        self.tableWidget.cellChanged.connect(self.cellchanged)

        r = 0

        # filling in table 3 with transitions, only looking at horizontal and filtering.
        for trH in self.system.horizontal_transitions_list:
            if r > 0:
                if self.duplicateCRNRuleCheck(prevTR, trH):
                    continue
            stateHT1 = QTableWidgetItem()
            stateHT1.setText(trH.returnLabel1())
            stateHT1.setTextAlignment(Qt.AlignCenter)
            self.tableWidget_3.setItem(r, 0, stateHT1)
            stateHT2 = QTableWidgetItem()
            stateHT2.setText(trH.returnLabel2())
            stateHT2.setTextAlignment(Qt.AlignCenter)
            self.tableWidget_3.setItem(r, 1, stateHT2)
            finalHT1 = QTableWidgetItem()
            finalHT1.setText(trH.returnLabel1Final())
            finalHT1.setTextAlignment(Qt.AlignCenter)
            self.tableWidget_3.setItem(r, 3, finalHT1)
            finalHT2 = QTableWidgetItem()
            finalHT2.setText(trH.returnLabel2Final())
            finalHT2.setTextAlignment(Qt.AlignCenter)
            self.tableWidget_3.setItem(r, 4, finalHT2)

            prevTR = trH
            r += 1

        #if single transitions exist add them
        for tr in self.system.single_transition_list:
            stateHT1 = QTableWidgetItem()
            stateHT1.setText(tr.returnLabel1())
            stateHT1.setTextAlignment(Qt.AlignCenter)
            self.tableWidget_3.setItem(r, 0, stateHT1)
            stateHT2 = QTableWidgetItem()
            stateHT2.setText("")
            stateHT2.setTextAlignment(Qt.AlignCenter)
            self.tableWidget_3.setItem(r, 1, stateHT2)
            finalHT1 = QTableWidgetItem()
            finalHT1.setText(tr.returnLabel1Final())
            finalHT1.setTextAlignment(Qt.AlignCenter)
            self.tableWidget_3.setItem(r, 3, finalHT1)
            finalHT2 = QTableWidgetItem()
            finalHT2.setText("")
            finalHT2.setTextAlignment(Qt.AlignCenter)
            self.tableWidget_3.setItem(r, 4, finalHT2)

            r += 1

        # filling in table 1 with states
        r = 0
        for s in self.system.states:
            color_cell = QTableWidgetItem()
            color_cell.setText(s.returnColor())
            color_cell.setTextAlignment(Qt.AlignCenter)
            color_cell.setForeground(QtGui.QColor("#" + s.returnColor()))
            color_cell.setBackground(QtGui.QColor("#" + s.returnColor()))
            self.tableWidget.setItem(r, 0, color_cell)

            label_cell = QTableWidgetItem()
            label_cell.setText(s.returnLabel())
            label_cell.setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(r, 1, label_cell)

            r += 1

     # action for 'apply' the changes made to the side edit window to the view states side
        self.pushButton.clicked.connect(self.Click_EditApply)
        # action for 'save' the changes made to the side edit window to the XML file
        self.pushButton_2.clicked.connect(self.Click_EditSaveAs)
        self.pushButton_3.clicked.connect(self.Click_AddRowStates)
        self.pushButton_5.clicked.connect(self.Click_AddRowTrans)

        # duplicate row
        self.pushButton_6.clicked.connect(self.click_duplicateRowState)
        self.pushButton_8.clicked.connect(self.click_duplicateRowTrans)

        # user deletes state - currently only deletes state from
        # state table.
        self.pushButton_9.clicked.connect(self.click_removeRowState)
        self.pushButton_11.clicked.connect(self.click_removeRowTran)

        # Seed Editor
        self.s.table = self.t

        self.t.states.clear()
        self.s.assembly = self.Engine.getCurrentAssembly()

        for st in engine.system.states:
            self.t.states.append(st)

        self.t.draw_table()
        self.s.draw_assembly()

        self.tableGraphicsView.setScene(self.t)
        self.tableGraphicsView.centerOn(0, 0)
        self.graphicsView.setScene(self.s)

    # for 'add state'
    def cellchanged(self, row, col):
        # only do anything is we are in the color column (0)
        if col == 0:

            color_cell = self.tableWidget.item(row, col)
            color = color_cell.text()
            color_cell.setForeground(QtGui.QColor("#" + color))
            color_cell.setBackground(QtGui.QColor("#" + color))

    #a function to check if the rule has already been parsed, just in a different orientation
    def duplicateCRNRuleCheck(self, rule1, rule2):
        if (rule1.returnLabel1() == rule2.returnLabel2()) and (rule1.returnLabel2() == rule2.returnLabel1()):
            if(rule1.returnLabel1Final() == rule2.returnLabel2Final()) and (rule1.returnLabel2Final() == rule2.returnLabel1Final()):
                print("duplicate found")
                return True

        return False

    def Click_AddRowStates(self):
        newrow = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(newrow + 1)

        color_cell = QTableWidgetItem()
        color_cell.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(newrow, 0, color_cell)

        label_cell = QTableWidgetItem()
        label_cell.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(newrow, 1, label_cell)

    def Click_AddRowTrans(self):
        print("Add Row in Transitions clicked")
        newrow = self.tableWidget_3.rowCount()
        self.tableWidget_3.setRowCount(newrow + 1)

        tLabel1 = QTableWidgetItem()
        tLabel1.setTextAlignment(Qt.AlignCenter)
        self.tableWidget_3.setItem(newrow, 0, tLabel1)

        tLabel2 = QTableWidgetItem()
        tLabel2.setTextAlignment(Qt.AlignCenter)
        self.tableWidget_3.setItem(newrow, 1, tLabel2)

        tFinal1 = QTableWidgetItem()
        tFinal1.setTextAlignment(Qt.AlignCenter)
        self.tableWidget_3.setItem(newrow, 3, tFinal1)

        tFinal2 = QTableWidgetItem()
        tFinal2.setTextAlignment(Qt.AlignCenter)
        self.tableWidget_3.setItem(newrow, 4, tFinal2)

    # remove/delete rows from state table
    def click_removeRowState(self):
        # only delete if there is something in the table, and if there is something selected
        if self.tableWidget.rowCount() > 0 and len(self.tableWidget.selectedIndexes()) > 0:
            self.tableWidget.removeRow(
                self.tableWidget.selectedIndexes()[0].row())

    def click_removeRowTran(self):
        if self.tableWidget_3.rowCount() > 0 and len(self.tableWidget_3.selectedIndexes()) > 0:
            self.tableWidget_3.removeRow(
                self.tableWidget_3.selectedIndexes()[0].row())

    def copy_widget(self, w):
        if isinstance(w, QtWidgets.QWidget):
            new_w = QCheckBox()
            newWidget = QtWidgets.QWidget()
            newChkLayout = QtWidgets.QHBoxLayout(newWidget)
            newChkLayout.addWidget(new_w)
            newChkLayout.setAlignment(Qt.AlignCenter)
            newChkLayout.setContentsMargins(0, 0, 0, 0)
            # copy values

            for widget in w.children():
                if isinstance(widget, QCheckBox):
                    if widget.isChecked():
                        new_w.setChecked(True)
            # else:
             #   new_w.setChecked(False)
        return newWidget

    def copy(self, cells, r):
        self.tableWidget.insertRow(r)
        for i, it in cells["items"]:
            self.tableWidget.setItem(r, i, it)
        for i, w in cells["widgets"]:
            self.tableWidget.setCellWidget(r, i, w)

    def copy_3(self, cells, r):
        self.tableWidget_3.insertRow(r)
        for i, it in cells["items"]:
            self.tableWidget_3.setItem(r, i, it)

    def click_duplicateRowState(self):
        currentRow = self.tableWidget.currentRow()

        if self.tableWidget.rowCount() > 0 and len(self.tableWidget.selectedIndexes()) > 0:
            cells = {"items": [], "widgets": []}
            for i in range(self.tableWidget.columnCount()):

                it = self.tableWidget.item(currentRow, i)
                if it:
                    cells["items"].append((i, it.clone()))

                w = self.tableWidget.cellWidget(currentRow, i)
                print(w)
                if w:
                    cells["widgets"].append((i, self.copy_widget(w)))
            self.copy(cells, currentRow+1)

    def click_duplicateRowTrans(self):
        currentRow = self.tableWidget_3.currentRow()

        if self.tableWidget_3.rowCount() > 0 and len(self.tableWidget_3.selectedIndexes()) > 0:
            cells = {"items": []}
            for i in range(self.tableWidget_3.columnCount()):

                it = self.tableWidget_3.item(currentRow, i)
                if it:
                    cells["items"].append((i, it.clone()))
            self.copy_3(cells, currentRow+1)

    def Click_EditApply(self):
        global currentSystem
        newtemp = 1

        newsys = System(newtemp, [], [], [], [], [], [], [], [], [], seed_assembly = self.s.getAssembly(), empty=True)
        currentSystem = newsys

        available_states = []
        states_used = []

        self.system = newsys

        # go through new rows, create states, add states to system
        for row in range(0, self.tableWidget.rowCount()):
            color_cell = self.tableWidget.item(row, 0)
            label_cell = self.tableWidget.item(row, 1)
            color = color_cell.text()
            label = label_cell.text()

            # print(initialCheckbox)
            # 'apply as' works now
            s = State(label, color)

            self.system.addState(s)

            available_states.append(s)

            self.system.addSeedState(s)

        # transitions
        for row in range(0, self.tableWidget_3.rowCount()):
            if ((self.tableWidget_3.item(row, 0).text() == "" and self.tableWidget_3.item(row, 1).text() == "") or (self.tableWidget_3.item(row, 3).text() == "" and self.tableWidget_3.item(row, 4).text() == "")):
                continue

            if self.tableWidget_3.item(row, 0).text() == "" and self.tableWidget_3.item(row, 1).text() != "":
                self.tableWidget_3.item(row, 0).setText(self.tableWidget_3.item(row, 1).text())
                self.tableWidget_3.item(row, 1).setText("")

            if self.tableWidget_3.item(row, 0).text() != "" and self.tableWidget_3.item(row, 1).text() == "":
                if self.tableWidget_3.item(row, 3).text() == "" and self.tableWidget_3.item(row, 4).text() != "":
                    self.tableWidget_3.item(row, 3).setText(self.tableWidget_3.item(row, 4).text())
                    self.tableWidget_3.item(row, 4).setText("")

                if self.tableWidget_3.item(row, 3).text() != "" and self.tableWidget_3.item(row, 4).text() == "":
                    tLabel1 = self.tableWidget_3.item(row, 0)
                    tFinal1 = self.tableWidget_3.item(row, 3)

                    tLab1 = tLabel1.text()
                    tFin1 = tFinal1.text()
                    
                    states_used.append(tFin1)

                    trRule = SingleTransitionRule(tLab1, tFin1)
                    self.system.addSingleTransitionRule(trRule)
            else:
                tLabel1 = self.tableWidget_3.item(row, 0)
                tLabel2 = self.tableWidget_3.item(row, 1)
                tFinal1 = self.tableWidget_3.item(row, 3)
                tFinal2 = self.tableWidget_3.item(row, 4)

                tLab1 = tLabel1.text()
                tLab2 = tLabel2.text()
                tFin1 = tFinal1.text()
                tFin2 = tFinal2.text()

                states_used.append(tFin1)
                states_used.append(tFin2)

                trRule1 = TransitionRule(tLab1, tLab2, tFin1, tFin2, "h")
                trRule2 = TransitionRule(tLab2, tLab1, tFin2, tFin1, "h")
                trRule3 = TransitionRule(tLab1, tLab2, tFin1, tFin2, "v")
                trRule4 = TransitionRule(tLab2, tLab1, tFin2, tFin1, "v")

                self.system.addTransitionRule(trRule1)
                self.system.addTransitionRule(trRule2)
                self.system.addTransitionRule(trRule3)
                self.system.addTransitionRule(trRule4)

        # Check here to see if states used in transitions exist
        states_not_used = self.StatesUsed_Exist(available_states, states_used)
        if len(states_not_used) != 0:
            error_states = ""
            for state in states_not_used:
                error_states += state
                error_states += " "

            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("The following states dont exist: \n" + error_states + "\n Click Cancel to go back or Ok to apply anyway")
            msgBox.setWindowTitle("Missing states")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            #msgBox.buttonClicked.connect(self.msgButtonClick)

            returnValue = msgBox.exec()

            if returnValue == QMessageBox.Cancel:
                return

        # assumes that the user is okay with their current system (they did not say cancel above)


        # check if states were used
        s_used = []
        for t in self.s.assembly.tiles:
            s_used.append(t.state.returnLabel())

        states_not_used = self.StatesUsed_Exist(self.system.states, s_used)
        if len(states_not_used) != 0:
            error_states = ""
            for state in states_not_used:
                error_states += state
                error_states += " "

            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("The following states dont exist in the assembly: \n" + error_states + "\n Click Cancel to go back or Ok to apply anyway (generates random seed)")
            msgBox.setWindowTitle("Missing states")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

            returnValue = msgBox.exec()

            if returnValue == QMessageBox.Ok:
                self.system.setSeedAssembly(Assembly())
            elif returnValue == QMessageBox.Cancel:
                return


        # update the engine, and update the main GUI
        self.Engine.reset_engine(self.system)

        self.mainGUI.SysLoaded = True
        currentSystem = self.system

        self.mainGUI.draw_assembly(self.Engine.getCurrentAssembly())
        self.mainGUI.Update_available_moves()

        # update the seed editor
        self.t.states.clear()
        self.s.assembly = self.Engine.getCurrentAssembly()

        for st in self.Engine.system.states:
            self.t.states.append(st)

        self.t.draw_table()
        self.s.draw_assembly()

    def Click_EditSaveAs(self):
        print("Save As button clicked")
        fileName = QFileDialog.getSaveFileName(
            self, "QFileDialog.getSaveFileName()", "", "XML Files (*.xml)")

        currentSystem.setSeedAssembly(self.s.getAssembly())
        if(fileName[0] != ''):
            SaveFile.main(currentSystem, fileName)

    #function to see if the states the user uses exist
    def StatesUsed_Exist(self, available_states, states_used):
        states_not_used = []
        for state in states_used:
            flag = 0
            for item in available_states:
                if state == item.returnLabel():
                    flag = 1                     #flag means the state exist
                    break

            for item in states_not_used:     #if state has already been added we dont need to add it again
                if item == state:
                    flag = 1
                    break

            if flag != 1:
                states_not_used.append(state)

        return states_not_used

    def msgButtonClick(self, i):
        print("Button clicked is:",i.text())

class Move(QWidget):

    def __init__(self, move, mw, parent):
        super().__init__(parent)
        self.move = move
        self.mw = mw
        self.initUI()

    def initUI(self):
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw(event, qp)
        qp.end()

    def draw(self, event, qp):
        moveText = ""

        if self.move == None:
            return

        if self.move["type"] == "a":
            moveText = "Attach\n" + self.move["state1"].returnLabel() + " at " + str(
                self.move["x"]) + " , " + str(self.move["y"])
        elif self.move["type"] == "t":
            if self.move["state1Final"] != None and self.move["state2Final"] != None:
                # Add Transition Direction
                if self.move["dir"] == "v":
                    moveText = "V "
                else:
                    moveText = "H "
                moveText += "Transition\n" + self.move["state1"].returnLabel() + ", " + self.move["state2"].returnLabel(
                ) + " to " + self.move["state1Final"].returnLabel() + ", " + self.move["state2Final"].returnLabel()
            else:
                moveText = "Error:\n state doesn't exist"

        pen = QApplication.palette().text().color()
        qp.setPen(pen)
        qp.drawText(event.rect(), Qt.AlignCenter, moveText)
        qp.drawRect(event.rect())

    def mousePressEvent(self, event):
        if self.move == None:
            return

        self.mw.do_move(self.move)


if __name__ == "__main__":
    # App Stuff
    app = QApplication(sys.argv)
    w = Ui_MainWindow()
    w.show()
    sys.exit(app.exec_())
    #