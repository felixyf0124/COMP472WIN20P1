import DFSearch as dfs
import DotPuzzle as dp

dotP = dp.DotPuzzle("../input.txt")

search = dfs.DFSearch(3)
search.doSearch(0, 'A')
