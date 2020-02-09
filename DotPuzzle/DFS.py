import DotPuzzle as dp


class DFS:
    # constructor add Max depth limit
    def __init__(self, max_d):
        self.closedList = []  # = search path
        self.openList = []
        self.visited = []
        self.solution = []
        self.current_d = 0
        self.max_d = max_d
        # here can be any number. after import it will be replaced
        self.virtualDP = dp.DotPuzzle(3)
        self.isSolFound = False

    # add initial root state also update initial step for solution
    def addRoot(self, rootState):
        self.openList.append(["0", 0, rootState])
        self.solution.append(["0", 0, rootState])
        self.current_d = 1
        self.virtualDP.import1DState(rootState)

    def doSearch(self):
        # TODO add one more check if low level dept available state is token by the high level one

        available = self.openList[0]

        if (available[0] == "0"):
            self.visited = available[0]
            nextAvailable = self.generateNextAvailableState()
            self.closedList.append(available)
            del self.openList[0]
            self.openList.extend(nextAvailable)
            for i in range(len(nextAvailable)):
                self.doSearch()
            return
        else:
            # pick a dot
            dot = [available[0], available[1]]
            # try touch dot
            self.virtualDP.touch(dot[0], dot[1])
            nextState = self.virtualDP.get1DState()
            if(nextState != available[2]):
                raise Exception(
                    "Error: touch dot not matching the associated state")
            if(self.isClosed(nextState)):
                # back to last state by touching same dot
                self.virtualDP.touch(dot[0], dot[1])
                raise Exception(
                    "Error: available state in open list should not be closed")
            else:
                self.current_d += 1
                self.visited = available
                nextAvailable = self.generateNextAvailableState()
                self.closedList.append(available)
                del self.openList[0]
                self.openList[0:0] = nextAvailable
                self.solution.append([dot[0], dot[1], nextState])
                if(self.isGoalState(nextState)):
                    return
                # if it reached the max depth go back for deepest parallel level
                elif(self.current_d >= self.max_d):
                    # back 1 depth up
                    lastTouch = self.solution[len(self.solution)-1]
                    self.virtualDP.touch(lastTouch[0], lastTouch[1])
                    lastState = self.virtualDP.get1DState()
                    del self.solution[len(self.solution)-1]
                    self.current_d -= 1
                    if (lastState != self.solution[len(self.solution)-1][2]):
                        raise Exception(
                            "Error: return back to last state failed")
                    return
                else:  # it does not reach the max depth limit yet
                    for i in range(len(nextAvailable)):
                        self.doSearch()  # DFS here 1 level deeper
                        if(self.isGoalState(nextState)):
                            return
                    # no solution found so return back
                    return

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
    def isGoalState(self, state):
        goalState = state.replace("1", "0")
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
                # touch it so we can get the next state
                puzzleM.touch(dot[0], dot[1])
                state1D = pupuzzleM.get1DState()
                available = [dot[0], dot[1], state1D]
                nextAvailable.append(available)  # add to nextAvailable list
                # touch it again so it go back to the last state (parent)
                puzzleM.touch(dot[0], dot[1])

        # so far we got all same level states with dot positions to touch
        # we have to filter what is not available in the list
        # as long as it is not the root state, the parent state's touch dot should be unavailable
        # because touching the same dot will go back to its last state (grand parent)
        # benefit of filtering this is because its max O(n) is n x n, size of the board
        # which is fixed and much less than O(n) of iterating the closed list after a while of search
        if(lastTouch[0] != "0"):
            for i in range(len(nextAvailable)):
                if(lastTouch[0] == nextAvailable[i][0] and lastTouch[1] == nextAvailable[i][1]):
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
