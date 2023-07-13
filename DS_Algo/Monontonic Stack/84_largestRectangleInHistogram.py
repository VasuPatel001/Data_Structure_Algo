"""
Leetcode 84. Largest Rectangle in Histogram

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4

Constraints:
1 <= heights.length <= 105
0 <= heights[i] <= 104
"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
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
        
        # find local answer
        globalmax = 0
        for i in range(len(heights)):
            localans = heights[i] * (left_span[i] + right_span[i] - 1)
            globalmax = max(globalmax, localans)
        return globalmax
        