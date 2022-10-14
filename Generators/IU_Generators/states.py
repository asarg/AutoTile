from components import *
from UniversalClasses import State

class GeneratedStates:
    def __init__(self):
        self.states_dict = {} #Label: State
        self.directions = ["N", "S", "E", "W"]
        self.dWire = {"N": "🡹", "S": "🡻", "E": "🡺", "W": "🡸",
                      "NE": "🡹🡺", "NW": "🡹🡸", "SE": "🡻🡺", "SW": "🡻🡸"}
        self.wss = {"N": "↟", "S": "↡", "E": "↠", "W": "↞"}
        self.wireWriterStatesGenerate()


    def states_class1_generate(self):
        print("generated states")

    def wireWriterStatesGenerate(self):
        #Wire Writer States
        for i in range(0, 10):
            for key, value in self.dWire.items():
                l = "wireWriter{}{}".format(key, i)
                dl = "🖋{}{}".format(value, i)
                self.states_dict[l] = State(l, Air_Superiority_Blue, dl)
                l = "wireWriter{}{}Inactive".format(key, i)
                dl = "🖋{}{}ⁱ".format(value, i)
                self.states_dict[l] = State(l, Light_Steel_Blue, dl)

        print("wireWriterStatesGenerated")


### Border
border_state = State("Border", outer_space_crayola, " ", "black")

### Wires
northWire = State("NorthWire", Blue_Sapphire, "🡹")
southWire = State("SouthWire", Blue_Sapphire, "🡻")
westWire = State("WestWire", Blue_Sapphire, "🡸")
eastWire = State("EastWire", Blue_Sapphire, "🡺")

northEastWire = State("NorthEastWire", Blue_Sapphire, "🡹🡺")
northWestWire = State("NorthWestWire", Blue_Sapphire, "🡹🡸")
southEastWire = State("SouthEastWire", Blue_Sapphire, "🡻🡺")
southWestWire = State("SouthWestWire", Blue_Sapphire, "🡻🡸")

northProtectedWire = State("NorthProtectedWire", Blue_Sapphire, "|🡹|")
southProtectedWire = State("SouthProtectedWire", Blue_Sapphire, "|🡻|")
eastProtectedWire = State("EastProtectedWire", Blue_Sapphire, "|🡺|")
westProtectedWire = State("WestProtectedWire", Blue_Sapphire, "|🡸|")
northEastProtectedWire = State("NorthEastProtectedWire", Blue_Sapphire, "|🡹🡺|")
northWestProtectedWire = State("NorthWestProtectedWire", Blue_Sapphire, "|🡹🡸|")
southEastProtectedWire = State("SouthEastProtectedWire", Blue_Sapphire, "|🡻🡺|")
southWestProtectedWire = State("SouthWestProtectedWire", Blue_Sapphire, "|🡻🡸|")

protectWireWalker = State("ProtectWireWalker", Air_Superiority_Blue, "|🖋|")

northCopyWire = State("NorthCopyWire", light_blue, "⇈")
southCopyWire = State("SouthCopyWire", light_blue, "⇊")
westCopyWire = State("WestCopyWire", light_blue, "⇇")
eastCopyWire = State("EastCopyWire", light_blue, "⇉")

#wireWriterSouth_Inactive = State("WireWriterSouth_Inactive5", Air_Superiority_Blue, "5🡻ⁱ")
""" wireWriterSouth = State("WireWriterSouth5", Air_Superiority_Blue, "5🡻")
wireWriterSouth4 = State("WireWriterSouth4", Air_Superiority_Blue, "4🡻")
wireWriterSouth3 = State("WireWriterSouth3", Air_Superiority_Blue, "3🡻")
wireWriterSouth2 = State("WireWriterSouth2", Air_Superiority_Blue, "2🡻")
wireWriterSouth1 = State("WireWriterSouth1", Air_Superiority_Blue, "1🡻")
wireWriterSouth0 = State("WireWriterSouth0", Air_Superiority_Blue, "0🡻") """

### Check For Prefixes
check_equality_inactive = State("CheckEqualityInactive", grey_pink, "=", "black")
check_for_any_prefix_inactive = State("CheckForAnyPrefix", grey_pink, "=*ₚ", "black")
check_for_N_prefix_inactive = State("CheckForNPrefixInactive", grey_pink, "=Nₚ", "black")
check_for_S_prefix_inactive = State("CheckForSPrefixInactive", grey_pink, "=Sₚ", "black")
check_for_E_prefix_inactive = State("CheckForEPrefixInactive", grey_pink, "=Eₚ", "black")
check_for_W_prefix_inactive = State("CheckForWPrefixInactive", grey_pink, "=Wₚ", "black")
check_for_P_prefix_inactive = State("CheckForProgramPrefixInactive", grey_pink, "=Pₚ", "black")
check_for_C_prefix_inactive = State("CheckForCustomPrefixInactive", grey_pink, "=Cₚ", "black")

check_for_any_prefix = State("CheckForAnyPrefix", mid_pink, "=*ₚ", "black")
check_for_N_prefix = State("CheckForNPrefix", mid_pink, "=Nₚ", "black")
check_for_S_prefix = State("CheckForSPrefix", mid_pink, "=Sₚ", "black")
check_for_E_prefix = State("CheckForEPrefix", mid_pink, "=Eₚ", "black")
check_for_W_prefix = State("CheckForWPrefix", mid_pink, "=Wₚ", "black")
check_for_P_prefix = State("CheckForProgramPrefix", mid_pink, "=Pₚ", "black")
check_for_C_prefix = State("CheckForCustomPrefix", mid_pink, "=Cₚ", "black")

confirm_equal_any_prefix = State("ConfirmEqualAnyPrefix", tea_green, "=*ₚ", "black")
confirm_equal_N_prefix = State("ConfirmEqualNPrefix", tea_green, "=Nₚ", "black")
confirm_equal_S_prefix = State("ConfirmEqualSPrefix", tea_green, "=Sₚ", "black")
confirm_equal_E_prefix = State("ConfirmEqualEPrefix", tea_green, "=Eₚ", "black")
confirm_equal_W_prefix = State("ConfirmEqualWPrefix", tea_green, "=Wₚ", "black")
confirm_equal_C_prefix = State("ConfirmEqualCustomPrefix", tea_green, "=Cₚ", "black")
confirm_equal_P_prefix = State("ConfirmEqualProgramPrefix", tea_green, "=Pₚ", "black")

### Check For Caps
confirm_for_any_cap = State("ConfirmForAnyCap", tea_green, "=*₍₎", "black")
confirm_for_any_start_cap = State("ConfirmForStartCap", tea_green, "=*ᵦ₍", "black")
confirm_for_any_end_cap = State("ConfirmForEndCap", tea_green, "=*ₔ₎", "black")
confirm_for_start_state_cap = State("ConfirmForStartStateCap", tea_green, "=(ᵦ", "black")
confirm_for_end_state_cap = State("ConfirmForEndStateCap", tea_green, "=)ₔ", "black")
confirm_for_end_string_cap = State("ConfirmForEndStringCap", tea_green, "=]ₔ", "black")
confirm_for_start_string_cap = State("ConfirmForStartStringCap", tea_green, "=[ᵦ", "black")

check_for_any_cap = State("CheckForAnyCap", mid_pink, "=*₍₎", "black")
check_for_any_start_cap = State("CheckForStartCap", mid_pink, "=*ᵦ₍", "black")
check_for_any_end_cap = State("CheckForEndCap", mid_pink, "=*ₔ₎", "black")
check_for_start_state_cap = State("CheckForStartStateCap", mid_pink, "=(ᵦ", "black")
check_for_end_state_cap = State("CheckForEndStateCap", mid_pink, "=)ₔ", "black")
check_for_end_string_cap = State("CheckForEndStringCap", mid_pink, "=]ₔ", "black")
check_for_start_string_cap = State("CheckForStartStringCap", mid_pink, "=[ᵦ", "black")

check_for_any_cap_inactive = State("CheckForAnyCapInactive", grey_pink, "=*₍₎", "black")
check_for_any_start_cap_inactive = State("CheckForStartCapInactive", grey_pink, "=*ᵦ₍", "black")
check_for_any_end_cap_inactive = State("CheckForEndCapInactive", grey_pink, "=*ₔ₎", "black")
check_for_start_state_cap_inactive = State("CheckForStartStateCapInactive", grey_pink, "=(ᵦ", "black")
check_for_end_state_cap_inactive = State("CheckForEndStateCapInactive", grey_pink, "=)ₔ", "black")
check_for_start_string_cap_inactive = State("CheckForStartStringCapInactive", grey_pink, "=[ᵦ", "black")
check_for_end_string_cap_inactive = State("CheckForEndStringCapInactive", grey_pink, "=]ₔ", "black")

### Check For Num Equality
confirm_for_any_num = State("ConfirmForEqualityAnyNum", tea_green, "=*", "black")
confirm_for_equality_zero = State("ConfirmForEqualityZero", tea_green, "=0", "black")
confirm_for_equality_one = State("ConfirmForEqualityOne", tea_green, "=1", "black")
confirm_for_equality_two = State("ConfirmForEqualityTwo", tea_green, "=2", "black")
confirm_for_equality_three = State("ConfirmForEqualityThree", tea_green, "=3", "black")
confirm_for_equality_four = State("ConfirmForEqualityFour", tea_green, "=4", "black")
confirm_for_equality_five = State("ConfirmForEqualityFive", tea_green, "=5", "black")
confirm_for_equality_six = State("ConfirmEqualityForSix", tea_green, "=6", "black")
confirm_for_equality_seven = State("ConfirmForEqualitySeven", tea_green, "=7", "black")
confirm_for_equality_eight = State("ConfirmForEqualityEight", tea_green, "=8", "black")
confirm_for_equality_nine = State("ConfirmForEqualityNine", tea_green, "=9", "black")

check_for_any_num = State("CheckForEqualityAnyNum", mid_pink, "=*", "black")
check_for_equality_zero = State("CheckForEqualityZero", mid_pink, "=0", "black")
check_for_equality_one = State("CheckForEqualityOne", mid_pink, "=1", "black")
check_for_equality_two = State("CheckForEqualityTwo", mid_pink, "=2", "black")
check_for_equality_three = State("CheckForEqualityThree", mid_pink, "=3", "black")
check_for_equality_four = State("CheckForEqualityFour", mid_pink, "=4", "black")
check_for_equality_five = State("CheckForEqualityFive", mid_pink, "=5", "black")
check_for_equality_six = State("CheckEqualityForSix", mid_pink, "=6", "black")
check_for_equality_seven = State("CheckForEqualitySeven", mid_pink, "=7", "black")
check_for_equality_eight = State("CheckForEqualityEight", mid_pink, "=8", "black")
check_for_equality_nine = State("CheckForEqualityNine", mid_pink, "=9", "black")

check_for_any_num_inactive = State("CheckForEqualityAnyNum_Inactive", grey_pink, "=*", "black")
check_for_equality_zero_inactive = State("CheckForEqualityZero_Inactive", grey_pink, "=0", "black")
check_for_equality_one_inactive = State("CheckForEqualityOne_Inactive", grey_pink, "=1", "black")
check_for_equality_two_inactive = State("CheckForEqualityTwo_Inactive", grey_pink, "=2", "black")
check_for_equality_three_inactive = State("CheckForEqualityThree_Inactive", grey_pink, "=3", "black")
check_for_equality_four_inactive = State("CheckForEqualityFour_Inactive", grey_pink, "=4", "black")
check_for_equality_five_inactive = State("CheckForEqualityFive_Inactive", grey_pink, "=5", "black")
check_for_equality_six_inactive = State("CheckEqualityForSix_Inactive", grey_pink, "=6", "black")
check_for_equality_seven_inactive = State("CheckForEqualitySeven_Inactive", grey_pink, "=7", "black")
check_for_equality_eight_inactive = State("CheckForEqualityEight_Inactive", grey_pink, "=8", "black")
check_for_equality_nine_inactive = State("CheckForEqualityNine_Inactive", grey_pink, "=9", "black")

### Trap Doors
trap_door_inactive = State("TrapDoorInactive", Barn_Red, "TD", "black")
trap_door_active = State("TrapDoorActive", Barn_Red, "TD", "black")

### Copy Up
copy_up = State("CopyUp", light_blue, "⇈", "black")
copy_down = State("CopyDown", light_blue, "⇊", "black")
copy_left = State("CopyLeft", light_blue, "⇇", "black")
copy_right = State("CopyRight", light_blue, "⇉", "black")

### Data States
ds_1 = State("1", Papaya_Whip, "①")
ds_2 = State("2", Papaya_Whip, "②")
ds_3 = State("3", Papaya_Whip, "③")
ds_4 = State("4", Papaya_Whip, "④")
ds_5 = State("5", Papaya_Whip, "⑤")
ds_6 = State("6", Papaya_Whip, "⑥")
ds_7 = State("7", Papaya_Whip, "⑦")
ds_8 = State("8", Papaya_Whip, "⑧")
ds_9 = State("9", Papaya_Whip, "⑨")
ds_0 = State("0", Papaya_Whip, "⓪")

start_state = State("EndcapDSOpen", Papaya_Whip, "(", "black")
end_state = State("EndcapDSClosed", Papaya_Whip, ")", "black")

start_state_pair = State("StartStatePair", Papaya_Whip, "[", "black")
end_state_pair = State("EndStatePair", Papaya_Whip, "]", "black")

north_prefix = State("NorthPrefix", Papaya_Whip, "𝗡", "black")
south_prefix = State("SouthPrefix", Papaya_Whip, "𝗦", "black")
east_prefix = State("EastPrefix", Papaya_Whip, "𝗘", "black")
west_prefix = State("WestPrefix", Papaya_Whip, "𝗪", "black")
program_prefix = State("ProgramPrefix", Papaya_Whip, "</>", "black")
reset_prefix = State("ResetPrefix", Papaya_Whip, "⭯", "black")

### Unicode Arrows
"""
↞ : 219E,
↟ : 219F,
↠ : 21A0,
↡ : 21A1,
"""

"""
← : 2190,
↑ : 2191,
→ : 2192,
↓ : 2193,
↔ : 2194,
↕ : 2195,
↖ : 2196,
↗ : 2197,
↘ : 2198,
↙ : 2199,
↚ : 219A,
↛ : 219B,
↜ : 219C,
↝ : 219D,
↞ : 219E,
↟ : 219F,
↠ : 21A0,
↡ : 21A1,
↢ : 21A2,
↣ : 21A3,
↤ : 21A4,
↥ : 21A5,
↦ : 21A6,
↧ : 21A7,
↨ : 21A8,
↩ : 21A9,
↪ : 21AA,
↫ : 21AB,
↬ : 21AC,
↭ : 21AD,
↮ : 21AE,
↯ : 21AF,
↰ : 21B0,
↱ : 21B1,
↲ : 21B2,
↳ : 21B3,
↴ : 21B4,
↵ : 21B5,
↶ : 21B6,
↷ : 21B7,
↸ : 21B8,
↹ : 21B9,
↺ : 21BA,
↻ : 21BB,
↼ : 21BC,
↽ : 21BD,
↾ : 21BE,
↿ : 21BF,
⇀ : 21C0,
⇁ : 21C1,
⇂ : 21C2,
⇃ : 21C3,
⇄ : 21C4,
⇅ : 21C5,
⇆ : 21C6,
⇇ : 21C7,
⇈ : 21C8,
⇉ : 21C9,
⇊ : 21CA,
⇋ : 21CB,
⇌ : 21CC,
⇍ : 21CD,
⇎ : 21CE,
⇏ : 21CF,
⇐ : 21D0,
⇑ : 21D1,
⇒ : 21D2,
⇓ : 21D3,
⇔ : 21D4,
⇕ : 21D5,
⇖ : 21D6,
⇗ : 21D7,
⇘ : 21D8,
⇙ : 21D9,
⇚ : 21DA,
⇛ : 21DB,
⇜ : 21DC,
⇝ : 21DD,
⇞ : 21DE,
⇟ : 21DF,
⇠ : 21E0,
⇡ : 21E1,
⇢ : 21E2,
⇣ : 21E3,
⇤ : 21E4,
⇥ : 21E5,
⇦ : 21E6,
⇧ : 21E7,
⇨ : 21E8,
⇩ : 21E9,
⇪ : 21EA,
⇫ : 21EB,
⇬ : 21EC,
⇭ : 21ED,
⇮ : 21EE,
⇯ : 21EF,
⇰ : 21F0,
⇱ : 21F1,
⇲ : 21F2,
⇳ : 21F3,
⇴ : 21F4,
⇵ : 21F5,
⇶ : 21F6,
⇷ : 21F7,
⇸ : 21F8,
⇹ : 21F9,
⇺ : 21FA,
⇻ : 21FB,
⇼ : 21FC,
⇽ : 21FD,
⇾ : 21FE,
⇿ : 21FF,   ⤀ : 2900,  ⤁ : 2901,  ⤂ : 2902,  ⤃ : 2903,  ⤄ : 2904,  ⤅ : 2905,  ⤆ : 2906,  ⤇ : 2907,  ⤈ : 2908,  ⤉ : 2909,  ⤊ : 290A,  ⤋ : 290B,  ⤌ : 290C,  ⤍ : 290D,  ⤎ : 290E,  ⤏ : 290F,  ⤐ : 2910,  ⤑ : 2911,  ⤒ : 2912,  ⤓ : 2913,  ⤔ : 2914,  ⤕ : 2915,  ⤖ : 2916,  ⤗ : 2917,  ⤘ : 2918,  ⤙ : 2919,  ⤚ : 291A,  ⤛ : 291B,  ⤜ : 291C,  ⤝ : 291D,  ⤞ : 291E,  ⤟ : 291F,  ⤠ : 2920,  ⤡ : 2921,  ⤢ : 2922,  ⤣ : 2923,  ⤤ : 2924,  ⤥ : 2925,  ⤦ : 2926,  ⤧ : 2927,  ⤨ : 2928,  ⤩ : 2929,  ⤪ : 292A,  ⤫ : 292B,  ⤬ : 292C,  ⤭ : 292D,  ⤮ : 292E,  ⤯ : 292F,  ⤰ : 2930,  ⤱ : 2931,  ⤲ : 2932,  ⤳ : 2933,  ⤴ : 2934,  ⤵ : 2935,  ⤶ : 2936,  ⤷ : 2937,  ⤸ : 2938,  ⤹ : 2939,  ⤺ : 293A,  ⤻ : 293B,  ⤼ : 293C,  ⤽ : 293D,  ⤾ : 293E,  ⤿ : 293F,  ⥀ : 2940,  ⥁ : 2941,  ⥂ : 2942,  ⥃ : 2943,  ⥄ : 2944,  ⥅ : 2945,  ⥆ : 2946,  ⥇ : 2947,  ⥈ : 2948,  ⥉ : 2949,  ⥊ : 294A,  ⥋ : 294B,  ⥌ : 294C,  ⥍ : 294D,  ⥎ : 294E,  ⥏ : 294F,  ⥐ : 2950,  ⥑ : 2951,  ⥒ : 2952,  ⥓ : 2953,  ⥔ : 2954,  ⥕ : 2955,  ⥖ : 2956,  ⥗ : 2957,  ⥘ : 2958,  ⥙ : 2959,  ⥚ : 295A,  ⥛ : 295B,  ⥜ : 295C,  ⥝ : 295D,  ⥞ : 295E,  ⥟ : 295F,  ⥠ : 2960,  ⥡ : 2961,  ⥢ : 2962,  ⥣ : 2963,  ⥤ : 2964,  ⥥ : 2965,  ⥦ : 2966,  ⥧ : 2967,  ⥨ : 2968,  ⥩ : 2969,  ⥪ : 296A,  ⥫ : 296B,  ⥬ : 296C,  ⥭ : 296D,  ⥮ : 296E,  ⥯ : 296F,  ⥰ : 2970,  ⥱ : 2971,  ⥲ : 2972,  ⥳ : 2973,  ⥴ : 2974,  ⥵ : 2975,  ⥶ : 2976,  ⥷ : 2977,  ⥸ : 2978,  ⥹ : 2979,  ⥺ : 297A,  ⥻ : 297B,  ⥼ : 297C,  ⥽ : 297D,  ⥾ : 297E,  ⥿ : 297F,

"""
"""
    ⦀ : 2980,  ⦁ : 2981,  ⦂ : 2982,  ⦃ : 2983,  ⦄ : 2984,  ⦅ : 2985,  ⦆ : 2986,  ⦇ : 2987,  ⦈ : 2988,  ⦉ : 2989,  ⦊ : 298A,  ⦋ : 298B,  ⦌ : 298C,  ⦍ : 298D,  ⦎ : 298E,  ⦏ : 298F,  ⦐ : 2990,  ⦑ : 2991,  ⦒ : 2992,  ⦓ : 2993,  ⦔ : 2994,  ⦕ : 2995,  ⦖ : 2996,  ⦗ : 2997,  ⦘ : 2998,  ⦙ : 2999,  ⦚ : 299A,  ⦛ : 299B,  ⦜ : 299C,  ⦝ : 299D,  ⦞ : 299E,  ⦟ : 299F,  ⦠ : 29A0,  ⦡ : 29A1,  ⦢ : 29A2,  ⦣ : 29A3,  ⦤ : 29A4,  ⦥ : 29A5,  ⦦ : 29A6,  ⦧ : 29A7,  ⦨ : 29A8,  ⦩ : 29A9,  ⦪ : 29AA,  ⦫ : 29AB,  ⦬ : 29AC,  ⦭ : 29AD,  ⦮ : 29AE,  ⦯ : 29AF,  ⦰ : 29B0,  ⦱ : 29B1,  ⦲ : 29B2,  ⦳ : 29B3,  ⦴ : 29B4,  ⦵ : 29B5,  ⦶ : 29B6,  ⦷ : 29B7,  ⦸ : 29B8,  ⦹ : 29B9,  ⦺ : 29BA,  ⦻ : 29BB,  ⦼ : 29BC,  ⦽ : 29BD,  ⦾ : 29BE,  ⦿ : 29BF,  ⧀ : 29C0,  ⧁ : 29C1,  ⧂ : 29C2,  ⧃ : 29C3,  ⧄ : 29C4,  ⧅ : 29C5,  ⧆ : 29C6,  ⧇ : 29C7,  ⧈ : 29C8,  ⧉ : 29C9,  ⧊ : 29CA,  ⧋ : 29CB,  ⧌ : 29CC,  ⧍ : 29CD,  ⧎ : 29CE,  ⧏ : 29CF,  ⧐ : 29D0,  ⧑ : 29D1,  ⧒ : 29D2,  ⧓ : 29D3,  ⧔ : 29D4,  ⧕ : 29D5,  ⧖ : 29D6,  ⧗ : 29D7,  ⧘ : 29D8,  ⧙ : 29D9,  ⧚ : 29DA,  ⧛ : 29DB,  ⧜ : 29DC,  ⧝ : 29DD,  ⧞ : 29DE,  ⧟ : 29DF,  ⧠ : 29E0,  ⧡ : 29E1,  ⧢ : 29E2,  ⧣ : 29E3,  ⧤ : 29E4,  ⧥ : 29E5,  ⧦ : 29E6,  ⧧ : 29E7,  ⧨ : 29E8,  ⧩ : 29E9,  ⧪ : 29EA,  ⧫ : 29EB,  ⧬ : 29EC,  ⧭ : 29ED,  ⧮ : 29EE,  ⧯ : 29EF,  ⧰ : 29F0,  ⧱ : 29F1,  ⧲ : 29F2,  ⧳ : 29F3,  ⧴ : 29F4,  ⧵ : 29F5,  ⧶ : 29F6,  ⧷ : 29F7,  ⧸ : 29F8,  ⧹ : 29F9,  ⧺ : 29FA,  ⧻ : 29FB,  ⧼ : 29FC,  ⧽ : 29FD,  ⧾ : 29FE,  ⧿ : 29FF,
"""

"""
🠀 : 1F800,  🠁 : 1F801,  🠂 : 1F802,  🠃 : 1F803,  🠄 : 1F804,  🠅 : 1F805,  🠆 : 1F806,  🠇 : 1F807,  🠈 : 1F808,  🠉 : 1F809,  🠊 : 1F80A,  🠋 : 1F80B,  🠌 : 1F80C,  🠍 : 1F80D,  🠎 : 1F80E,  🠏 : 1F80F,  🠐 : 1F810,  🠑 : 1F811,  🠒 : 1F812,  🠓 : 1F813,  🠔 : 1F814,  🠕 : 1F815,  🠖 : 1F816,  🠗 : 1F817,  🠘 : 1F818,  🠙 : 1F819,  🠚 : 1F81A,  🠛 : 1F81B,  🠜 : 1F81C,  🠝 : 1F81D,  🠞 : 1F81E,  🠟 : 1F81F,  🠠 : 1F820,  🠡 : 1F821,  🠢 : 1F822,  🠣 : 1F823,  🠤 : 1F824,  🠥 : 1F825,  🠦 :
1F826,  🠧 : 1F827,  🠨 : 1F828,  🠩 : 1F829,  🠪 : 1F82A,  🠫 : 1F82B,  🠬 : 1F82C,  🠭 : 1F82D,  🠮 : 1F82E,  🠯 : 1F82F,  🠰 : 1F830,  🠱 : 1F831,  🠲 : 1F832,  🠳 : 1F833,  🠴 : 1F834,  🠵 : 1F835,  🠶 : 1F836,  🠷 : 1F837,  🠸 : 1F838,  🠹 : 1F839,  🠺 : 1F83A,  🠻 : 1F83B,  🠼 : 1F83C,  🠽 : 1F83D,  🠾 : 1F83E,  🠿 : 1F83F,  🡀 : 1F840,  🡁 : 1F841,  🡂 : 1F842,  🡃 : 1F843,  🡄 : 1F844,  🡅 : 1F845,  🡆 : 1F846,  🡇 : 1F847,  🡈 : 1F848,  🡉 : 1F849,  🡊 : 1F84A,  🡋 : 1F84B,  🡌 : 1F84C,
🡍 : 1F84D,  🡎 : 1F84E,  🡏 : 1F84F,  🡐 : 1F850,  🡑 : 1F851,  🡒 : 1F852,  🡓 : 1F853,  🡔 : 1F854,  🡕 : 1F855,  🡖 : 1F856,  🡗 : 1F857,  🡘 : 1F858,  🡙 : 1F859,  🡚 : 1F85A,  🡛 : 1F85B,  🡜 : 1F85C,  🡝 : 1F85D,  🡞 : 1F85E,  🡟 : 1F85F,  🡠 : 1F860,  🡡 : 1F861,  🡢 : 1F862,  🡣 : 1F863,  🡤 : 1F864,  🡥 : 1F865,  🡦 : 1F866,  🡧 : 1F867,  🡨 : 1F868,  🡩 : 1F869,  🡪 : 1F86A,  🡫 : 1F86B,  🡬 : 1F86C,  🡭 : 1F86D,  🡮 : 1F86E,  🡯 : 1F86F,  🡰 : 1F870,  🡱 : 1F871,  🡲 : 1F872,  🡳 :
1F873,  🡴 : 1F874,  🡵 : 1F875,  🡶 : 1F876,  🡷 : 1F877,  🡸 : 1F878,  🡹 : 1F879,  🡺 : 1F87A,  🡻 : 1F87B,  🡼 : 1F87C,  🡽 : 1F87D,  🡾 : 1F87E,  🡿 : 1F87F,  🢀 : 1F880,  🢁 : 1F881,  🢂 : 1F882,  🢃 : 1F883,  🢄 : 1F884,  🢅 : 1F885,  🢆 : 1F886,  🢇 : 1F887,    🢐 : 1F890,  🢑 : 1F891,  🢒 : 1F892,  🢓 : 1F893,  🢔 : 1F894,  🢕 : 1F895,  🢖 : 1F896,  🢗 : 1F897,  🢘 : 1F898,  🢙 : 1F899,  🢚 : 1F89A,  🢛 : 1F89B,  🢜 : 1F89C,  🢝 : 1F89D,  🢞 : 1F89E,  🢟 : 1F89F,  🢠 : 1F8A0,  🢡 :
1F8A1,  🢢 : 1F8A2,  🢣 : 1F8A3,  🢤 : 1F8A4,  🢥 : 1F8A5,  🢦 : 1F8A6,  🢧 : 1F8A7,  🢨 : 1F8A8,  🢩 : 1F8A9,  🢪 : 1F8AA,  🢫 : 1F8AB,  🢬 : 1F8AC,  🢭 : 1F8AD,

 """

"""

"""
### Curving Arrows ⤶
