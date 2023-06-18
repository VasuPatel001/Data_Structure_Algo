"""
TARJAN'S ALGORITHM:
Pseudo code for Bridges problem on Undirected DFS graph:

https://uplevel.interviewkickstart.com/resource/editorial/rc-codingproblem-484800-917569-54-337

Bridges problem: Identify important connection which if taken out disconnects the graph.
Bridges problem is solved using "DFS undirected graph Arrival time of back edges". 

"""


def bridges(n: int, connections: list[int]):
    # form a graph using adjacency_list
    adjList = [[] for _ in range(n)]  # where n is total number of nodes
    for (src, dst) in connections:
        adjList[src].append(dst)
        adjList[dst].append(src)
    
    visited = [-1] * n
    parent = [-1] * n

    # dfs undirected graph arrival, departure time
    timestamp = [0]
    arrival = [-1] * n
    departure = [-1] * n

    # minArrival is used to keep track of back edges going to the highest level
    minArrival = [-1] * n

    # result array stores all the bridges
    result = []

    def dfs(node: int):
        visited[node] = 1

        # update arrival time
        arrival[node] = timestamp[0]
        timestamp[0] += 1

        # initialize the minArrival of the node to be its own arrival time
        minArrival[node] = arrival[node]

        for neighbor in adjList[node]:
            if visited[neighbor] == -1:
                minArrival[node] = min(dfs(neighbor), minArrival[node])
            else:  # neighbor is already visited and CAN be a back edge
                if parent[node] != neighbor:  # it is a back edge
                    minArrival[node] = min(arrival[neighbor], minArrival[node])

        # TARJAN'S ALGO 
        # when minArrival[node] == its own arrival time, we can say that the node -> parent connection is a bridge
        if arrival[node] == minArrival[node] and node != 0:  # last condition is used to check if the node is NOT root (0 node)
            result.append([node, parent[node]])  # identified bridge connection, append it to result

        # update departure time
        departure[node] = timestamp[0]
        timestamp[0] += 1

        return minArrival[node]
