
from UniversalClasses import Tile
from Generators.IU_Generators.binaryStates import ds_1_inactive_mc, start_state_pair, end_state_pair, ds_pos_placeholder, ds_1
from Generators.IU_Generators.General_IU_Helper_Functions import *


def topOfColumnLabel(self, tl, tr, unary_state_num, start_end_state_style="[]", max_state_len=None, style="UnaryMaxWidth",
                      blank_template=None):
        tiles = []
        """Makes the top of the column label"""
        x_current = tr[0] - 1
        if start_end_state_style == "[]":
            tiles.append(Tile(end_state_pair, x_current))
            x_current -= 1

        if style == "UnaryMaxWidth":
            if max_state_len == None:
               pass
            else:
                j = len(unary_state_num)

                for i in range(x_current, tl[0], -1):
                    if j > 0:
                        tiles.append(Tile(ds_1, i, tl[1]))
                        j = j - 1
                    elif i == tl[0] - 1:
                        tiles.append(Tile(start_state_pair, i, tl[1]))
                    else:
                        tiles.append(Tile(ds_pos_placeholder, i, tl[1]))

        else:
            j = len(unary_state_num)
            for i in range(x_current, x_current - len(unary_state_num) -1, -1):
                if j > 0:
                    tiles.append(Tile(ds_1, i, tl[1]))
                    j = j - 1
                else:
                    tiles.append(Tile(start_state_pair, i, tl[1]))




def topOfColumnLabelBlankTemplate(self, tl, tr, max_label_width, start_end_state_style="[]"):
        tiles = []
        """Makes the top of the column label"""


# def blankTopOfColumnTemplateLabel(self, tl, tr, unary_state_num, start_end_state_style="[]", style="UnaryMaxWidth",
#                      max_label_width=None, blank_template=blank_state):
#     pass

        #self.drawCell(column, row, label, style, self.topOfColumnLabelStyle)