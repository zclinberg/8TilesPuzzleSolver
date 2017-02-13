import copy
from random import randint


class PuzzleBoard(object):
    def __init__(self):
        self.board =  self.generateRandomState()
        self.blankCell = self.getBlankCell()
        self.h = self.manhattanHeuristic() + 2 * self.getLinearConflict()

    def __str__(self):
        s = ""
        for b in self.board:
            for i in b:
                s += str(i)
            s += "\n"
        return s

    def __eq__(self, other):
        if self.board == other.board:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.board < other.board:
            return

    def copy(self):
        """creates a copy of the PuzzleBoard"""
        pb = PuzzleBoard()
        pb.board = copy.deepcopy(self.board)
        pb.blankCell = self.blankCell.copy()
        pb.h = self.h
        return pb

    def printBoard(self):
        """Prints the board"""
        s = '+-+-+-+\n'
        for b in self.board:
            s += "|"
            for i in b:
                s += str(i) + "|"
            s += "\n+-+-+-+\n"
        print(s)

    def printCell(self, i, j):
        """Prints the cell"""
        print(self.board[i][j])

    def getCell(self, i, j):
        """Returns a cell's value"""
        return self.board[i][j]

    def setCell(self, i, j, value):
        """Sets a cell's value"""
        self.board[i][j] = value

    def getCellToSwap(self, direction):
        """returns the cell to swap with the blank cell according to the direction parameter"""
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
        """returns the coordinates of the blank cell"""
        i = 0
        for a in self.board:
            j = 0
            for b in a:
                if b == 0:
                    return [i, j]
                j += 1
            i += 1

    def moveBlankCell(self, direction):
        """Moves the blank cell in the given direction"""
        if direction in self.getValidMoves():
            cellToSwap = self.getCellToSwap(direction)
            cell = self.getCell(cellToSwap[0], cellToSwap[1])
            self.setCell(self.blankCell[0], self.blankCell[1], cell)
            self.setCell(cellToSwap[0], cellToSwap[1], 0)
            self.blankCell = cellToSwap
            self.h = self.manhattanHeuristic() + 2 * self.getLinearConflict()
        else:
            print("invalid direction")

    def getValidMoves(self):
        """Returns a list of valid moves"""
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

    def getGoalRow(self, x):
        """returns a values goal row"""
        if x == 0 or x == 1 or x == 2:
            return 0
        elif x == 3 or x == 4 or x == 5:
            return 1
        elif x == 6 or x == 7 or x == 8:
            return 2

    def getGoalColumn(self, x):
        """return's a values goal column"""
        if x == 0 or x == 3 or x == 6:
            return 0
        elif x == 1 or x == 4 or x == 7:
            return 1
        elif x == 2 or x == 5 or x == 8:
            return 2

    def getGoalCell(self, x):
        """returns a value's goal cell"""
        i = self.getGoalRow(x)
        j = self.getGoalColumn(x)
        return [i, j]

    def distanceFromGoal(self, i, j, value):
        """returns a cell's distance from its goal"""
        goal = self.getGoalCell(value)
        if value == 0:
            return 0
        else:
            return abs(i - goal[0]) + abs(j - goal[1])

    def manhattanHeuristic(self):
        """returns the total distance all cells are from their goal"""
        h = 0
        i = 0
        while i < len(self.board):
            row = self.board[i]
            j = 0
            while j < len(row):
                h += self.distanceFromGoal(i, j, self.getCell(i, j))
                j += 1
            i += 1
        return h

    def generateRandomState(self):
        """Generates a random board state"""
        board = []
        while not self.isSolvable(board):
            numbers = [x for x in range(9)]
            board = []
            for i in range(3):
                row = []
                for j in range(3):
                    row.append(numbers.pop(randint(0, len(numbers) - 1)))
                board.append(row)
        return board

    def isSolvable(self, board):
        """Checks to see if a board is solvable.
        returns true if the number of inversions is even
        false if odd"""
        if len(board) == 0:
            return False
        order = self.getOrder(board)
        inversions = self.getInversions(order)
        if inversions % 2 == 0:
            return True
        else:
            return False

    def getOrder(self, board):
        """Returns the linear order of the board.
        this is used to check if the board is solvable"""
        order = []
        for x in range(3):
            for y in range(3):
                order.append(board[x][y])
        order.remove(0)
        return order

    def getInversions(self, order):
        """Returns the number of inversions in the linear order
        of a board."""
        inversions = 0
        for x in range(len(order)):
            b = order[x]
            for y in range(x + 1, len(order)):
                if order[y] < b:
                    inversions += 1
        return inversions

    def getLinearConflict(self):
        """Gets the linear conflict of a board state"""
        conflicts = 0
        r = 0
        for row in self.board:
            for i in range(len(row)):
                if self.getGoalRow(row[i]) == r:
                    for x in range(i + 1, len(row)):
                        if self.getGoalRow(row[x]) == r and row[x] < row[i]:
                            conflicts += 1
            r += 1
        return conflicts