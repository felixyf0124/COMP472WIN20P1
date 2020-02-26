
import PuzzleAdapter as PA


class Loader:
    def __init__(self, path):
        self.myPuzzleList = []
        # self.numPuzzles=0
        # number of lines in the input file, aka. number of puzzles to be solved
        file = open(path, "r")
        for line in file:
            c = line.split(" ")
            c[3] = c[3].replace('\n', '')
            myPuzzle = PA.PuzzleAdapter(c[0], c[1], c[2], c[3])
            self.myPuzzleList.append(myPuzzle)
            # self.numPuzzles+1
        file.close()

    # get specific puzzle at index
    # tested
    def getMyPuzzleAt(self, index):
        return self.myPuzzleList[index]

    # get size of list of puzzles in the path file
    def getMyPuzzleSize(self):
        return len(self.myPuzzleList)

    # show all puzzle game list
    # tested
    def showMyPuzzleList(self):
        for i in range(len(self.myPuzzleList)):
            line = ""
            line += self.myPuzzleList[i].n + " "
            line += self.myPuzzleList[i].max_d + " "
            line += self.myPuzzleList[i].max_l + " "
            line += self.myPuzzleList[i].state_1d + ""
            print(line)


# test
# l = Loader("../test.txt")
# l.showMyPuzzleList()
