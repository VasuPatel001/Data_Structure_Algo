"""
Leetcode 213. House Robber II
Medium

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:
Input: nums = [1,2,3]
Output: 3

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 1000
"""


class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        if len(nums) == 3:
            return max(nums[0], nums[1], nums[2])
        if len(nums) == 4:
            return max(nums[0]+nums[2], nums[1]+nums[3])

        dp = [0 for _ in range(len(nums))]

        # We need to break the circle into a line
        # Case 1: if house[0] is robbed, in that case, house[1], house[n-1] cannot be robbed
        # we have to consult the best solution for house 2, ... n-2 
        dp[2] = nums[2]
        dp[3] = max(nums[2], nums[3])
        for i in range(4, len(nums)-1):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        case_1 = nums[0] + dp[len(nums) - 2]  # solution for this scenario

        # case 2: house[0] was not robbed
        # we have to consult the best solution for house 1, ... n-1
        dp[1] = nums[1]
        dp[2] = max(nums[1], nums[2])
        for i in range(3, len(nums)-1):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        case_2 = dp[len(nums) - 1]  # solution for this scenario

        return max(case_1, case_2)
