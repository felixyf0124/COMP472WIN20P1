
class SolutionWriter:
    def __init__(self, puzzleId, searchType):
        self.puzzleId = puzzleId
        self.searchType = searchType

    def createSearchSolutionFile(self, outputType, output):
        searchFile = str(self.puzzleId) + "_" + \
            str(self.searchType) + "_" + str(outputType) + ".txt"
        file = open(str(searchFile), "w+")
        file.write(str(output))
        file.close()
