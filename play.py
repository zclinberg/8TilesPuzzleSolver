from puzzle_board import PuzzleBoard
from puzzle_solver import PuzzleSolver
import fileinput
s=''
for line in fileinput.input():
    s+=line

pb = PuzzleBoard(s)
while pb.manhattanHeuristic() > 0:
    print(pb)
    pb.moveBlankCell(input("pick a direction "))
