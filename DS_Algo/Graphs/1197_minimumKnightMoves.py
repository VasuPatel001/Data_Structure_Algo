"""
Leetcode 1197: Minimum Knight Moves

In an infinited chess board with coordinates from -infinity to +infinity, you have a knight placed at (0, 0).
A knight has 8 possible moves it can make, as illustrated in the figure below. Each move is two squares in cardinal direction
and one other move in orthogonal direction.

Return the minimum number of moves required to place knight from (0, 0) to (x, y). It is guranteed that answer exist.
"""
import heapq


class Solution:
    def minKnightMoves(self, x: int, y: int):
        """
        Implement A* graph version where we keep track of captured coordinates
        where f(v) = g(v) +h(v)
        h(v) = heuristic of v
        g(v) = actual cost of v

        Parameters
        ----------
        x : int
            goal x coordinate
        y : int
            goal x coordinate
        """
        captured = {}
        pq = []
        # Note: priority below is f(v) = g(v) +h(v)
        # 2nd value is g(v)
        # 3rd, 4th value is current coordinate
        heapq.heappush(pq, ((x+y)//3, 0, 0, 0))
        while pq:
            (f, g, curr_x, curr_y) = heapq.heappop(pq)
            if (curr_x, curr_y) in captured:
                continue
            captured[(curr_x, curr_y)] = g
            if (curr_x, curr_y) == (x, y):
                return g
            
            for ngb_x, ngb_y in self.getNgbs(curr_x, curr_y):
                if (ngb_x, ngb_y) not in captured:
                    heapq.heappush(pq, ((1 + g + (abs(ngb_x - x) + abs(ngb_y - y)) // 3), g + 1, ngb_x, ngb_y))

    def getNgbs(self, x, y):
        ngbs = []
        dirs = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                (2, -1), (2, 1), (1, -2), (1, 2)]
        for dir_x, dir_y in dirs:
            ngbs.append((x + dir_x), (y + dir_y))
        return ngbs