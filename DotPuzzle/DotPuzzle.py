import numpy as np

class DotPuzzle:
    def __init__(self, input):
        if(isinstance(input,int)):
            self.newGame(int(input))
        else:
            # self.readInput(str(input))
            # self.createPuzzle(1)
            pass
    
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
            out+="\n"
        print(out)  
    
    #generate new nxn game with rand initials
    # tested
    def newGame(self,n):
        self.n = n
        self.board = np.random.rand(n,n)
        for i in range(n):
            for j in range(n):
                x = (self.board[i][j])
                y = 0.5
                if x >= y:
                    self.board[i][j] = 1
                else:
                    self.board[i][j] = 0
        self.board = self.board.astype(int)


    #flips each dot above, below, left, and right of a specified dot
    # tested
    def touch(self, y, x):
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        jy = alpha.find(y.upper())
        ix = int(x)-1
        i1 = ix-1
        i2 = ix+1
        j1 = jy-1
        j2 = jy+1
        self.touchMath(ix,jy)
        if (i1 >= 0):
            self.touchMath(i1,jy)
        if (i2 < self.n):
            self.touchMath(i2,jy)
        if (j1 >= 0):
            self.touchMath(ix,j1)
        if (j2 < self.n):
            self.touchMath(ix,j2)
        
        #debug print each touchOuput, in future write to file
        self.display()
        #self.touchOutput(x, y)

    #flips a dot to 1 or 0 and vice-versa 
    #for some reason, x and y need to be inverted in the def for it to work correctly
    def touchMath(self, y, x):        
        dotVal = self.board[x][y]+1
        if dotVal == 1:
            self.board[x][y] = 1
        else:
            self.board[x][y] = 0 
    
    #Generates the YX ######### string and writes it to the search file
    def touchOutput(self, x, y):        
        touchChange = str(chr(ord('@')+(y+1)) + str(x) + " " + str(self.getBoard()) + "\n")
        file=open(self.searchFile,"a")
        file.write(touchChange)
        file.close()

    #return current game board status in string
    # tested
    def getBoard(self):
        boardStr = ""
        for i in range(self.n):
            for j in range(self.n):
                boardStr += str(self.board[i][j])
        return boardStr

    #import from existing game status
    def importInit(self, board):
        self.board = board
        self.n = len(board)

    #Reads an input file
    def readInput(self, string):
        self.numPuzzles=0
        #number of lines in the input file, aka. number of puzzles to be solved

        self.puzzle=[]
        file = open(string, "r")
        for line in file: 
            self.numPuzzles+1
            self.puzzle.append(line)
        file.close()

    #Generates puzzle based on input, must be told which puzzle to analyze  
    def createPuzzle(self, numPuzzle):
        puzzleStr=self.puzzle[numPuzzle-1].split()
        #breaks up input string into a list with each 'part' as a list item

        self.n = int(puzzleStr[0])
        n=self.n
        self.board = np.random.rand(n,n)
        puzzlePos = 0
        for i in range(n):
            for j in range(n):
                x = int(puzzleStr[3][puzzlePos])
                y = 0.5
                if x >= y:
                    self.board[i][j] = 1
                else:
                    self.board[i][j] = 0
                puzzlePos=puzzlePos+1

        self.board = self.board.astype(int)
        self.createSearchFile(numPuzzle)

    #creates search file for current puzzle
    #in future will be made dynamic for search type
    def createSearchFile(self, numPuzzle):
        self.searchFile = str(numPuzzle-1)+"_dfs_search.txt"
        file=open(self.searchFile,"w")
        file.write(str("0 " + str(self.getBoard()) + "\n"))
        file.close()
   
# test  
#p = DotPuzzle(4)
# print(p.board)
# p.display()
