from puzzle_board import PuzzleBoard
from puzzle_solver import PuzzleSolver
import sys
import time

starttime =time.time()

pb = PuzzleBoard()

solver = PuzzleSolver(pb)
solution = solver.aStarSolve()

pb.printBoard()
print("A* solution")
print("--- %s seconds ---" % (time.time() - starttime))
print(solution)
print(len(solution)," moves")
print(solver.expansions, " expansions")
if "bfs" in sys.argv:
    starttime = time.time()
    solver.clearSolver()
    bfsSolution = solver.bfs_search()
    print("BFS solution")
    print("--- %s seconds ---" % (time.time() - starttime))
    print(solution)
    print(len(solution)," moves")
    print(solver.expansions, " expansions")

if "p" in sys.argv:
    for m in solution:
        pb.moveBlankCell(m)
        pb.printBoard()