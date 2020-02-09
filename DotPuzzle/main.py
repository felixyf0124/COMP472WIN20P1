import DFS as dfs
import Loader as ld

# dotP = dp.DotPuzzle("../input.txt")
loader = ld.Loader("../test.txt")

initSet = loader.getMyPuzzleAt(1)
dfSearcher = dfs.DFS(initSet.getMaxDeepth(), True)
dfSearcher.addRoot(initSet.get1DState())
# search = dfs.DFSearch(3)
dfSearcher.doSearch()
