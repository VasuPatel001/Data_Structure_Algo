"""
Leetcode 773: Sliding Puzzle
This is a question from State Space Search

On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty square represented by 0. A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.
The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].
Given the puzzle board board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1. 

Example 1:
Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.

Example 2:
Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.

Example 3:
Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]

Constraints:
board.length == 2
board[i].length == 3
0 <= board[i][j] <= 5
Each value board[i][j] is unique.
"""
from collections import deque


class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        """
        Time Complexity:
            Normal BFS run time is (E+V) here we have E = V
            O(N^2 factorial)
            for given N * N grid, first cell can be filled in N^2 times, 
            next cell in N^2 - 1,
            upto last cell in 1 ways
            Hence O(N^2 factorial) is total run time
        """
        # solving through BFS
        visited = {}
        ((i, j, k), (l, m, n)) = board
        q = deque()
        q.append(((i, j, k), (l, m, n)))
        visited[((i, j, k), (l, m, n))] = 0
        while q:
            node = q.popleft()
            for ngb in self.getNgbs(node):
                if ngb not in visited:
                    visited[ngb] = 1 + visited[node]
                    q.append(ngb)
            if ((1, 2, 3), (4, 5, 0)) in visited:
                return visited[((1, 2, 3), (4, 5, 0))]
        # else:
        return -1

    def getNgbs(self, node):
        ((i, j, k), (l, m, n)) = node
        ngbs = []
        if i == 0:
            ngbs.append(((j, i, k), (l, m, n)))
            ngbs.append(((l, j, k), (i, m, n)))
        elif j == 0:
            ngbs.append(((j, i, k), (l, m, n)))
            ngbs.append(((i, k, j), (l, m, n)))
            ngbs.append(((i, m, k), (l, j, n)))
        elif k == 0:
            ngbs.append(((i, k, j), (l, m, n)))
            ngbs.append(((i, j, n), (l, m, k)))
        elif l == 0:
            ngbs.append(((l, j, k), (i, m, n)))
            ngbs.append(((i, j, k), (m, l, n)))
        elif m == 0:
            ngbs.append(((i, j, k), (m, l, n)))
            ngbs.append(((i, m, k), (l, j, n)))
            ngbs.append(((i, j, k), (l, n, m)))
        else:  # n == 0
            ngbs.append(((i, j, n), (l, m, k)))
            ngbs.append(((i, j, k), (l, n, m)))
        return ngbs
