"""
Leetcode 40: Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[[1,1,6],
[1,2,5],
[1,7],
[2,6]]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output:
[[1,2,2],
[5]]

Constraints:
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""


class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        arr = sorted(candidates, reverse=True)
        self.result = []
        self.helper(arr, 0, target, [])
        return self.result

    def helper(self, arr: list[int], cur_idx: int, target: int, slate: list[int]):
        if sum(slate) == target:
            self.result.append(slate[:])
            return
        if sum(slate) > target or cur_idx == len(arr) or sum(arr[cur_idx:]) < target - sum(slate):
            return

        # internal node worker
        count = 0
        for i in range(cur_idx, len(arr)):
            if arr[i] == arr[cur_idx]:
                count += 1
            else:
                break

        # include
        for _ in range(count):
            slate.append(arr[cur_idx])
            self.helper(arr, cur_idx + count, target, slate)

        for _ in range(count):
            slate.pop()

        # exclude
        self.helper(arr, cur_idx + count, target, slate)
