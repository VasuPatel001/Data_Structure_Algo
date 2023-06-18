"""
DFS Pseudocode
Time complexity: O(V + E), because recursion call is made for O(V) time and for loop runs over E times, hence O(V+E)
Space complexity: O(V) because we visited array is O(V) and recursion call stack can also go as deep as # of vertex.
"""


class Graph:
    def dfs(source):
        # visited and parent initialized to 0 and null
        visited[source] = 1
        for neighbor in adjacencyList[source]:
            if visited[neighbor] == -1:
                parent[neighbor] = source
                dfs(neighbor)