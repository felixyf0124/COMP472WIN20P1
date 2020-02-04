import numpy as np

class DotPuzzle:
    def __init__(self, n):
        self.n = int(n)
        self.board = np.random.rand(n,n)
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                x = self.board[i][j]
                y = 0.5
                if x >= y:
                    self.board[i][j] = 1
                else:
                    self.board[i][j] = 0
        self.board = self.board.astype(int)
        
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
            out+="\n"
        print(out)  
    

    #flips each dot above, below, left, and right of a specified dot
    def touch(self, x, y):
        i1 = x-1
        i2 = x+1
        j1 = y-1
        j2 = y+1
        if (i1 >= 0):
            self.touchMath(i1,y)
        if (i2 < self.n):
            self.touchMath(i2,y)
        if (j1 >= 0):
            self.touchMath(x,j1)
        if (j2 < self.n):
            self.touchMath(x,j2)

    #flips a dot to 1 or 0 and vice-versa 
    #for some reason, x and y need to be inverted in the def for it to work correctly
    def touchMath(self, y, x):        
        dotVal = self.board[x][y]+1
        if dotVal == 1:
            self.board[x][y] = 1
        else:
            self.board[x][y] = 0  

    #import from existing game status
    def importInit(self, board):
        self.board = board
        self.n = len(board)

    #TODO return current game board status in 1D array
    def getBoard(self):
        pass

    #Reads an input file
    def readInput(self):
        self.numPuzzles=0
        #number of lines in the input file, aka. number of puzzles to be solved

        file = open("input.txt", "r")
        self.puzzle=[]
        for line in file: 
            self.numPuzzles+1
            self.puzzle.append(line)
        print (self.puzzle[0])
        print (self.puzzle[1])
   
# test  
p = DotPuzzle(3)
print(p.board)
p.display()
p.touch(1,0)
p.display()
p.readInput()
