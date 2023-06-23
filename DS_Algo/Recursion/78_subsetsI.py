"""
Leetcode 78: Subsets I

Given an integer array nums of unique elements, return all possible 
subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""


class Solution:
    def helper(self, nums: List[int], cur_idx: int, slate: List[int], output: List[List[int]]):
        ####################################################
        # Solution 1: Optimal
        ####################################################
        if cur_idx == len(nums):
            output.append(slate)
            return
        
        # include
        self.helper(nums, cur_idx + 1, slate + [nums[cur_idx]], output)

        # exclude
        self.helper(nums, cur_idx + 1, slate, output)
        
        ####################################################
        # Solution 2: Not that Optimal, but follows template of append and pop
        ####################################################
        if cur_idx == len(nums):
            output.append(slate[:])
            return
        
        # include
        slate.append(nums[cur_idx])
        self.helper(nums, cur_idx + 1, slate, output)
        slate.pop()

        # exclude
        self.helper(nums, cur_idx + 1, slate, output)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        self.helper(nums, 0, [], output)
        return output
