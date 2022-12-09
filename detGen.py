import UniversalClasses as uc
import SaveFile

import math

red = "f03a47"
blue = "3f88c5"
green = "0ead69"
orange = "f39237"
black = "323031"
white = "DFE0E2"



# Must be passed an interger
def genDoubleIndexStates(vLen):
    seedA = uc.State("SA", black)
    genSys = uc.System(1, [], [], [seedA], [], [], [], [])

    sqrtLen = math.ceil(math.sqrt(vLen))

    # Get starting points
    offset = sqrtLen**2 - vLen

    startA = math.floor(offset / sqrtLen)
    startB = offset % sqrtLen

    #print("A: ", startA)
    #print("B: ", startB)


    # Create States and add to lists

    for i in range(sqrtLen):
        # Big A states
        bigAState = uc.State(str(i) + "A", red)
        genSys.addState(bigAState)
        # A' (prime) states
        aPrime = uc.State(str(i) + "A'", red)
        genSys.addState(aPrime)
        # B states (Initial States)
        bState = uc.State(str(i) + "B", blue)
        genSys.addState(bState)
        genSys.addInitialState(bState)

    # Blank A and A' states
    singleA = uc.State("A", red)
    genSys.addState(singleA)
    genSys.addInitialState(singleA)
    singleAPrime = uc.State("A'", red)
    genSys.addState(singleAPrime)
    genSys.addInitialState(singleAPrime)
    # Seed States
    genSys.addState(seedA)
    seedB = uc.State("SB", black)
    #     seedB is an Initial State
    genSys.addInitialState(seedB)
    genSys.addState(seedB)
    # B prime states
    Bprime = uc.State(str(sqrtLen - 1) + "B'", blue)
    genSys.addState(Bprime)
    Bprime2 = uc.State(str(sqrtLen - 1) + "B''", blue)
    genSys.addState(Bprime2)

    northWallA = uc.State("NA", black)
    genSys.addState(northWallA)
    genSys.addInitialState(northWallA)
    northWallB = uc.State("NB", black)
    genSys.addState(northWallB)
    genSys.addInitialState(northWallB)

    # Adding Affinity Rules
    #       Seed Affinities to start building
    #       Getting offset of B for first B
    affinityB0 = uc.AffinityRule(str(startB) + "B", "SB", "v", 1)
    genSys.addAffinity(affinityB0)
    affinitySeed = uc.AffinityRule("SA", "SB", "h", 1)
    genSys.addAffinity(affinitySeed)

    for i in range(sqrtLen - 1):
        # Affinity Rules to build each column
        affB = uc.AffinityRule(str(i + 1) + "B", str(i) + "B", "v", 1)
        genSys.addAffinity(affB)

    # The last state of the B column allows for A' to attach to the left
    affLB = uc.AffinityRule("A'", str(sqrtLen - 1) + "B", "h", 1)
    genSys.addAffinity(affLB)
    # B prime allows for the B states to attach below
    affAPrime = uc.AffinityRule("A'", "A", "v", 1)
    genSys.addAffinity(affAPrime)
    affADown = uc.AffinityRule("A", "A", "v", 1)
    genSys.addAffinity(affADown)

    #       Affinity Rules to grow the next section of the B column
    affGrowB = uc.AffinityRule("0B", str(sqrtLen - 1) + "B'", "v", 1)
    genSys.addAffinity(affGrowB)

    #<Rule Label1="N" Label2="2A'" Dir="v" Strength="1"></Rule>
    northAff = uc.AffinityRule("NA", str(sqrtLen - 1) + "A'", "v")
    genSys.addAffinity(northAff)

    northWallAff = uc.AffinityRule("NA", "NB", "h")
    genSys.addAffinity(northWallAff)

    # Transition Rules


    # Rule for when A state reaches seed and marked as 0A
    trAseed = uc.TransitionRule("A", "SA", str(startA) + "A", "SA", "v")
    genSys.addTransitionRule(trAseed)

    trAPrimeseed = uc.TransitionRule("A'", "SA", str(startA) + "A'", "SA", "v")
    genSys.addTransitionRule(trAPrimeseed)


    for i in range(sqrtLen):

        # Rule for A state reaches bottom of the column to increment
        if i < sqrtLen - 1:
            trIncA = uc.TransitionRule("A", str(i) + "A'", str(i + 1) + "A", str(i) + "A'", "v")
            genSys.addTransitionRule(trIncA)

        # Rules for propagating the A index upward
        propUp = uc.TransitionRule("A", str(i) + "A", str(i) + "A", str(i) + "A", "v")
        genSys.addTransitionRule(propUp)
        propUpPrime = uc.TransitionRule("A'", str(i) + "A", str(i) + "A'", str(i) + "A", "v")
        genSys.addTransitionRule(propUpPrime)

        # Rule allowing B column to start the next section
        if i < sqrtLen - 1:
            trGrowB = uc.TransitionRule(str(i) + "A'", str(sqrtLen - 1) + "B", str(i) + "A'", str(sqrtLen - 1) + "B'", "h")
            genSys.addTransitionRule(trGrowB)

        trBPrime = uc.TransitionRule("0B", str(sqrtLen - 1) + "B'", "0B", str(sqrtLen - 1) + "B''", "v")
        genSys.addTransitionRule(trBPrime)

        trBPrime1 = uc.TransitionRule("NB", str(sqrtLen - 1) + "B", "NB", str(sqrtLen - 1) + "B''", "v")
        genSys.addTransitionRule(trBPrime1)

    return genSys


# Can be passed an interger or string (binary string)
def genSqrtBinString(value):
    if isinstance(value, int):
        value = bin(value)[2:]

    vLen = len(value)
    sqrtLen = math.ceil(math.sqrt(vLen))

    # Get starting points
    offset = sqrtLen**2 - vLen


    revValue = value[::-1]
    genSys = genDoubleIndexStates(len(value))

    sqrtLen = math.ceil(math.sqrt(len(value)))

    # Add Binary Symbol states
    state0 = uc.State("0s", black)
    state1 = uc.State("1s", white)
    genSys.addState(state0)
    genSys.addState(state1)

    trBPrime0 = uc.TransitionRule("0s", str(sqrtLen - 1) + "B'", "0s", str(sqrtLen - 1) + "B''", "v")
    genSys.addTransitionRule(trBPrime0)
    trBPrime1 = uc.TransitionRule("1s", str(sqrtLen - 1) + "B'", "1s", str(sqrtLen - 1) + "B''", "v")
    genSys.addTransitionRule(trBPrime1)

    for i in range(sqrtLen):
        for j in range(sqrtLen):
            index = (i * sqrtLen) + j
            if index < offset:
                continue

            if j < sqrtLen - 1:
                labelB = str(j) + "B"
            else:
                labelB = str(j) + "B''"

            if j < sqrtLen - 1:
                labelA = str(i) + "A"
            else:
                labelA = str(i) + "A'"


            symbol = str(revValue[index - offset]) + "s"

            tr = uc.TransitionRule(labelA, labelB, labelA, symbol, "h")
            genSys.addTransitionRule(tr)

    return genSys

# Can be passed an interger or string (binary string)
def genSqrtBaseBString(value, base):
    if isinstance(value, int):
        value = bin(value)[2:]


    revValue = value[::-1]
    genSys = genDoubleIndexStates(len(value))

    sqrtLen = math.ceil(math.sqrt(len(value)))

    # Add Binary Symbol states
    for i in range(base):
        if i % 2 == 0:
            color = black
        else:
            color = white

        stateI = uc.State(str(i) + "s", color)
        genSys.addState(stateI)

        trBPrimeI = uc.TransitionRule(str(i) + "s", str(sqrtLen - 1) + "B'", str(i) + "s", str(sqrtLen - 1) + "B''", "v")
        genSys.addTransitionRule(trBPrimeI)

        trBPrimeI = uc.TransitionRule(str(i) + "s", str(sqrtLen - 1) + "B'", str(i) + "s", str(sqrtLen - 1) + "B''", "v")
        genSys.addTransitionRule(trBPrimeI)

    trBPrime = uc.TransitionRule(
        "0B", str(sqrtLen - 1) + "B'", "0B", str(sqrtLen - 1) + "B''", "v")
    genSys.addTransitionRule(trBPrime)


    for i in range(sqrtLen):
        for j in range(sqrtLen):
            if i == sqrtLen - 1:
                labelB = str(j) + "B"
            elif j < sqrtLen - 1:
                labelB = str(j) + "B"
            else:
                labelB = str(j) + "B''"

            if j < sqrtLen - 1:
                labelA = str(i) + "A"
            else:
                labelA = str(i) + "A'"

            index = (i * sqrtLen) + j
            if index < len(value):
                symbol = str(revValue[index]) + "s"
            else:
                symbol = str(base - 1) + "s"

            tr = uc.TransitionRule(labelA, labelB, labelA, symbol, "h")
            genSys.addTransitionRule(tr)

    return genSys


# Can be passed an interger or string (binary string)
def genSqrtBinCount(value):
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

    sqrtLen = math.ceil(math.sqrt(len(value)))

    print("Length: ", value)

    #binString = format(value, "b")
    genSys = genSqrtBinString(value)

    # Add states for binary counter
    state0 = uc.State("0", orange)
    state1 = uc.State("1", green)
    genSys.addState(state0)
    genSys.addState(state1)


    # New Initial States
    # State for indicating carry
    carry = uc.State("c", blue)
    genSys.addState(carry)
    genSys.addInitialState(carry)

    # State for indicating no carry
    noCarry = uc.State("nc", red)
    genSys.addState(noCarry)
    genSys.addInitialState(noCarry)

    ##
    incState = uc.State("+", black)
    genSys.addState(incState)
    genSys.addInitialState(incState)


    # Other States
    northWall = uc.State("N", black)
    genSys.addState(northWall)
    southWall = uc.State("S", black)
    genSys.addState(southWall)

    zeroCarry = uc.State("0c", orange)
    genSys.addState(zeroCarry)

    # <Rule Label1="SB" Label2="+" Dir="h" Strength="1"></Rule>
    incSeed = uc.AffinityRule("SB", "+", "h")
    genSys.addAffinity(incSeed)
    #        <Rule Label1="S" Label2="+" Dir="h" Strength="1"></Rule>
    incAff = uc.AffinityRule("S", "+", "h")
    genSys.addAffinity(incAff)
    #        <Rule Label1="c" Label2="+" Dir="v" Strength="1"></Rule>
    carInc = uc.AffinityRule("c", "+", "v")
    genSys.addAffinity(carInc)
    #        <Rule Label1="c" Label2="0c" Dir="v" Strength="1"></Rule>
    carryAff = uc.AffinityRule("c", "0c", "v")
    genSys.addAffinity(carryAff)
    #        <Rule Label1="nc" Label2="1" Dir="v" Strength="1"></Rule>
    nc1 = uc.AffinityRule("nc", "1", "v")
    genSys.addAffinity(nc1)
    #        <Rule Label1="nc" Label2="0" Dir="v" Strength="1"></Rule>
    nc0 = uc.AffinityRule("nc", "0", "v")
    genSys.addAffinity(nc0)


    # <Rule Label1="0" Label2="c" Label1Final="0" Label2Final="1" Dir="h"></Rule>
    carry0TRi = uc.TransitionRule("0s", "c", "0s", "1", "h")
    genSys.addTransitionRule(carry0TRi)
    # <Rule Label1="0" Label2="nc" Label1Final="0" Label2Final="0" Dir="h"></Rule>
    noCarry0TRi = uc.TransitionRule("0s", "nc", "0s", "0", "h")
    genSys.addTransitionRule(noCarry0TRi)
    # <Rule Label1="1" Label2="c" Label1Final="1" Label2Final="0c" Dir="h"></Rule>
    zeroCarryTRi = uc.TransitionRule("1s", "c", "1s", "0c", "h")
    genSys.addTransitionRule(zeroCarryTRi)
    # <Rule Label1="1" Label2="nc" Label1Final="1" Label2Final="1" Dir="h"></Rule>
    noCarry1TRi = uc.TransitionRule("1s", "nc", "1s", "1", "h")
    genSys.addTransitionRule(noCarry1TRi)
    # <Rule Label1="0" Label2="c" Label1Final="0" Label2Final="1" Dir="h"></Rule>
    carry0TR = uc.TransitionRule("0", "c", "0", "1", "h")
    genSys.addTransitionRule(carry0TR)
    # <Rule Label1="0" Label2="nc" Label1Final="0" Label2Final="0" Dir="h"></Rule>
    noCarry0TR = uc.TransitionRule("0", "nc", "0", "0", "h")
    genSys.addTransitionRule(noCarry0TR)
    # <Rule Label1="1" Label2="c" Label1Final="1" Label2Final="0c" Dir="h"></Rule>
    zeroCarryTR = uc.TransitionRule("1", "c", "1", "0c", "h")
    genSys.addTransitionRule(zeroCarryTR)
    # <Rule Label1="1" Label2="nc" Label1Final="1" Label2Final="1" Dir="h"></Rule>
    noCarry1TR = uc.TransitionRule("1", "nc", "1", "1", "h")
    genSys.addTransitionRule(noCarry1TR)
    # <Rule Label1="1" Label2="+" Label1Final="1" Label2Final="S" Dir="v"></Rule>
    next1TR = uc.TransitionRule("1", "+", "1", "S", "v")
    genSys.addTransitionRule(next1TR)
    # <Rule Label1="0" Label2="+" Label1Final="0" Label2Final="S" Dir="v"></Rule>
    next0TR = uc.TransitionRule("0", "+", "0", "S", "v")
    genSys.addTransitionRule(next0TR)
    # <Rule Label1="1" Label2="0c" Label1Final="1" Label2Final="0" Dir="v"></Rule>
    down1TR = uc.TransitionRule("1", "0c", "1", "0", "v")
    genSys.addTransitionRule(down1TR)
    # <Rule Label1="0" Label2="0c" Label1Final="0" Label2Final="0" Dir="v"></Rule>
    down0TR = uc.TransitionRule("0", "0c", "0", "0", "v")
    genSys.addTransitionRule(down0TR)

    # <Rule Label1="1" Label2="nc" Label1Final="1" Label2Final="1" Dir="h"></Rule>
    northPropB = uc.TransitionRule("NB", "nc", "NB", "N", "h")
    genSys.addTransitionRule(northPropB)
    northProp = uc.TransitionRule("N", "nc", "N", "N", "h")
    genSys.addTransitionRule(northProp)

    return genSys


def genSqrtBaseBCount(value, base=None):
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

    if base == None:
        # To do, calculate optimal base
        base = 10

    sqrtLen = math.ceil(math.sqrt(len(value)))

    print("Length: ", value)

    #binString = format(value, "b")
    genSys = genSqrtBaseBString(value, base)

    # Add states for binary counter
    for i in range(base):
        if i % 2 == 0:
            color = black
        else:
            color = white
        stateI = uc.State(str(i), color)
        genSys.addState(stateI)

    # New Initial States
    # State for indicating carry
    carry = uc.State("c", blue)
    genSys.addState(carry)
    genSys.addInitialState(carry)

    # State for indicating no carry
    noCarry = uc.State("nc", red)
    genSys.addState(noCarry)
    genSys.addInitialState(noCarry)

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

    zeroCarry = uc.State("0c", orange)
    genSys.addState(zeroCarry)

    # <Rule Label1="SB" Label2="+" Dir="h" Strength="1"></Rule>
    incSeed = uc.AffinityRule("SB", "+", "h")
    genSys.addAffinity(incSeed)
    #        <Rule Label1="S" Label2="+" Dir="h" Strength="1"></Rule>
    incAff = uc.AffinityRule("S", "+", "h")
    genSys.addAffinity(incAff)
    #        <Rule Label1="c" Label2="+" Dir="v" Strength="1"></Rule>
    carInc = uc.AffinityRule("c", "+", "v")
    genSys.addAffinity(carInc)
    #        <Rule Label1="c" Label2="0c" Dir="v" Strength="1"></Rule>
    carryAff = uc.AffinityRule("c", "0c", "v")
    genSys.addAffinity(carryAff)

    for i in range(base):
        #        <Rule Label1="nc" Label2="1" Dir="v" Strength="1"></Rule>
        nc1 = uc.AffinityRule("nc", str(i), "v")
        genSys.addAffinity(nc1)
        nc1s = uc.AffinityRule("nc", str(i) + "s", "v")
        genSys.addAffinity(nc1s)

        if i < base - 1:
            # <Rule Label1="0" Label2="c" Label1Final="0" Label2Final="1" Dir="h"></Rule>
            carry0TR = uc.TransitionRule(str(i), "c", str(i), str(i + 1), "h")
            genSys.addTransitionRule(carry0TR)
            carry0TRs = uc.TransitionRule(str(i) + "s", "c", str(i) + "s", str(i + 1), "h")
            genSys.addTransitionRule(carry0TRs)
        else:
            # <Rule Label1="1" Label2="c" Label1Final="1" Label2Final="0c" Dir="h"></Rule>
            zeroCarryTR = uc.TransitionRule(str(i), "c", (str(i)), "0c", "h")
            genSys.addTransitionRule(zeroCarryTR)
            zeroCarryTRs = uc.TransitionRule(str(i) + "s", "c", str(i) + "s", "0c", "h")
            genSys.addTransitionRule(zeroCarryTRs)


        # <Rule Label1="0" Label2="nc" Label1Final="0" Label2Final="0" Dir="h"></Rule>
        noCarryTR = uc.TransitionRule(str(i), "nc", str(i), str(i), "h")
        genSys.addTransitionRule(noCarryTR)
        noCarryTRs = uc.TransitionRule(str(i) + "s", "nc", str(i) + "s", str(i), "h")
        genSys.addTransitionRule(noCarryTRs)


        # <Rule Label1="1" Label2="+" Label1Final="1" Label2Final="S" Dir="v"></Rule>
        nextTR = uc.TransitionRule(str(i), "+", str(i), "S", "v")
        genSys.addTransitionRule(nextTR)

        # <Rule Label1="1" Label2="0c" Label1Final="1" Label2Final="0" Dir="v"></Rule>
        downTR = uc.TransitionRule(str(i), "0c", str(i), "0", "v")
        genSys.addTransitionRule(downTR)

    return genSys


def genString(value, base=None):
    if base == None:
        return genSqrtBinString(value)

def genRect(length, base=None):
    if base == None:
        return genSqrtBinCount(length)

def genNFLine(value, base=10):
    value = str(int(value) - len(value) - 1)

    seedLabel = value[0] + "_0"

    inpStates = [seedLabel]

    seed = uc.State(seedLabel, blue)
    sys = uc.System(1, [seed], [], [seed])

    for i in range(1, len(value)):
        iLabel = value[i] + "_" + str(i)
        inpStates.append(iLabel)
        iState = uc.State(iLabel, blue)
        sys.addInitialState(iState)
        sys.addState(iState)

    for i in range(base):
        #littleA = uc.State(str(i) + "a", red)
        #sys.addState(littleA)
        #sys.addInitialState(littleA)

        #bigB = uc.State(str(i) + "B", blue)
        #sys.addState(bigB)
        #sys.addInitialState(bigB)

        # Blue States is the 'top of the loop', we always return to an assembly with all the blue tiles and it grows 1
        blueI = uc.State(str(i), blue)
        sys.addState(blueI)

        # Red states are waiting states
        redR = uc.State(str(i) + "r", red)
        sys.addState(redR)

    # decrement attaches on the right and decrements the number
    decr = uc.State("-", orange)
    sys.addState(decr)

    # State to copy digit
    Buffer = uc.State("B", white)
    sys.addState(Buffer)
    sys.addInitialState(Buffer)

    BufferP = uc.State("B'", white)
    sys.addState(BufferP)

    # State when needing to borrow
    borrow = uc.State("br", green)
    sys.addState(borrow)

    # State to copy digit
    copy = uc.State("cp", orange)
    sys.addState(copy)

    # State to copy digit
    xState = uc.State("X", white)
    sys.addState(xState)


    ## Affinity Rules

    # TEMP Build our starting assembly
    for i in range(len(inpStates) - 1):
        inpAff = uc.AffinityRule(inpStates[i], inpStates[i + 1], "h", 1)
        sys.addAffinity(inpAff)

    # Aff to attach first buffer
    lastInp = inpStates[len(inpStates) - 1]
    inpDecAff = uc.AffinityRule(lastInp, "B", "h", 1)
    sys.addAffinity(inpDecAff)

    # Aff to attach decr
    for i in range(base):
        decAff = uc.AffinityRule(str(i), "-", "h", 1)
        sys.addAffinity(decAff)

    # Aff for buffer to attach
    bufferAff = uc.AffinityRule("B'", "B", "h", 1)
    sys.addAffinity(bufferAff)

    ## Transition Rules

    # TEMP first buffer
    bufferInp = uc.TransitionRule(lastInp, "B", lastInp, "B'", "h")
    sys.addTransitionRule(bufferInp)

    # TEMP first decrement
    intLast = int(lastInp[0])
    if intLast == 0:
        fstDec = uc.TransitionRule(lastInp, "-", "cp", "br", "h")
        sys.addTransitionRule(fstDec)
    else:
        fstDecLabel2 = str(intLast - 1) + "r"
        fstDec = uc.TransitionRule(lastInp, "-", "cp", fstDecLabel2, "h")
        sys.addTransitionRule(fstDec)

    # TEMP First copy step
    for i in range(1, len(inpStates) - 1):
        fstCopyTR = uc.TransitionRule(inpStates[i], "cp", "cp", inpStates[i][0] + "r", "h")
        sys.addTransitionRule(fstCopyTR)

    fstBitCP = uc.TransitionRule(inpStates[0], "cp", "X", inpStates[0][0], "h")
    sys.addTransitionRule(fstBitCP)

    # Change Buffer to dec
    bufDec = uc.TransitionRule("B'", "B", "-", "B", "h")
    sys.addTransitionRule(bufDec)

    # Flip red state to blue state
    for i in range(base):
        for j in range(base):
            blueRed = uc.TransitionRule(str(i), str(j) + "r", str(i), str(j), "h")
            sys.addTransitionRule(blueRed)


    for i in range(base):
        if i > 0:
            # Decrement blue states
            blueDec = uc.TransitionRule(str(i), "-", "cp", str(i - 1) + "r", "h")
            sys.addTransitionRule(blueDec)

            # Borrow from blue states
            blueBr = uc.TransitionRule(str(i), "br", str(i - 1), str(base - 1), "h")
            sys.addTransitionRule(blueBr)

            # X turns red states into blue states
            redX = uc.TransitionRule("X", str(i) + "r", "X", str(i), "h")
            sys.addTransitionRule(redX)

        # Blue states turn buffers into buffer primes
        blueBuffer = uc.TransitionRule(str(i), "B", str(i), "B'", "h")
        sys.addTransitionRule(blueBuffer)

        # Copy blue states
        blueCP = uc.TransitionRule(str(i), "cp", "cp", str(i) + "r", "h")
        sys.addTransitionRule(blueCP)





    # Dec 0 goes to borrow
    dec0 = uc.TransitionRule("0", "-", "cp", "br", "h")
    sys.addTransitionRule(dec0)

    # Borrow from blue 0
    br0 = uc.TransitionRule("0", "br", "br", str(base - 1) + "r", "h")
    sys.addTransitionRule(br0)

    # X turns 0r to X
    x0 = uc.TransitionRule("X", "0r", "X", "X", "h")
    sys.addTransitionRule(x0)

    # Copy hits X it goes to X
    copyX = uc.TransitionRule("X", "cp", "X", "X", "h")
    sys.addTransitionRule(copyX)



    return sys

if __name__ == "__main__":
    sys = genSqrtBaseBCount("956217662", 10)
    SaveFile.main(sys, ["doubleTest.xml"])

    #flag = 0

    #if(flag == 0):



        #states = sys.returnStates()



        #SaveFile.main(sys, ["tripleTest.xml"])

    #if(flag == 1):
        #value = input("Please Enter an interger")
        #sys = genSqrtBinCount(int(value))
        #fileName = input("Please Enter file name: ")  + ".xml"

        #SaveFile.main(sys, [fileName])
        #print("Generated File: saved as ", fileName)
