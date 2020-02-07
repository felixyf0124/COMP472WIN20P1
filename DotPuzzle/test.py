import DotPuzzle as dp
import Loader as ld
# import PuzzleAdapter as PA

dotP = dp.DotPuzzle("input.txt")
dotP.display()
print(dotP.board)

dotP.touch("a",2)
