
import PuzzleAdapter as PA

class Loader:
    def __init__(self, path):
        self.myPuzzleList = []
        file = open(path, "r")
        for line in file:
            c = line.split(" ")
            c[3] = c[3].replace('\n','')
            myPuzzle = PA.PuzzleAdapter(c[0],c[1],c[2],c[3])
            self.myPuzzleList.append(myPuzzle)
        file.close()

    def getMyPuzzleAt(self, index):
        return self.myPuzzleList[index]

    def showMyPuzzleList(self):
        for i in range(len(self.myPuzzleList)):
            line = ""
            line += self.myPuzzleList[i].n + " "
            line += self.myPuzzleList[i].max_d + " "
            line += self.myPuzzleList[i].max_l + " "
            line += self.myPuzzleList[i].state_1d + ""
            print(line)

#test
l = Loader("../test.txt")
l.showMyPuzzleList()
  
