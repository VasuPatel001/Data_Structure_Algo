"""
Leetcode 498. Diagonal Traverse
Medium

Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

Example 1:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]

Example 2:
Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]

Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
-105 <= mat[i][j] <= 105
"""
from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        """
        NOTE: The key here is to realize that the sum of indices on all DIAGONALS are EQUAL.

        Time Comlexity: O(N)
        Space: O(N)
        """
        hmap = {}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                diag_val = i+j
                if diag_val not in hmap:
                    hmap[diag_val] = []
                hmap[diag_val].append(mat[i][j])

        result = []
        for diag_sum, lst in hmap.items():
            if not diag_sum % 2:
                [result.append(i) for i in hmap[diag_sum][::-1]]
            else:
                [result.append(i) for i in hmap[diag_sum][::]]

        return result
