"""
Minimum Spanning Tree
Kruskal'a Algo:
    It is greedy approach of selecting edges with minimum weights and then keep building MST and 
    only nelgecting a min weight edge when it form a cycle/loop

Implementation:
    Kruskal's Algo uses Quick Find, Union and Path Compression technique, so the template for Kruskal's algo 
    has minor modifications to Quick Find, Union template to calculate total weight/cost and MST edges
"""

"""
Time complexity:
    Time complexity for MST Kruskal's algo: 
        1. O(E x logE) for sorting edges based on weight
        2. O(V) for quick find, union implementation

    Hence, depending on dense (E ~ V^2) or sparse (E ~ V) graph, time complexity are:
        O(E x logV) for dense graph
        O(V x logV) for sparse graph
"""


def find(x: int, parent: list[int]):
    # Best Approach: Path compression technique
    # amortized complexity of path compression is O(1) because first time when find(x) is called, it will take O(logN)
    # following all subsequent calls will take O(1)
    # Base case
    if x == parent[x]:
        return x

    # recursive case
    root_x = find(parent[x])
    parent[x] = root_x
    return root_x


def KruskalsAlgo(connections: list[list[int]], n: int):
    # initialize parent and size array
    parent = [i for i in range(n)]
    size = [1 for _ in range(n)]
    components = n
    totalCost = 0
    MSTedges = []

    # connections = [[u, v, w], ...]
    # connections is list of list having (u, v, weight/cost)
    connections.sort(key=lambda x: x[-1])  # using key = lambda x: x[-1] allows to sort based on weight/cost

    for (u, v, weight) in connections:
        rootu = find(u, parent)
        rootv = find(v, parent)

        if rootu != rootv:
            if size[rootu] < size[rootv]:
                parent[rootu] = rootv
                size[rootv] += size[rootu]
            else:
                parent[rootv] = rootu
                size[rootu] += size[rootv]

            # when union operation is performed, component is reduced by 1
            # Note: this is inside if condition
            components -= 1
            totalCost += weight
            MSTedges.append((u, v))

    if components == 1:
        return totalCost, MSTedges  # return both/either of these values depending on output required

    # we know that # of components > 1
    return -1  # return default value of cost as expected in problem statement
