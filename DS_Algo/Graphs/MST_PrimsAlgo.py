"""
Minimum Spanning Tree
Prims Algo:
    It is greedy approach of selecting edges with minimum weights starting from a source vertex (captured) and
    keep on expanding captured area.

Implementation:
    Prims Algo uses priority queue
"""

"""
Time complexity:
    Time complexity for MST Prims algo: 
        since we are not changing the priority of the already existing node in pq;
        but rather we are adding duplicate values of nodes with different priority to pq
        so at most we would be adding all Edges (E) to pq
        Hence, E insertions and deletions need to be made in Heap-priority queue which is each O(logE)
        So, total is O(E x logE)

    Hence, time complexity is given as:
        dense graph: O(E x logV)
        sparse graph: O(V x logV)
"""
import heapq


def primsAlgo(source: int, n: int, connections: list[list[int]]):
    adjList = [[] for _ in range(n)]
    for (u, v, cost) in connections:
        adjList[u].append((v, cost))
        adjList[v].append((u, cost))

    captured = [-1 for _ in range(n)]
    captured[source] = 1
    pq = []
    for (ngb, cost) in adjList[source]:
        heapq.heappush(pq, (cost, ngb))

    totalCost = 0

    while pq:
        priority, node = heapq.heappop(pq)
        if captured[node] == 1:  # if node has already been capture, we let it go
            continue

        captured[node] = 1
        totalCost += priority

        for (ngb, cost) in adjList[node]:
            if captured[node] == -1:
                heapq.heappush(pq, (cost, ngb))

    return totalCost
