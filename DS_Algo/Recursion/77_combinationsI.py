"""
Leetcode 77: Combination I

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
You may return the answer in any order.

Example 1:
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

Example 2:
Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.

Constraints:
1 <= n <= 20
1 <= k <= n
"""


class Solution:
    """
    Time Complexity:
        # of leaf node worker * leaf work: 
        # of internal node worker * internal node work

    Space Complexity:
        Input: O(1)
        Aux array: nums[]: O(N)
        Output: result[]: O(nCk * k)
    """
    def combine(self, n: int, k: int) -> list[list[int]]:
        nums = [i for i in range(1, n+1)]  # space: O(N)
        self.result = []  # space = nCk * k
        self.helper(nums, 0, k, [])
        return self.result

    def helper(self, nums: list[int], cur_idx: int, k: int, slate: list[int]):
        # backtracking case
        if len(slate) == k:
            self.result.append(slate[:])  # time: O(k)
            return
        # base-case /leaf-node
        if cur_idx == len(nums):
            return

        # recursive case
        # exclude
        self.helper(nums, cur_idx + 1, k, slate)

        # include
        slate.append(nums[cur_idx])  # time: O(1)
        self.helper(nums, cur_idx + 1, k, slate)
        slate.pop()  # time: O(1)
