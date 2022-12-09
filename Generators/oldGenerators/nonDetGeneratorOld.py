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
    genSys.addState(seedA)
    #     seedB is an Initial State
    seedB = uc.State("SB", black)
    genSys.addInitialState(seedB)
    genSys.addState(seedB)
    #     seedC is an Initial State
    seedC = uc.State("SC", black)
    genSys.addInitialState(seedC)
    genSys.addState(seedC)
    #     seedD is an Initial State
    seedD = uc.State("SD", black)
    genSys.addInitialState(seedD)
    genSys.addState(seedD)

    # Blank A and A' states
    singleA = uc.State("A", red)
    genSys.addState(singleA)
    singleAPrime = uc.State("A'", red)
    genSys.addState(singleAPrime)
    # Blank B and B' states
    singleB = uc.State("B", blue)
    genSys.addState(singleB)
    BPrime = uc.State("B'", blue)
    genSys.addState(BPrime)
    BPrime2 = uc.State("B''", blue)
    genSys.addState(BPrime2)
    # Blank C and C' states
    singleC = uc.State("C", orange)
    genSys.addState(singleC)
    singleCPrime = uc.State("C'", orange)
    genSys.addState(singleCPrime)

    # Small Letter States
    for i in range(2 * rt4Len):
        # Little a states (Initial States)
        aState = uc.State(str(i) + "a", red)
        genSys.addState(aState)
        genSys.addInitialState(aState)
        # Little b states (Initial States)
        bState = uc.State(str(i) + "b", blue)
        genSys.addState(bState)
        genSys.addInitialState(bState)
        # Little b states (Initial States)
        cState = uc.State(str(i) + "c", orange)
        genSys.addState(cState)
        genSys.addInitialState(cState)
    # Large Letter States
    for i in range(rt4Len):
        # Big A states
        bigAState = uc.State(str(i) + "A", red)
        genSys.addState(bigAState)
        # Base A states
        southAState = uc.State(str(i) + "As", red)
        genSys.addState(southAState)
        # A' (prime) states
        bigAPrime = uc.State(str(i) + "A'", red)
        genSys.addState(bigAPrime)
        # Big B states
        bigBState = uc.State(str(i) + "B", blue)
        genSys.addState(bigBState)
        # Base B states
        southBState = uc.State(str(i) + "Bs", blue)
        genSys.addState(southBState)
        # B prime states
        Bprime = uc.State(str(i) + "B'", blue)
        genSys.addState(Bprime)
        Bprime2 = uc.State(str(i) + "B''", blue)
        genSys.addState(Bprime2)
        # C states (Initial States)
        cState = uc.State(str(i) + "C", orange)
        genSys.addState(cState)
        # Base C states
        southCState = uc.State(str(i) + "Cs", orange)
        genSys.addState(southCState)
        # C prime states
        Cprime = uc.State(str(i) + "C'", orange)
        genSys.addState(Cprime)
        # D states (Initial States)
        dState = uc.State(str(i) + "D", green)
        genSys.addState(dState)
        genSys.addInitialState(dState)
        # Base D states
        southDState = uc.State(str(i) + "Ds", green)
        genSys.addState(southDState)
        genSys.addInitialState(southDState)

    # Little a prime state
    aPrime = uc.State(str((2 * rt4Len) - 1) + "a'", red)
    genSys.addState(aPrime)
    # Little b prime state
    bPrime = uc.State(str((2 * rt4Len) - 1) + "b'", blue)
    genSys.addState(bPrime)

    ### Affinity Rules
    #       Seed Affinities to start building
    affinityA0 = uc.AffinityRule("0a", "SA", "v", 1)
    genSys.addAffinity(affinityA0)
    affinityB0 = uc.AffinityRule("0b", "SB", "v", 1)
    genSys.addAffinity(affinityB0)
    affinityC0 = uc.AffinityRule("0c", "SC", "v", 1)
    genSys.addAffinity(affinityC0)
    affinityD0 = uc.AffinityRule("0Ds", "SD", "v", 1)
    genSys.addAffinity(affinityD0)
    affinitySeed = uc.AffinityRule("SA", "SB", "h", 1)
    genSys.addAffinity(affinitySeed)
    affinitySeed2 = uc.AffinityRule("SB", "SC", "h", 1)
    genSys.addAffinity(affinitySeed2)
    affinitySeed3 = uc.AffinityRule("SC", "SD", "h", 1)
    genSys.addAffinity(affinitySeed3)

    for i in range((2 * rt4Len) - 1):
        # Affinity Rules to build each column
        affA = uc.AffinityRule(str(i + 1) + "a", str(i) + "a", "v", 1)
        genSys.addAffinity(affA)
        affB = uc.AffinityRule(str(i + 1) + "b", str(i) + "b", "v", 1)
        genSys.addAffinity(affB)
        affC = uc.AffinityRule(str(i + 1) + "c", str(i) + "c", "v", 1)
        genSys.addAffinity(affC)

    for i in range(rt4Len - 1):
        affD = uc.AffinityRule(str(i) + "D", str(i) + "Ds", "v", 1)
        genSys.addAffinity(affD)
        affDs = uc.AffinityRule(str(i + 1) + "Ds", str(i) + "D", "v", 1)
        genSys.addAffinity(affDs)

        # Affinity Rule to start the next section of the A and B column
        affGrowA = uc.AffinityRule("0a", str(i) + "A'", "v", 1)
        genSys.addAffinity(affGrowA)
        affGrowB = uc.AffinityRule("0b", str(i) + "B'", "v", 1)
        genSys.addAffinity(affGrowB)
        affGrowC = uc.AffinityRule("0c", str(i) + "C'", "v", 1)
        genSys.addAffinity(affGrowC)

    affLD = uc.AffinityRule(str(rt4Len - 1) + "D", str(rt4Len - 1) + "Ds", "v", 1)
    genSys.addAffinity(affLD)

    ### Transitions
    # Transition once the C and D column are complete
    trCTop = uc.TransitionRule(str((2 * rt4Len) - 1) + "c", str(rt4Len - 1) + "D", "C'", str(rt4Len - 1) + "D", "h")
    genSys.addTransitionRule(trCTop)

    # Rule for starting propagation of A state
    AprimeProp = uc.TransitionRule(
        "A'", str((2 * rt4Len) - 2) + "a", "A'", "A", "v")
    genSys.addTransitionRule(AprimeProp)
    BprimeProp = uc.TransitionRule(
        "B'", str((2 * rt4Len) - 2) + "b", "B'", "B", "v")
    genSys.addTransitionRule(BprimeProp)
    CprimeProp = uc.TransitionRule(
        "C'", str((2 * rt4Len) - 2) + "c", "C'", "C", "v")
    genSys.addTransitionRule(CprimeProp)

    for i in range(2 * rt4Len - 1):
        # Rule for continued propagation of A state downward
        Aprop = uc.TransitionRule("A", str(i) + "a", "A", "A", "v")
        genSys.addTransitionRule(Aprop)
        Bprop = uc.TransitionRule("B", str(i) + "b", "B", "B", "v")
        genSys.addTransitionRule(Bprop)
        Cprop = uc.TransitionRule("C", str(i) + "c", "C", "C", "v")
        genSys.addTransitionRule(Cprop)


    # Rule for when A/B state reaches seed or last B' and marked as 0As/0Bs
    trAseed = uc.TransitionRule("A", "SA", "0As", "SA", "v")
    genSys.addTransitionRule(trAseed)
    trBseed = uc.TransitionRule("B", "SB", "0Bs", "SB", "v")
    genSys.addTransitionRule(trBseed)
    trCseed = uc.TransitionRule("C", "SC", "0Cs", "SC", "v")
    genSys.addTransitionRule(trCseed)

    for i in range(rt4Len):

        # Rules for propagating the A index upward
        propUpA = uc.TransitionRule("A", str(i) + "A", str(i) + "As", str(i) + "A", "v")
        genSys.addTransitionRule(propUpA)
        propUpAs = uc.TransitionRule("A", str(i) + "As", str(i) + "A", str(i) + "As", "v")
        genSys.addTransitionRule(propUpAs)
        propUpPrimeA = uc.TransitionRule("A'", str(i) + "As", str(i) + "A'", str(i) + "As", "v")
        genSys.addTransitionRule(propUpPrimeA)

        propUpB = uc.TransitionRule("B", str(i) + "B", str(i) + "Bs", str(i) + "B", "v")
        genSys.addTransitionRule(propUpB)
        propUpBs = uc.TransitionRule("B", str(i) + "Bs", str(i) + "B", str(i) + "Bs", "v")
        genSys.addTransitionRule(propUpBs)
        propUpPrimeB = uc.TransitionRule("B'", str(i) + "Bs", str(i) + "B'", str(i) + "Bs", "v")
        genSys.addTransitionRule(propUpPrimeB)

        propUpC = uc.TransitionRule("C", str(i) + "C", str(i) + "Cs", str(i) + "C", "v")
        genSys.addTransitionRule(propUpC)
        propUpCs = uc.TransitionRule("C", str(i) + "Cs", str(i) + "C", str(i) + "Cs", "v")
        genSys.addTransitionRule(propUpCs)
        propUpPrimeC = uc.TransitionRule("C'", str(i) + "Cs", str(i) + "C'", str(i) + "Cs", "v")
        genSys.addTransitionRule(propUpPrimeC)

        # Once the B index reaches the top transition the a and b columns
        trBC = uc.TransitionRule(str(2 * rt4Len - 1) + "b", str(i) + "C'", str(2 * rt4Len - 1) + "b'", str(i) + "C'", "h")
        genSys.addTransitionRule(trBC)
        trAB = uc.TransitionRule(str(2 * rt4Len - 1) + "a", str(2 * rt4Len - 1) + "b'", str(2 * rt4Len - 1) + "a'", str(2 * rt4Len - 1) + "b'", "h")
        genSys.addTransitionRule(trAB)

    return genSys



if __name__ == "__main__":
    sys = genQuadIndexStates(81)
    SaveFile.main(sys, ["quadTest.xml"])
