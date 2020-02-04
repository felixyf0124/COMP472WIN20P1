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
    

    #TODO
    def touch(self, x, y):
        pass

    #import from existing game status
    def importInit(self, board):
        self.board = board
        self.n = len(board)

    #TODO return current game board status in 1D array
    def getBoard(self):
        pass
   
# test  
p = DotPuzzle(3)
print(p.board)
p.display()
