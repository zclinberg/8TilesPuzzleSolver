from puzzle_board import PuzzleBoard
class PuzzleNode(object):
    def __init__(self, data = None, moves = [], left = None,right =None, up = None, down = None):
        self.data = data
        self.moves = moves
        self.f = data.h + len(moves)
        self.closed = False

    def __str__(self):
        return str(self.data)

    def __eq__(self, other):
        if self.data == other.data:
            return True
        else: return False

    def __lt__(self,other):
        if self.data < other.data:
            return True
        else: return False


