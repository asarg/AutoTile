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

    # Get starting points
    offset = rt4Len**4 - vLen

    startD = offset % rt4Len
    tempOffset = math.floor(offset / rt4Len)
    startC = tempOffset % rt4Len
    tempOffset = math.floor(tempOffset / rt4Len)
    startB = tempOffset % rt4Len
    tempOffset = math.floor(tempOffset / rt4Len)
    startA = tempOffset % rt4Len
    
    

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

    #     seedA is an Initial State
    northA = uc.State("NA", black)
    genSys.add_State(northA)
    genSys.add_Initial_State(northA)
    #     seedB is an Initial State
    northB = uc.State("NB", black)
    genSys.add_Initial_State(northB)
    genSys.add_State(northB)
    #     seedC is an Initial State
    northC = uc.State("NC", black)
    genSys.add_Initial_State(northC)
    genSys.add_State(northC)
    #     seedD is an Initial State
    northD = uc.State("ND", black)
    genSys.add_Initial_State(northD)
    genSys.add_State(northD)

    # Blank A and A' states
    singleA = uc.State("A", red)
    genSys.add_State(singleA)
    genSys.add_Initial_State(singleA)
    singleAPrime = uc.State("A'", red)
    genSys.add_State(singleAPrime)
    genSys.add_Initial_State(singleAPrime)
    # Blank B and B' states
    singleB = uc.State("B", blue)
    genSys.add_State(singleB)
    genSys.add_Initial_State(singleB)
    BPrime = uc.State("B'", blue)
    genSys.add_State(BPrime)
    genSys.add_Initial_State(BPrime)
    BPrime2 = uc.State("B''", blue)
    genSys.add_State(BPrime2)
    # Blank C and C' states
    singleC = uc.State("C", orange)
    genSys.add_State(singleC)
    genSys.add_Initial_State(singleC)
    singleCPrime = uc.State("C'", orange)
    genSys.add_State(singleCPrime)
    genSys.add_Initial_State(singleCPrime)


    # Large Letter States
    for i in range(rt4Len):
        # Big A states
        bigAState = uc.State(str(i) + "An", red)
        genSys.add_State(bigAState)
        # Base A states
        southAState = uc.State(str(i) + "A", red)
        genSys.add_State(southAState)
        # A' (prime) states
        bigAPrime = uc.State(str(i) + "An'", red)
        genSys.add_State(bigAPrime)
        # Big B states
        bigBState = uc.State(str(i) + "Bn", blue)
        genSys.add_State(bigBState)
        # Base B states
        southBState = uc.State(str(i) + "B", blue)
        genSys.add_State(southBState)
        # B prime states
        Bprime = uc.State(str(i) + "Bn'", blue)
        genSys.add_State(Bprime)
        Bprime2 = uc.State(str(i) + "Bn''", blue)
        genSys.add_State(Bprime2)
        # C states (Initial States)
        cState = uc.State(str(i) + "Cn", orange)
        genSys.add_State(cState)
        # Base C states
        southCState = uc.State(str(i) + "C", orange)
        genSys.add_State(southCState)
        # C prime states
        Cprime = uc.State(str(i) + "Cn'", orange)
        genSys.add_State(Cprime)
        Cprime2 = uc.State(str(i) + "Cn''", orange)
        genSys.add_State(Cprime2)
        # D states (Initial States)
        dState = uc.State(str(i) + "Dn", green)
        genSys.add_State(dState)
        genSys.add_Initial_State(dState)
        # Base D states
        southDState = uc.State(str(i) + "D", green)
        genSys.add_State(southDState)
        genSys.add_Initial_State(southDState)

        # C prime states
    
    Dprime = uc.State(str(rt4Len - 1) + "Dn'", green)
    genSys.add_State(Dprime)

    ### Affinity Rules
    #       Seed Affinities to start building seed row and attach first tile of D column
    affinityD0 = uc.AffinityRule(str(startD) + "D", "SD", "v", 1)
    genSys.add_affinity(affinityD0)
    affinitySeed = uc.AffinityRule("SA", "SB", "h", 1)
    genSys.add_affinity(affinitySeed)
    affinitySeed2 = uc.AffinityRule("SB", "SC", "h", 1)
    genSys.add_affinity(affinitySeed2)
    affinitySeed3 = uc.AffinityRule("SC", "SD", "h", 1)
    genSys.add_affinity(affinitySeed3)

    # Affinities to build D column
    for i in range(rt4Len - 1):
        affD = uc.AffinityRule(str(i) + "Dn", str(i) + "D", "v", 1)
        genSys.add_affinity(affD)
        affDs = uc.AffinityRule(str(i + 1) + "D", str(i) + "Dn", "v", 1)
        genSys.add_affinity(affDs)

    affLD = uc.AffinityRule(str(rt4Len - 1) + "Dn", str(rt4Len - 1) + "D", "v", 1)
    genSys.add_affinity(affLD)

    # The last state of the D column allows for C' to attach to the left 
    affLD = uc.AffinityRule("C'", str(rt4Len - 1) + "Dn", "h", 1)
    genSys.add_affinity(affLD)
    # C prime allows for the C states to attach below
    affCPrime = uc.AffinityRule("C'", "C", "v", 1)
    genSys.add_affinity(affCPrime)
    affCDown = uc.AffinityRule("C", "C", "v", 1)
    genSys.add_affinity(affCDown)

    # The last state of the C column allows for B' to attach to the left 
    affLC = uc.AffinityRule("B'", str(rt4Len - 1) + "Cn'", "h", 1)
    genSys.add_affinity(affLC)
    # B prime allows for the B states to attach below
    affBPrime = uc.AffinityRule("B'", "B", "v", 1)
    genSys.add_affinity(affBPrime)
    affBDown = uc.AffinityRule("B", "B", "v", 1)
    genSys.add_affinity(affBDown)

    # The last state of the B column allows for A' to attach to the left 
    affLB = uc.AffinityRule("A'", str(rt4Len - 1) + "Bn'", "h", 1)
    genSys.add_affinity(affLB)
    # B prime allows for the B states to attach below
    affAPrime = uc.AffinityRule("A'", "A", "v", 1)
    genSys.add_affinity(affAPrime)
    affADown = uc.AffinityRule("A", "A", "v", 1)
    genSys.add_affinity(affADown)

    # Affinity for D column to grow
    affDgrow = uc.AffinityRule("0D", str(rt4Len - 1) + "Dn'", "v", 1)
    genSys.add_affinity(affDgrow)

    northAaff = uc.AffinityRule("NA", str(rt4Len - 1) + "An'", "v")
    genSys.add_affinity(northAaff)
    northBaff = uc.AffinityRule("NA", "NB", "h")
    genSys.add_affinity(northBaff)
    northCaff = uc.AffinityRule("NB", "NC", "h")
    genSys.add_affinity(northCaff)
    northCaff = uc.AffinityRule("NC", "ND", "h")
    genSys.add_affinity(northCaff)

    ### Transitions
    # Rule for when A/B/C state reaches seed and marked as 0As/0Bs
    trAseed = uc.TransitionRule("A", "SA", str(startA) + "A", "SA", "v")
    genSys.add_transition_rule(trAseed)
    trBseed = uc.TransitionRule("B", "SB", str(startB) + "B", "SB", "v")
    genSys.add_transition_rule(trBseed)
    trCseed = uc.TransitionRule("C", "SC", str(startC) + "C", "SC", "v")
    genSys.add_transition_rule(trCseed)

    for i in range(rt4Len):
        iA = str(i) + "A"
        iB = str(i) + "B"
        iC = str(i) + "C"
        # Rules for propagating the A/B/C index upward
        propUpA = uc.TransitionRule("A", iA + "n", iA, iA + "n", "v")
        genSys.add_transition_rule(propUpA)
        propUpAs = uc.TransitionRule("A", iA, iA + "n", iA, "v")
        genSys.add_transition_rule(propUpAs)
        propUpPrimeA = uc.TransitionRule("A'", iA, iA + "n'", iA, "v")
        genSys.add_transition_rule(propUpPrimeA)

        propUpB = uc.TransitionRule("B", iB + "n", iB, iB + "n", "v")
        genSys.add_transition_rule(propUpB)
        propUpBs = uc.TransitionRule("B", iB, iB + "n", iB, "v")
        genSys.add_transition_rule(propUpBs)
        propUpPrimeB = uc.TransitionRule("B'", iB, iB + "n'", iB, "v")
        genSys.add_transition_rule(propUpPrimeB)

        propUpC = uc.TransitionRule("C", iC + "n", iC, iC + "n", "v")
        genSys.add_transition_rule(propUpC)
        propUpCs = uc.TransitionRule("C", iC, iC + "n", iC, "v")
        genSys.add_transition_rule(propUpCs)
        propUpPrimeC = uc.TransitionRule("C'", iC, iC + "n'", iC, "v")
        genSys.add_transition_rule(propUpPrimeC)


    rtCP = str(rt4Len - 1) + "Cn'"
    rtCP2 = str(rt4Len - 1) + "Cn''"
    rtBP = str(rt4Len - 1) + "Bn'"
    rtBP2 = str(rt4Len - 1) + "Bn''"
    
    for i in range(rt4Len - 1):
        iAP = str(i) + "An'"
        iBP = str(i) + "Bn'"
        iCP = str(i) + "Cn'"

        i1As = str(i + 1) + "A"
        i1Bs = str(i + 1) + "B"
        i1Cs = str(i + 1) + "C"



        # Transition Rule for when C reach the top of the column
        growCD = uc.TransitionRule(iCP, str(rt4Len - 1) + "Dn", iCP, str(rt4Len - 1) + "Dn'", "h")
        genSys.add_transition_rule(growCD)

        growBC = uc.TransitionRule(iBP, rtCP, iBP, rtCP2, "h")
        genSys.add_transition_rule(growBC)

        growAB = uc.TransitionRule(iAP, rtBP, iAP, rtBP2, "h")
        genSys.add_transition_rule(growAB)

        # Transitions to increment A/B/C column from not the seed
        trAinc = uc.TransitionRule("A", iAP, i1As, iAP, "v")
        genSys.add_transition_rule(trAinc)
        trBinc = uc.TransitionRule("B", iBP, i1Bs, iBP, "v")
        genSys.add_transition_rule(trBinc)
        trCinc = uc.TransitionRule("C", iCP, i1Cs, iCP, "v")
        genSys.add_transition_rule(trCinc)

    # Once the B column complete and transition the C column to double prime D can start growing again
    resetCD = uc.TransitionRule(rtCP2, str(rt4Len - 1) + "Dn", rtCP2, str(rt4Len - 1) + "Dn'", "h")
    genSys.add_transition_rule(resetCD)   

    # We need to add a special case TR for when the C column is building down and see C double prime
    resetC2 = uc.TransitionRule("C", rtCP2, "0C", rtCP2, "v")
    genSys.add_transition_rule(resetC2)
    resetB2 = uc.TransitionRule("B", rtBP2, "0B", rtBP2, "v")
    genSys.add_transition_rule(resetB2)

    # B double prime transitions C prime to C double prime
    doublePrimeProp = uc.TransitionRule(rtBP2, rtCP, rtBP2, rtCP2, "h")
    genSys.add_transition_rule(doublePrimeProp)

    return genSys

def genQuadBinString(value):
    if isinstance(value, int):
        value = bin(value)[2:]


    revValue = value[::-1]
    vLen = len(value)
    genSys = genQuadIndexStates(vLen)

    rt4Len = math.ceil(vLen**(1.0/4.0))

    offset = rt4Len**4 - vLen

    # Add Binary Symbol states
    state0 = uc.State("0i", black)
    state1 = uc.State("1i", white)
    genSys.add_State(state0)
    genSys.add_State(state1)

    # Add look up states for A and D to store values
    for i in range(rt4Len):
        iA0 = uc.State(str(i) + "A0", black)
        genSys.add_State(iA0)
        iA1 = uc.State(str(i) + "A1", white)
        genSys.add_State(iA1)
        iD0 = uc.State(str(i) + "D0", black)
        genSys.add_State(iD0)
        iD1 = uc.State(str(i) + "D1", white)
        genSys.add_State(iD1)

        # Base B prime states. Used to prevent early look up transitions
        southBState = uc.State(str(i) + "B'", blue)
        genSys.add_State(southBState)

    # Additional Index States are needed
    blankB = uc.State("Bx", blue)
    genSys.add_State(blankB)
    blankC = uc.State("Cx", orange)
    genSys.add_State(blankC)

    # Look up states transtion to these pass and fail states based on whether or not they match the As or Ds state
    passA0 = uc.State("PA0", black)
    genSys.add_State(passA0)
    passA1 = uc.State("PA1", white)
    genSys.add_State(passA1)
    passD0 = uc.State("PD0", black)
    genSys.add_State(passD0)
    passD1 = uc.State("PD1", white)
    genSys.add_State(passD1)

    failA = uc.State("FA", blue)
    genSys.add_State(failA)
    failD = uc.State("FD", orange)
    genSys.add_State(failD)



    # For each index we add a look up rule between the B and C states
    for a in range(rt4Len):
        for b in range(rt4Len):

            # Transition to change iBs to iBs'
            iAs = str(a) + "A"
            iBs = str(b) + "B"

            trBsPrime = uc.TransitionRule(iAs, iBs, iAs, iBs + "'", "h")
            genSys.add_transition_rule(trBsPrime)


            for c in range(rt4Len):
                for d in range(rt4Len):
                    # Compute the bit index
                    bitI = a * (rt4Len**3)
                    bitI += b * (rt4Len**2)
                    bitI += c * rt4Len
                    bitI += d

                    if bitI < offset:
                        continue

                    # Get the current bit
                    bit = revValue[bitI - offset]

                    # The B and C state are the first pair in the rule
                    bB = str(b) + "B'"
                    cC = str(c) + "C"
                    # The A and D state will be the second pair in the rule and will store the bit value
                    aA = str(a) + "A" + bit
                    dD = str(d) + "D" + bit

                    # Look up transition rule
                    trLU = uc.TransitionRule(bB, cC, aA, dD, "h")
                    genSys.add_transition_rule(trLU)

    # Verification checks i will be index of A/D of the outer states and j will be the index of the inner states
    for i in range(rt4Len):
        for j in range(rt4Len):
            iAs = str(i) + "A"
            jA1 = str(j) + "A1"
            jA0 = str(j) + "A0"

            iDs = str(i) + "D"
            jD1 = str(j) + "D1"
            jD0 = str(j) + "D0"

            if i == j:
                trApass0 = uc.TransitionRule(iAs, jA0, iAs, "PA0", "h")
                genSys.add_transition_rule(trApass0)
                trApass1 = uc.TransitionRule(iAs, jA1, iAs, "PA1", "h")
                genSys.add_transition_rule(trApass1)

                trDpass0 = uc.TransitionRule(jD0, iDs, "PD0", iDs, "h")
                genSys.add_transition_rule(trDpass0)
                trDpass1 = uc.TransitionRule(jD1, iDs,"PD1", iDs, "h")
                genSys.add_transition_rule(trDpass1)
            else:
                trAfail0 = uc.TransitionRule(iAs, jA0, iAs, "FA", "h")
                genSys.add_transition_rule(trAfail0)
                trAfail1 = uc.TransitionRule(iAs, jA1, iAs, "FA", "h")
                genSys.add_transition_rule(trAfail1)

                trDfail0 = uc.TransitionRule(jD0, iDs, "FD", iDs, "h")
                genSys.add_transition_rule(trDfail0)
                trDfail1 = uc.TransitionRule(jD1, iDs,"FD", iDs, "h")
                genSys.add_transition_rule(trDfail1)

    # Transition rule for when both transitions pass
    trADpass0 = uc.TransitionRule("PA0", "PD0", "PA0", "0i", "h")
    genSys.add_transition_rule(trADpass0)
    trADpass1 = uc.TransitionRule("PA1", "PD1", "PA1", "1i", "h")
    genSys.add_transition_rule(trADpass1)

    trAfail0 = uc.TransitionRule("PA0", "FD", "Bx", "Cx", "h")
    genSys.add_transition_rule(trAfail0)
    trAfail1 = uc.TransitionRule("PA1", "FD", "Bx", "Cx", "h")
    genSys.add_transition_rule(trAfail1)

    trDfail0 = uc.TransitionRule("FA", "PD0", "Bx", "Cx", "h")
    genSys.add_transition_rule(trDfail0)
    trDfail1 = uc.TransitionRule("FA", "PD1", "Bx", "Cx", "h")
    genSys.add_transition_rule(trDfail1)

    trADfail = uc.TransitionRule("FA", "FD", "Bx", "Cx", "h")
    genSys.add_transition_rule(trADfail)


    
    for i in range(rt4Len):
        ##### TRs to reset the B tile
        labelB = str(i) + "Bn"
        labelBprime = str(i) + "Bn'"
        labelBprime2 = str(i) + "Bn''"
        labelBs = str(i) + "B'"
        resetBtr = uc.TransitionRule(labelB, "Bx", labelB, labelBs, "v")
        genSys.add_transition_rule(resetBtr)
        resetBtrPrime = uc.TransitionRule(labelBprime, "Bx", labelBprime, labelBs, "v")
        genSys.add_transition_rule(resetBtrPrime)
        resetBtrPrime2 = uc.TransitionRule(labelBprime2, "Bx", labelBprime2, labelBs, "v")
        genSys.add_transition_rule(resetBtrPrime2)

        ##### TRs to reset the C tile
        labelC = str(i) + "Cn"
        labelCprime = str(i) + "Cn'"
        labelCprime2 = str(i) + "Cn''"
        labelCs = str(i) + "C"
        resetCtr = uc.TransitionRule(labelC, "Cx", labelC, labelCs, "v")
        genSys.add_transition_rule(resetCtr)
        resetCtrPrime = uc.TransitionRule(labelCprime, "Cx", labelCprime, labelCs, "v")
        genSys.add_transition_rule(resetCtrPrime)
        resetCtrPrime2 = uc.TransitionRule(labelCprime2, "Cx", labelCprime2, labelCs, "v")
        genSys.add_transition_rule(resetCtrPrime2)

        labelDs = str(i) + "D"
        tr0Ds = uc.TransitionRule("0i", labelDs, "0i", "0i", "h")
        genSys.add_transition_rule(tr0Ds)
        tr1Ds = uc.TransitionRule("1i", labelDs, "1i", "1i", "h")
        genSys.add_transition_rule(tr1Ds)




    return genSys

def quadBinCount(value):
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

    rt4Len = math.ceil(len(value)**(1.0/4.0))

    genSys = genQuadBinString(value)

    # Add Binary Counter States

    # New Initial States
    # State for indicating carry
    carry = uc.State("c", blue)
    genSys.add_State(carry)
    genSys.add_Initial_State(carry)


    # State for indicating no carry
    noCarry = uc.State("nc", red)
    genSys.add_State(noCarry)
    genSys.add_Initial_State(noCarry)

    # Add Binary Symbol states
    state0 = uc.State("0", black)
    state1 = uc.State("1", white)
    genSys.add_State(state0)
    genSys.add_State(state1)

    # North Bit states
    n1 = uc.State("1n", white)
    genSys.add_State(n1)
    genSys.add_Initial_State(n1)
    n0 = uc.State("0n", black)
    genSys.add_State(n0)
    genSys.add_Initial_State(n0)

    ##
    incState = uc.State("+", black)
    genSys.add_State(incState)
    genSys.add_Initial_State(incState)

    northWall = uc.State("N", black)
    genSys.add_State(northWall)
    genSys.add_Initial_State(northWall)


    # Other States

    southWall = uc.State("S", black)
    genSys.add_State(southWall)

    zeroCarry = uc.State("0c", black)
    genSys.add_State(zeroCarry)
    zeroCarryN = uc.State("0cn", black)
    genSys.add_State(zeroCarryN)
    genSys.add_Initial_State(zeroCarryN)



    ##### Affinities

    # <Rule Label1="SB" Label2="+" Dir="h" Strength="1"></Rule>
    incSeed = uc.AffinityRule("SD", "+", "h")
    genSys.add_affinity(incSeed)
    incSouth = uc.AffinityRule("S", "+", "h")
    genSys.add_affinity(incSouth)

    # Affinity to let carry attach
    incCarry = uc.AffinityRule("c", "+", "v")
    genSys.add_affinity(incCarry)
    carry0aff = uc.AffinityRule("c", "0cn", "v")
    genSys.add_affinity(carry0aff)
    ncAff0 = uc.AffinityRule("nc", "0n", "v")
    genSys.add_affinity(ncAff0)   
    ncAff1 = uc.AffinityRule("nc", "1n", "v")
    genSys.add_affinity(ncAff1)   

    # Affinity to attach north bit state
    north1Aff = uc.AffinityRule("1n", "1", "v")
    genSys.add_affinity(north1Aff)
    north0Aff = uc.AffinityRule("0n", "0", "v")
    genSys.add_affinity(north0Aff)
    north0carry = uc.AffinityRule("0cn", "0c", "v")
    genSys.add_affinity(north0carry)

    # Affinity to attach north bit state
    nWall1 = uc.AffinityRule("N1", str(rt4Len - 1) + "An'", "v")
    genSys.add_affinity(nWall1)
    nWall2 = uc.AffinityRule("N1", "N2", "h")
    genSys.add_affinity(nWall2)
    nWall3 = uc.AffinityRule("N2", "N3", "h")
    genSys.add_affinity(nWall3)
    nWall4 = uc.AffinityRule("N3", "N", "h")
    genSys.add_affinity(nWall4)

    ###### Transitions
    ### Carry state transitions
    carry0 = uc.TransitionRule("0", "c", "0", "1", "h")
    genSys.add_transition_rule(carry0)
    carry1 = uc.TransitionRule("1", "c", "1", "0c", "h")
    genSys.add_transition_rule(carry1)
    carry0i = uc.TransitionRule("0i", "c", "0i", "1", "h")
    genSys.add_transition_rule(carry0i)
    carry1i = uc.TransitionRule("1i", "c", "1i", "0c", "h")
    genSys.add_transition_rule(carry1i)

    ### No Carry transitions
    noCarry0 = uc.TransitionRule("0", "nc", "0", "0", "h")
    genSys.add_transition_rule(noCarry0)
    noCarry1 = uc.TransitionRule("1", "nc", "1", "1", "h")
    genSys.add_transition_rule(noCarry1)
    noCarry0i = uc.TransitionRule("0i", "nc", "0i", "0", "h")
    genSys.add_transition_rule(noCarry0i)
    noCarry1i = uc.TransitionRule("1i", "nc", "1i", "1", "h")
    genSys.add_transition_rule(noCarry1i)

    ### Once a number is set in the Least Significant Bit transtions the '+' state to the south wall state "S"
    resetInc1 = uc.TransitionRule("1", "+", "1", "S", "v")
    genSys.add_transition_rule(resetInc1)
    resetInc0 = uc.TransitionRule("0", "+", "0", "S", "v")
    genSys.add_transition_rule(resetInc0)

    ### Transition downward to only let the next column place if a 1 appears in the last number
    northCarryReset1 = uc.TransitionRule("1", "0cn", "1", "0n", "v")
    genSys.add_transition_rule(northCarryReset1)
    northCarryReset0 = uc.TransitionRule("0", "0cn", "0", "0n", "v")
    genSys.add_transition_rule(northCarryReset0)   
    CarryReset = uc.TransitionRule("0n", "0c", "0n", "0", "v")
    genSys.add_transition_rule(CarryReset)  

    nPropD = uc.TransitionRule("ND", "nc", "ND", "N", "h")
    genSys.add_transition_rule(nPropD)  
    nProp1 = uc.TransitionRule("N", "nc", "N", "N", "h")
    genSys.add_transition_rule(nProp1)  

    return genSys          

                    
def genString(value):
    return genQuadBinString(value)

def genRect(length):
    return quadBinCount(length)


if __name__ == "__main__":

    num = ""

    for i in range(27):
        num += "101"

    sys = quadBinCount(num)
    SaveFile.main(sys, ["quadCountTest.xml"])

