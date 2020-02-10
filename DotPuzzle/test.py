import DotPuzzle as dp
import Loader as ld
# import PuzzleAdapter as PA
import SolutionWriter as wr

# dotP = dp.DotPuzzle("../input.txt")
# dotP.display()
# print(dotP.board)

# dotP.touch("a", 2)
# dotP.touch("b", 1)
# dotP.touch("d", 3)
# dotP.touch("a", 1)
# dotP.touch("c", 2)

# print("===================")

# loader = ld.Loader("../1_dfs_search.txt")

# for i in range(10):
#     dotP.import1DState(loader.getMyPuzzleAt(i).get1DState())
#     dotP.display()

writer = wr.SolutionWriter(0, "dfs")
writer.createSearchSolutionFile("solution", "THIS IS THE CONTENT")
writer.createSearchSolutionFile("search", "THIS IS THE SEARCH")
