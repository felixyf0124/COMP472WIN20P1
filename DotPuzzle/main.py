import BFS as bfs
import DFS as dfs
import Loader as ld
import SolutionWriter as wr
import time

# loads the test.txt input file.
loader = ld.Loader("test.txt")

# get solution for dfs
# for i in range(loader.getMyPuzzleSize()):
#     # calculate the time
#     start = time.time()
#     # loads puzzle #1
#     initSet = loader.getMyPuzzleAt(i)
#     dfSearcher = dfs.DFS(initSet.getMaxDeepth(), False)
#     dfSearcher.addRoot(initSet.get1DState())
#     # runs search using DFS method
#     dfSearcher.doSearch()
#     print("FINAL SOLUTION")
#     print(dfSearcher.solution)
#     print("SOL FOUND?")
#     print(dfSearcher.isSolFound)
#     solution = dfSearcher.getFinalSolution()
#     search = dfSearcher.getSearchPath()
#     print(solution)
#     # prints output
#     writer = wr.SolutionWriter(i, "dfs")
#     writer.createSearchSolutionFile("solution", solution)
#     writer.createSearchSolutionFile("search", search)
#     end = time.time()
#     print(end - start)

# get solution for bfs
for i in range(loader.getMyPuzzleSize()):
    # calculate the time
    start = time.time()
    # loads puzzle #1
    initSet = loader.getMyPuzzleAt(i)
    bfSearcher = bfs.BFS(initSet.getMaxDeepth(), False)
    # bfSearcher = bfs.BFS(4, True)
    bfSearcher.addRoot(initSet.get1DState())
    # runs search using DFS method
    bfSearcher.doSearch()
    print("FINAL SOLUTION")
    print(bfSearcher.solution)
    print("SOL FOUND?")
    print(bfSearcher.isSolFound)
    solution = bfSearcher.getFinalSolution()
    search = bfSearcher.getSearchPath()
    print(solution)
    # prints output
    writer = wr.SolutionWriter(i, "bfs")
    writer.createSearchSolutionFile("solution", solution)
    writer.createSearchSolutionFile("search", search)
    end = time.time()
    print(end - start)
