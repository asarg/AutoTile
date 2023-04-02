import Generators.IU_Generators.Old_IU_Files.activeStateRegion as asr
import UniversalClasses as uc
import Generators.IU_Generators.Old_IU_Files.IUEqualityChanges as iuec



class SampleGenerator:
    def __init__(self, gadgetRegion):
        if gadgetRegion == "Active State Region":
            return asr.ActiveStateRegion()
        else:
            return None

class IUGenerators:
    def __init__(self, gadgetName):
        if gadgetName == "MacroCell Sample":
            self.MacroCellSample()

    def MacroCellSample(self):
        s = iuec.IUGenerators_EC("MacroCell Sample")

        return s.macroCellCopyNorthTest()
