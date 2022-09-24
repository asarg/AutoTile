import sys

from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import Qt
from UniversalClasses import Assembly, Tile, State


class TestWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        scene = SeedScene()
        view = QtWidgets.QGraphicsView(scene)

        self.resize(800, 600)

        self.setCentralWidget(view)


class SeedScene(QtWidgets.QGraphicsScene):
    def __init__(self):
        super().__init__()

        self.width: int = 8000
        self.height: int = 8000
        self.seedX = self.width / 2
        self.seedY = self.height / 2
        self.label = QtWidgets.QLabel()
        self.canvas = QtGui.QPixmap(self.width, self.height)
        self.scenePixmapItem = self.addPixmap(self.canvas)

        self.tileSize = 40
        self.textSize = int(self.tileSize / 3)

        # Testing Assembly
        self.ass = Assembly()
        s1 = State("yo", "ff0000")
        s2 = State("ma", "00ff00")
        s3 = State("ya", "0000ff")
        self.ass.tiles.append(Tile(s1, 0, 0))
        self.ass.tiles.append(Tile(s2, 1, 0))
        self.ass.tiles.append(Tile(s3, 0, 1))
        self.ass.tiles.append(Tile(s2, -1, 0))
        self.draw_assembly(self.ass)

    def mouseReleaseEvent(self, e):
        x = e.scenePos().x()
        y = e.scenePos().y()
        x = x - self.seedX
        y = y - self.seedY
        if x < 0:
            x -= 40
        if y < 0:
            y -= 40
        x = int(x / self.tileSize)
        y = int(y / -self.tileSize)

        # will be replaced by the selected state
        s = State("new", "ff00ff")

        # Find x,y if it is in use
        for t in self.ass.tiles:
            if t.x == x and t.y == y:
                self.ass.tiles.remove(t)
                break

        self.ass.tiles.append(Tile(s, x, y))
        self.draw_assembly(self.ass)

    def draw_to_screen(self, x, y, state, painter, brush):
        painter.setBrush(brush)
        ts = self.tileSize
        ts_x = int((x * ts) + self.seedX)
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
        painter = QtGui.QPainter(self.canvas)
        pen = QtGui.QPen()
        brush = QtGui.QBrush()
        font = QtGui.QFont()

        pen.setWidth(3)
        brush.setStyle(Qt.SolidPattern)
        pen.setColor(QtGui.QColor("white"))
        brush.setColor(QtGui.QColor("white"))
        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawRect(0, 0, self.width, self.height)

        # Font
        font.setFamily("Fira Code")
        font.setBold(True)
        font.setPixelSize(self.textSize)
        painter.setFont(font)

        pen.setColor(QtGui.QColor("black"))
        painter.setPen(pen)
        for tile in assembly.tiles:
            brush.setColor(QtGui.QColor("#" + tile.returnColor()))
            self.draw_to_screen(tile.x, tile.y, tile.state, painter, brush)

        painter.end()

        self.scenePixmapItem.setPixmap(self.canvas)
        self.update()


app = QtWidgets.QApplication(sys.argv)
window = TestWindow()
window.show()
app.exec_()
