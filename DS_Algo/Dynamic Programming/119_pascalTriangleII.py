"""
Leetcode 119. Pascal's Triangle II

Easy

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1,1]

Constraints:
0 <= rowIndex <= 33
Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
"""


class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        dp_table = [[1 for _ in range(row+1)] for row in range(rowIndex+1)]

        if rowIndex < 2:
            return dp_table[rowIndex]

        for row in range(2, len(dp_table)):
            for col in range(1, len(dp_table[row]) - 1):
                dp_table[row][col] = dp_table[row-1][col-1] + dp_table[row-1][col]
        return dp_table[rowIndex]