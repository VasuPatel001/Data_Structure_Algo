"""
Leetcode 323: Number of Connected Components in an Undirected Graph
https://uplevel.interviewkickstart.com/resource/rc-codingproblem-484799-917568-250-1586

Count Connected Components In An Undirected Graph
Given an undirected graph, find its total number of connected components.

Example One
{
"n": 5,
"edges": [[0 ,1], [1, 2], [0, 2], [3, 4]]
}
Output:
2

Example Two
{
"n": 4,
"edges": [[0 , 1], [0 , 3], [0 , 2], [2 , 1], [2 , 3]]
}
Output:
1
"""

"""
Time complexity: O(V + E): for either bfs/dfs traverse each node (V) exactly once and check for each  neigbors (edges/E)
Space complexity: O(V + E): because we create adjacency list which list [[]] of length V and each list will be E long for each nodes
"""


import collections
def number_of_connected_components(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     int32
    """
    # Write your code here.

    # Step 1:form a graph representation using adjacency list representation
    adjacency_list = [[] for _ in range(n)]

    for (i, j) in edges:
        # undirected graph, so i <-> j are connected both ways
        adjacency_list[i].append(j)
        adjacency_list[j].append(i)

    # initialize visited[] to -1
    visited = [-1] * n

    # Depth First seach method
    def dfs(source: int):
        nonlocal visited
        visited[source] = 1
        for neighbor in adjacency_list[source]:
            if visited[neighbor] == -1:
                dfs(neighbor)

    # Breadth First seach method
    def bfs(source: int):
        visited[source] = 1
        q = collections.deque([source])
        while len(q) > 0:
            node = q.popleft()
            for neigbor in adjacency_list[node]:
                if visited[neigbor] == -1:
                    visited[neigbor] = 1
                    q.append(neigbor)

    # Step 2: perform bfs/dfs to identify number of connected components
    components = 0
    for i in range(n):
        if visited[i] == -1:
            components += 1
            dfs(i)

            # may replace it with bfs
            # bfs(i)

    return components
