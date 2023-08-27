"""
Leetcode 37. Sudoku Solver

Write a program to solve a Sudoku puzzle by filling the empty cells.
A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.


Example 1:
Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:

Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
"""


class Solution:
    def is_safe(self, board: list[list[str]], num: int, row: int, col: int) -> bool:
        """ returns True when there is no-repeating char found
        """
        # check along the given row
        for col_i in range(9):
            if board[row][col_i] == str(num):
                return False

        # check along given col
        for row_i in range(9):
            if board[row_i][col] == str(num):
                return False

        # check in the sub-box
        boxRowStart = row - row % 3
        boxColStart = col - col % 3
        for row_i in range(boxRowStart, boxRowStart + 3):
            for col_i in range(boxColStart, boxColStart + 3):
                if board[row_i][col_i] == str(num):
                    return False
        return True

    def helper(self, board: list[list[str]]) -> bool:
        # check for first empty cell located in [row, col]
        row, col = 0, 0
        unfilledCell = False
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    row, col = i, j
                    unfilledCell = True
                    break
            if unfilledCell:
                break

        # when no unfilledCell is found, means the suoku is solved
        if not unfilledCell:
            return True

        for num in range(1, 10):
            # check if it is safe to put num in board[row][col]
            if self.is_safe(board, num, row, col):
                board[row][col] = str(num)

                if self.helper(board):
                    return True

                else: # not safe to keep
                    board[row][col] = '.'
        # Starting from the state of the board passed to this call, no solution is possible.
        # This cannot be the initial call (root call in the recursion hierarchy of calls) because
        # problem statement guarantees that a solution exists for every test board.
        # So returning false will lead to backtracking.
        return False

    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.helper(board)
        return board
