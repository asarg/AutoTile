from Generators.IU_Generators.binaryStates import *
from UniversalClasses import State, TransitionRule, AffinityRule, System, Tile, Assembly
from Assets.colors import *
from Generators.IU_Generators.binaryStates import *
import sys

class AttachmentPoint(AffinityRule):

    def __init__(self, gadget1, tile1, gadget2, tile2, dir, strength=None):
        """
        gadget 1 is the gadget that is being attached to gadget 2
        the tiles are the tiles being attached the other
        tiles must be in a state that is compatible with the attachment
        dir is the direction of the attachment to gadget 2
        if gadget 1 is being attached to the north of gadget 2 then dir = 'N'
        The combined assembly will have the x and y coordinates of gadget 2
        Tile 2 must use local gadget coordinates rather than global coordinates
        """
        self.gadget1 = gadget1
        self.tile1 = tile1

        self.gadget2 = gadget2
        self.tile2 = tile2

        self.dir = dir # direction of g1s attachment to g2 at xy point (N, S, E, W)
        if dir == 'N':
            label1 = gadget1.label_id
            label2 = gadget2.label_id
            aff_dir = 'v'
        elif dir == 'S':
            label1 = gadget2.label_id
            label2 = gadget1.label_id
            aff_dir = 'v'
        elif dir == 'E':
            label1 = gadget1.label_id
            label2 = gadget2.label_id
            aff_dir = 'h'
        else:
            label1 = gadget2.label_id
            label2 = gadget1.label_id
            aff_dir = 'h'

        super().__init__(label1, label2, aff_dir, strength)


class SuperState(State):
    def __init__(self, input_state, unary_state_num=0, row_dir_nums_dict={"N": int, "S": int, "E": int, "W": int}):
        self.input_state = input_state
        self.unary_state_num = unary_state_num
        self.col_num = int(unary_state_num, 1)
        self.row_nums = row_dir_nums_dict

    def __str__(self):
        return f'{self.input_state.label}_{self.unary_state_num}_superstate'

    def __repr__(self, include_python_variable_name=False):
        if include_python_variable_name:
            f'{self.input_state.label}_{self.unary_state_num}_superstate = SuperState({self.input_state.label}, {self.unary_state_num}, {self.row_nums})'
        return SuperState(self.input_state, self.unary_state_num, self.row_nums)


class Gadget(Assembly):
    """_summary_

    Args:
        Assembly (_type_): _description_
    """

    def __init__(self, id=-1, label=' ', gadget_type='abstract gadget', relative_coords={}, seedStates=[]):
        super().__init__()
        self.label_id = label + '_' + str(id)
        self.gadget_type = gadget_type
        self.id = id
        self.relative_coords = relative_coords # relative coordinates of the tiles/states in the gadget
        self.seedStates = seedStates

    def update_gadget_location(self, local_x, local_y, global_x, global_y):
        pass

    def appendSeedAssembly(self, tile):
        pass

    @property
    def seed_tiles(self):
        pass

    @property
    def vertical_transitions(self):
        pass

    @property
    def horizontal_transitions(self):
        pass

    @property
    def vertical_affinities(self):
        pass

    @property
    def horizontal_affinities(self):
        pass

    @property
    def gadget_id(self):
        pass

    # @property
    # def attachment_points(self):

    #     return self._attachment_points

    # @attachment_points.setter()
    # def attachment_points(self, att_points_list):
    #     pass

    # def append_attachment_point(self, local_x, local_y, global_x, global_y, direction):
    #     pass





class CompoundGadget(Gadget):
    def __init__(self, label, id, seed_gadget=None, other_gadgets=[], attachment_points=[]):
        super().__init__(label=label)
        self.label_id = label + '_' + str(id)
        self.seed_gadget = seed_gadget
        self.other_gadgets = other_gadgets
        self.attachment_points = attachment_points






class Door(Gadget):
    states = [State('open'), State('closed')]
    pass

class Wire(Gadget):
    pass

class MacroCell(CompoundGadget):
    """The Super States of the intersection of a row and a column with the direction the row is
        coming from and the column of the current superblocks state

    Args:
        CompoundGadget (_type_): _description_
        super_state (SuperState): _description_
    """
    def __init__(self, super_state, incoming_state, coming_from_dir):
        super().__init__()
        self.super_state = super_state
        self.incoming_state = incoming_state
        self.coming_from_dir = coming_from_dir
        self.affinity = None
        self.transition = None



class Column(CompoundGadget):
    pass

class Row(CompoundGadget):
    pass

class Table(CompoundGadget):
    pass

class MacroBlock(CompoundGadget):
    pass

class IU_System(System):
    full_tileset_unit_states = {}
    full_tileset_unit_initial_states = {}
    full_tileset_unit_seed_states = {}
    full_tileset_vertical_affinities_dict = {}
    full_tileset_horizontal_affinities_dict = {}
    full_tileset_vertical_transitions_dict = {}
    full_tileset_horizontal_transitions_dict = {}

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, input_system):
        self.input_system = input_system
        self.temp = input_system.temp
        self.states, self.initial_states, self.seed_states = {}
        self.vertical_transitions_dict = {}
        self.horizontal_transitions_dict = {}
        self.vertical_affinities_dict = {}
        self.horizontal_affinities_dict = {}

    def write_all_to_file(self, filename="iu_system_all_states_aff_tr.txt", open_type='x'):
        self.write_all_states_to_file_in_list(filename, open_type)
        self.write_all_initial_states_to_file_in_list(filename, open_type)
        self.write_all_seed_states_to_file_in_list(filename, open_type)

    def write_all_states_to_file_in_list(self, file_name="iu_system_all_states.txt", open_type='x'):

        with open(file_name, open_type) as file:
            file.write('\# States \n \n')
            file.write(f'{state.label}_state = State({state.label}, {state.color}, {state.display_label}) \n'
             for state in self.initial_states)

            file.write(f'states = [')
            for state in self.states:
                var_name = f'{state.label}_state,\n'
                file.write(var_name)
            file.write(f'] \n')

    def write_all_initial_states_to_file_in_list(self, file_name="iu_system_all_initial_states.txt", open_type='x'):
        with open(file_name, open_type) as file:
            file.write('\# Initial States \n \n')
            file.write(f'initial_states = [')
            for state in self.initial_states:
                var_name = f'{state.label}_state, \n'
                file.write(var_name)
            file.write(f'] \n')


    def write_all_seed_states_to_file_in_list(self, file_name="iu_system_all_seed_states.txt", open_type='x'):
        with open(file_name, open_type) as file:
            file.write('\# Seed States \n \n')
            file.write(f'seed_states = [')
            for state in self.seed_states:
                var_name = f'{state.label}_state, \n'
                file.write(var_name)
            file.write(f'] \n')

    def write_all_horizontal_affinities_to_file_in_list(self, file_name="iu_system_all_horizontal_affinities.txt", open_type='x'):
        with open(file_name, open_type) as file:
            file.write('\# Horizontal Affinities \n \n')
            file.write(f'horizontal_affinities = [')
            for aff in self.horizontal_affinities_dict:
                var_name = f'{aff.state1.label}_{aff.state2.label}_h_aff = AffinityRule(\'{aff.label1}\', \'{aff.label2}\', \'h\' {aff.strength}), \n'
                file.write(var_name)
            file.write(f'] \n')

    def write_all_vertical_affinities_to_file_in_list(self, file_name="iu_system_all_vertical_affinities.txt", open_type='x'):
        with open(file_name, open_type) as file:
            file.write('\# Vertical Affinities \n \n')
            file.write(f'vertical_affinities = [')
            for aff in self.vertical_affinities_dict:
                var_name = f'{aff.label1}_{aff.label2}_v_aff = AffinityRule(\'{aff.label1}\', \'{aff.label2}\', \'v\', {aff.strength}) \n'
                file.write(var_name)
            file.write(f'] \n')

    def write_all_horizontal_transitions_to_file_in_list(self, file_name="iu_system_all_horizontal_transitions.txt", open_type='x'):
        with open(file_name, open_type) as file:
            file.write('\# Horizontal Transitions \n \n')
            file.write(f'horizontal_transitions = [')
            for tr in self.horizontal_transitions_dict:
                var_name = f'{tr.label1}_{tr.label2}_h_tr = TransitionRule(\'{tr.label1}\', \'{tr.label2}\', \'{tr.label1Final}\', \'{tr.label2Final}\',\'h\') \n'
                file.write(var_name)
            file.write(f'] \n')

    def write_all_vertical_transitions_to_file_in_list(self, file_name="iu_system_all_vertical_tr.txt", open_type='x'):
        with open(file_name, open_type) as file:
            file.write('\# Horizontal Transitions \n \n')
            file.write(f'vertical_transitions = [')
            for tr in self.horizontal_transitions_dict:
                var_name = f'{tr.label1}_{tr.label2}_h_tr = TransitionRule(\'{tr.label1}\', \'{tr.label2}\', \'{tr.label1Final}\', \'{tr.label2Final}\',\'v\') \n'
                file.write(var_name)
            file.write(f'] \n')
