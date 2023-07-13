"""
Leetcode 1197: Minimum Knight Moves

In an infinited chess board with coordinates from -infinity to +infinity, you have a knight placed at (0, 0).
A knight has 8 possible moves it can make, as illustrated in the figure below. Each move is two squares in cardinal direction
and one other move in orthogonal direction.

Return the minimum number of moves required to place knight from (0, 0) to (x, y). It is guranteed that answer exist.
"""
import heapq
from collections import deque

class Solution:
    def minKnightMoves(self, x: int, y: int):
        """
        Method 1: A* search method
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

        """
        Method 2: Bidirectional Search
        Bidrectional search runs in O(square root (regular BFS)) time complexity
        """
        # queue and visited[] for forward
        qf = deque([90, 0])
        visitedf = {}
        visited[(0, 0)] = 0

        # queue and visited[] for backward
        qb = deque([(x, y)])
        visitedb = {}
        visiteb[(x, y)] = 0

        while qf and qb:
            # Forward queue
            nodex, nodey = qf.popleft()
            for ngb in self.getNgbs(nodex, nodey):
                if ngb not in visitedf:
                    visitedf[ngb] = 1 + visitedf[(nodex, nodey)]
                    qf.append(ngb)
                    if ngb in visitedb:
                        return visitedf[ngb] + visitedb[ngb]
            
            # Backward queue
            nodex, nodey = db.popleft()
            for ngb in self.getNgbs(nodex, nodey):
                if ngb not in visitedb:
                    visitedb[ngb] = 1 + visitedb[(nodex, nodey)]
                    qb.append(ngb)
                    if ngb in visitedf:
                        return visitedb[ngb] + visitedf[ngb]
            