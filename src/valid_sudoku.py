from itertools import product
from typing import List
from typing import Tuple


class Solution:
    def isValidSquare(
        self, squareOffset: Tuple[int, int], board: List[List[str]]
    ) -> bool:
        x, y = squareOffset
        cache = set()
        for i in range(3):
            for j in range(3):
                val = board[i + 3 * x][j + 3 * y]
                if val in cache:
                    return False
                else:
                    if val != ".":
                        cache.add(val)
        return True

    def isValidColumn(self, col: int, board: List[List[str]]) -> bool:
        cache = set()
        for i in range(9):
            val = board[i][col]
            if val in cache:
                return False
            else:
                if val != ".":
                    cache.add(val)
        return True

    def isValidRow(self, row: int, board: List[List[str]]) -> bool:
        cache = set()
        for i in range(9):
            val = board[row][i]
            if val in cache:
                return False
            else:
                if val != ".":
                    cache.add(val)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for offset in product([0, 1, 2], [0, 1, 2]):
            if not self.isValidSquare(offset, board):
                return False

        for i in range(9):
            if not self.isValidRow(i, board) or not self.isValidColumn(
                i, board
            ):
                return False

        return True


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

sol = Solution()
print(sol.isValidSudoku(board))

board = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

print(sol.isValidSudoku(board))
