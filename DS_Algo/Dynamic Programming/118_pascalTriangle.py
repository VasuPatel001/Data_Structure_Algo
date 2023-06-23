"""
Leetcode 118: Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]

Constraints:
1 <= numRows <= 30
"""


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        dp_table = [[1 for _ in range(row+1)] for row in range(numRows)]

        for row in range(2, len(dp_table)):
            for col in range(1, len(dp_table[row]) - 1):
                dp_table[row][col] = dp_table[row-1][col-1] + dp_table[row-1][col]

        return dp_table
