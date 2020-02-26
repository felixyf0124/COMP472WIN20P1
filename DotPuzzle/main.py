import DFS as dfs
import Loader as ld
import SolutionWriter as wr

# loads the test.txt input file.
loader = ld.Loader("test.txt")

# get solution for dfs
for i in range(loader.getMyPuzzleSize()):
    # loads puzzle #1
    initSet = loader.getMyPuzzleAt(i)
    dfSearcher = dfs.DFS(initSet.getMaxDeepth(), False)
    dfSearcher.addRoot(initSet.get1DState())
    # runs search using DFS method
    dfSearcher.doSearch()
    print("FINAL SOLUTION")
    print(dfSearcher.solution)
    print("SOL FOUND?")
    print(dfSearcher.isSolFound)
    solution = dfSearcher.getFinalSolution()
    search = dfSearcher.getSearchPath()
    print(solution)
    # prints output
    writer = wr.SolutionWriter(i, "dfs")
    writer.createSearchSolutionFile("solution", solution)
    writer.createSearchSolutionFile("search", search)
