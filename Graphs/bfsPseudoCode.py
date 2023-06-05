import queue

class Graph:
    def bfs(source):
        # visited and parent list initialized to 0 and null respectively
        visited[source] = 1

        q = queue.Queue(maxsize=0)
        q.put(source)

        while not q.empty():
            node = q.get()

            for neighbor in adjacencyList(node):
                if visited[neighbor] == -1:
                    visited[neighbor] = 1
                    parent[neighbor] = source
                    q.put(neighbor)
        