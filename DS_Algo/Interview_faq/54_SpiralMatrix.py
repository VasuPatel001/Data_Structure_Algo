"""
Leetcode 54. Spiral Matrix
Medium
Solution: https://www.youtube.com/watch?v=RSjo4A8WfQ8&t=4s

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Time complexity:O(row X col)
        Space complexity:O(1)
        """
        x, y = 0, 0
        dx, dy = 1, 0
        row, col = len(matrix), len(matrix[0])
        result = []
        for _ in range(row * col):
            result.append(matrix[y][x])
            matrix[y][x] = '.'

            if not 0 <= x+dx < col or not 0 <= y+dy < row or matrix[y+dy][x+dx] == '.':
                dx, dy = -dy, dx

            x += dx
            y += dy

        return result
