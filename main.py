from puzzle_board import PuzzleBoard
from puzzle_solver import PuzzleSolver
import fileinput
import time

starttime =time.time()

pb = PuzzleBoard()
pb.printBoard()


solver = PuzzleSolver(pb)
solution = solver.solve()
print("--- %s seconds ---" % (time.time() - starttime))
print(solution,len(solution)," moves")
print(solver.expansions)
pb.printBoard()
for m in solution:
    pb.moveBlankCell(m)
    pb.printBoard()