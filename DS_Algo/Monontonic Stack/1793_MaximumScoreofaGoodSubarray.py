"""
Leetcode 1793. Maximum Score of a Good Subarray

You are given an array of integers nums (0-indexed) and an integer k.
The score of a subarray (i, j) is defined as min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1). A good subarray is a subarray where i <= k <= j.
Return the maximum possible score of a good subarray.

Example 1:
Input: nums = [1,4,3,7,4,5], k = 3
Output: 15
Explanation: The optimal subarray is (1, 5) with a score of min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15. 

Example 2:
Input: nums = [5,5,4,5,4,1,1,1], k = 0
Output: 20
Explanation: The optimal subarray is (0, 4) with a score of min(5,5,4,5,4) * (4-0+1) = 4 * 5 = 20.

Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 2 * 104
0 <= k < nums.length
"""


class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        # pre-computer LEFT spans for previous smaller value
        st = []
        left_span = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            while st and st[-1][0] >= nums[i]:
                st.pop()
            # prev small value is at top of stack
            if st:
                left_span[i] = i - st[-1][1]
            else:
                left_span[i] = i + 1
            st.append((nums[i], i))

        # pre-computer RIGHT spans for next smaller value
        st = []
        right_span = [0 for _ in range(len(nums))]
        for i in range(len(nums) -1, -1, -1):
            while st and st[-1][0] >= nums[i]:
                st.pop()
            # prev small value is at top of stack
            if st:
                right_span[i] = st[-1][1] - i
            else:
                right_span[i] = len(nums) - i
            st.append((nums[i], i))

        # find local answer
        globalmax = 0
        for i in range(len(nums)):
            localans = nums[i] * (left_span[i] + right_span[i] - 1)
            if i - left_span[i] + 1 <= k <= i + right_span[i] - 1:
                globalmax = max(globalmax, localans)
        return globalmax
