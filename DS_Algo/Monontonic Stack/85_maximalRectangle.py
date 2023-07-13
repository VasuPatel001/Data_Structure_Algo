"""
Leetcode 85. Maximal Rectangle

Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.

Example 2:
Input: matrix = [["0"]]
Output: 0

Example 3:
Input: matrix = [["1"]]
Output: 1

Constraints:
rows == matrix.length
cols == matrix[i].length
1 <= row, cols <= 200
matrix[i][j] is '0' or '1'.
"""


class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        """
        Idea to solve this problem:
            Logic in continuation from Leetcode Q: 84
            In this question, ground or the base of the buildings is not fixed.
            Hence, we take each row as inidividual ground level and solve for the
            heights of the buildings to find the maximum area of rectangle in histogram.
            Hence, we loop over each row to form the heights[] and then apply same
            logic as for Leetcode 84: Largest rectangle in histogram.

        Time Complexity:
            O(row * col) because we loop over each row O(row) to find heights
            of the rectangles and then left_span, right_span and updating global_max takes O(col)
        Space Complexity:
            Input: O(row * col): matrix[[]] 
            Aux: O(n): heights[], left_span, right_span
            Output: O(1), global_max is only returned
        """
        rows = len(matrix)
        cols = len(matrix[0])
        heights = [0 for _ in range(cols)]
        global_max = 0

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == '1':
                    heights[col] += 1
                else:  # matrix[row][col] == 0
                    heights[col] = 0

            # pre-computer LEFT spans for previous smaller value
            st = []
            left_span = [0 for _ in range(len(heights))]
            for i in range(len(heights)):
                while st and st[-1][0] >= heights[i]:
                    st.pop()
                # prev small value is at top of stack
                if st:
                    left_span[i] = i - st[-1][1]
                else:
                    left_span[i] = i + 1
                st.append((heights[i], i))

            # pre-computer RIGHT spans for next smaller value
            st = []
            right_span = [0 for _ in range(len(heights))]
            for i in range(len(heights) -1, -1, -1):
                while st and st[-1][0] >= heights[i]:
                    st.pop()
                # prev small value is at top of stack
                if st:
                    right_span[i] = st[-1][1] - i
                else:
                    right_span[i] = len(heights) - i
                st.append((heights[i], i))

            # update global_max
            for i in range(len(heights)):
                localans = heights[i] * (left_span[i] + right_span[i] - 1)
                global_max = max(global_max, localans)
        return global_max
