class Solution(object):
    salved = False
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    squares = [set() for _ in range(9)]
    board = []

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.board = board
        for row in range(9):
            for col in range(9):
                if self.board[row][col] != ".":
                    num = int(self.board[row][col])
                    self.placeNum(num, row, col)
        self.backtrack(0, 0)

    def canPlace(self, num, row, col):
        return num not in self.rows[row] and num not in self.cols[col] and num not in self.squares[
            self.boxIndex(row, col)]

    def placeNum(self, num, row, col):
        self.rows[row].add(num)
        self.cols[col].add(num)
        self.squares[self.boxIndex(row, col)].add(num)
        self.board[row][col] = str(num)

    def removeNum(self, num, row, col):
        self.rows[row].remove(num)
        self.cols[col].remove(num)
        self.squares[self.boxIndex(row, col)].remove(num)
        self.board[row][col] = "."

    def placeNextNum(self, row, col):
        if col == 8 and row == 8:
            self.salved = True
        else:
            if col == 8:
                self.backtrack(row + 1, 0)
            else:
                self.backtrack(row, col + 1)

    def backtrack(self, row, col):
        if self.board[row][col] == ".":
            for num in range(1, 10):
                if self.canPlace(num, row, col):
                    self.placeNum(num, row, col)
                    self.placeNextNum(row, col)
                    if not self.salved:
                        self.removeNum(num, row, col)
        else:
            self.placeNextNum(row, col)

    def boxIndex(self, row, col):
        return row // 3 * 3 + col // 3