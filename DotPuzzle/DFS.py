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
        self.isSolFound = False

    # add initial root state also update initial step for solution
    def addRoot(self, rootState):
        self.openList.append(rootState)
        self.solution.append(["0", rootState])
        self.current_d = 1
        self.virtualDP.import1DState(rootState)

    def doSearch(self):
        # TODO 
        if(self.current_d >= self.max_d):
            # back 1 depth up
        # pick a dot  
        dot = ["y", 0]
        # try touch dot
        self.virtualDP.touch(dot[0],dot[1])
        nextState = self.virtualDP.get1DState()
        if(self.isVisited(nextState)):
            # back to last state by touching same dot
            self.virtualDP.touch(dot[0],dot[1])
        else:
            self.current_d += 1
            self.visited.append(nextState)
            self.closedList.append(nextState)
            self.solution.append([dot[0]+str(dot[1]), nextState])
            if(self.isGoalState(nextState)):
                break
        


    # check if the state is visited
    def isVisited(self, stateNode):
        isVisited = False
        for i in range(self.visited):
            if(stateNode == self.visited[i]):
                isVisited = True
                break
        return isVisited

    # check if state is a goal state 
    # and update isSolFound as True
    # and return bool
    def isGoalState(self,state):
        goalState = state.replace("1","0")
        if(state == goalState):
            self.isSolFound = True
            return True
        else:
            return False

    # go back to parent state of current state
    # def backToParentState(self):
    #     lastTouch = self.solution[len(self.solution)-1]
    #     self.virtualDP.touch(lastTouch[0])

    # TODO generateCurrentDepthAvailableState