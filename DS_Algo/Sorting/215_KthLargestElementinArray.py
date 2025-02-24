"""
Leetcode 215. Kth Largest Element in an Array
Medium

Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:
1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
"""
from typing import List
import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Quick Select algo
        def quickSelect(nums: List[int], start: int, end: int):
            if start > end:
                return

            pivot_idx = random.randint(start, end)
            nums[start], nums[pivot_idx] = nums[pivot_idx], nums[start]

            # lomutos partitioning
            small = start
            for big in range(start, end+1):
                if nums[big] < nums[start]:
                    small += 1
                    nums[small], nums[big] = nums[big], nums[small]
            nums[small], nums[start] = nums[start], nums[small]

            if len(nums)-k == small:
                return nums[small]
            elif len(nums)-k > small:
                return quickSelect(nums, small+1, end)
            else:  # k < small
                return quickSelect(nums, start, small-1)

        return quickSelect(nums, 0, len(nums)-1)
