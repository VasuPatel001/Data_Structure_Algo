"""
Leetcode 59. Spiral Matrix II
Medium
Solution: https://www.youtube.com/watch?v=pLjhGbKMxL4&t=5s

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]
Constraints:

1 <= n <= 20
"""
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0 for _ in range(n)] for _ in range(n)]
        x, y = 0, 0
        dx, dy = 1, 0
        cur = 1
        for _ in range(n*n):
            result[y][x] = cur 
            cur += 1

            if not 0 <= x+dx < n or not 0 <= y+dy < n or result[y+dy][x+dx] != 0:
                dx, dy = -dy, dx

            x += dx
            y += dy

        return result
