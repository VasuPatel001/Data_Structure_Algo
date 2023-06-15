"""
Leetcode 55. Jump Game

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:
1 <= nums.length <= 104
0 <= nums[i] <= 105
"""


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # Approach 1 (efficient): beats ~80% in leetcode
        n = len(nums)
        last = n - 1
        for  i in range(n-1, -1, -1):
            if i + nums[i] >= last:
                last = i  # remember the last house you can reach
        return last == 0

        # Approach 2 (less efficient but easy to understand): beats ~6% in leetcode
        n = len(nums)
        dp = [False for _ in range(n)]
        dp[n-1] = True

        for i in range(n-2, -1, -1):
            steps = nums[i]
            for step in range(1, steps+1):
                if dp[i+step] == True:
                    dp[i] = True
                    break
        return dp[0]

        