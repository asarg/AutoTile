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


class TableScene(QtWidgets.QGraphicsScene):
    def __init__(self):
        super().__init__()

        self.width: int = 150
        self.height: int = 4000
        self.seedX = self.width / 2
        self.seedY = self.height / 2
        self.canvas = QtGui.QPixmap(self.width, self.height)
        self.scenePixmapItem = self.addPixmap(self.canvas)

        self.tileSize = 40
        self.textSize = int(self.tileSize / 3)

        # Testing states
        self.states = []
        self.selected = -1

    def draw_to_screen(self, x, y, state, painter, brush):
        painter.setBrush(brush)
        ts = self.tileSize
        rect = QtCore.QRect(x, y, ts, ts)

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

                painter.drawText(rect, Qt.AlignCenter, decoded_display_label[0:3])
            else:
                painter.drawText(rect, Qt.AlignCenter, decoded_display_label)

    def mouseReleaseEvent(self, e):
        x = e.scenePos().x()
        y = e.scenePos().y()
        section_y = int(y / (self.tileSize + 20))

        if (
            y >= ((section_y * (self.tileSize + 20)) + 20)
            and y <= ((section_y + 1) * (self.tileSize + 20))
            and x >= int(self.width / 2 - (self.tileSize / 2))
            and x <= int(self.width / 2 + (self.tileSize / 2))
        ):
            self.selected = section_y
            self.draw_table()

    def draw_table(self):
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
        x = int(self.width / 2 - (self.tileSize / 2))
        y = int(20)
        i = 0
        for s in self.states:
            brush.setColor(QtGui.QColor("#" + s.returnColor()))
            self.draw_to_screen(x, y, s, painter, brush)

            if i == self.selected:
                self.highlight_tile(s, x, y, painter, brush, pen)

            i += 1
            y += self.tileSize + 20



        painter.end()

        self.scenePixmapItem.setPixmap(self.canvas)
        self.update()

    def highlight_tile(self, state, x, y, painter, brush, pen):
        brush.setColor(QtGui.QColor("#" + state.returnColor()))
        pen.setColor(QtGui.QColor("blue"))
        painter.setPen(pen)
        self.draw_to_screen(x, y, state, painter, brush)
        pen.setColor(QtGui.QColor("black"))
        painter.setPen(pen)


class SeedScene(QtWidgets.QGraphicsScene):
    def __init__(self):
        super().__init__()

        self.width: int = 8000
        self.height: int = 8000
        self.seedX = self.width / 2
        self.seedY = self.height / 2
        self.canvas = QtGui.QPixmap(self.width, self.height)
        self.scenePixmapItem = self.addPixmap(self.canvas)

        self.tileSize = 40
        self.textSize = int(self.tileSize / 3)

        self.assembly = Assembly()
        self.table = None

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

        # Find x,y if it is in use
        for t in self.assembly.tiles:
            if t.x == x and t.y == y:
                self.assembly.tiles.remove(t)
                break

        if e.button() == Qt.LeftButton:
            # selected state
            s = self.table.states[self.table.selected]
            self.assembly.setTiles([Tile(s, x, y)])

        self.draw_assembly()

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

                painter.drawText(rect, Qt.AlignCenter, decoded_display_label[0:3])
            else:
                painter.drawText(rect, Qt.AlignCenter, decoded_display_label)

    def draw_assembly(self):
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
        for tile in self.assembly.tiles:
            brush.setColor(QtGui.QColor("#" + tile.returnColor()))
            self.draw_to_screen(tile.x, tile.y, tile.state, painter, brush)

        painter.end()

        self.scenePixmapItem.setPixmap(self.canvas)
        self.update()
    
    def getAssembly(self):
        return self.assembly


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TestWindow()
    window.show()
    app.exec_()
