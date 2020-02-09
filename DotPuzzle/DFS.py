import DotPuzzle as dp

class DFS:
    # constructor add Max depth limit
    def __init__(self, max_d):
        self.closedList = []
        self.openList = []
        self.visited = [] # = search path
        self.solution = []
        self.current_d = 0
        self.max_d = max_d
        self.virtualDP = dp.DotPuzzle(2)  # here can be any number. after import it will be replaced

    # add initial root state also update initial step for solution
    def addRoot(self, rootState):
        self.openList.append(rootState)
        self.solution.append(["0", rootState])
        self.current_d = 1
        self.virtualDP.import1DState(rootState)

    def doSearch(self):
        pass
