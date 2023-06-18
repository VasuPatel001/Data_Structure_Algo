"""
Leetcode 785: Is Graph Bipartite?

There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.

Example 1:
Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.

Example 2:
Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.

Constraints:
graph.length == n
1 <= n <= 100
0 <= graph[u].length < n
0 <= graph[u][i] <= n - 1
graph[u] does not contain u.
All the values of graph[u] are unique.
If graph[u] contains v, then graph[v] contains u.
"""

"""
Time complexity: O(V + E): We visit each node once and all neighbors exactly once.
Space complexity: O(E): since the adjacency list provided as an input, we only need to create a queue/deque
"""

import collections

class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        # graph is in the form of adjacency list
        n = len(graph)
        visited = [-1] * n
        parent = [None] * n
        distance = [-1] * n
        color = [-1] * n

        def dfs_check_bipartite(source):
            visited[source] = 1
            for ngb in graph[source]:
                if visited[ngb] == -1:
                    parent[ngb] = source
                    color[ngb] = not color[source]
                    if not dfs_check_bipartite(ngb):
                        return False
                else:  # ngb is already visited and hence cycle might be there
                    if color[source] == color[ngb]:
                        return False
            return True
        
        def bfs_check_same_level(source):
            # nonlocal visited
            # nonlocal level

            visited[source] = 1
            distance[source] = 0
            q = collections.deque([source])
            while len(q) > 0:
                node = q.popleft()
                for neighbor in graph[node]:
                    if visited[neighbor] == -1:
                        visited[neighbor] = 1
                        parent[neighbor] = node
                        distance[neighbor] = distance[node] + 1
                        q.append(neighbor)
                    else:
                        if parent[node] != neighbor: # check if there's a loop
                            if distance[neighbor] == distance[node]: # same level loop -> odd number of edges/nodes in the loop
                                return True

            return False

        components = 0
        for i in range(n):
            components += 1
            if visited[i] == -1:
                if bfs_check_same_level(i):
                    return False

                # check bi-partite using dfs
                color[i] = 0  # set the color of source to be 0 and other adjoining will be set to opposite colors
                if not dfs_check_bipartite(i):
                    return False
        return True
