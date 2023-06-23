"""
Leetcode 47: Permutations II

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Constraints:
1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""


class Solution:
    def helper(self, nums: list[int], cur_idx: int):
        if cur_idx == len(nums):
            self.result.append(nums[:])
            return

        # internal node workers
        hmap = {}
        for pick in range(cur_idx, len(nums)):
            if nums[pick] not in hmap:
                hmap[nums[pick]] = 1
                nums[cur_idx], nums[pick] = nums[pick], nums[cur_idx]
                self.helper(nums, cur_idx + 1)
                nums[cur_idx], nums[pick] = nums[pick], nums[cur_idx]

    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        self.result = []
        self.helper(nums, 0)
        return self.result
