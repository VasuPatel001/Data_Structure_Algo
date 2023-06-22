"""
Leetcode 51: N-Queens

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:
Input: n = 1
Output: [["Q"]]

Constraints:
1 <= n <= 9
"""


class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        if n == 1:
            return ['Q']
        results = []
        # idx -> row and nums[idx] -> col
        nums = [i for i in range(n)]
        self.helper(nums, 0, results)
        # convert results array to chess board
        solutions = []
        for result in results:
            sol = []
            board = [['.'] * n for _ in range(n)]
            row = 0
            for col in result:
                board[row][col] = 'Q'
                # convert board[row] from list to string
                sol.append(''.join(board[row]))
                row += 1
            solutions.append(sol)
        board = []
        return solutions

    def back_track(self, nums: list[int], row: int):
        # back tracking case: returns True if the queens placed from 0 to row - 1
        # does not satisfy constraint by check (row - 1) with (0 to row - 2)
        if len(nums) <= 3:
            return True
        check_row = row - 1
        for row_i in range(row - 1):
            # present in same col
            if nums[check_row] == nums[row_i]:
                return True
            row_diff = abs(check_row - row_i)
            col_diff = abs(nums[check_row] - nums[row_i])
            # present diagonally
            if row_diff == col_diff:
                return True

    def helper(self, nums: list[int], row: int, results: list[list[int]]):
        # row -> row and nums[row] -> col    
        # back tracking case: returns if the queens placed from 0 to row - 1 does not satisfy constraint
        if self.back_track(nums, row):
            return

        # base case
        if row == len(nums):
            results.append(nums[:])
            return

        # internal node workers
        for i in range(row, len(nums)):
            nums[row], nums[i] = nums[i], nums[row]
            self.helper(nums, row + 1, results)

            # re-swap to reverse the changes done
            nums[row], nums[i] = nums[i], nums[row]
