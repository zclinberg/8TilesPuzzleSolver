from puzzle_board import PuzzleBoard
from PuzzleNode import PuzzleNode
import sys
class PuzzleSolver(object):
    def __init__(self,puzzleBoard):
        self.root = PuzzleNode(puzzleBoard)
        self.frontierNodes = [self.root]
        self.recursions = 0
        self.allNodes = [self.root]
        self.closedNodes = []
        sys.setrecursionlimit(10000)


    def solve(self,node = None):
        self.recursions += 1
        if node is None:
            node = self.root
        node.visited = True
        if node.data.h == 0:
            return node.moves

        for m in node.data.getValidMoves():
            pb = node.data.copy()
            pb.moveBlankCell(m)
            moves = node.moves.copy()
            moves.append(m)
            newNode = PuzzleNode(pb,moves)
            if m == "up":
                node.up = newNode
            elif m == "left":
                node.left = newNode
            elif m == "down":
                node.down = newNode
            elif m == "right":
                node.right = newNode
            self.closeNode(newNode)
            if not newNode.closed:
                self.frontierNodes.append(newNode)
                self.allNodes.append(newNode)

        self.closedNodes.append(self.frontierNodes.pop(0))
        self.frontierNodes.sort(key=lambda node:node.f)
        return self.solve(self.frontierNodes[0])

    def getIndex(self,node):
        if node in self.allNodes:
            return self.allNodes.index(node)
        else:
            return -1

    def closeNode(self,node):
        index = self.getIndex(node)
        if self.getIndex(node) >= 0:
            if node.f >= self.allNodes[index].f:
                node.closed =True

    def selectNode(self):
        for n in self.frontierNodes:
            if not n.closed and not n.visited:
                return n

