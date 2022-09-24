import sys

from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import Qt
from UniversalClasses import Assembly, Tile, State


class TestWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TestWindow")

        # Seed Editor Code
        self.width: int = 800
        self.height: int = 600
        self.resize(self.width, self.height)
        self.seedX = self.geometry().width() / 2
        self.seedY = self.geometry().height() / 2
        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(self.width, self.height)
        # canvas.fill(Qt.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)

        self.tileSize = 40
        self.textSize = int(self.tileSize / 3)

        # Testing Assembly
        s1 = State("yo", "ff0000")
        s2 = State("ma", "00ff00")
        s3 = State("ya", "0000ff")
        tiles = []
        tiles.append(Tile(s1, 0, 0))
        tiles.append(Tile(s2, 1, 0))
        tiles.append(Tile(s3, 0, 1))
        tiles.append(Tile(s2, -1, 0))
        ass = Assembly()
        ass.setTilesFromList(tiles)
        self.draw_assembly(ass)

    def onScreen_check(self, x, y):
        if((x * self.tileSize) + self.seedX > self.geometry().width() or (x * self.tileSize) + self.seedX < -self.tileSize):
            return 1
        if((y * -self.tileSize) + self.seedY > self.geometry().height() or (y * -self.tileSize) + self.seedY < -self.tileSize):
            return 1
        return 0

    def mouseReleaseEvent(self, e):
        print("Click at", e.x(), ",", e.y())
        x = e.x() - self.seedX
        y = e.y() - self.seedY
        if x < 0:
            x -= 40
        if y < 0:
            y -= 40

        x = int(x / self.tileSize)
        y = int(y / self.tileSize)
        print("Tile would be at", x, y)

    def draw_to_screen(self, x, y, state, painter, brush):
        painter.setBrush(brush)
        ts = self.tileSize
        ts_x = int((x * ts) + self.seedX)
        ts_y = int((y * -ts) + self.seedY)
        rect = QtCore.QRect(ts_x, ts_y, ts, ts)

        painter.drawRect(rect)
        print("Drew tile", x, y, "::", ts_x, ts_y, ts, ts)

        if state == "":
            painter.drawText(rect, Qt.AlignCenter, "")
            return
        else:
            decoded_display_label = state.display_label

        if self.tileSize > 10:
            fm = QtGui.QFontMetrics(painter.font())
            txt_width = fm.width(decoded_display_label)

            if decoded_display_label is None:
                if len(state.label) > 4:
                    painter.drawText(rect, Qt.AlignCenter, state.label[0:3])
                else:
                    painter.drawText(rect, Qt.AlignCenter, state.label)
            elif len(decoded_display_label) > 4:

                painter.drawText(rect, Qt.AlignCenter,
                                 decoded_display_label[0:3])
            else:
                painter.drawText(rect, Qt.AlignCenter, decoded_display_label)

    def draw_assembly(self, assembly):
        painter = QtGui.QPainter(self.label.pixmap())
        pen = QtGui.QPen()
        brush = QtGui.QBrush()
        font = QtGui.QFont()

        pen.setWidth(3)
        brush.setStyle(Qt.SolidPattern)
        pen.setColor(QtGui.QColor("white"))
        brush.setColor(QtGui.QColor("white"))
        painter.setPen(pen)
        painter.setBrush(brush)
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

        painter.end()

        self.update()


app = QtWidgets.QApplication(sys.argv)
window = TestWindow()
window.show()
app.exec_()
