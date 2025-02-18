"""
Leetcode 566. Reshape the Matrix
Easy

In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.
You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.
The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.
If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]

Example 2:
Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]

Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 100
-1000 <= mat[i][j] <= 1000
1 <= r, c <= 300
"""
from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        """
        flatten = [0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10, 11]
                                [0,  1,  2,  3,  4,  5,   6,  7,  8,  9,  10, 11]
        row_index: 0			| c0  c1  c2  c3  c4  c5 |
        row_index: 1                           			 | c0  c1  c2  c3  c4  c5 |

        index in flatten:  [row_index * c : row_index * c + c])

		        	            [0*6       :      0*6 + 6],
				        						         [1*6        :       1*6+6]
												 
                                [0          :           6],  
								        		         [6          :          12]
        """
        m = len(mat)
        n = len(mat[0])
        if (m*n) != (r*c):
            return mat

        flatten = []
        for row in mat:
            for num in row:
                flatten.append(num)

        result = []
        for row_idx in range(r):
            result.append(flatten[row_idx * c: row_idx*c + c])

        return result
