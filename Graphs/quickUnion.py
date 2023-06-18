"""
Earliest moment when everyone becomes a friend

Quick Weighted Union used to find number of connected components in dynamically increasing edges with time.
find() implements path compression technique
"""

"""
Time Complexity: 
    # of Union Ops: n-1 * O(1) because of weighted Quick Union algorithm
    # of Find ops: 2m * O(1) because of Path Compression technique
    Hence total time complexity: n + m
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

    # stratight forward find() which takes O(logN)
    while x != parent[x]:
        x = parent[x]
    return x


def minTimeWhenBecomesFriends(logs: list[list[int]], n: int):
    # initialize parent and size array
    parent = [i for i in range(n)]
    size = [1 for _ in range(n)]
    components = n

    # logs = [[t, u, v], ...] 
    # logs is list of list having (timestamp, u, v) timestamp at which u and v became friends
    logs.sort()

    for (t, u, v) in logs:
        rootu = find(u, parent)
        rootv = find(v, parent)
        
        if rootu != rootv:
            if size[rootu] < size[rootv]:
                parent[rootu] = rootv
                size[rootv] += size[rootu]
            else:
                parent[rootv] = rootu
                size[rootu] += size[rootv]
        components -= 1
        if components == 1:
            return t  # timestamp at which everyone become friends
    
    # we know that # of components > 1
    return -1  # return default value of time as expected in problem statement