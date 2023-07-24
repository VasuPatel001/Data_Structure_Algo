"""
Leetcode 1762: Buildings with Ocean View

Observation: The buildings with an ocean view are in strictly (monotonically) decreasing order of heights.

There are n buildings in a line. You are given an integer array 'heights' of size 'n' that represents
the height of the buildings in the line.
The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without
obstruction.

Formally, a building has an ocean view, if the all the buildings to its right are smaller in height.
Return a list of indices (0) indexed of buldings that have an ocean view, sorted in increasing order.

Example 1: heights = [4, 2, 3, 1]
Output: [0, 2, 3]
Explanation: Building 1 (0-indexed) does not have ocean view beacuse it is obstructed by building of height 3.

Example 2: heights = [4, 3, 2, 1]
Output: [0, 1, 2, 3]
Explanation: Since the buildings are placed in decreasing order of heights, all buildings have ocean view.

Example 3: heights: [1, 3, 2, 4]
Output: [3]
Explanation: Only last building with height 4 has ocean view.

Constraints:
1<= heights.length <= 10^5
1< = heights[i] <= 10^9
"""


class Solution:
    def buildingsWithOceanView(heights: list[int]) -> list[int]:
        """
        Context 1:
        Streaming context when buildings are constructed one after another from left to right
        Use the concept of monotonic stack
        Decrease and conquer approach from Left to Right
        Time Complexity:
            O(n) because amortized analysis of individual building enters and exits the monotonic stack is atmost 1
        Space Complexity:
            Input: O(n)
            Output result: O(n)

        """
        monotonic_stack = []
        for i in range(len(heights)):
            while monotonic_stack and monotonic_stack[-1][0] <= heights[i]:
                monotonic_stack.pop()
            monotonic_stack.append(heights[i], i)
        result = []
        for _, i in monotonic_stack:
            result.append(i)
        return result


        """
        Context 2:
        When all buildings are given as an array at the same time
        Decrease and conquer approach from Right to Left
        Time Complexity:
            O(n) since a linear scan from right to left is required for decrease and conquer approach.
        Space Complexity:
            Input: O(n)
            Aux space: O(1) of maxheight variable
            Output result: O(n)
        """
        result = []
        maxheight = 0
        for i in range(len(heights)-1, -1, -1):
            if heights[i] > maxheight:
                result.append(i)
                maxheight = heights[i]
        result.reverse()
        return result
