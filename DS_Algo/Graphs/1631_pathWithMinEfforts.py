"""
Leetcode 1631: Path With Minimum Effort

You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.
A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.
Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

Example 1:
Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

Example 2:
Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].

Example 3:
Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.

Constraints:
rows == heights.length
columns == heights[i].length
1 <= rows, columns <= 100
1 <= heights[i][j] <= 106
"""

"""
Time Complexity:
    Inserting and deleting single element to heap-pq is O(logN) for N elements in heap-pq, since we have at most E elements in heap-pq and # of E can be at most V^2 for dense graph, so time complexity are:
    Here edges (E) and vertices (V) are both m x n
    Dense graph: O(E x logV)
    Sparse Graph: O(V x logV)

Space Complexity:
    Here edges (E) and vertices (V) are both m x n
    adjList: O(V+E)
    pq: O(E)
    auxillary array: captured and distance: O(V)
    Total: O(V+E)
"""
import heapq


class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        m = len(heights)
        n = len(heights[0])

        captured = {}
        # priority queue is (weight, (row, col))
        pq = [(0, (0, 0))]

        def getNgbs(row: int, col: int):
            ngbs = []
            dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            for (dir_x, dir_y) in dirs:
                if 0 <= row + dir_x < m and 0 <= col + dir_y < n:
                    ngbs.append((row + dir_x, col + dir_y))
            return ngbs

        # dijktra's algo
        while len(pq) > 0:
            (effort, node) = heapq.heappop(pq)
            nodex, nodey = node
            if node in captured:
                continue

            if node == (m-1, n-1):
                return effort

            captured[node] = effort
            for ngb in getNgbs(nodex, nodey):
                ngbx, ngby = ngb
                if ngb not in captured:
                    heapq.heappush(pq, (max(effort, abs(heights[ngbx][ngby] - heights[nodex][nodey])),
                                        ngb))
