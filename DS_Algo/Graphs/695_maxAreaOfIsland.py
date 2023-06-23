"""
Leetcode 695: Max Area of Island

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
The area of an island is the number of cells with a value 1 in the island.
Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
"""

"""
Time Complexity:
Space Complexity: O(E) for neighbors
"""


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        # identify appropriate neighbors and return it as list of neighbors
        def getNeighbors(row, col):
            neighbors = []
            if row > 0:
                neighbors.append((row - 1, col))
            if col > 0:
                neighbors.append((row, col - 1))
            if row + 1 <= len(grid) - 1:
                neighbors.append((row + 1, col))
            if col + 1 <= len(grid[0]) - 1:
                neighbors.append((row, col + 1))
            return neighbors
        
        # performs dfs to identify total nodes in a dfs search
        def dfs(row, col):
            grid[row][col] = 0  # mark it as visited
            neighbors = getNeighbors(row, col)
            
            # leaf node worker
            if neighbors == []:
                return 1
            
            # internal node worker
            depth = 1
            for (i, j) in neighbors:
                if grid[i][j]:
                    depth += dfs(i, j)  # post-order / bottom-up flow of information
            return depth

        maxDepth = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    maxDepth = max(maxDepth, dfs(i, j))
        
        return maxDepth