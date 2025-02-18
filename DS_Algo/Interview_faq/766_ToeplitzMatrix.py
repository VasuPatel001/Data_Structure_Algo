"""
Leetcode 766. Toeplitz Matrix
Imp solution: https://leetcode.com/problems/toeplitz-matrix/solutions/516366/python-follow-up-1-with-explanation-and-diagrams/

Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

Example 1:
Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true

Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.

Example 2:
Input: matrix = [[1,2],[2,2]]
Output: false
Explanation:
The diagonal "[1, 2]" has different elements.

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 20
0 <= matrix[i][j] <= 99 

Follow up:
What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
What if the matrix is so large that you can only load up a partial row into the memory at once?
"""
from collections import deque
from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        """
            Runtime: O(MN)
               Every cell is touched about once.
            Space: O(N)
               We need to store a deque of length equal to the number of columns.
        """
        # Validate Input
        if not matrix or not matrix[0]:
            return False                

        # Create a deque tracking the expected values for the next row
        expected = deque(matrix[0])

        # Iterate through all the remaining rows, verifying they align with the
        #   expected row.
        for row_i in range(1, len(matrix)):
            row = matrix[row_i]
            expected.pop()
            expected.appendleft(row[0])


            # Only check from index 1 and down as we've just added index 0 to expected
            for col_i in range(1, len(row)):
                if row[col_i] != expected[col_i]:
                    return False
            break

        # If we've reached here, all diagonals aligned
        return True
