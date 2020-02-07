import DotPuzzle as dp
import Loader as ld
# import PuzzleAdapter as PA

dotP = dp.DotPuzzle("input.txt")
dotP.display()
print(dotP.board)

dotP.touch("a",2)
dotP.touch("b",1)
dotP.touch("d",3)
dotP.touch("a",1)
dotP.touch("c",2)
