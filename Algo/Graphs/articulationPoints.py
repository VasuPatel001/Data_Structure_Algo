"""
TARJAN'S ALGORITHM:
Pseudo code for Articulation points problem on Undirected DFS graph:

https://uplevel.interviewkickstart.com/resource/rc-video-484801-918329-246-1547-4872479

Articulation point problem: Identify important nodes which if taken out disconnects the graph.
Articulation point problem is solved using "DFS undirected graph Arrival time of back edges".
"""


def articulationPoints(n: int, connections: list[int]):
    # Step 1: form a graph using adjacency_list
    adjList = [[] for _ in range(n)]  # where n is total number of nodes
    for (src, dst) in connections:
        adjList[src].append(dst)
        adjList[dst].append(src)

    # standard template of visited[], parent[]
    visited = [-1] * n
    parent = [-1] * n

    # dfs undirected graph arrival, departure time template
    timestamp = [0]
    arrival = [-1] * n
    departure = [-1] * n

    # minArrival is used to keep track of back edges going to the highest level
    minArrival = [-1] * n
    articulationPointFlag = [False for _ in range(n)]

    # result array stores all the bridges
    articulationPointsList = []

    # Step 2: dfs function
    def dfs(node: int):
        visited[node] = 1

        # update arrival time
        arrival[node] = timestamp[0]
        timestamp[0] += 1

        # initialize the minArrival of the node to be its own arrival time
        minArrival[node] = arrival[node]

        for neighbor in adjList[node]:
            if visited[neighbor] == -1:
                ngb_arrival = dfs(neighbor)
                # use ngb_arrival to check if a given node is an articulation point
                # if any of the neighbor's arrival time >= arrival[node], it means that current node is an articulation point
                if ngb_arrival >= arrival[node]:
                    articulationPointFlag[node] = True

                # standard bridges code template
                minArrival[node] = min(ngb_arrival, minArrival[node])

            else:  # neighbor is already visited and CAN be a back edge
                if parent[node] != neighbor:  # it is a back edge
                    minArrival[node] = min(arrival[neighbor], minArrival[node])

        # TARJAN'S ALGO
        # when articulationPointFlag[node] == True, we can say that the node is an articulation point
        # in the below if condition, 2nd condition is used to check for all nodes except the root (0)th node, we check for the root node after outer loop is completed
        if articulationPointFlag[node] == True and node != 0:  # last condition is used to check if the node is NOT root (0 node)
            articulationPointsList.append(node)  # identified articulation point, append it to result

        # update departure time
        departure[node] = timestamp[0]
        timestamp[0] += 1

        return minArrival[node]

    # Step 3: outer loop
    dfs(0)

    # IMP: check for the root node 0 if it has atleast two childred
    cnt = 0
    for parent_node in parent:
        if parent_node == 0:
            cnt += 1
    if cnt >= 2:  # if 0 is a parent of more than two nodes, in that case taking out 0th node will disconnect graph
        articulationPointsList.append(0)

    return articulationPointsList
