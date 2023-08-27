"""
Leetcode 46: Permutations I

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""


class Solution:
    """
    Space optimized Mutable solution is presented below
    We use the input [] of nums to swap the ith and cur_idx position.

    Time Comlexity:
        Leaf node worker: O(n! * n)
        Internal node worker: O(n! * n)
        Total: O(n1 * n)
    Space Complexity:
        Input: O(n)
        Aux: O(1)  NOTE: since we use space optimized Mutable solution, aux space if O(1)
        Output: O(n! * n)
    """
    def helper(self, nums: list[int], cur_idx: int, result: list[list[int]]):
        if cur_idx == len(nums):
            result.append(nums[:])
            return

        # internal worker
        for i in range(cur_idx, len(nums)):
            nums[cur_idx], nums[i] = nums[i], nums[cur_idx]
            self.helper(nums, cur_idx + 1, result)
            nums[cur_idx], nums[i] = nums[i], nums[cur_idx]

    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        self.helper(nums, 0, result)
        return result

    """
    Mutable solution with non-optimized solution using slate []
    
    Time Comlexity:
        Leaf node worker: O(n! * n)
        Internal node worker: O(n! * n)
        Total: O(n1 * n)
    Space Complexity:
        Input: O(n)
        Aux: O(n)  NOTE: since we do NOT use space optimized Mutable solution, aux space if O(n)
        Output: O(n! * n)
    """
    def helper(self, nums: list[int], cur_idx: int, slate: list[int]):
        # base case/leaf node worker
        if cur_idx == len(nums):
            self.result.append(slate[:])
            return
        
        # internal node worker
        for i in range(cur_idx, len(nums)):
            nums[cur_idx], nums[i] = nums[i], nums[cur_idx]
            slate.append(nums[i])  # NOTE: this is the difference
            self.helper(nums, cur_idx + 1, slate)
            slate.pop()  # NOTE: this is the difference
            nums[cur_idx], nums[i] = nums[i], nums[cur_idx]


    def permute(self, nums: list[int]) -> list[int]:
        self.result = []
        self.helper(nums, 0, [])
        return self.result
