import UniversalClasses as uc
import SaveFile
import detGen
import oneSidedGen
import nonDetGen
import squareGen


red = "f03a47"
blue = "3f88c5"
green = "0ead69"
orange = "f39237"
black = "323031"
white = "DFE0E2"
grey = "9EA9A4"
light_blue = "C2DCFE"

# This function handles all generators from UI
def generator(shape, value, model):
    
    if model == "Deterministic":
        if shape == "Strings":
            return detGen.genString(value)
        if shape == "Rectangle":
            value = int(value)
            return detGen.genRect(value - 1)


    if model == "Single-Transition":
        if shape == "Strings":
            return oneSidedGen.genString(value)
        if shape == "Rectangle":
            value = int(value)
            return oneSidedGen.genRect(value - 1)   

    if model == "Non-Deterministic":
        if shape == "Strings":
            return nonDetGen.genString(value)
        if shape == "Rectangle":
            value = int(value)
            return nonDetGen.genRect(value - 1)    

    if shape == "Squares":
        value = int(value)
        return squareGen.genSquare(value, model)

    if shape == "Lines":
        return detGen.genNFLine(value)





def genSamples():
    # Sample determinsitic systems
    sys1 = detGen.genDoubleIndexStates(9)
    SaveFile.main(sys1, ["XML Files/samples/IndexStates/smallIndexStatesDet.xml"])

    sys2 = detGen.genDoubleIndexStates(100)
    SaveFile.main(sys2, ["XML Files/samples/IndexStates/largeIndexStatesDet.xml"])

    sys3 = detGen.genSqrtBinString("110011010")
    SaveFile.main(sys3, ["XML Files/samples/Strings/smallBinStringDet.xml"])

    sys4 = detGen.genSqrtBinString("1100110101101010101100110")
    SaveFile.main(sys4, ["XML Files/samples/Strings/largeBinStringDet.xml"])

    sys5 = detGen.genSqrtBinCount(50)
    SaveFile.main(sys5, ["XML Files/samples/Counters/smallBinCountDet.xml"])

    sys6 = detGen.genSqrtBinCount(125)
    SaveFile.main(sys6, ["XML Files/samples/Counters/largeBinCountDet.xml"])

    sys7 = detGen.genSqrtBaseBString("123456789", 10)
    SaveFile.main(sys7, ["XML Files/samples/Strings/smallDecimalStringDet.xml"])

    sys8 = detGen.genSqrtBaseBString("123456789012345", 10)
    SaveFile.main(sys8, ["XML Files/samples/Strings/largeDecimalStringDet.xml"])

    sys9 = detGen.genSqrtBaseBCount("9950", 10)
    SaveFile.main(sys9, ["XML Files/samples/Counters/smallDecimalCountDet.xml"])

    sys10 = detGen.genSqrtBaseBCount("999999000", 10)
    SaveFile.main(sys10, ["XML Files/samples/Counters/largeDecimalCountDet.xml"])

    # Sample One Sided systems
    sys11 = oneSidedGen.genTripleIndexStates(27)
    SaveFile.main(sys11, ["XML Files/samples/IndexStates/smallIndexStatesSR.xml"])

    sys12 = oneSidedGen.genTripleIndexStates(125)
    SaveFile.main(sys12, ["XML Files/samples/IndexStates/largeIndexStatesSR.xml"])

    sys13 = oneSidedGen.cbrtBinString("110011010110011010110011010")
    SaveFile.main(sys13, ["XML Files/samples/Strings/BinStringSR.xml"])

    sys14 = oneSidedGen.cbrtBinCount(1000)
    SaveFile.main(sys14, ["XML Files/samples/Counters/BinCountSR.xml"])

    # Sample General systems
    sys15 = nonDetGen.genQuadIndexStates(81)
    SaveFile.main(sys15, ["XML Files/samples/IndexStates/IndexStatesND.xml"])

    num = ""

    for i in range(27):
        num += "101"

    sys16 = nonDetGen.genQuadBinString(num)
    SaveFile.main(sys16, ["XML Files/samples/Strings/BinStringND.xml"])

    sys16 = nonDetGen.quadBinCount(1500)
    SaveFile.main(sys16, ["XML Files/samples/Counters/BinCountND.xml"])

if __name__ == "__main__":
    genSamples()