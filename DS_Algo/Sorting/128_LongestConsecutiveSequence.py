"""
128. Longest Consecutive Sequence
Medium - https://leetcode.com/problems/longest-consecutive-sequence/description/

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Time: O(n), outer for loop will run only for start of sequence element, 
        and innter while loop for run for intermediate values of sequence present in hash_set
        Space: O(n), used for hash_set
        """
        hash_set = set(nums)
        max_len = 0
        for n in hash_set:
            if n-1 not in hash_set:
                local_len = 1
                while n+local_len in hash_set:
                    local_len += 1
                max_len = max(max_len, local_len)
        return max_len
