"""
Leetcode 416: Partition Equal Subset Sum

Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

Constraints:
1 <= nums.length <= 200
1 <= nums[i] <= 100
"""

"""
Time Complexity: O(len(nums) * target)
Space Complexity: 
"""


class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        tot_sum = sum(nums)
        if tot_sum % 2:
            return False

        target = tot_sum // 2

        dp_table = [[None for _ in range(target + 1)] for _ in range(len(nums) + 1)]

        for row in range(len(nums) + 1):
            dp_table[row][0] = True

        for col in range(1, target + 1):
            dp_table[len(nums)][col] = False

        for i in range(len(nums) - 1, -1, -1):
            for s in range(1, target + 1):
                if s >= nums[i]:
                    dp_table[i][s] = dp_table[i+1][s-nums[i]]
                dp_table[i][s] = dp_table[i][s] or dp_table[i+1][s]

        return dp_table[0][target]

        """
        Space Optimized
        """
        tot_sum = sum(nums)
        if tot_sum % 2:
            return False
        
        target = tot_sum // 2

        dp_table = [[None for _ in range(target + 1)] for _ in range(2)]

        for row in range(2):
            dp_table[row][0] = True
        
        for col in range(1, target + 1):
            dp_table[len(nums) % 2][col] = False
        
        for i in range(len(nums) - 1, -1, -1):
            for s in range(1, target + 1):
                if s >= nums[i]:
                    dp_table[i%2][s] = dp_table[(i+1)%2][s-nums[i]]
                dp_table[i%2][s] = dp_table[i%2][s] or dp_table[(i+1)%2][s]

        return dp_table[0][target]