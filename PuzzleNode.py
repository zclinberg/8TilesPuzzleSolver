
class PuzzleNode(object):
    def __init__(self, data = None, moves = []):
        self.data = data
        self.moves = moves
        self.f = data.h + len(moves)
        self.closed = False

    def __str__(self):
        return str(self.data)

    def __eq__(self, other):
        if self.f == other.f:
            return True
        else: return False

    def __lt__(self,other):
        if self.f < other.f:
            return True
        else: return False
    def toString(self):
        s = ""
        for x in range(3):
            for y in range(3):
                s += str(self.data.getCell(x,y))

        return s