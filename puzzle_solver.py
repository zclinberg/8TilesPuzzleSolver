from heapq import *
from PuzzleNode import PuzzleNode
class PuzzleSolver(object):
    def __init__(self,puzzleBoard):
        self.root = PuzzleNode(puzzleBoard)
        self.frontierNodes = [self.root]
        self.expansions = 0
        self.allNodes = {self.root.toString():self.root.f}

    def aStarSolve(self):
        """Recursively searches for the optimal solution using A* search"""
        node = heappop(self.frontierNodes)
        while node.data.h != 0:
            self.expansions += 1
            for m in node.data.getValidMoves():
                if len(node.moves) < 1 or not node.moves[-1] == self.getOppositeDirection(m):
                    pb = node.data.copy()
                    pb.moveBlankCell(m)
                    moves = node.moves.copy()
                    moves.append(m)
                    newNode = PuzzleNode(pb,moves)
                    self.updateNodes(newNode)

            node = heappop(self.frontierNodes)
        return node.moves

    def bfs_search(self):
        node = self.frontierNodes.pop()
        while node.data.h != 0:
            self.expansions += 1
            for m in node.data.getValidMoves():
                if len(node.moves) < 1 or not node.moves[-1] == self.getOppositeDirection(m):
                    pb = node.data.copy()
                    pb.moveBlankCell(m)
                    moves = node.moves.copy()
                    moves.append(m)
                    newNode = PuzzleNode(pb,moves)
                    key = newNode.toString()
                    if key not in self.allNodes:
                        self.allNodes[key] = node.f
                        self.frontierNodes.append(newNode)
            node = self.frontierNodes.pop(0)
        return node.moves

    def updateNodes(self, node):
        key = node.toString()
        if key not in self.allNodes or self.allNodes[key] >= node.f:
            self.allNodes[key] = node.f
            heappush(self.frontierNodes,node)


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

    def clearSolver(self):
        self.frontierNodes = [self.root]
        self.expansions = 0
        self.allNodes = {self.root.toString():self.root.f}