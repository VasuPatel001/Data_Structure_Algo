""" 
Meeting Rooms II (N meeting Rooms): Leetcode 253

Given an array of meeting time intervals 'intervals' where intervals = [start, end]
return the minimum number of meeting rooms needed.

Ex: intervals: [[10, 30], [5, 10], [15, 20]]
Output: 2

Ex: intervals: [[7, 10], [2, 4]]
Output: 1
"""
import heapq

def minMeetingRooms(intervals: list[list[int]]) -> int:
    intervals.sort()  # Presorting: O(N * logN)
    pq = []
    globalmax = 0

    for i in range(len(intervals)):
        if i == len(intervals) - 1:
            nextStart = float('inf')
        else:
            nextStart = intervals[i+1][0]
        
        heapq.heappush(pq, intervals[i][1])
        globalmax = max(globalmax, len(pq))

        while pq and pq[0] < nextStart:
            heapq.heappop(pq)
    
    return globalmax