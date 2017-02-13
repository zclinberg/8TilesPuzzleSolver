import resource

from PuzzleNode import PuzzleNode
import sys
class PuzzleSolver(object):
    def __init__(self,puzzleBoard):
        self.root = PuzzleNode(puzzleBoard)
        self.frontierNodes = [self.root]
        self.expansions = 0
        self.allNodes = {self.root.toString():self.root.f}

    def solve(self):
        """Recursively searches for the optimal solution"""
        self.expansions += 1
        node =self.root
        while node.data.h != 0:
            for m in node.data.getValidMoves():
                if len(node.moves) < 1 or not node.moves[-1] == self.getOppositeDirection(m):
                    pb = node.data.copy()
                    pb.moveBlankCell(m)
                    moves = node.moves.copy()
                    moves.append(m)
                    newNode = PuzzleNode(pb,moves)
                    self.updateNodes(newNode)
            self.frontierNodes.pop(0)
            self.frontierNodes.sort(key=lambda node:node.f)
            node = self.frontierNodes[0]
        return node.moves


    def updateNodes(self, node):
        key = node.toString()
        if key not in self.allNodes or self.allNodes[key] > node.f:
            self.allNodes[key] = node.f
            self.frontierNodes.append(node)


    def getOppositeDirection(self,direction):
        """Returns the opposite direction of a given direction.
        This is used to ignore suboptimal solutions because an optimal solution
        cannot have """
        if direction == "up":
            return "down"
        elif direction == "down":
            return "up"
        elif direction == "left":
            return "right"
        else:
            return "left"