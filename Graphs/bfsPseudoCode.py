from collections import deque

"""
BFS Pseudocode
Time complexity: O(V + E), because while loop runs over each vertex and for loop runs over each of the edges.
Space complexity: O(V) because we create a queue
"""


class Graph:
    def bfs(source):
        # visited and parent list initialized to 0 and null respectively
        visited[source] = 1

        # q = queue.Queue(maxsize=0)
        q = deque()
        q.append(source)

        while q:
            node = q.popleft()

            for neighbor in adjacencyList[node]:
                if visited[neighbor] == -1:
                    visited[neighbor] = 1
                    parent[neighbor] = source
                    q.append(neighbor)
        