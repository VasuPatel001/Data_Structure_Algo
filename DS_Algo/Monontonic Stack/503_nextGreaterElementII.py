"""
Leetcode 503. Next Greater Element II

Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.
The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

Example 1:
Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.

Example 2:
Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]

Constraints:
1 <= nums.length <= 104
-109 <= nums[i] <= 109
"""


class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        """
        Time complexity:
        O(2n) because 1 is used for stack initialization and
        2nd pass is used for performing normal monotonic stack (next larger) implementation

        Space Complexity:
            Input: O(n)
            Aux: O(n) because of st[]
            output: O(n) because of result[]
        """

        # initialization
        st = []
        for i in range(len(nums)-1, -1, -1):
            while st and st[-1] <= nums[i]:
                st.pop()
            # append nums[i] to st
            st.append(nums[i])

        # normal template for monotonic stack for finding next greater element
        result = [-1 for _ in range(len(nums))]
        for i in range(len(nums)-1, -1, -1):
            while st and st[-1] <= nums[i]:
                st.pop()
            # process next greater element
            if st:
                result[i] = st[-1]

            # append nums[i] to st
            st.append(nums[i])
        return result
