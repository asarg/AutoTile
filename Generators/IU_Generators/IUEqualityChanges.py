import UniversalClasses as uc
from components import *
import sys


class IUGenerators:
    all_states = []
    all_aff = []
    all_tr = []
    all_sys = {}

    def __init__(self, exampleSysName=""):
        self.exampleSysName = exampleSysName
        self.genSys = None

        self.example_states_data = [north_prefix, start_state, ds_1, ds_2, ds_5, end_state]
        self.aff_list = []

    def basicWireSeedAssembly(self):
        seed_states = [westWire]
        seed_tiles = []
        c = 4
        for i in self.example_states_data:
            seed_states.append(i)
            temp_tile = uc.Tile(i, c, 0)
            seed_tiles.append(temp_tile)
            c = c + 1

        for i in range(4):
            temp_tile = uc.Tile(westWire, i, 0)
            seed_tiles.append(temp_tile)

        asb = uc.Assembly()
        asb.setTilesFromList(seed_tiles)
        return asb, seed_states, seed_tiles

    def basicWireGenerator(self):
        asb, seed_states, seed_tiles = self.basicWireSeedAssembly()

        #System takes in temp, states, initial states, seed states, vertical_affinitys, horizontal_affinitys, vert transitions, horiz transitions, tile vertical transitions, tile horizontal transitions, seed assembly
        self.genSys = uc.System(1, seed_states, [], seed_states,  [], [], [], [], [], [], asb)

        for i in self.example_states_data:
            aff = uc.AffinityRule(westWire.label, i.label, "h", 1)
            self.all_aff.append(aff)
            self.genSys.addAffinity(aff)
            aff = uc.AffinityRule(i.label, westWire.label, "h", 1)
            self.genSys.addAffinity(aff)
            self.all_aff.append(aff)
            tr = uc.TransitionRule(westWire.label, i.label, i.label, westWire.label, "h")
            self.genSys.addTransitionRule(tr)
            self.all_tr.append(tr)

        aff = uc.AffinityRule(westWire.label, westWire.label, "h", 1)
        self.genSys.addAffinity(aff)
        self.all_aff.append(aff)
        self.all_sys["basicWire"] = self.genSys

        return self.genSys





### Border
border_state = uc.State("Border", outer_space_crayola, " ", "black")

### Wires
northWire = uc.State("NorthWire", Blue_Sapphire, "🡹")
southWire = uc.State("SouthWire", Blue_Sapphire, "🡻")
westWire = uc.State("WestWire", Blue_Sapphire, "🡸")
eastWire = uc.State("EastWire", Blue_Sapphire, "🡺")

northCopyWire = uc.State("NorthCopyWire", light_blue, "⇈")
southCopyWire = uc.State("SouthCopyWire", light_blue, "⇊")
westCopyWire = uc.State("WestCopyWire", light_blue, "⇇")
eastCopyWire = uc.State("EastCopyWire", light_blue, "⇉")

wireWriterSouth_Inactive = uc.State("WireWriterSouth_Inactive5", Air_Superiority_Blue, "5🡻ⁱ")
wireWriterSouth = uc.State("WireWriterSouth5", Air_Superiority_Blue, "5🡻")
wireWriterSouth4 = uc.State("WireWriterSouth4", Air_Superiority_Blue, "4🡻")
wireWriterSouth3 = uc.State("WireWriterSouth3", Air_Superiority_Blue, "3🡻")
wireWriterSouth2 = uc.State("WireWriterSouth2", Air_Superiority_Blue, "2🡻")
wireWriterSouth1 = uc.State("WireWriterSouth1", Air_Superiority_Blue, "1🡻")
wireWriterSouth0 = uc.State("WireWriterSouth0", Air_Superiority_Blue, "0🡻")

### Check For Prefixes
check_equality_inactive = uc.State("CheckEqualityInactive", grey_pink, "=", "black")
check_for_any_prefix_inactive = uc.State("CheckForAnyPrefix", grey_pink, "=*ₚ", "black")
check_for_N_prefix_inactive = uc.State("CheckForNPrefixInactive", grey_pink, "=Nₚ", "black")
check_for_S_prefix_inactive = uc.State("CheckForSPrefixInactive", grey_pink, "=Sₚ", "black")
check_for_E_prefix_inactive = uc.State("CheckForEPrefixInactive", grey_pink, "=Eₚ", "black")
check_for_W_prefix_inactive = uc.State("CheckForWPrefixInactive", grey_pink, "=Wₚ", "black")
check_for_P_prefix_inactive = uc.State("CheckForProgramPrefixInactive", grey_pink, "=Pₚ", "black")
check_for_C_prefix_inactive = uc.State("CheckForCustomPrefixInactive", grey_pink, "=Cₚ", "black")

check_for_any_prefix = uc.State("CheckForAnyPrefix", mid_pink, "=*ₚ", "black")
check_for_N_prefix = uc.State("CheckForNPrefix", mid_pink, "=Nₚ", "black")
check_for_S_prefix = uc.State("CheckForSPrefix", mid_pink, "=Sₚ", "black")
check_for_E_prefix = uc.State("CheckForEPrefix", mid_pink, "=Eₚ", "black")
check_for_W_prefix = uc.State("CheckForWPrefix", mid_pink, "=Wₚ", "black")
check_for_P_prefix = uc.State("CheckForProgramPrefix", mid_pink, "=Pₚ", "black")
check_for_C_prefix = uc.State("CheckForCustomPrefix", mid_pink, "=Cₚ", "black")

confirm_equal_any_prefix = uc.State("ConfirmEqualAnyPrefix", tea_green, "=*ₚ", "black")
confirm_equal_N_prefix = uc.State("ConfirmEqualNPrefix", tea_green, "=Nₚ", "black")
confirm_equal_S_prefix = uc.State("ConfirmEqualSPrefix", tea_green, "=Sₚ", "black")
confirm_equal_E_prefix = uc.State("ConfirmEqualEPrefix", tea_green, "=Eₚ", "black")
confirm_equal_W_prefix = uc.State("ConfirmEqualWPrefix", tea_green, "=Wₚ", "black")
confirm_equal_C_prefix = uc.State("ConfirmEqualCustomPrefix", tea_green, "=Cₚ", "black")
confirm_equal_P_prefix = uc.State("ConfirmEqualProgramPrefix", tea_green, "=Pₚ", "black")

### Check For Caps
confirm_for_any_cap = uc.State("ConfirmForAnyCap", tea_green, "=*₍₎", "black")
confirm_for_any_start_cap = uc.State("ConfirmForStartCap", tea_green, "=*ᵦ₍", "black")
confirm_for_any_end_cap = uc.State("ConfirmForEndCap", tea_green, "=*ₔ₎", "black")
confirm_for_start_state_cap = uc.State("ConfirmForStartStateCap", tea_green, "=(ᵦ", "black")
confirm_for_end_state_cap = uc.State("ConfirmForEndStateCap", tea_green, "=)ₔ", "black")
confirm_for_end_string_cap = uc.State("ConfirmForEndStringCap", tea_green, "=]ₔ", "black")
confirm_for_start_string_cap = uc.State("ConfirmForStartStringCap", tea_green, "=[ᵦ", "black")

check_for_any_cap = uc.State("CheckForAnyCap", mid_pink, "=*₍₎", "black")
check_for_any_start_cap = uc.State("CheckForStartCap", mid_pink, "=*ᵦ₍", "black")
check_for_any_end_cap = uc.State("CheckForEndCap", mid_pink, "=*ₔ₎", "black")
check_for_start_state_cap = uc.State("CheckForStartStateCap", mid_pink, "=(ᵦ", "black")
check_for_end_state_cap = uc.State("CheckForEndStateCap", mid_pink, "=)ₔ", "black")
check_for_end_string_cap = uc.State("CheckForEndStringCap", mid_pink, "=]ₔ", "black")
check_for_start_string_cap = uc.State("CheckForStartStringCap", mid_pink, "=[ᵦ", "black")

check_for_any_cap_inactive = uc.State("CheckForAnyCapInactive", grey_pink, "=*₍₎", "black")
check_for_any_start_cap_inactive = uc.State("CheckForStartCapInactive", grey_pink, "=*ᵦ₍", "black")
check_for_any_end_cap_inactive = uc.State("CheckForEndCapInactive", grey_pink, "=*ₔ₎", "black")
check_for_start_state_cap_inactive = uc.State("CheckForStartStateCapInactive", grey_pink, "=(ᵦ", "black")
check_for_end_state_cap_inactive = uc.State("CheckForEndStateCapInactive", grey_pink, "=)ₔ", "black")
check_for_start_string_cap_inactive = uc.State("CheckForStartStringCapInactive", grey_pink, "=[ᵦ", "black")
check_for_end_string_cap_inactive = uc.State("CheckForEndStringCapInactive", grey_pink, "=]ₔ", "black")

### Check For Num Equality
confirm_for_any_num = uc.State("ConfirmForEqualityAnyNum", tea_green, "=*", "black")
confirm_for_equality_zero = uc.State("ConfirmForEqualityZero", tea_green, "=0", "black")
confirm_for_equality_one = uc.State("ConfirmForEqualityOne", tea_green, "=1", "black")
confirm_for_equality_two = uc.State("ConfirmForEqualityTwo", tea_green, "=2", "black")
confirm_for_equality_three = uc.State("ConfirmForEqualityThree", tea_green, "=3", "black")
confirm_for_equality_four = uc.State("ConfirmForEqualityFour", tea_green, "=4", "black")
confirm_for_equality_five = uc.State("ConfirmForEqualityFive", tea_green, "=5", "black")
confirm_for_equality_six = uc.State("ConfirmEqualityForSix", tea_green, "=6", "black")
confirm_for_equality_seven = uc.State("ConfirmForEqualitySeven", tea_green, "=7", "black")
confirm_for_equality_eight = uc.State("ConfirmForEqualityEight", tea_green, "=8", "black")
confirm_for_equality_nine = uc.State("ConfirmForEqualityNine", tea_green, "=9", "black")

check_for_any_num = uc.State("CheckForEqualityAnyNum", mid_pink, "=*", "black")
check_for_equality_zero = uc.State("CheckForEqualityZero", mid_pink, "=0", "black")
check_for_equality_one = uc.State("CheckForEqualityOne", mid_pink, "=1", "black")
check_for_equality_two = uc.State("CheckForEqualityTwo", mid_pink, "=2", "black")
check_for_equality_three = uc.State("CheckForEqualityThree", mid_pink, "=3", "black")
check_for_equality_four = uc.State("CheckForEqualityFour", mid_pink, "=4", "black")
check_for_equality_five = uc.State("CheckForEqualityFive", mid_pink, "=5", "black")
check_for_equality_six = uc.State("CheckEqualityForSix", mid_pink, "=6", "black")
check_for_equality_seven = uc.State("CheckForEqualitySeven", mid_pink, "=7", "black")
check_for_equality_eight = uc.State("CheckForEqualityEight", mid_pink, "=8", "black")
check_for_equality_nine = uc.State("CheckForEqualityNine", mid_pink, "=9", "black")

check_for_any_num_inactive = uc.State("CheckForEqualityAnyNum_Inactive", grey_pink, "=*", "black")
check_for_equality_zero_inactive = uc.State("CheckForEqualityZero_Inactive", grey_pink, "=0", "black")
check_for_equality_one_inactive = uc.State("CheckForEqualityOne_Inactive", grey_pink, "=1", "black")
check_for_equality_two_inactive = uc.State("CheckForEqualityTwo_Inactive", grey_pink, "=2", "black")
check_for_equality_three_inactive = uc.State("CheckForEqualityThree_Inactive", grey_pink, "=3", "black")
check_for_equality_four_inactive = uc.State("CheckForEqualityFour_Inactive", grey_pink, "=4", "black")
check_for_equality_five_inactive = uc.State("CheckForEqualityFive_Inactive", grey_pink, "=5", "black")
check_for_equality_six_inactive = uc.State("CheckEqualityForSix_Inactive", grey_pink, "=6", "black")
check_for_equality_seven_inactive = uc.State("CheckForEqualitySeven_Inactive", grey_pink, "=7", "black")
check_for_equality_eight_inactive = uc.State("CheckForEqualityEight_Inactive", grey_pink, "=8", "black")
check_for_equality_nine_inactive = uc.State("CheckForEqualityNine_Inactive", grey_pink, "=9", "black")

### Trap Doors
trap_door_inactive = uc.State("TrapDoorInactive", Barn_Red, "TD", "black")
### Data States
ds_1 = uc.State("1", Papaya_Whip, "①")
ds_2 = uc.State("2", Papaya_Whip, "②")
ds_3 = uc.State("3", Papaya_Whip, "③")
ds_4 = uc.State("4", Papaya_Whip, "④")
ds_5 = uc.State("5", Papaya_Whip, "⑤")
ds_6 = uc.State("6", Papaya_Whip, "⑥")
ds_7 = uc.State("7", Papaya_Whip, "⑦")
ds_8 = uc.State("8", Papaya_Whip, "⑧")
ds_9 = uc.State("9", Papaya_Whip, "⑨")
ds_0 = uc.State("0", Papaya_Whip, "⓪")
data_states_list_nums_only = [ds_0, ds_1, ds_2, ds_3, ds_4, ds_5, ds_6, ds_7, ds_8, ds_9]

start_state = uc.State("EndcapDSOpen", Papaya_Whip, "(", "black")
end_state = uc.State("EndcapDSClosed", Papaya_Whip, ")", "black")
data_states_list_all = [start_state] + data_states_list_nums_only + [end_state]

north_prefix = uc.State("NorthPrefix", Papaya_Whip, "𝗡", "black")
south_prefix = uc.State("SouthPrefix", Papaya_Whip, "𝗦", "black")
east_prefix = uc.State("EastPrefix", Papaya_Whip, "𝗘", "black")
west_prefix = uc.State("WestPrefix", Papaya_Whip, "𝗪", "black")
program_prefix = uc.State("ProgramPrefix", Papaya_Whip, "</>", "black")
reset_prefix = uc.State("ResetPrefix", Papaya_Whip, "⭯", "black")

data_states_list_prefixes = [north_prefix, south_prefix, east_prefix, west_prefix, program_prefix, reset_prefix]
data_states_list_all_with_prefixes_no_order = data_states_list_prefixes + \
    data_states_list_all
data_states_list_all_with_north_prefixes = [
    north_prefix] + data_states_list_all
