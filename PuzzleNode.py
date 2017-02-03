from puzzle_board import PuzzleBoard
class PuzzleNode(object):
    def __init__(self, data = None, moves = [], left = None,right =None, up = None, down = None):
        self.data = data
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        self.moves = moves
        self.f = data.h + len(moves)
        self.closed = False
        self.visited = False

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


