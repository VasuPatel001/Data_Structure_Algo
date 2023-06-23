"""
Leetcode 347: Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order. 

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
"""
import heapq


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        cnt = {}
        for num in nums:
            if num not in cnt:
                cnt[num] = 0
            cnt[num] += 1
        ########################################################
        # Method 1: Use sorted() with key and lambda function
        ########################################################
        dct = dict(sorted(cnt.items(), key=lambda x: x[1], reverse=True)[:k])
        return [key for key in dct.keys()]

        ########################################################
        # Method 2: Use heapq
        ########################################################
        min_heap = []
        for num, freq in cnt.items():
            if len(min_heap) == k:
                heapq.heappushpop(min_heap, (freq, num))
            else:
                heapq.heappush(min_heap, (freq, num))

        result = []
        while min_heap:
            result.append(heapq.heappop(min_heap)[1])
        return result
