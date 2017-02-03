import copy


class PuzzleBoard(object):

        def __init__(self,input=None):
            grid =  []
            if input != None:
                for s in input.split("\n"):
                    b = [int(c) for c in s]
                    grid.append(b)

            self.board = grid
            self.blankCell = self.getBlankCell()
            self.h = self.manhattanHeuristic()


        def __str__(self):
            s = ""
            for b in self.board:
                for i in b:
                    s += str(i)
                s+= "\n"
            return s
        def __eq__(self, other):
            if self.board == other.board:
                return True
            else: return False
        def __lt__(self, other):
            if self.board < other.board:
                return
        def copy(self):
            pb = PuzzleBoard()
            pb.board = copy.deepcopy(self.board)
            pb.blankCell = self.blankCell.copy()
            pb.h = self.h
            return pb

        def printBoard(self):
            s = '+-+-+-+\n'
            for b in self.board:
                s += "|"
                for i in b:
                    s += str(i) + "|"
                s+= "\n+-+-+-+\n"
            print(s)
        def printCell(self,i,j):
            print(self.board[i][j])

        def getCell(self,i,j):
            return self.board[i][j]

        def setCell(self,i,j,value):
            self.board[i][j] = value

        def moveBlankCell(self,direction):
            if direction in self.getValidMoves():
                self.h += self.getMoveChangeInH(direction)
                cellToSwap = self.getCellToSwap(direction)
                self.swapCellWithBlank(cellToSwap)
            else:
                print("invalid direction")

        def getCellToSwap(self,direction):
            cellToSwap = [self.blankCell[0], self.blankCell[1]]
            if direction in self.getValidMoves():
                if direction == "left":
                    cellToSwap[1] -= 1
                elif direction == "right":
                    cellToSwap[1] += 1
                elif direction == "up":
                    cellToSwap[0] -= 1
                elif direction == "down":
                    cellToSwap[0] += 1
            else:
                print("invalid direction")
            return cellToSwap

        def getBlankCell(self):
            i = 0
            for a in self.board:
                j = 0
                for b in a:
                    if b == 0:
                        return [i,j]
                    j += 1
                i += 1


        def swapCellWithBlank(self,c):
            cell = self.getCell(c[0],c[1])
            self.setCell(self.blankCell[0],self.blankCell[1],cell)
            self.setCell(c[0],c[1],0)
            self.blankCell = c


        def getValidMoves(self):
            validMoves = []
            if self.blankCell[0] > 0:
                validMoves.append("up")
            if self.blankCell[1] > 0:
                validMoves.append("left")
            if self.blankCell[0] < 2:
                validMoves.append("down")
            if self.blankCell[1] < 2:
                validMoves.append("right")
            return validMoves


        def getGoalCell(self,x):
            i = j = 0
            if x == 0 or x == 1 or x == 2:
                i = 0
            elif x == 3 or x == 4 or x == 5:
                i = 1
            elif x == 6 or x == 7 or x == 8:
                i = 2

            if x == 0 or x == 3 or x == 6:
                j = 0
            elif x == 1 or x == 4 or x == 7:
                j = 1
            elif x == 2 or x == 5 or x == 8:
                j = 2
            return [i,j]

        def distanceFromGoal(self,i,j,value):
            goal = self.getGoalCell(value)
            if value == 0:
                return 0
            else:
                return abs(i - goal[0]) + abs(j - goal[1])

        def manhattanHeuristic(self):
            h = 0
            i = 0
            while i < len(self.board):
                row = self.board[i]
                j = 0
                while j < len(row):
                    h += self.distanceFromGoal(i,j,self.getCell(i,j))
                    j+= 1
                i += 1
            return h


        def getMoveChangeInH(self,direction):
            cellToSwap = self.getCellToSwap(direction)
            cellToSwapValue = self.getCell(cellToSwap[0],cellToSwap[1])
            h0 = self.distanceFromGoal(cellToSwap[0], cellToSwap[1], cellToSwapValue)
            h1 = self.distanceFromGoal(self.blankCell[0], self.blankCell[1], cellToSwapValue)
            return h1 - h0







