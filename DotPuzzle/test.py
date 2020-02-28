import DotPuzzle as dp
import BFS as bfs
import DFS as dfs
import AStar as ass
import Loader as ld
import SolutionWriter as wr
import time

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

# writer = wr.SolutionWriter(0, "dfs")
# writer.createSearchSolutionFile("solution", "THIS IS THE CONTENT")
# writer.createSearchSolutionFile("search", "THIS IS THE SEARCH")

# a = set()
# a.add((1,2,3))
# b = (1,2,4) in a
# print(b)
# print(a)

# loads the test.txt input file.
loader = ld.Loader("test.txt")

# get solution for dfs
# for i in range(loader.getMyPuzzleSize()):
i =1
# calculate the time
start = time.time()
# loads puzzle #1
initSet = loader.getMyPuzzleAt(i)
asSearcher = ass.AStar(initSet.getMaxSearchPathLength(), False)
asSearcher.addRoot(initSet.get1DState())
# runs search using DFS method
asSearcher.doSearch()
print("FINAL SOLUTION")
print(asSearcher.solution)
print("SOL FOUND?")
print(asSearcher.isSolFound)
solution = asSearcher.getFinalSolution()
search = asSearcher.getSearchPath()
print(solution)
# prints output
writer = wr.SolutionWriter(i, "astar")
writer.createSearchSolutionFile("solution", solution)
writer.createSearchSolutionFile("search", search)
end = time.time()
print(end - start)


a = [0,1,2,3,4]
print(a[:-1])