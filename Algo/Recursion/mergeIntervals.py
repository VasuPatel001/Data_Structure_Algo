"""LeetCode 56. Merge Intervals
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.


"""

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        result = [intervals[0]]
        for i in range(len(intervals)):
            if result[-1][1] >= intervals[i][0]:
                result[-1] = (result[-1][0], (max(result[-1][1], intervals[i][1])))
            else: # no overlap
                result.append(intervals[i])
        return result