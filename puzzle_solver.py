from PuzzleNode import PuzzleNode
import sys
class PuzzleSolver(object):
    def __init__(self,puzzleBoard):
        self.root = PuzzleNode(puzzleBoard)
        self.frontierNodes = [self.root]
        self.recursions = 0
        self.allNodes = [self.root]
        sys.setrecursionlimit(10000)

    def solve(self,node = None):
        self.recursions += 1
        if node is None:
            node = self.root
        if node.data.h == 0:
            return node.moves

        for m in node.data.getValidMoves():
            if len(node.moves) < 1 or not node.moves[-1] == self.getOppositeDirection(m):
                pb = node.data.copy()
                pb.moveBlankCell(m)
                moves = node.moves.copy()
                moves.append(m)
                newNode = PuzzleNode(pb,moves)
                self.closeNode(newNode)
                if not newNode.closed:
                    self.frontierNodes.append(newNode)
                    self.allNodes.append(newNode)

        self.frontierNodes.pop(0)
        self.frontierNodes.sort(key=lambda node:node.f)
        return self.solve(self.frontierNodes[0])
    def getIndex(self,node):
        if node in self.allNodes:
            return self.allNodes.index(node)
        else:
            return -1

    def closeNode(self,node):
        index = self.getIndex(node)
        if index >= 0:
            if node.f >= self.allNodes[index].f:
                node.closed =True

    def getOppositeDirection(self,direction):
        if direction == "up":
            return "down"
        elif direction == "down":
            return "up"
        elif direction == "left":
            return "right"
        else:
            return "left"