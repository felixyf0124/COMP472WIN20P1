import DotPuzzle as dp
import Loader as ld
# import PuzzleAdapter as PA

dotP = dp.DotPuzzle(3)
dotP.display()
print(dotP.board)

dotP.touch("b",2)

loader = ld.Loader("../test.txt")
loader.showMyPuzzleList()

pInfo = loader.getMyPuzzleAt(0)

print(pInfo)

dotP.import1DState(pInfo.get1DState())
dotP.display()