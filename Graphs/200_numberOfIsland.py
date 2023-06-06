"""
Leetcode 200: Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""

"""
Time complexity: O(V + E) since we visit each vertice and check for neighbors (4 directions here).
Space complexity: O(E) we create neighbors list which can grow upto O(E) long
"""

import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def getNeighbors(row, col):
            neighbors = []
            if row > 0:
                neighbors.append([row-1, col])
            if row < len(grid) - 1:
                neighbors.append([row+1, col])
            if col > 0:
                neighbors.append([row, col-1])
            if col < len(grid[0]) - 1:
                neighbors.append([row, col + 1])
            return neighbors
    
        # depth first search solution
        def dfs(row, col):
            grid[row][col] = '0'
            neighborS = getNeighbors(row, col)
            for neighbor in neighborS:
                i, j = neighbor
                if grid[i][j] != '0':
                    dfs(i, j)
        
        # breadth first search solution
        def bfs(row, col):
            # make this visited
            grid[row][col] = '0'
            q = collections.deque()
            q.append((row, col))
            while len(q) > 0:
                (i, j) = q.popleft()
                neighborS = getNeighbors(i, j)
                for (n_i, n_j) in neighborS:
                    if grid[n_i][n_j] == '1':  # univsited
                        q.append((n_i, n_j))
                        grid[n_i][n_j] = '0'  # make it visited

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != '0':
                    islands += 1
                    dfs(i, j)
                    # bfs(i, j)

        return islands