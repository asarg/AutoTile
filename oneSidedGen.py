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

#################
# Generators for one sided non determinsitic TA
# All system are temp 1
# One sided means only a transition rule only changes of the states.


# Builds a 3 x O(n)
# Input a integer n
def genTripleIndexStates(vLen):
    seedA = uc.State("SA", black)
    genSys = uc.System(1, [], [], [seedA], [], [], [], [])

    cbrtLen = math.ceil(vLen**(1.0/3.0))

    # Get starting points
    offset = cbrtLen**3 - vLen

    startC = offset % cbrtLen
    tempOffset = math.floor(offset / cbrtLen)
    startB = tempOffset % cbrtLen
    tempOffset = math.floor(tempOffset / cbrtLen)
    startA = tempOffset % cbrtLen


    for i in range(cbrtLen):
        # Big A states
        bigAState = uc.State(str(i) + "An", red)
        genSys.addState(bigAState)
        # Base A states
        southAState = uc.State(str(i) + "A", red)
        genSys.addState(southAState)
        # A' (prime) states
        bigAPrime = uc.State(str(i) + "An'", red)
        genSys.addState(bigAPrime)
        # Big B states
        bigBState = uc.State(str(i) + "Bn", blue)
        genSys.addState(bigBState)
        # Base B states
        southBState = uc.State(str(i) + "B", blue)
        genSys.addState(southBState)
        # B prime states
        Bprime = uc.State(str(i) + "Bn'", blue)
        genSys.addState(Bprime)
        Bprime2 = uc.State(str(i) + "Bn''", blue)
        genSys.addState(Bprime2)
        # C states (Initial States)
        cState = uc.State(str(i) + "Cn", orange)
        genSys.addState(cState)
        genSys.addInitialState(cState)
        # Base C states
        southCState = uc.State(str(i) + "C", orange)
        genSys.addState(southCState)
        genSys.addInitialState(southCState)

    # Blank A and A' states
    singleA = uc.State("A", red)
    genSys.addState(singleA)
    genSys.addInitialState(singleA)
    singleAPrime = uc.State("A'", red)
    genSys.addState(singleAPrime)
    genSys.addInitialState(singleAPrime)
    # Blank B and B' states
    singleB = uc.State("B", blue)
    genSys.addState(singleB)
    genSys.addInitialState(singleB)
    BPrime = uc.State("B'", blue)
    genSys.addState(BPrime)
    genSys.addInitialState(BPrime)
    BPrime2 = uc.State("B''", blue)
    genSys.addState(BPrime2)


    # C prime states
    Cprime = uc.State(str(cbrtLen - 1) + "Cn'", orange)
    genSys.addState(Cprime)
    Cprime2 = uc.State(str(cbrtLen - 1) + "Cn''", orange)
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

    northA = uc.State("NA", black)
    genSys.addState(northA)
    genSys.addInitialState(northA)
    northB = uc.State("NB", black)
    genSys.addState(northB)
    genSys.addInitialState(northB)
    northC = uc.State("NC", black)
    genSys.addState(northC)
    genSys.addInitialState(northC)


    # Adding Affinity Rules
    #       Seed Affinities to start building
    affinityB0 = uc.AffinityRule(str(startC) + "C", "SC", "v", 1)
    genSys.addAffinity(affinityB0)
    affinitySeed = uc.AffinityRule("SA", "SB", "h", 1)
    genSys.addAffinity(affinitySeed)
    affinitySeed2 = uc.AffinityRule("SB", "SC", "h", 1)
    genSys.addAffinity(affinitySeed2)


    for i in range(cbrtLen - 1):
        affC = uc.AffinityRule(str(i) + "Cn", str(i) + "C", "v", 1)
        genSys.addAffinity(affC)
        affC = uc.AffinityRule(str(i + 1) + "C", str(i) + "Cn", "v", 1)
        genSys.addAffinity(affC)



    # Last C state affinity
    affLC = uc.AffinityRule(str(cbrtLen - 1) + "Cn",
                            str(cbrtLen - 1) + "C", "v", 1)
    genSys.addAffinity(affLC)
    affGrowC = uc.AffinityRule("0C", str(cbrtLen - 1) + "Cn'", "v", 1)
    genSys.addAffinity(affGrowC)


    northAaff = uc.AffinityRule("NA", str(cbrtLen - 1) + "An'", "v")
    genSys.addAffinity(northAaff)
    northBaff = uc.AffinityRule("NA", "NB", "h")
    genSys.addAffinity(northBaff)
    northCaff = uc.AffinityRule("NB", "NC", "h")
    genSys.addAffinity(northCaff)



    # Rule for when A/B state reaches seed or last B' and marked as 0As/0Bs
    trAseed = uc.TransitionRule("A", "SA", str(startA) + "A", "SA", "v")
    genSys.addTransitionRule(trAseed)
    trBseed = uc.TransitionRule("B", "SB", str(startB) + "B", "SB", "v")
    genSys.addTransitionRule(trBseed)
    trBreset = uc.TransitionRule("B", str(cbrtLen - 1) + "Bn''", "0B", str(cbrtLen - 1) + "Bn''", "v")
    genSys.addTransitionRule(trBreset)


    # The last state of the C column allows for B' to attach to the left
    affLC = uc.AffinityRule("B'", str(cbrtLen - 1) + "Cn", "h", 1)
    genSys.addAffinity(affLC)
    # B prime allows for the B states to attach below
    affBPrime = uc.AffinityRule("B'", "B", "v", 1)
    genSys.addAffinity(affBPrime)
    affBDown = uc.AffinityRule("B", "B", "v", 1)
    genSys.addAffinity(affBDown)

    # The last state of the B column allows for A' to attach to the left
    affLB = uc.AffinityRule("A'", str(cbrtLen - 1) + "Bn'", "h", 1)
    genSys.addAffinity(affLB)
    # B prime allows for the B states to attach below
    affAPrime = uc.AffinityRule("A'", "A", "v", 1)
    genSys.addAffinity(affAPrime)
    affADown = uc.AffinityRule("A", "A", "v", 1)
    genSys.addAffinity(affADown)





    for i in range(cbrtLen):
        # Rule for A state reaches bottom of the column to increment
        if i < cbrtLen - 1:
            trIncA = uc.TransitionRule(
                "A", str(i) + "An'", str(i + 1) + "A", str(i) + "An'", "v")
            genSys.addTransitionRule(trIncA)
            trIncB = uc.TransitionRule(
                "B", str(i) + "Bn'", str(i + 1) + "B", str(i) + "Bn'", "v")
            genSys.addTransitionRule(trIncB)
            # Rule allowing B column to start the next section
            trGrowC = uc.TransitionRule(str(i) + "Bn'", str(cbrtLen - 1) + "Cn", str(i) + "Bn'", str(cbrtLen - 1) + "Cn'", "h")
            genSys.addTransitionRule(trGrowC)
            # Rule allowing B to start next section after A increments
            trGrowB = uc.TransitionRule(str(i) + "An'", str(cbrtLen - 1) + "Bn'", str(i) + "An'", str(cbrtLen - 1) + "Bn''", "h")
            genSys.addTransitionRule(trGrowB)


        # Rules for propagating the A index upward
        propUpA = uc.TransitionRule(
            "A", str(i) + "An", str(i) + "A", str(i) + "An", "v")
        genSys.addTransitionRule(propUpA)
        propUpAs = uc.TransitionRule(
            "A", str(i) + "A", str(i) + "An", str(i) + "A", "v")
        genSys.addTransitionRule(propUpAs)
        propUpPrimeA = uc.TransitionRule(
            "A'", str(i) + "A", str(i) + "An'", str(i) + "A", "v")
        genSys.addTransitionRule(propUpPrimeA)

        propUpB = uc.TransitionRule(
            "B", str(i) + "Bn", str(i) + "B", str(i) + "Bn", "v")
        genSys.addTransitionRule(propUpB)
        propUpAs = uc.TransitionRule(
            "B", str(i) + "B", str(i) + "Bn", str(i) + "B", "v")
        genSys.addTransitionRule(propUpAs)
        propUpPrimeB = uc.TransitionRule(
            "B'", str(i) + "B", str(i) + "Bn'", str(i) + "B", "v")
        genSys.addTransitionRule(propUpPrimeB)

        # Rule allowing B to start next section after A increments
        trGrowC = uc.TransitionRule(str(cbrtLen - 1) + "Bn''", str(cbrtLen - 1) + "Cn", str(cbrtLen - 1) + "Bn''", str(cbrtLen - 1) + "Cn'", "h")
        genSys.addTransitionRule(trGrowC)




    return genSys


# Builds a O(|S|) x 3 assembly that represent a binary string
# Input a binary string S
def cbrtBinString(value):
    if isinstance(value, int):
        value = bin(value)[2:]


    revValue = value[::-1]
    vLen = len(value)
    genSys = genTripleIndexStates(vLen)

    cbrtLen = math.ceil(vLen**(1.0/3.0))

    offset = cbrtLen**3 - vLen

    # We must add TRs to reset the special cases
    #trGrowC = uc.TransitionRule(str(cbrtLen - 1) + "B''", str(cbrtLen - 1) + "C", str(cbrtLen - 1) + "B''", str(cbrtLen - 1) + "C'", "h")
    #genSys.addTransitionRule(trGrowC)


    # Add Binary Symbol states
    state0 = uc.State("0i", black)
    state1 = uc.State("1i", white)
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
        labelA = str(i) + "A"

        for j in range(cbrtLen):
            labelB = str(j) + "B"

            for k in range(cbrtLen):
                # Get the index of the current bit
                bitIndex = i * cbrtLen**2
                bitIndex += j * cbrtLen
                bitIndex += k

                if bitIndex < offset:
                    continue

                # Get the current bit
                bit = revValue[bitIndex - offset]

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
            labelC = str(j) + "C"

            # If the index matches we grabbed the right value
            if i == j:
                tr0 = uc.TransitionRule(labelC0, labelC, labelC0, "0i", "h")
                tr1 = uc.TransitionRule(labelC1, labelC, labelC1, "1i", "h")
            else:
                # If the index is incorrect we transtion back to the blank assembly
                tr0 = uc.TransitionRule(labelC0, labelC, "Bx", labelC, "h")
                tr1 = uc.TransitionRule(labelC1, labelC, "Bx", labelC, "h")

            genSys.addTransitionRule(tr0)
            genSys.addTransitionRule(tr1)


    ##### TRs to reset the B tile
    for i in range(cbrtLen):
        labelB = str(i) + "Bn"
        labelBprime = str(i) + "Bn'"
        labelBs = str(i) + "B"
        resetBtr = uc.TransitionRule(labelB, "Bx", labelB, labelBs, "v")
        genSys.addTransitionRule(resetBtr)
        resetBtrPrime = uc.TransitionRule(labelBprime, "Bx", labelBprime, labelBs, "v")
        genSys.addTransitionRule(resetBtrPrime)

    # add final reset Bx rule for the double prime
    labelBprime2 = str(cbrtLen - 1) + "Bn''"
    labelBs = str(cbrtLen - 1) + "B"
    resetBtrPrime2 = uc.TransitionRule(labelBprime2, "Bx", labelBprime2, labelBs, "v")
    genSys.addTransitionRule(resetBtrPrime2)

    # Transition to north wall
    northTR = uc.TransitionRule("NC", "nc", "NC", "N", "h")
    genSys.addTransitionRule(northTR)

    return genSys


# Builds a n x O(log n) rectangle
# Input an Integer
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

    # Add Binary Symbol states
    state0 = uc.State("0", black)
    state1 = uc.State("1", white)
    genSys.addState(state0)
    genSys.addState(state1)


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
    carry0i = uc.TransitionRule("0i", "c", "0i", "1", "h")
    genSys.addTransitionRule(carry0i)
    carry1i = uc.TransitionRule("1i", "c", "1i", "0c", "h")
    genSys.addTransitionRule(carry1i)

    ### No Carry transitions
    noCarry0 = uc.TransitionRule("0", "nc", "0", "0", "h")
    genSys.addTransitionRule(noCarry0)
    noCarry1 = uc.TransitionRule("1", "nc", "1", "1", "h")
    genSys.addTransitionRule(noCarry1)
    noCarry0i = uc.TransitionRule("0i", "nc", "0i", "0", "h")
    genSys.addTransitionRule(noCarry0i)
    noCarry1i = uc.TransitionRule("1i", "nc", "1i", "1", "h")
    genSys.addTransitionRule(noCarry1i)

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

    nProp1 = uc.TransitionRule("N", "nc", "N", "N", "h")
    genSys.addTransitionRule(nProp1)

    return genSys


def genString(value):
    return cbrtBinString(value)

def genRect(length):
    return cbrtBinCount(length)

if __name__ == "__main__":
    #sys = genTripleIndexStates(27)
    #SaveFile.main(sys, ["tripleTest2.xml"])

    sys = cbrtBinCount(1500)
    SaveFile.main(sys, ["tripleTest3.xml"])