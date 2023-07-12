"""
Leetcode 907: Sum of Subarray Minimums

Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

Example 1:
Input: arr = [3,1,2,4]
Output: 17
Explanation:
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.

Example 2:
Input: arr = [11,81,94,43,3]
Output: 444

Constraints:
1 <= arr.length <= 3 * 104
1 <= arr[i] <= 3 * 104
"""


class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        """
        Time Complexity:
            O(n)
        Space Complexity:
            Input: arr: O(n)
            Aux: O(n) since localans[] and st[]
            Output: globalsum O(1)
        """
        # NOTE: Here we implement decrease and conquer from left to right, so we find 'previous smaller' value
        # if we were to implement decrease and conquer from right to left, we can use 'next smaller' value

        globalsum = 0
        localans = [0 for _ in range(len(arr))]
        st = []
        for i in range(len(arr)):
            while st and st[-1][0] >= arr[i]:
                st.pop()
            # process the previous smaller value
            if st:
                span = i - st[-1][1]
                localans[i] = localans[st[-1][1]]
            else:
                span = i + 1
            # update localans and globalsum
            localans[i] += span * arr[i]
            globalsum = (globalsum + localans[i]) % 1000000007

            # append arr[i] to st
            st.append((arr[i], i))
        return globalsum