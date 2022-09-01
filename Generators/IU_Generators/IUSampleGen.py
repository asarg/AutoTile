import Generators.IU_Generators.activeStateRegion as asr
import UniversalClasses as uc


class SampleGenerator:
    def __init__(self, gadgetRegion):
        if gadgetRegion == "Active State Region":
            return asr.ActiveStateRegion()
        else:
            return None
