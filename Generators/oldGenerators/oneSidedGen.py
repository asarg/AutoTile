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


def genTripleIndexStates(vLen):
    seedA = uc.State("SA", black)
    genSys = uc.System(1, [], [], [seedA], [], [], [], [])

    cbrtLen = math.ceil(vLen**(1.0/3.0))

    for i in range(2 * cbrtLen):
        # Little a states (Initial States)
        aState = uc.State(str(i) + "a", red)
        genSys.addState(aState)
        genSys.addInitialState(aState)
        # Little b states (Initial States)
        bState = uc.State(str(i) + "b", blue)
        genSys.addState(bState)
        genSys.addInitialState(bState)

    for i in range(cbrtLen):
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
        genSys.addInitialState(cState)
        # Base C states
        southCState = uc.State(str(i) + "Cs", orange)
        genSys.addState(southCState)
        genSys.addInitialState(southCState)

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

    # Little a prime state
    aPrime = uc.State(str((2 * cbrtLen) - 1) + "a'", red)
    genSys.addState(aPrime)
    # C prime states
    Cprime = uc.State(str(cbrtLen - 1) + "C'", orange)
    genSys.addState(Cprime)
    Cprime2 = uc.State(str(cbrtLen - 1) + "C''", orange)
    genSys.addState(Cprime2)

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




    # Adding Affinity Rules
    #       Seed Affinities to start building
    affinityA0 = uc.AffinityRule("0a", "SA", "v", 1)
    genSys.addAffinity(affinityA0)
    affinityB0 = uc.AffinityRule("0b", "SB", "v", 1)
    genSys.addAffinity(affinityB0)
    affinityB0 = uc.AffinityRule("0Cs", "SC", "v", 1)
    genSys.addAffinity(affinityB0)
    affinitySeed = uc.AffinityRule("SA", "SB", "h", 1)
    genSys.addAffinity(affinitySeed)
    affinitySeed2 = uc.AffinityRule("SB", "SC", "h", 1)
    genSys.addAffinity(affinitySeed2)

    for i in range((2 * cbrtLen) - 1):
        # Affinity Rules to build each column
        affA = uc.AffinityRule(str(i + 1) + "a", str(i) + "a", "v", 1)
        genSys.addAffinity(affA)
        affB = uc.AffinityRule(str(i + 1) + "b", str(i) + "b", "v", 1)
        genSys.addAffinity(affB)

    for i in range(cbrtLen - 1):
        affC = uc.AffinityRule(str(i) + "C", str(i) + "Cs", "v", 1)
        genSys.addAffinity(affC)
        affC = uc.AffinityRule(str(i + 1) + "Cs", str(i) + "C", "v", 1)
        genSys.addAffinity(affC)
        # Affinity Rule to start the next section of the A and B column
        affGrowA = uc.AffinityRule("0a", str(i) + "A'", "v", 1)
        genSys.addAffinity(affGrowA)
        affGrowB = uc.AffinityRule("0b", str(i) + "B'", "v", 1)
        genSys.addAffinity(affGrowB)

    affResetB = uc.AffinityRule("0b", str(cbrtLen - 1) + "B''", "v", 1)
    genSys.addAffinity(affResetB)

    # Last C state affinity
    affLC = uc.AffinityRule(str(cbrtLen - 1) + "C",
                            str(cbrtLen - 1) + "Cs", "v", 1)
    genSys.addAffinity(affLC)
    affGrowC = uc.AffinityRule("0Cs", str(cbrtLen - 1) + "C'", "v", 1)
    genSys.addAffinity(affGrowC)
    # State to continue column A
    affGrowA2 = uc.AffinityRule(
        "0a", str((2 * cbrtLen) - 1) + "a'", "v", 1)
    genSys.addAffinity(affGrowA2)

    # Transition Rules
    #   Transition for when the B and C columns of the sections are complete
    trBTop = uc.TransitionRule(str((2 * cbrtLen) - 1) + "b",
                               str(cbrtLen - 1) + "C", "B'", str(cbrtLen - 1) + "C", "h")
    genSys.addTransitionRule(trBTop)
    #   Transition for to start A propagation when B column has reached it's last index
    trATop = uc.TransitionRule(str((2 * cbrtLen) - 1) + "a", str(cbrtLen - 1) + "B'", "A'", str(cbrtLen - 1) + "B'", "h")
    genSys.addTransitionRule(trATop)


    # Rule for starting propagation of A state
    AprimeProp = uc.TransitionRule(
        "A'", str((2 * cbrtLen) - 2) + "a", "A'", "A", "v")
    genSys.addTransitionRule(AprimeProp)
    BprimeProp = uc.TransitionRule(
        "B'", str((2 * cbrtLen) - 2) + "b", "B'", "B", "v")
    genSys.addTransitionRule(BprimeProp)

    # Rule for when A/B state reaches seed or last B' and marked as 0As/0Bs
    trAseed = uc.TransitionRule("A", "SA", "0As", "SA", "v")
    genSys.addTransitionRule(trAseed)
    trBseed = uc.TransitionRule("B", "SB", "0Bs", "SB", "v")
    genSys.addTransitionRule(trBseed)
    trBreset = uc.TransitionRule("B", str(cbrtLen - 1) + "B''", "0Bs", str(cbrtLen - 1) + "B''", "v")
    genSys.addTransitionRule(trBreset)

    # Rule to allow B to transition to allow a string to print
    veriB2 = uc.TransitionRule("0Bs", str(
        cbrtLen - 1) + "B'", "0Bs", str(cbrtLen - 1) + "B''", "v")
    genSys.addTransitionRule(veriB2)
    veriC = uc.TransitionRule("0Cs", str(
        cbrtLen - 1) + "C'", "0Cs", str(cbrtLen - 1) + "C''", "v")
    genSys.addTransitionRule(veriC)

    for i in range(2 * cbrtLen - 1):
        # Rule for continued propagation of A state downward
        Aprop = uc.TransitionRule("A", str(i) + "a", "A", "A", "v")
        genSys.addTransitionRule(Aprop)
        Bprop = uc.TransitionRule("B", str(i) + "b", "B", "B", "v")
        genSys.addTransitionRule(Bprop)


    ApropPrime = uc.TransitionRule("A", str(2 * cbrtLen - 1) + "a'", "A" , "A", "v")
    genSys.addTransitionRule(ApropPrime)



    for i in range(cbrtLen):
        # Rule for A state reaches bottom of the column to increment
        if i < cbrtLen - 1:
            trIncA = uc.TransitionRule("A", str(i) + "A'", str(i + 1) + "As", str(i) + "A'", "v")
            genSys.addTransitionRule(trIncA)
            trIncB = uc.TransitionRule("B", str(i) + "B'", str(i + 1) + "Bs", str(i) + "B'", "v")
            genSys.addTransitionRule(trIncB)
            # Rule allowing B column to start the next section
            trGrowA = uc.TransitionRule(str((2 * cbrtLen) - 1) + "a", str(i) + "B'", str((2 * cbrtLen) - 1) + "a'", str(i) + "B'", "h")
            genSys.addTransitionRule(trGrowA)
            # Rule allowing B column to start the next section
            trGrowC = uc.TransitionRule(str(i) + "B'", str(cbrtLen - 1) + "C", str(i) + "B'", str(cbrtLen - 1) + "C'", "h")
            genSys.addTransitionRule(trGrowC)
            # Rule allowing B to start next section after A increments
            trGrowB = uc.TransitionRule(str(i) + "A'", str(cbrtLen - 1) + "B'", str(i) + "A'", str(cbrtLen - 1) + "B''", "h")
            genSys.addTransitionRule(trGrowB)


        # Rules for propagating the A index upward
        propUpA = uc.TransitionRule("A", str(i) + "A", str(i) + "As", str(i) + "A", "v")
        genSys.addTransitionRule(propUpA)
        propUpAs = uc.TransitionRule("A", str(i) + "As", str(i) + "A", str(i) + "As", "v")
        genSys.addTransitionRule(propUpAs)
        propUpPrimeA = uc.TransitionRule("A'", str(i) + "As", str(i) + "A'", str(i) + "As", "v")
        genSys.addTransitionRule(propUpPrimeA)

        propUpB = uc.TransitionRule("B", str(i) + "B", str(i) + "Bs", str(i) + "B", "v")
        genSys.addTransitionRule(propUpB)
        propUpAs = uc.TransitionRule("B", str(i) + "Bs", str(i) + "B", str(i) + "Bs", "v")
        genSys.addTransitionRule(propUpAs)
        propUpPrimeB = uc.TransitionRule("B'", str(i) + "Bs", str(i) + "B'", str(i) + "Bs", "v")
        genSys.addTransitionRule(propUpPrimeB)

        # Rule allowing B to start next section after A increments
        trGrowC = uc.TransitionRule(str(cbrtLen - 1) + "B''", str(cbrtLen - 1) + "C", str(cbrtLen - 1) + "B''", str(cbrtLen - 1) + "C'", "h")
        genSys.addTransitionRule(trGrowC)




    return genSys


def cbrtBinString(value):
    if isinstance(value, int):
        value = bin(value)[2:]


    revValue = value[::-1]
    vLen = len(value)
    genSys = genTripleIndexStates(vLen)

    cbrtLen = math.ceil(vLen**(1.0/3.0))


    # We must add TRs to reset the special cases
    #trGrowC = uc.TransitionRule(str(cbrtLen - 1) + "B''", str(cbrtLen - 1) + "C", str(cbrtLen - 1) + "B''", str(cbrtLen - 1) + "C'", "h")
    #genSys.addTransitionRule(trGrowC)


    # Add Binary Symbol states
    state0 = uc.State("0", black)
    state1 = uc.State("1", white)
    genSys.addState(state0)
    genSys.addState(state1)

    # Additional Index States are needed
    blankB = uc.State("Bx", blue)
    genSys.addState(blankB)

    for i in range(cbrtLen):
        # States used to temp store values ND pulled from table
        stateC0 = uc.State(str(i) + "C0", black)
        genSys.addState(stateC0)
        stateC1 = uc.State(str(i) + "C1", white)
        genSys.addState(stateC1)

    # No new affinities are used

    # Transitions
    # STEP 1: ND select a value using A and B
    for i in range(cbrtLen):
        labelA = str(i) + "As"

        for j in range(cbrtLen):
            labelB = str(j) + "Bs"

            for k in range(cbrtLen):
                # Get the index of the current bit
                bitIndex = i * cbrtLen**2
                bitIndex += j * cbrtLen
                bitIndex += k

                # Get the current bit
                if bitIndex < len(value):
                    bit = revValue[bitIndex]
                else:
                    bit = "1"

                # The current bit and the k index are used to indicate the final state
                labelTempC = str(k) + "C" + bit

                # A rule will be added for each bit indexed by A B and C
                luTR = uc.TransitionRule(labelA, labelB, labelA, labelTempC, "h")
                genSys.addTransitionRule(luTR)





        ###### STEP 2: Error Checking
        # Here i will indicate the left state that was just created in the last loop
        # The only logic here is to reset if the first number matches and transition back to Bx if not
    for i in range(cbrtLen):
        labelC0 = str(i) + "C0"
        labelC1 = str(i) + "C1"

        for j in range(cbrtLen):
            labelC = str(j) + "Cs"

            # If the index matches we grabbed the right value
            if i == j:
                tr0 = uc.TransitionRule(labelC0, labelC, labelC0, "0", "h")
                tr1 = uc.TransitionRule(labelC1, labelC, labelC1, "1", "h")
            else:
                # If the index is incorrect we transtion back to the blank assembly
                tr0 = uc.TransitionRule(labelC0, labelC, "Bx", labelC, "h")
                tr1 = uc.TransitionRule(labelC1, labelC, "Bx", labelC, "h")

            genSys.addTransitionRule(tr0)
            genSys.addTransitionRule(tr1)


    ##### TRs to reset the B tile
    for i in range(cbrtLen):
        labelB = str(i) + "B"
        labelBprime = str(i) + "B'"
        labelBs = str(i) + "Bs"
        resetBtr = uc.TransitionRule(labelB, "Bx", labelB, labelBs, "v")
        genSys.addTransitionRule(resetBtr)
        resetBtrPrime = uc.TransitionRule(labelBprime, "Bx", labelBprime, labelBs, "v")
        genSys.addTransitionRule(resetBtrPrime)

    # add final reset Bx rule for the double prime
    labelBprime2 = str(cbrtLen - 1) + "B''"
    labelBs = str(cbrtLen - 1) + "Bs"
    resetBtrPrime2 = uc.TransitionRule(labelBprime2, "Bx", labelBprime2, labelBs, "v")
    genSys.addTransitionRule(resetBtrPrime2)

    return genSys

def cbrtBinCount(value):
    if isinstance(value, int):
        # Since the system has one column that is behind the start of the counter
        # we subtract one to


        # get the cieling of the log of the number
        # This tells us how long the string will be
        bits = math.ceil(math.log(value, 2))

        # Get the number we're counting up to
        # The assembly stops at after overflow so we add one to the max count
        maxCount = 2**bits + 1
        start = maxCount - value
        startBin = bin(start)[2:]

        # Need to add leading 0s
        count0 = bits - len(startBin)
        lead0 = ""
        for i in range(count0):
            lead0 = lead0 + "0"


        value = lead0 + startBin

    cbrtLen = math.ceil(len(value)**(1.0/3.0))

    genSys = cbrtBinString(value)

    # Add Binary Counter States

    # New Initial States
    # State for indicating carry
    carry = uc.State("c", blue)
    genSys.addState(carry)
    genSys.addInitialState(carry)


    # State for indicating no carry
    noCarry = uc.State("nc", red)
    genSys.addState(noCarry)
    genSys.addInitialState(noCarry)


    # North Bit states
    n1 = uc.State("1n", white)
    genSys.addState(n1)
    genSys.addInitialState(n1)
    n0 = uc.State("0n", black)
    genSys.addState(n0)
    genSys.addInitialState(n0)

    ##
    incState = uc.State("+", black)
    genSys.addState(incState)
    genSys.addInitialState(incState)

    northWall = uc.State("N", black)
    genSys.addState(northWall)
    genSys.addInitialState(northWall)

    # Other States

    southWall = uc.State("S", black)
    genSys.addState(southWall)

    zeroCarry = uc.State("0c", black)
    genSys.addState(zeroCarry)
    zeroCarryN = uc.State("0cn", black)
    genSys.addState(zeroCarryN)
    genSys.addInitialState(zeroCarryN)

    ##### Affinities

    # <Rule Label1="SB" Label2="+" Dir="h" Strength="1"></Rule>
    incSeed = uc.AffinityRule("SC", "+", "h")
    genSys.addAffinity(incSeed)
    incSouth = uc.AffinityRule("S", "+", "h")
    genSys.addAffinity(incSouth)

    # Affinity to let carry attach
    incCarry = uc.AffinityRule("c", "+", "v")
    genSys.addAffinity(incCarry)
    carry0aff = uc.AffinityRule("c", "0cn", "v")
    genSys.addAffinity(carry0aff)
    ncAff0 = uc.AffinityRule("nc", "0n", "v")
    genSys.addAffinity(ncAff0)
    ncAff1 = uc.AffinityRule("nc", "1n", "v")
    genSys.addAffinity(ncAff1)

    # Affinity to attach north bit state
    north1Aff = uc.AffinityRule("1n", "1", "v")
    genSys.addAffinity(north1Aff)
    north0Aff = uc.AffinityRule("0n", "0", "v")
    genSys.addAffinity(north0Aff)
    north0carry = uc.AffinityRule("0cn", "0c", "v")
    genSys.addAffinity(north0carry)


    ###### Transitions
    ### Carry state transitions
    carry0 = uc.TransitionRule("0", "c", "0", "1", "h")
    genSys.addTransitionRule(carry0)
    carry1 = uc.TransitionRule("1", "c", "1", "0c", "h")
    genSys.addTransitionRule(carry1)

    ### No Carry transitions
    noCarry0 = uc.TransitionRule("0", "nc", "0", "0", "h")
    genSys.addTransitionRule(noCarry0)
    noCarry1 = uc.TransitionRule("1", "nc", "1", "1", "h")
    genSys.addTransitionRule(noCarry1)

    ### Once a number is set in the Least Significant Bit transtions the '+' state to the south wall state "S"
    resetInc1 = uc.TransitionRule("1", "+", "1", "S", "v")
    genSys.addTransitionRule(resetInc1)
    resetInc0 = uc.TransitionRule("0", "+", "0", "S", "v")
    genSys.addTransitionRule(resetInc0)

    ### Transition downward to only let the next column place if a 1 appears in the last number
    northCarryReset1 = uc.TransitionRule("1", "0cn", "1", "0n", "v")
    genSys.addTransitionRule(northCarryReset1)
    northCarryReset0 = uc.TransitionRule("0", "0cn", "0", "0n", "v")
    genSys.addTransitionRule(northCarryReset0)
    CarryReset = uc.TransitionRule("0n", "0c", "0n", "0", "v")
    genSys.addTransitionRule(CarryReset)

    return genSys


if __name__ == "__main__":
    sys = cbrtBinCount(120)
    SaveFile.main(sys, ["tripleTest2.xml"])