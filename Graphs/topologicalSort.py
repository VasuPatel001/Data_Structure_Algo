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
                # back edge
                if departure time of neighbor is NOT set

                # forward edge
                elif arrival[source] < arrival[neighbor] and departure time of neighbor is set

                # cross edge
                else: arrival[source] > arrival[neighbor] and departure time of neighbor is set
        
        departure[source] = time + 1
        topologicalSort.append(source)

