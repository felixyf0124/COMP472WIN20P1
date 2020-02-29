# from sets import Set
import DotPuzzle as dp


class DepthFirst:
    # constructor add Max length limit
    def __init__(self, max_d,debug):
        self.sPath = [] # search path
        self.closedList = dict()
        self.openList = []
        self.visited = []
        self.solution = []
        # self.current_d = 0
        self.max_d = max_d
        self.heuristicType = 1
        self.debug = debug
        # here can be any number. after import it will be replaced
        self.virtualDP = dp.DotPuzzle(3)
        self.isSolFound = False
        self.counter = 0
        self.finalState = []

    # add initial root state also update initial step for solution
    def addRoot(self, rootState):
        # self.current_d = 1
        hn = 0
        gn = 0
        fn = 0
        root = ["0", 0, rootState, fn, hn, gn, [["0", 0, rootState, fn, hn, gn]]]

        self.openList.append(root)
        self.virtualDP.import1DState(rootState)

    def doSearch(self):
        self.counter += 1
        
        # # sort by fn
        # self.sortOpenList()
       
        available = self.openList[0]

        if (available[0] == "0"):
            self.visited = available
            self.solution = available[-1]
            # if(not self.isClosed(available[2])):
            # search path add
            self.sPath.append(available)
            # dict add
            self.closedList[available[2]]=len(available[-1])
            
            del self.openList[0]
            nextAvailable = self.generateNextAvailableState()
            self.openList.extend(nextAvailable)
            for i in range(len(nextAvailable)):
                self.doSearch()
                if(self.isSolFound):
                    return
            return
        else:
            self.visited = available
            self.solution = available[-1]
            
            # search path add
            self.sPath.append(available)
            # dict add
            if (self.isClosed(available[2])):
                self.closedList[available[2]] = min(len(available[-1]),self.closedList[available[2]])
            else:
                self.closedList[available[2]]=len(available[-1])

            del self.openList[0]

            # print("visited")
            # print(self.visited)
            if(self.isGoalState(available[2])):
                self.finalState = available
                print("final")
                print(self.finalState)
                self.solution = self.finalState[-1]
                return
            # if it reached the max length end
            elif(len(available[-1]) >= self.max_d):
                
                return
            else:  # it does not reach the max length limit yet
                nextAvailable = self.generateNextAvailableState()
                self.openList[0:0] = nextAvailable
                for i in range(len(nextAvailable)):
                    self.doSearch()  # DFS here 1 level deeper
                    if(self.isSolFound):
                        return
                
                return

    # check if the state is closed

    def isClosed(self, stateNode):
        # print("here")
        isClosed =  (stateNode) in self.closedList
        # print(isClosed)
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
        
        lastTouch = self.solution[len(self.solution)-1]
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
                hn = 0
                gn = 0
                fn = 0
                PathToRoot = self.visited[6] + [[dot[0], dot[1], state1D, fn, hn, gn]]
                # PathToRoot[0:0] = 
                available = [dot[0], dot[1], state1D, fn, hn, gn, PathToRoot]
                nextAvailable.append(available)  # add to nextAvailable list
                # touch it again so it go back to the last state (parent)
                puzzleM.touch(dot[0], dot[1])

        # so far we got all same level states with dot positions to touch
        # we have to filter what is not available in the list
        # as long as it is not the root state, the parent state's touch dot should be unavailable
        # because touching the same dot will go back to its last state (grand parent)

        # del list
        unavailableIndex = []
        for i in range(len(nextAvailable)):
            if(self.isClosed(nextAvailable[i][2])):
                # in order to guarentee the solution as much as possible
                # we have to keep the lower depth level state that already in the closed list
                # remove >= depth level state that already in the closed list 
                # and remove those already in the open list 
                if (self.closedList[nextAvailable[i][2]] <= len(nextAvailable[i][-1]) | self.isInOpenList(nextAvailable[i][2])):
                    unavailableIndex.append(i)

        # del from the last to the first so we won't be bothered by the changed subsequence
        for i in sorted(unavailableIndex, reverse=True):
            del nextAvailable[i]
        if(self.debug):
            print("next available")
            print(nextAvailable)

        return nextAvailable

    # check if in the open list
    def isInOpenList(self, state):
        for i in range(len(self.openList)):
            if(self.openList[i][2] == state ):
                return True
        return False

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

    # get 4th element
    def get4th(self, elem):
        return elem[4]

    # sort openlist based on the 3rd elemt (fn)
    def sortOpenList(self):
        self.openList.sort(key=self.get4th)


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
        for i in range(len(self.sPath)):
            searchPath += str(self.sPath[i][3]) + " "
            searchPath += str(self.sPath[i][4]) + " "
            searchPath += str(self.sPath[i][5]) + " "
            searchPath += self.sPath[i][2] + "\n"
            
        return searchPath