from puzzle_board import PuzzleBoard

pb = PuzzleBoard(s)
while pb.manhattanHeuristic() > 0:
    print(pb)
    pb.moveBlankCell(input("pick a direction "))
