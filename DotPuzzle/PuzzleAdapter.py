# import DotPuzzle

class PuzzleAdapter:
    #constructor
    def __init__(self, n, max_d, max_l, state_1d):
        self.n = n
        self.max_d = max_d
        self.max_l = max_l
        self.state_1d = state_1d

    def getDimension(self):
        return self.n

    def getMaxDeepth(self):
        return self.max_d

    def getMaxSearchPathLength(self):
        return self.max_l

    def get1DState(self):
        return self.state_1d

    # def get2DSate():
        

    
