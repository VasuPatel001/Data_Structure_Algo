"""
Leetcode 261: Graph Valid Tree 
https://uplevel.interviewkickstart.com/resource/rc-codingproblem-484799-917568-250-1587

Given an undirected graph, find out whether it is a tree.
The undirected edges are given by two arrays edge_start and edge_end of equal size. Edges of the given graph connect nodes edge_start[i] and edge_end[i] for all valid i.

Example One
Graph 1
{
"node_count": 4,
"edge_start": [0, 0, 0],
"edge_end": [1, 2, 3]
}
Output:
1
This graph is a tree because all the nodes are connected, and it does not have cycles.

Example Two
Graph 2
{
"node_count": 4,
"edge_start": [0, 0],
"edge_end": [1, 2]
}
Output:
0
This graph is not a tree because node 3 is not connected to the other nodes.

Example Three
Graph 3
{
"node_count": 4,
"edge_start": [0, 0, 1, 2],
"edge_end": [3, 1, 2, 0]
}
Output:
0
This graph is not a tree: nodes 0, 1 and 2 form a cycle.

Example Four
Graph 4
{
"node_count": 4,
"edge_start": [0, 0, 0, 1],
"edge_end": [1, 2, 3, 0]
}
Output:
0
This graph is not a tree because the two edges that connect nodes 0 and 1 form a cycle.

Notes
A tree is an undirected connected acyclic graph.
"""

"""
Condition for being a valide tree:
1. No loop
2. Only 1 Connected Components
"""

"""
Time complexity: O(V + E): for either bfs/dfs traverse each node (V) exactly once and check for each  neigbors (edges/E)
Space complexity: O(V + E): because we create adjacency list which list [[]] of length V and each list will be E long for each nodes
"""

import collections
def is_it_a_tree(node_count, edge_start, edge_end):
    """
    Args:
        node_count(int32)
        edge_start(list_int32)
        edge_end(list_int32)
    Returns:
        bool
    """
    # Write your code here.

    # Step 1: form a graph using adjacency_list representation
    adjacency_list = [[] for _ in range(node_count)]
    for i, j in zip(edge_start, edge_end):
        adjacency_list[i].append(j)
        adjacency_list[j].append(i)

    visited = [-1] * node_count
    parent = [None] * node_count

    # Depth first search method
    def dfs_check_loop(source: int):
        nonlocal visited
        nonlocal parent

        visited[source] = 1
        for neighbor in adjacency_list[source]:
            if visited[neighbor] == -1:
                parent[neighbor] = source
                if dfs_check_loop(neighbor):  # check if there's cycle when neighbor is passed
                    return True
            else:  # neighbor is already visited -> check for loops
                if parent[source] != neighbor:  # if the parent of the source is NOT neighbor => there's a loop
                    return True
        return False

    # Breadth first search method
    def bfs_check_loop(source: int):
        nonlocal visited
        nonlocal parent

        visited[source] = 1
        q = collections.deque([source])
        while len(q) > 0:
            node = q.popleft()
            for neighbor in adjacency_list[node]:
                if visited[neighbor] == -1:
                    visited[neighbor] = 1
                    parent[neighbor] = node
                    q.append(neighbor)
                else: # potentially there could be a loop
                    if parent[node] != neighbor:
                        return True
        return False

    # Step 2: run through visited[] and see if there are more than 1 components
    components = 0
    for i in range(node_count):
        if visited[i] == -1:
            components += 1
            if components > 1:  # condition #2 for being a valid tree
                return False

            #  for below dfs, we can alternatively use bfs_check_loop function as well
            if dfs_check_loop(i):  # condition #1 for being a valid tree
                return False
    return True
