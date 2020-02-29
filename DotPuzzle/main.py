# import BFS as bfs
import BestFirst as bfs
import AStar as ass
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
#     print(end - start, "second(s)")

# get solution for Best-First search
for i in range(loader.getMyPuzzleSize()):
    # calculate the time
    start = time.time()
    # loads puzzle #1
    initSet = loader.getMyPuzzleAt(i)
    bfSearcher = bfs.BestFirst(initSet.getMaxSearchPathLength(), False)
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
    print(end - start, "second(s)")

# get solution for A* search
for i in range(loader.getMyPuzzleSize()):
# i =1
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
