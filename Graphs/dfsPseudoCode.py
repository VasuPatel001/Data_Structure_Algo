"""
DFS Pseudocode
Time complexity: O(m + n)
Space complexity: O()
"""

class Graph:
    def dfs(source):
        # visited and parent initialized to 0 and null
        visited[source] = 1
        for neighbor in adjacencyList[source]:
            if visited[neighbor] == -1:
                parent[neighbor] = source
                dfs(neighbor)