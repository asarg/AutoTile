from generators import genSqrtBinCount
import UniversalClasses as uc
import SaveFile

import math

red = "f03a47"
blue = "3f88c5"
green = "0ead69"
orange = "f39237"
black = "323031"
white = "DFE0E2"


def genQuadIndexStates(vLen):
    rt4Len = math.ceil(vLen**(1.0/4.0))

    seedA = uc.State("SA", black)
    genSys = uc.System(1, [], [], [seedA], [], [], [], [])

    # Seed States
    genSys.add_State(seedA)
    #     seedB is an Initial State
    seedB = uc.State("SB", black)
    genSys.add_Initial_State(seedB)
    genSys.add_State(seedB)
    #     seedC is an Initial State
    seedC = uc.State("SC", black)
    genSys.add_Initial_State(seedC)
    genSys.add_State(seedC)
    #     seedD is an Initial State
    seedD = uc.State("SD", black)
    genSys.add_Initial_State(seedD)
    genSys.add_State(seedD)

    # Blank A and A' states
    singleA = uc.State("A", red)
    genSys.add_State(singleA)
    singleAPrime = uc.State("A'", red)
    genSys.add_State(singleAPrime)
    # Blank B and B' states
    singleB = uc.State("B", blue)
    genSys.add_State(singleB)
    BPrime = uc.State("B'", blue)
    genSys.add_State(BPrime)
    BPrime2 = uc.State("B''", blue)
    genSys.add_State(BPrime2)
    # Blank C and C' states
    singleC = uc.State("C", orange)
    genSys.add_State(singleC)
    singleCPrime = uc.State("C'", orange)
    genSys.add_State(singleCPrime)

    # Small Letter States
    for i in range(2 * rt4Len):
        # Little a states (Initial States)
        aState = uc.State(str(i) + "a", red)
        genSys.add_State(aState)
        genSys.add_Initial_State(aState)
        # Little b states (Initial States)
        bState = uc.State(str(i) + "b", blue)
        genSys.add_State(bState)
        genSys.add_Initial_State(bState)
        # Little b states (Initial States)
        cState = uc.State(str(i) + "c", orange)
        genSys.add_State(cState)
        genSys.add_Initial_State(cState)
    # Large Letter States
    for i in range(rt4Len):
        # Big A states
        bigAState = uc.State(str(i) + "A", red)
        genSys.add_State(bigAState)
        # Base A states
        southAState = uc.State(str(i) + "As", red)
        genSys.add_State(southAState)
        # A' (prime) states
        bigAPrime = uc.State(str(i) + "A'", red)
        genSys.add_State(bigAPrime)
        # Big B states
        bigBState = uc.State(str(i) + "B", blue)
        genSys.add_State(bigBState)
        # Base B states
        southBState = uc.State(str(i) + "Bs", blue)
        genSys.add_State(southBState)
        # B prime states
        Bprime = uc.State(str(i) + "B'", blue)
        genSys.add_State(Bprime)
        Bprime2 = uc.State(str(i) + "B''", blue)
        genSys.add_State(Bprime2)
        # C states (Initial States)
        cState = uc.State(str(i) + "C", orange)
        genSys.add_State(cState)
        # Base C states
        southCState = uc.State(str(i) + "Cs", orange)
        genSys.add_State(southCState)
        # C prime states
        Cprime = uc.State(str(i) + "C'", orange)
        genSys.add_State(Cprime)
        # D states (Initial States)
        dState = uc.State(str(i) + "D", green)
        genSys.add_State(dState)
        genSys.add_Initial_State(dState)
        # Base D states
        southDState = uc.State(str(i) + "Ds", green)
        genSys.add_State(southDState)
        genSys.add_Initial_State(southDState)

    # Little a prime state
    aPrime = uc.State(str((2 * rt4Len) - 1) + "a'", red)
    genSys.add_State(aPrime)
    # Little b prime state
    bPrime = uc.State(str((2 * rt4Len) - 1) + "b'", blue)
    genSys.add_State(bPrime)

    ### Affinity Rules
    #       Seed Affinities to start building
    affinityA0 = uc.AffinityRule("0a", "SA", "v", 1)
    genSys.add_affinity(affinityA0)
    affinityB0 = uc.AffinityRule("0b", "SB", "v", 1)
    genSys.add_affinity(affinityB0)
    affinityC0 = uc.AffinityRule("0c", "SC", "v", 1)
    genSys.add_affinity(affinityC0)
    affinityD0 = uc.AffinityRule("0Ds", "SD", "v", 1)
    genSys.add_affinity(affinityD0)
    affinitySeed = uc.AffinityRule("SA", "SB", "h", 1)
    genSys.add_affinity(affinitySeed)
    affinitySeed2 = uc.AffinityRule("SB", "SC", "h", 1)
    genSys.add_affinity(affinitySeed2)
    affinitySeed3 = uc.AffinityRule("SC", "SD", "h", 1)
    genSys.add_affinity(affinitySeed3)

    for i in range((2 * rt4Len) - 1):
        # Affinity Rules to build each column
        affA = uc.AffinityRule(str(i + 1) + "a", str(i) + "a", "v", 1)
        genSys.add_affinity(affA)
        affB = uc.AffinityRule(str(i + 1) + "b", str(i) + "b", "v", 1)
        genSys.add_affinity(affB)
        affC = uc.AffinityRule(str(i + 1) + "c", str(i) + "c", "v", 1)
        genSys.add_affinity(affC)

    for i in range(rt4Len - 1):
        affD = uc.AffinityRule(str(i) + "D", str(i) + "Ds", "v", 1)
        genSys.add_affinity(affD)
        affDs = uc.AffinityRule(str(i + 1) + "Ds", str(i) + "D", "v", 1)
        genSys.add_affinity(affDs)

        # Affinity Rule to start the next section of the A and B column
        affGrowA = uc.AffinityRule("0a", str(i) + "A'", "v", 1)
        genSys.add_affinity(affGrowA)
        affGrowB = uc.AffinityRule("0b", str(i) + "B'", "v", 1)
        genSys.add_affinity(affGrowB)
        affGrowC = uc.AffinityRule("0c", str(i) + "C'", "v", 1)
        genSys.add_affinity(affGrowC)

    affLD = uc.AffinityRule(str(rt4Len - 1) + "D", str(rt4Len - 1) + "Ds", "v", 1)
    genSys.add_affinity(affLD)

    ### Transitions
    # Transition once the C and D column are complete
    trCTop = uc.TransitionRule(str((2 * rt4Len) - 1) + "c", str(rt4Len - 1) + "D", "C'", str(rt4Len - 1) + "D", "h")
    genSys.add_transition_rule(trCTop)

    # Rule for starting propagation of A state
    AprimeProp = uc.TransitionRule(
        "A'", str((2 * rt4Len) - 2) + "a", "A'", "A", "v")
    genSys.add_transition_rule(AprimeProp)
    BprimeProp = uc.TransitionRule(
        "B'", str((2 * rt4Len) - 2) + "b", "B'", "B", "v")
    genSys.add_transition_rule(BprimeProp)
    CprimeProp = uc.TransitionRule(
        "C'", str((2 * rt4Len) - 2) + "c", "C'", "C", "v")
    genSys.add_transition_rule(CprimeProp)

    for i in range(2 * rt4Len - 1):
        # Rule for continued propagation of A state downward
        Aprop = uc.TransitionRule("A", str(i) + "a", "A", "A", "v")
        genSys.add_transition_rule(Aprop)
        Bprop = uc.TransitionRule("B", str(i) + "b", "B", "B", "v")
        genSys.add_transition_rule(Bprop)
        Cprop = uc.TransitionRule("C", str(i) + "c", "C", "C", "v")
        genSys.add_transition_rule(Cprop)


    # Rule for when A/B state reaches seed or last B' and marked as 0As/0Bs
    trAseed = uc.TransitionRule("A", "SA", "0As", "SA", "v")
    genSys.add_transition_rule(trAseed)
    trBseed = uc.TransitionRule("B", "SB", "0Bs", "SB", "v")
    genSys.add_transition_rule(trBseed)
    trCseed = uc.TransitionRule("C", "SC", "0Cs", "SC", "v")
    genSys.add_transition_rule(trCseed)

    for i in range(rt4Len):
      
        # Rules for propagating the A index upward
        propUpA = uc.TransitionRule(
            "A", str(i) + "A", str(i) + "As", str(i) + "A", "v")
        genSys.add_transition_rule(propUpA)
        propUpAs = uc.TransitionRule(
            "A", str(i) + "As", str(i) + "A", str(i) + "As", "v")
        genSys.add_transition_rule(propUpAs)
        propUpPrimeA = uc.TransitionRule(
            "A'", str(i) + "As", str(i) + "A'", str(i) + "As", "v")
        genSys.add_transition_rule(propUpPrimeA)

        propUpB = uc.TransitionRule(
            "B", str(i) + "B", str(i) + "Bs", str(i) + "B", "v")
        genSys.add_transition_rule(propUpB)
        propUpBs = uc.TransitionRule(
            "B", str(i) + "Bs", str(i) + "B", str(i) + "Bs", "v")
        genSys.add_transition_rule(propUpBs)
        propUpPrimeB = uc.TransitionRule(
            "B'", str(i) + "Bs", str(i) + "B'", str(i) + "Bs", "v")
        genSys.add_transition_rule(propUpPrimeB)

        propUpC = uc.TransitionRule(
            "C", str(i) + "C", str(i) + "Cs", str(i) + "C", "v")
        genSys.add_transition_rule(propUpC)
        propUpCs = uc.TransitionRule(
            "C", str(i) + "Cs", str(i) + "C", str(i) + "Cs", "v")
        genSys.add_transition_rule(propUpCs)
        propUpPrimeC = uc.TransitionRule(
            "C'", str(i) + "Cs", str(i) + "C'", str(i) + "Cs", "v")
        genSys.add_transition_rule(propUpPrimeC)

        # Once the B index reaches the top transition the a and b columns
        trBC = uc.TransitionRule(str(2 * rt4Len - 1) + "b", str(i) + "C'", str(2 * rt4Len - 1) + "b'", str(i) + "C'", "h")
        genSys.add_transition_rule(trBC)
        trAB = uc.TransitionRule(str(2 * rt4Len - 1) + "a", str(2 * rt4Len - 1) + "b'", str(2 * rt4Len - 1) + "a'", str(2 * rt4Len - 1) + "b'", "h")
        genSys.add_transition_rule(trAB)

    return genSys



if __name__ == "__main__":
    sys = genQuadIndexStates(81)
    SaveFile.main(sys, ["quadTest.xml"])

