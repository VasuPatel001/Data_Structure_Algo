"""
Leetcode 739: Daily Temperatures

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]

Constraints:
1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """
        Time Complexity:
            O(n) since we append and remove the temperature of day atmost once.
        Space Complexity:
            Input: O(n)
            Aux: O(n) st[] has (temp, i)
            Output: O(n) for answer[]
        """
        st = []
        answer = []
        for i in range(len(temperatures)-1, -1, -1):
            while st and st[-1][0] <= temperatures[i]:
                st.pop()
            
            # next greater value exist on top of stack
            if len(st) > 0:
                answer.append(st[-1][1] - i)
            else:
                answer.append(0)

            # append temperatures[i], i to st
            st.append((temperatures[i], i))
        # reverse the answer [] to get result from left to right
        answer.reverse()
        return answer