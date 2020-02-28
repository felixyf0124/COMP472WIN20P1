# from sets import Set
import DotPuzzle as dp


class AStar:
    # constructor add Max length limit
    def __init__(self, max_l,debug):
        self.sPath = [] # search path
        self.closedList = set()
        self.openList = []
        self.visited = []
        self.solution = []
        # self.current_d = 0
        self.max_l = max_l
        self.heuristicType = 1
        self.debug = debug
        # here can be any number. after import it will be replaced
        self.virtualDP = dp.DotPuzzle(3)
        self.isSolFound = False
        self.counter = 0

    # add initial root state also update initial step for solution
    def addRoot(self, rootState):
        # self.current_d = 1
        hn = self.getHeuristic(rootState)
        gn = 0
        fn = hn + gn
        self.openList.append(["0", 0, rootState, fn, hn, gn])
        self.solution.append(["0", 0, rootState])
        self.virtualDP.import1DState(rootState)

    def doSearch(self):
        # TODO add one more check if low level dept available state is token by the high level one
        self.counter += 1
        
        if(self.debug):
            print("======================================")
            # print("CURRENT DEPTH")
            # print(self.current_d)
            print("CURRENT GAME STATE")
            print(self.virtualDP.get1DState())
            print("VISITED")
            print(self.visited)
            print("OPEN LIST")
            print(self.openList)
            print("CLOSED LIST")
            print(self.closedList)
            print("SOLUTION")
            print(self.solution)

        # sort by fn
        self.sortOpenList()

        available = self.openList[0]

        if (available[0] == "0"):
            self.visited = available
            if(self.isClosed(available[2])):
                # search path add
                self.sPath.append(available)
                # set add
                self.closedList.add((available[0]))
            del self.openList[0]
            nextAvailable = self.generateNextAvailableState()

            self.openList.extend(nextAvailable)
            # sort by fn
            self.sortOpenList()
            self.doSearch()
            if(self.isSolFound):
                return
            return
        else:
            # pick a dot
            dot = [available[0], available[1]]
            # try touch dot
            self.virtualDP.touch(dot[0], dot[1])
            nextState = self.virtualDP.get1DState()
            if(self.isClosed(nextState)):  # the same state might be token by parallel's children
                # back to last state by touching same dot
                self.virtualDP.touch(dot[0], dot[1])
                return
            elif(nextState != available[2]):
                self.virtualDP.touch(dot[0], dot[1])
                return
                # raise Exception(
                #     "Error: touch dot not matching the associated state")
            else:
                # self.current_d += 1
                self.visited = available
                if(self.isClosed(available[2])):
                    # search path add
                    self.sPath.append(available)
                    # set add
                    self.closedList.add((available[0]))
                del self.openList[0]
                self.solution.append([dot[0], dot[1], nextState])
                if(self.counter % 10000 == 0):
                    print("SOLUTION")
                    print(self.solution)
                if(self.isGoalState(nextState)):
                    return
                # if it reached the max depth go back for deepest parallel level
                elif(len(self.sPath) >= self.max_l):

                    # no solution
                    return
                else:  # it does not reach the max length limit yet
                    nextAvailable = self.generateNextAvailableState()
                    self.openList[0:0] = nextAvailable
                    # sort by fn
                    self.sortOpenList()
                    self.doSearch()  
                    if(self.isSolFound):
                       return
                    
                    return

    # check if the state is closed

    def isClosed(self, stateNode):
        isClosed =  (stateNode) in self.closedList
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

    # return next available state with associated dot in the same depth level
    # TODO option: make a parent class and move this to parent class?
    def generateNextAvailableState(self):
        if(self.debug):
            print("====================================generateNextAvailableState")
        lastTouch = self.solution[-1]
        nextAvailable = []
        puzzleM = dp.DotPuzzle(3)
        puzzleM.import1DState(lastTouch[2])
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for j in range(puzzleM.n):
            for i in range(puzzleM.n):
                dot = [alpha[j], i+1]
                # touch it so we can get the next state
                puzzleM.touch(dot[0], dot[1])
                state1D = puzzleM.get1DState()
                hn = self.getHeuristic(state1D)
                gn = self.visited[3] + 1
                fn = hn + gn
                available = [dot[0], dot[1], state1D, fn, hn, gn]
                nextAvailable.append(available)  # add to nextAvailable list
                # touch it again so it go back to the last state (parent)
                puzzleM.touch(dot[0], dot[1])

        # so far we got all same level states with dot positions to touch
        # we have to filter what is not available in the list
        # as long as it is not the root state, the parent state's touch dot should be unavailable
        # because touching the same dot will go back to its last state (grand parent)
        # benefit of filtering this is because its max O(n) is n x n, size of the board
        # which is fixed and much less than O(n) of iterating the closed list after a while of search
        if(self.debug):
            print("-------------------------------------------------------")
            print(lastTouch)
            print(nextAvailable)
            print("-------------------------------------------------------")

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
        if(self.debug):
            print("next available")
            print(nextAvailable)

        return nextAvailable

    # get h(n)
    def getHeuristic(self, state):
        if(self.heuristicType == 1):
            return self.getHn1(state)

    # get h1
    # Hamming distance: count number of 1s
    def getHn1(self, state):
        hn = 0
        for i in range(len(state)):
            if(state[i] == "1"):
                hn += 1
        return hn

    # get 3rd element
    def get3rd(self, elem):
        return elem[3]

    # sort openlist based on the 3rd elemt (fn)
    def sortOpenList(self):
        self.openList.sort(key=self.get3rd)


    # return null if not found
    # else return final solution
    def getFinalSolution(self):
        solution = "No Solution"
        if(self.isSolFound):
            solution = ""
            for i in range(len(self.solution)):
                if(self.solution[i][0] == "0"):
                    solution += self.solution[i][0]
                else:
                    solution += self.solution[i][0] + str(self.solution[i][1])
                solution += " " + self.solution[i][2] + "\n"
       
        return solution

    # return search path
    def getSearchPath(self):
        searchPath = ""
        for i in range(len(self.closedList)):
            searchPath += "0 0 0 " + self.closedList[i][2] + "\n"
            
        return searchPath