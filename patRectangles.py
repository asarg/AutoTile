import UniversalClasses as uc
# Importing Generators from squares paper
import detGen 


def doublePat(pattern):
    colors = ["f03a47", "3f88c5", "0ead69"]
    strSys = []

    for i in range(3):
        strSys.append(detGen.genSqrtBaseBString(pattern, 3, colors[i]))

    firstColor = int(pattern[0])
    mainSys = strSys[firstColor]

    return mainSys






