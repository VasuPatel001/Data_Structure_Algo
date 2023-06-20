"""
Leetcode 90: Subsets II

Given an integer array nums that may contain duplicates, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""


class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        self.result = []
        nums.sort()
        self.helper(nums, 0, [])
        return self.result

    def helper(self, nums: list[int], cur_idx: int, slate: list[int]):
        if cur_idx == len(nums):
            self.result.append(slate[:])
            return

        # internal node worker
        copies = 0
        for i in range(cur_idx, len(nums)):
            if nums[cur_idx] == nums[i]:
                copies += 1
            else:
                break

        # exclude
        self.helper(nums, cur_idx + copies, slate)

        # include
        for copy_i in range(copies):
            slate.append(nums[cur_idx])
            self.helper(nums, cur_idx + copies, slate)

        for pop_i in range(copies):
            slate.pop()
