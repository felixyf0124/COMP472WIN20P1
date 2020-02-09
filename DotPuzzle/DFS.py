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
        self.virtualDP = dp.DotPuzzle(3)  # here can be any number. after import it will be replaced
        self.isSolFound = False

    # add initial root state also update initial step for solution
    def addRoot(self, rootState):
        self.openList.append(rootState)
        self.solution.append(["0", 0, rootState])
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
        if(self.isClosed(nextState)):
            # back to last state by touching same dot
            self.virtualDP.touch(dot[0],dot[1])
        else:
            self.current_d += 1
            self.visited.append(nextState)
            self.closedList.append(nextState)
            self.solution.append([dot[0], dot[1], nextState])
            if(self.isGoalState(nextState)):
                break
        


    # check if the state is closed
    def isClosed(self, stateNode):
        isClosed = False
        for i in range(self.closedList):
            if(stateNode == self.closedList[i]):
                isClosed = True
                break
        return isClosed

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

    # return next available state with associated dot in the same depth level
    # TODO option: make a parent class and move this to parent class?
    def generateNextAvailableState(self):
        lastTouch = self.solution[len(self.solution)-1]
        nextAvailable = []
        puzzleM = dp.DotPuzzle(3)
        puzzleM.import1DState(lastTouch[2])
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for j in range(puzzleM.n):
            for i in range(puzzleM.n):
                dot = [alpha[j], i]
                puzzleM.touch(dot[0],dot[1]) # touch it so we can get the next state
                state1D = pupuzzleM.get1DState() 
                available = [dot[0],dot[1],state1D]
                nextAvailable.append(available) # add to nextAvailable list
                puzzleM.touch(dot[0],dot[1]) # touch it again so it go back to the last state (parent)

        # so far we got all same level states with dot positions to touch
        # we have to filter what is not available in the list
        # as long as it is not the root state, the parent state's touch dot should be unavailable
        # because touching the same dot will go back to its last state (grand parent)
        # benefit of filtering this is because its max O(n) is n x n, size of the board
        # which is fixed and much less than O(n) of iterating the closed list after a while of search
        if(lastTouch[0] != "0"):
            for i in range(len(nextAvailable)):
                if(lastTouch[0] == nextAvailable[i][0]
                && lastTouch[1] == nextAvailable[i][1]):
                    del nextAvailable[i]
                    break
        # del list
        unavailableIndex = []
        for i in range(len(nextAvailable)):
            if(self.isClosed(nextAvailable[i][2])):
                unavailableIndex.append(i)
        
        # del from the last to the first so we won't be bothered by the changed subsequence
        for i in sorted(unavailableIndex, reverse=True):
            del nextAvailable[i]
            
        return nextAvailable



