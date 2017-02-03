from puzzle_board import PuzzleBoard
from puzzle_solver import PuzzleSolver
import fileinput
import time
s=''
starttime =time.time()
for line in fileinput.input():
    s+=line

pb = PuzzleBoard(s)

solver = PuzzleSolver(pb)
solution = solver.solve()
print("--- %s seconds ---" % (time.time() - starttime))
print(solution,len(solution)," moves")
print(solver.recursions)
pb.printBoard()
for m in solution:
    pb.moveBlankCell(m)
    pb.printBoard()

