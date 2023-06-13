"""
Leetcode 120: Triangle

Given a triangle array, return the minimum path sum from top to bottom.
For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Example 2:
Input: triangle = [[-10]]
Output: -10

Constraints:
1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-104 <= triangle[i][j] <= 104
"""


class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        # construct a dp_table similar to shape of trianlge
        dp_table = [[0 for _ in range(row+1)] for row in range(len(triangle))]

        # base case is last row of the dp_table
        for col in range(len(triangle)):
            dp_table[-1][col] = triangle[-1][col]

        # start filling in dp_table by using the min_value of dp_table and current value from triangle
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(row + 1):
                min_value = min(dp_table[row+1][col], dp_table[row+1][col+1])
                dp_table[row][col] = triangle[row][col] + min_value

        return dp_table[0][0]
