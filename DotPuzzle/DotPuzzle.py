import numpy as np
import math
import Loader as ld


class DotPuzzle:
    def __init__(self, input):
        if(isinstance(input, int)):
            self.newGame(int(input))
        else:
            self.puzzles = ld.Loader(input)
            self.createPuzzle(0)

    # display game board
    # tested
    def display(self):
        out = "\n  |"
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in range(len(self.board[0])):
            out += " " + str(i+1)

        out += "\n--|"

        for i in range(len(self.board[0])):
            out += "--"

        out += "\n"

        for i in range(len(self.board)):
            out += " " + alpha[i] + "|"
            for j in range(len(self.board[i])):
                x = self.board[i][j]
                y = 1
                if x == y:
                    out += " X"
                else:
                    out += " O"
            out += "\n"
        print(out)

    # generate new nxn game with rand initials
    # tested
    def newGame(self, n):
        self.n = n
        self.board = np.random.rand(n, n)
        for i in range(n):
            for j in range(n):
                x = (self.board[i][j])
                y = 0.5
                if x >= y:
                    self.board[i][j] = 1
                else:
                    self.board[i][j] = 0
        self.board = self.board.astype(int)

    # flips each dot above, below, left, and right of a specified dot
    # tested

    def touch(self, y, x):
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        jy = alpha.find(y.upper())
        ix = int(x)-1
        i1 = ix-1
        i2 = ix+1
        j1 = jy-1
        j2 = jy+1
        self.touchMath(ix, jy)
        if (i1 >= 0):
            self.touchMath(i1, jy)
        if (i2 < self.n):
            self.touchMath(i2, jy)
        if (j1 >= 0):
            self.touchMath(ix, j1)
        if (j2 < self.n):
            self.touchMath(ix, j2)

        self.touchOutput(y, x)
        # debug print each touchOuput
        self.display()

    # flips a dot to 1 or 0 and vice-versa
    # for some reason, x and y need to be inverted in the def for it to work correctly
    def touchMath(self, y, x):
        dotVal = self.board[x][y]+1
        if dotVal == 1:
            self.board[x][y] = 1
        else:
            self.board[x][y] = 0

    # Generates the YX ######### string and writes it to the search file
    def touchOutput(self, y, x):
        touchChange = str(y.upper() + str(x) + " " + self.get1DState() + "\n")
        file = open(self.searchFile, "a")
        file.write(touchChange)
        file.close()

    # return current game board
    # tested
    def getBoard(self):
        return self.board

    # return current game board status in 1D string
    def get1DState(self):
        stateStr = ""
        for i in range(self.n):
            for j in range(self.n):
                stateStr += str(self.board[i][j])
        return stateStr

    # import from existing 2d game status
    def importBoard(self, board):
        self.board = board
        self.n = len(board)

    # import from existing 1d str game status
    def import1DState(self, state1DStr):
        self.n = int(math.sqrt(len(state1DStr)))
        self.board = np.zeros((self.n, self.n))
        for i in range(self.n):
            for j in range(self.n):
                self.board[i][j] = int(state1DStr[i*self.n+j])
        self.board = self.board.astype(int)

    # Generates puzzle based on input, must be told which puzzle to analyze
    def createPuzzle(self, numPuzzle):
        self.n = self.puzzles.myPuzzleList[numPuzzle].n
        self.max_d = self.puzzles.myPuzzleList[numPuzzle].max_d
        self.max_l = self.puzzles.myPuzzleList[numPuzzle].max_l
        self.state_1d = self.puzzles.myPuzzleList[numPuzzle].state_1d
        self.board = np.random.rand(self.n, self.n)
        puzzlePos = 0
        for i in range(self.n):
            for j in range(self.n):
                x = int(self.state_1d[puzzlePos])
                y = 0.5
                if x >= y:
                    self.board[i][j] = 1
                else:
                    self.board[i][j] = 0
                puzzlePos = puzzlePos+1

        self.board = self.board.astype(int)
        self.createSearchFile(numPuzzle)

    # creates search file for current puzzle
    # in future will be made dynamic for search type
    def createSearchFile(self, numPuzzle):
        self.searchFile = str(numPuzzle)+"_dfs_search.txt"
        file = open(self.searchFile, "w")
        file.write(str("0 " + self.state_1d + "\n"))
        file.close()

# test
#p = DotPuzzle(4)
# print(p.board)
# p.display()
