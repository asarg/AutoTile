
from UniversalClasses import Tile
from Generators.IU_Generators.binaryStates import ds_1_inactive_mc, start_state_pair, end_state_pair, ds_pos_placeholder
from Generators.IU_Generators.General_IU_Helper_Functions import *

def topOfColumnLabel(self, tl, tr, unary_state_num, start_end_state_style="[]", style="UnaryMaxWidth",
                     max_label_width=None, blank_template=None):
        tiles = []
        """Makes the top of the column label"""

        if style == "UnaryMaxWidth":
            if max_label_width == None:
               pass

            elif len(unary_state_num) < max_label_width:
                pass
        else:
         pass


def topOfColumnLabelBlankTemplate(self, tl, tr, max_label_width, start_end_state_style="[]"):
        tiles = []
        """Makes the top of the column label"""


# def blankTopOfColumnTemplateLabel(self, tl, tr, unary_state_num, start_end_state_style="[]", style="UnaryMaxWidth",
#                      max_label_width=None, blank_template=blank_state):
#     pass

        #self.drawCell(column, row, label, style, self.topOfColumnLabelStyle)