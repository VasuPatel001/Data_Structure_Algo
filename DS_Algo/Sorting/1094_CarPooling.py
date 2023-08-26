"""
Leetcode 1094. Car Pooling

There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).
You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.
Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

Example 1:
Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false

Example 2:
Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true

Constraints:
1 <= trips.length <= 1000
trips[i].length == 3
1 <= numPassengersi <= 100
0 <= fromi < toi <= 1000
1 <= capacity <= 105
"""
import heapq


class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        trips = sorted(trips, key=lambda x: x[1])
        pq = []
        current_people = 0
        for i in range(len(trips)):
            # Step 1: extract nextstart
            if i == len(trips) - 1:
                nextstart = float('inf')
            else:
                nextstart = trips[i+1][1]

            # Step 2: start the CURRENT interval
            heapq.heappush(pq, (trips[i][2], trips[i][0]))
            current_people += trips[i][0]
            if current_people > capacity:
                return False

            # Step 3: End the CUREENT interval by 
            # restore capacity when min trip's end duration < nextstart
            while pq and pq[0][0] <= nextstart:
                end, passenger = heapq.heappop(pq)
                current_people -= passenger
        return True
