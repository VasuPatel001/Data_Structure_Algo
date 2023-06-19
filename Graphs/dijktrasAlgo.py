"""
Shortest path from source to destination in a Weighted Directed Graph
Dijktra's Algo:
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
import queue


def dijktrasAlgo(source: int, n: int, connections: list[list[int]]):
    adjList = [[] for _ in range(n)]
    for (u, v, cost) in connections:
        adjList[u].append((v, cost))

        # Note dijktra's algo work on both Directed and Undirected graph,
        # so depending on type of graph include it if needed.
        adjList[v].append((u, cost))

    captured = [-1 for _ in range(n)]
    distance = [-1 for _ in range(n)]

    # start capturing source node and begin the dijktra's algo
    captured[source] = 1
    distance[0] = 0
    pq = queue.PriorityQueue(maxsize=0)
    for (ngb, cost) in adjList[source]:
        pq.put((cost, ngb))   

    while pq.qsize > 0:
        priority, node = pq.get()
        if captured[node] == 1:  # if node has already been capture, we let it go
            continue

        captured[node] = 1
        distance[node] = priority

        for (ngb, cost) in adjList[node]:
            if captured[node] == -1:
                # NOTE: Main difference between prims and dijktra's algo is
                # during pushing ngb with shortest distance to priority queue.
                pq.put((distance[node] + cost, ngb))

    return distance  # we may return distance[] entirely or distance[destination] if asked for specific destination node
