import pandas as pd
import numpy as np

# Create an iu unit state dataframe

'''
Attributes:
id
label
base_state
category
color
applicable_colors
display_label
applicable_symbols
is_initial_state
is_seed_state
has_activity_status
activity_status
has_direction_iter
directions
wire_travel_capacity
wire_travel_directions
reverse_wire_travel_directions
gadgets_in
affinities_with
transitions_with
'''
# 'color', 'applicable_colors', 'display_label', 'applicable_symbols', 'activity_status', 'directions', 'reverse_wire_travel_directions',
# # 'wire_travel_directions' mark negative values for reverse travel

# Create a dataframe with the following columns:
#states_df = pd.DataFrame(columns=['id', 'label', 'base_state', 'category',  'is_initial_state', 'has_activity_status',
                         #'has_direction', 'has_wire_travel_capacity', 'wire_travel_directions', 'gadgets_in', 'affinities_with', 'construction_state', 'transitions_with'])

base_states_df = pd.DataFrame(columns=['id', 'base_state', 'category',  'has_activity_status',
                                       'has_direction_iter', 'has_wire_travel_capacity', 'construction_state', 'has_transitions'])
