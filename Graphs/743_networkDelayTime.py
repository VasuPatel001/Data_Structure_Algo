"""
Leetcode 743: Network Delay Time

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.
We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Example 2:
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

Example 3:
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1

Constraints:
1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
"""
import queue


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Time Complexity:
            Inserting and deleting single element to heap-pq is O(logN) for N elements in heap-pq, since we have at most E elements in heap-pq and # of E can be at most V^2 for dense graph, so time complexity are:
            Dense graph: O(E x logV)
            Sparse Graph: O(V x logV)

        Space Complexity:
            adjList: O(V+E)
            pq: O(E)
            auxillary array: captured and distance: O(V)
            Total: O(V+E)
        """

        # 1. Build a weighted directed graph using adjacency list
        adjList = [[] for _ in range(n+1)]
        for (src, dst, time) in times:
            adjList[src].append((dst, time))

        # 2. Dijktra's algo
        captured = [-1 for _ in range(n+1)]
        distance = [-1 for _ in range(n+1)]

        # start with source node k
        captured[k] = 1
        distance[k] = 0  # note, we may use single captured array to keep track of distance as well.

        # book-keeping required for given question
        numCaptured = 1
        lastDist = 0

        pq = queue.PriorityQueue(maxsize=0)
        for (ngb, time) in adjList[k]:
            pq.put((distance[k] + time, ngb))

        while pq.qsize() > 0:
            priority, node = pq.get()  # extract's min priority (time) value
            if captured[node] != -1:
                continue

            # we know that node is not captured and it still lies in discovered zone
            captured[node] = 1
            distance[node] = priority
            numCaptured += 1
            lastDist = priority

            for (ngb, time) in adjList[node]:
                if captured[ngb] == -1:
                    pq.put((distance[node] + time, ngb))

        return lastDist if numCaptured == n else -1
