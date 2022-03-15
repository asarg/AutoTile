import sampleGen 
from UniversalClasses import Tile, Assembly
from assemblyEngine import Engine
import svgwrite


tileSize = 25


def addTile(drawing, tile):

    x = tileSize * tile.x
    y = tileSize * tile.y

    color = "fill:#" + tile.get_color()


    tileImg = svgwrite.shapes.Rect((x,y), (tileSize, tileSize), style=color)
    drawing.add(tileImg)




def export(filename, assembly):
    dwg = svgwrite.Drawing(filename, profile='tiny')

    
    for t in assembly.tiles:
        addTile(dwg, t)

    

    dwg.save()


if __name__ == "__main__":
    sys = sampleGen.generator("Strings", "101010101", "Deterministic")

    eng = Engine(sys)
    
    while True:
        if eng.step() == -1:
            break

    terminal = eng.getCurrentAssembly()


    export("assembly.svg", terminal)