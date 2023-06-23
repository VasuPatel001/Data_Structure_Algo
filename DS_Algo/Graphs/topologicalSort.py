"""
Cycle detection pseudo code in directed graph using DFS
"""

class Graph:
    time = 0
    # arrival[], departure[] are initialized to -1 * len(grpah)
    # arrival[], departure[] record the arrival, departing time for each node in the graph traversal

    # visited[], parent[] are also initialized to - 1 and null respectively for each nodes in the graph

    def dfs(source):
        visited[source] = 1
        arrival[source] = time + 1

        for neighbor in adjacencyList[source]:
            if visited[neighbor] == -1:
                dfs(neighbor)
            else:  # neighbor is already visited
                # back edge -> cycle/loop found
                if departure time of neighbor is NOT set

                # forward edge
                elif arrival[source] < arrival[neighbor] and departure time of neighbor is set

                # cross edge
                else: arrival[source] > arrival[neighbor] and departure time of neighbor is set
        
        departure[source] = time + 1
        topologicalSort.append(source)


    # kahn's algorithm uses the concept of 0 indegree to build topological sort
    def kahn_algo(edges_list: list[list[int]], totalNode: int):
        from collections import deque
        q = deque()
        adjList = [[] for _ in range(totalNode)]
        indegree = [0 for _ in range(totalNode)]
        topsort = []

        for src, dst in edges_list:
            adjList[src].append(dst)
            indegree[dst] += 1
        
        for node in range(totalNode):
            if indegree[node] == 0:
                q.append(node)
        
        while q:
            node = q.popleft()
            topsort.append(node)
            for ngb in adjList[node]:
                indegree[ngb] -= 1
                if indegree[node] == 0:
                    q.append(ngb)
        if len(topsort) < totalNode:
            # cycle is found and hence topsort is not possible because DAG cannot be found
            return [] # topsort would be an empty list
        
        # Directed Acyclic Graph is found and hence topsort should be return as it is without reversing unlike the arrival, departure mehtod 
        return topsort

