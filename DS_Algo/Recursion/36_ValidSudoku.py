"""
Leetcode 36: Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example 1:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false

Explanation: 
Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid. 

Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""


class Solution:
    def is_safe(self, board: list[list[str]], row: int, col: int) -> bool:
        """ returns True when there is no-repeating char found
        """
        # check along the given row
        for col_i in range(9):
            if board[row][col] == board[row][col_i] and col != col_i:
                return False

        # check along given col
        for row_i in range(9):
            if board[row][col] == board[row_i][col] and row != row_i:
                return False

        # check in the sub-box
        boxRowStart = row - row % 3
        boxColStart = col - col % 3
        for row_i in range(boxRowStart, boxRowStart + 3):
            for col_i in range(boxColStart, boxColStart + 3):
                if board[row][col] == board[row_i][col_i] and row != row_i and col != col_i:
                    return False
        return True

    def helper(self, board: list[list[str]], row: int) -> bool:
        if row == len(board):
            return True

        for col in range(len(board)):
            if board[row][col] != '.':
                if not self.is_safe(board, row, col):
                    return False

        return self.helper(board, row + 1)

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        return self.helper(board, 0)
