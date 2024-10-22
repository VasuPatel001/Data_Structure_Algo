"""
64. Minimum Path Sum
Medium

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 200
"""


class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        """
        Time: O(m*n) for two for loops
        Space: O(m*n) for dp [[]]
        """
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        dp[0][0] = grid[0][0]

        for row in range(1, m):
            dp[row][0] = dp[row-1][0] + grid[row][0]

        for col in range(1, n):
            dp[0][col] = dp[0][col-1] + grid[0][col]

        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = grid[row][col] + min(dp[row-1][col], dp[row][col-1])
        return dp[m-1][n-1]
