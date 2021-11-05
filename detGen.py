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

    # Create States and add to lists

    for i in range(sqrtLen):
        # Big A states
        bigAState = uc.State(str(i) + "A", red)
        genSys.add_State(bigAState)
        # A' (prime) states
        aPrime = uc.State(str(i) + "A'", red)
        genSys.add_State(aPrime)
        # B states (Initial States)
        bState = uc.State(str(i) + "B", blue)
        genSys.add_State(bState)
        genSys.add_Initial_State(bState)

    # Blank A and A' states
    singleA = uc.State("A", red)
    genSys.add_State(singleA)
    genSys.add_Initial_State(singleA)
    singleAPrime = uc.State("A'", red)
    genSys.add_State(singleAPrime)
    genSys.add_Initial_State(singleAPrime)
    # Seed States
    genSys.add_State(seedA)
    seedB = uc.State("SB", black)
    #     seedB is an Initial State
    genSys.add_Initial_State(seedB)
    genSys.add_State(seedB)
    # B prime states
    Bprime = uc.State(str(sqrtLen - 1) + "B'", blue)
    genSys.add_State(Bprime)
    Bprime2 = uc.State(str(sqrtLen - 1) + "B''", blue)
    genSys.add_State(Bprime2)

    # Adding Affinity Rules
    #       Seed Affinities to start building
    affinityB0 = uc.AffinityRule("0B", "SB", "v", 1)
    genSys.add_affinity(affinityB0)
    affinitySeed = uc.AffinityRule("SA", "SB", "h", 1)
    genSys.add_affinity(affinitySeed)

    for i in range(sqrtLen - 1):
        # Affinity Rules to build each column
        affB = uc.AffinityRule(str(i + 1) + "B", str(i) + "B", "v", 1)
        genSys.add_affinity(affB)

    # The last state of the B column allows for A' to attach to the left 
    affLB = uc.AffinityRule("A'", str(sqrtLen - 1) + "B", "h", 1)
    genSys.add_affinity(affLB)
    # B prime allows for the B states to attach below
    affAPrime = uc.AffinityRule("A'", "A", "v", 1)
    genSys.add_affinity(affAPrime)
    affADown = uc.AffinityRule("A", "A", "v", 1)
    genSys.add_affinity(affADown)

    #       Affinity Rules to grow the next section of the B column
    affGrowB = uc.AffinityRule("0B", str(sqrtLen - 1) + "B'", "v", 1)
    genSys.add_affinity(affGrowB)

    # Transition Rules


    # Rule for when A state reaches seed and marked as 0A
    trAseed = uc.TransitionRule("A", "SA", "0A", "SA", "v")
    genSys.add_transition_rule(trAseed)



    for i in range(sqrtLen):
        # Rule for continued propagation of A state downward
        if i < sqrtLen - 2:
            Aprop = uc.TransitionRule("A", str(i) + "a", "A", "A", "v")
            genSys.add_transition_rule(Aprop)

        # Rule for A state reaches bottom of the column to increment
        if i < sqrtLen - 1:
            trIncA = uc.TransitionRule(
                "A", str(i) + "A'", str(i + 1) + "A", str(i) + "A'", "v")
            genSys.add_transition_rule(trIncA)

        # Rules for propagating the A index upward
        propUp = uc.TransitionRule(
            "A", str(i) + "A", str(i) + "A", str(i) + "A", "v")
        genSys.add_transition_rule(propUp)
        propUpPrime = uc.TransitionRule(
            "A'", str(i) + "A", str(i) + "A'", str(i) + "A", "v")
        genSys.add_transition_rule(propUpPrime)

        # Rule allowing B column to start the next section
        if i < sqrtLen - 1:
            trGrowB = uc.TransitionRule(str(
                i) + "A'", str(sqrtLen - 1) + "B", str(i) + "A'", str(sqrtLen - 1) + "B'", "h")
            genSys.add_transition_rule(trGrowB)

    return genSys


# Can be passed an interger or string (binary string)
def genSqrtBinString(value):
    if isinstance(value, int):
        value = bin(value)[2:]


    revValue = value[::-1]
    genSys = genDoubleIndexStates(len(value))

    sqrtLen = math.ceil(math.sqrt(len(value)))

    # Add Binary Symbol states
    state0 = uc.State("0i", orange)
    state1 = uc.State("1i", green)
    genSys.add_State(state0)
    genSys.add_State(state1)

    trBPrime = uc.TransitionRule(
        "0B", str(sqrtLen - 1) + "B'", "0B", str(sqrtLen - 1) + "B''", "v")
    genSys.add_transition_rule(trBPrime)

    trBPrime1 = uc.TransitionRule(
        "1i", str(sqrtLen - 1) + "B'", "1i", str(sqrtLen - 1) + "B''", "v")
    genSys.add_transition_rule(trBPrime1)

    trBPrime0 = uc.TransitionRule(
        "0i", str(sqrtLen - 1) + "B'", "0i", str(sqrtLen - 1) + "B''", "v")
    genSys.add_transition_rule(trBPrime0)

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
                symbol = str(revValue[index]) + "i"
            else:
                symbol = "1i"

            tr = uc.TransitionRule(labelA, labelB, labelA, symbol, "h")
            genSys.add_transition_rule(tr)

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
        genSys.add_State(stateI)

        trBPrimeI = uc.TransitionRule(
            str(i) + "s", str(sqrtLen - 1) + "B'", str(i) + "s", str(sqrtLen - 1) + "B''", "v")
        genSys.add_transition_rule(trBPrimeI)

    trBPrime = uc.TransitionRule(
        "0B", str(sqrtLen - 1) + "B'", "0B", str(sqrtLen - 1) + "B''", "v")
    genSys.add_transition_rule(trBPrime)


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
            genSys.add_transition_rule(tr)

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
    genSys.add_State(state0)
    genSys.add_State(state1)


    # New Initial States
    # State for indicating carry
    carry = uc.State("c", blue)
    genSys.add_State(carry)
    genSys.add_Initial_State(carry)

    # State for indicating no carry
    noCarry = uc.State("nc", red)
    genSys.add_State(noCarry)
    genSys.add_Initial_State(noCarry)

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

    zeroCarry = uc.State("0c", orange)
    genSys.add_State(zeroCarry)

    #<Rule Label1="N" Label2="2A'" Dir="v" Strength="1"></Rule>
    northAff = uc.AffinityRule("N", str(sqrtLen - 1) + "A'", "v")
    genSys.add_affinity(northAff)
    # <Rule Label1="SB" Label2="+" Dir="h" Strength="1"></Rule>
    incSeed = uc.AffinityRule("SB", "+", "h")
    genSys.add_affinity(incSeed)
    #        <Rule Label1="S" Label2="+" Dir="h" Strength="1"></Rule>
    incAff = uc.AffinityRule("S", "+", "h")
    genSys.add_affinity(incAff)
    #        <Rule Label1="c" Label2="+" Dir="v" Strength="1"></Rule>
    carInc = uc.AffinityRule("c", "+", "v")
    genSys.add_affinity(carInc)
    #        <Rule Label1="c" Label2="0c" Dir="v" Strength="1"></Rule>
    carryAff = uc.AffinityRule("c", "0c", "v")
    genSys.add_affinity(carryAff)
    #        <Rule Label1="nc" Label2="1" Dir="v" Strength="1"></Rule>
    nc1 = uc.AffinityRule("nc", "1", "v")
    genSys.add_affinity(nc1)
    #        <Rule Label1="nc" Label2="0" Dir="v" Strength="1"></Rule>
    nc0 = uc.AffinityRule("nc", "0", "v")
    genSys.add_affinity(nc0)

    #        <Rule Label1="nc" Label2="1" Dir="v" Strength="1"></Rule>
    nc1 = uc.AffinityRule("N", "1i", "v")
    genSys.add_affinity(nc1)
    #        <Rule Label1="nc" Label2="0" Dir="v" Strength="1"></Rule>
    nc0 = uc.AffinityRule("N", "0i", "v")
    genSys.add_affinity(nc0)

    # <Rule Label1="0" Label2="c" Label1Final="0" Label2Final="1" Dir="h"></Rule>
    carry0TRi = uc.TransitionRule("0i", "c", "0i", "1", "h")
    genSys.add_transition_rule(carry0TRi)
    # <Rule Label1="0" Label2="nc" Label1Final="0" Label2Final="0" Dir="h"></Rule>
    noCarry0TRi = uc.TransitionRule("0i", "nc", "0i", "0", "h")
    genSys.add_transition_rule(noCarry0TRi)
    # <Rule Label1="1" Label2="c" Label1Final="1" Label2Final="0c" Dir="h"></Rule>
    zeroCarryTRi = uc.TransitionRule("1i", "c", "1i", "0c", "h")
    genSys.add_transition_rule(zeroCarryTRi)
    # <Rule Label1="1" Label2="nc" Label1Final="1" Label2Final="1" Dir="h"></Rule>
    noCarry1TRi = uc.TransitionRule("1i", "nc", "1i", "1", "h")
    genSys.add_transition_rule(noCarry1TRi)
    # <Rule Label1="0" Label2="c" Label1Final="0" Label2Final="1" Dir="h"></Rule>
    carry0TR = uc.TransitionRule("0", "c", "0", "1", "h")
    genSys.add_transition_rule(carry0TR)
    # <Rule Label1="0" Label2="nc" Label1Final="0" Label2Final="0" Dir="h"></Rule>
    noCarry0TR = uc.TransitionRule("0", "nc", "0", "0", "h")
    genSys.add_transition_rule(noCarry0TR)
    # <Rule Label1="1" Label2="c" Label1Final="1" Label2Final="0c" Dir="h"></Rule>
    zeroCarryTR = uc.TransitionRule("1", "c", "1", "0c", "h")
    genSys.add_transition_rule(zeroCarryTR)
    # <Rule Label1="1" Label2="nc" Label1Final="1" Label2Final="1" Dir="h"></Rule>
    noCarry1TR = uc.TransitionRule("1", "nc", "1", "1", "h")
    genSys.add_transition_rule(noCarry1TR)
    # <Rule Label1="1" Label2="+" Label1Final="1" Label2Final="S" Dir="v"></Rule>
    next1TR = uc.TransitionRule("1", "+", "1", "S", "v")
    genSys.add_transition_rule(next1TR)
    # <Rule Label1="0" Label2="+" Label1Final="0" Label2Final="S" Dir="v"></Rule>
    next0TR = uc.TransitionRule("0", "+", "0", "S", "v")
    genSys.add_transition_rule(next0TR)
    # <Rule Label1="1" Label2="0c" Label1Final="1" Label2Final="0" Dir="v"></Rule>
    down1TR = uc.TransitionRule("1", "0c", "1", "0", "v")
    genSys.add_transition_rule(down1TR)
    # <Rule Label1="0" Label2="0c" Label1Final="0" Label2Final="0" Dir="v"></Rule>
    down0TR = uc.TransitionRule("0", "0c", "0", "0", "v")
    genSys.add_transition_rule(down0TR)

    # <Rule Label1="1" Label2="nc" Label1Final="1" Label2Final="1" Dir="h"></Rule>
    northProp = uc.TransitionRule("N", "nc", "N", "N", "h")
    genSys.add_transition_rule(northProp)

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
        genSys.add_State(stateI)

    # New Initial States
    # State for indicating carry
    carry = uc.State("c", blue)
    genSys.add_State(carry)
    genSys.add_Initial_State(carry)

    # State for indicating no carry
    noCarry = uc.State("nc", red)
    genSys.add_State(noCarry)
    genSys.add_Initial_State(noCarry)

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

    zeroCarry = uc.State("0c", orange)
    genSys.add_State(zeroCarry)

    #<Rule Label1="N" Label2="2A'" Dir="v" Strength="1"></Rule>
    northAff = uc.AffinityRule("N", str(sqrtLen - 1) + "A'", "v")
    genSys.add_affinity(northAff)
    # <Rule Label1="SB" Label2="+" Dir="h" Strength="1"></Rule>
    incSeed = uc.AffinityRule("SB", "+", "h")
    genSys.add_affinity(incSeed)
    #        <Rule Label1="S" Label2="+" Dir="h" Strength="1"></Rule>
    incAff = uc.AffinityRule("S", "+", "h")
    genSys.add_affinity(incAff)
    #        <Rule Label1="c" Label2="+" Dir="v" Strength="1"></Rule>
    carInc = uc.AffinityRule("c", "+", "v")
    genSys.add_affinity(carInc)
    #        <Rule Label1="c" Label2="0c" Dir="v" Strength="1"></Rule>
    carryAff = uc.AffinityRule("c", "0c", "v")
    genSys.add_affinity(carryAff)

    for i in range(base):
        #        <Rule Label1="nc" Label2="1" Dir="v" Strength="1"></Rule>
        nc1 = uc.AffinityRule("nc", str(i), "v")
        genSys.add_affinity(nc1)
        nc1s = uc.AffinityRule("nc", str(i) + "s", "v")
        genSys.add_affinity(nc1s)

        if i < base - 1:
            # <Rule Label1="0" Label2="c" Label1Final="0" Label2Final="1" Dir="h"></Rule>
            carry0TR = uc.TransitionRule(str(i), "c", str(i), str(i + 1), "h")
            genSys.add_transition_rule(carry0TR)
            carry0TRs = uc.TransitionRule(str(i) + "s", "c", str(i) + "s", str(i + 1), "h")
            genSys.add_transition_rule(carry0TRs)
        else:
            # <Rule Label1="1" Label2="c" Label1Final="1" Label2Final="0c" Dir="h"></Rule>
            zeroCarryTR = uc.TransitionRule(str(i), "c", (str(i)), "0c", "h")
            genSys.add_transition_rule(zeroCarryTR)
            zeroCarryTRs = uc.TransitionRule(str(i) + "s", "c", str(i) + "s", "0c", "h")
            genSys.add_transition_rule(zeroCarryTRs)


        # <Rule Label1="0" Label2="nc" Label1Final="0" Label2Final="0" Dir="h"></Rule>
        noCarryTR = uc.TransitionRule(str(i), "nc", str(i), str(i), "h")
        genSys.add_transition_rule(noCarryTR)
        noCarryTRs = uc.TransitionRule(str(i) + "s", "nc", str(i) + "s", str(i), "h")
        genSys.add_transition_rule(noCarryTRs)


        # <Rule Label1="1" Label2="+" Label1Final="1" Label2Final="S" Dir="v"></Rule>
        nextTR = uc.TransitionRule(str(i), "+", str(i), "S", "v")
        genSys.add_transition_rule(nextTR)

        # <Rule Label1="1" Label2="0c" Label1Final="1" Label2Final="0" Dir="v"></Rule>
        downTR = uc.TransitionRule(str(i), "0c", str(i), "0", "v")
        genSys.add_transition_rule(downTR)

    return genSys


def genString(value, base=None):
    if base == None:
        return genSqrtBinString(value)

def genRect(length, base=None):
    if base == None:
        return genSqrtBinCount(length)



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









