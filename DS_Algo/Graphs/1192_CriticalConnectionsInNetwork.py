"""
1192. Critical Connections in a Network
Hard

There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.
A critical connection is a connection that, if removed, will make some servers unable to reach some other server.
Return all critical connections in the network in any order.

Example 1:
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.

Example 2:
Input: n = 2, connections = [[0,1]]
Output: [[0,1]]

Constraints:
2 <= n <= 105
n - 1 <= connections.length <= 105
0 <= ai, bi <= n - 1
ai != bi
There are no repeated connections.
"""


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adjList = [[] for _ in range(n)]
        for src, dst in connections:
            adjList[src].append(dst)
            adjList[dst].append(src)

        visited = [-1] * n
        parent = [-1] * n

        # dfs undirected graph arrival, departure time
        timestep = [0]
        arrival = [-1] * n
        departure = [-1] * n

        # minArrival is used to keep track of back edges going to the highest level
        minArrival = [-1] * n

        bridges = []

        def dfs(src: int):
            visited[src] = 1

            # set the arrival for src node
            arrival[src] = timestep[0]
            timestep[0] += 1

            # initialize the minArrival of the node to be its own arrival time
            minArrival[src] = arrival[src]

            for ngb in adjList[src]:
                if visited[ngb] == -1:  # ngb is NOT visited so far
                    parent[ngb] = src
                    minArrival[src] = min(dfs(ngb), minArrival[src])
                else:  # ngb is already visited
                    if parent[src] != ngb:  # back edge
                        minArrival[src] = min(arrival[ngb], minArrival[ngb])

            # TARGAN's algo
            if minArrival[src] == arrival[src] and src != 0:
                bridges.append([src, parent[src]])

            # set the departure time
            departure[src] = timestep[0]
            timestep[0] += 1

            return minArrival[src]

        dfs(0)
        return bridges
