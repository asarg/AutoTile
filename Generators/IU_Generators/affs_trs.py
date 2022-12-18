
from UniversalClasses import AffinityRule
from binaryStates import *

AffinityRule(ds_1.label, signal_door_inactive_east.label, "h", 1)
AffinityRule(ds_1.label, signal_door_find_corner_north.label, "h", 1)
AffinityRule(ds_1.label,signal_door_find_corner_south.label, "h", 1)
AffinityRule(ds_1.label, signal_door_active_waiting_east.label, "h", 1)
AffinityRule(ds_1.label, signal_door_pass_accept_north.label, "h", 1)
AffinityRule(ds_1.label, signal_door_pass_accept_south.label, "h", 1)
