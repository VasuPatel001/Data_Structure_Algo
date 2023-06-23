"""
Leetcode 63: Unique Paths II

You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The testcases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Example 2:
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1

Constraints:
m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp_table = [[0 for _ in range(n)] for _ in range(m)]
        # dp_table = [[0] * n] * m  IMP Note: do NOT use this method for creating multi-dimension array because python array created using this approach does not work well specifically for multi-dimension array
        # https://www.geeksforgeeks.org/python-list-comprehension-vs-operator/
        dp_table[0][0] = 1

        # setting 0th col to 1
        for row in range(1, m):
            if obstacleGrid[row][0] == 1:
                break
            dp_table[row][0] = 1

        # setting 0th row to 1
        for col in range(1, n):
            if obstacleGrid[0][col] == 1:
                break
            dp_table[0][col] = 1

        # initialize dp_table
        for row in range(1, m):
            for col in range(1, n):
                # considering obstacles
                if obstacleGrid[row][col] == 1:
                    dp_table[row][col] = 0
                dp_table[row][col] = dp_table[row-1][col] + dp_table[row][col-1]

        return dp_table[m-1][n-1]
