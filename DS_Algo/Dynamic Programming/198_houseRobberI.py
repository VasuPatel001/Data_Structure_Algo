"""
Leetcode 198: House Robber I

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 400
"""


class Solution:
    def rob(self, nums: list[int]) -> int:
        # Approach 1 (efficient)
        n = len(nums)
        dp_list = [0] * (n+1)

        # base-case
        dp_list[1] = nums[0]
        if n > 1:
            dp_list[2] = max(nums[0], nums[1])

        for idx in range(3, n+1):
            dp_list[idx] = max(dp_list[idx-1],
                               dp_list[idx-2] + nums[idx-1])
        return dp_list[n]

        # Approach 2 (less efficient)
        n = len(nums)
        dp = [0 for _ in range(n+2)]
        for i in range(2, n+2):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-2])
        return dp[-1]