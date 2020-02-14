import DFS as dfs
import Loader as ld
import SolutionWriter as wr

# loads the test.txt input file.
loader = ld.Loader("../test.txt")
# loads puzzle #1
initSet = loader.getMyPuzzleAt(0)
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
writer = wr.SolutionWriter(1, "dfs")
writer.createSearchSolutionFile("solution", solution)
writer.createSearchSolutionFile("search", search)

