import UniversalClasses as uc

class ActiveStateRegion:
    def __init__(self):
        self.seed_states = []
        self.genSys = uc.System(1, [], [], [self.seed_states], [], [], [], [], [], [], None, False)

    def returnASR(self):
        return self.genSys