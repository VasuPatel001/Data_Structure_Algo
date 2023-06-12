"""
https://uplevel.interviewkickstart.com/resource/rc-codingproblem-578599-921813-56-344

Create A Transpose Of A Directed Graph
Given a strongly connected directed graph, return its transpose. The graph will be given as a reference to one of its nodes; the rest of the graph can be discovered by walking its edges.

Example
Input: a node of a graph like this:
Input
Output: a node of a graph like this:

Output
Notes

Constraints:
1 <= number of nodes <= 315
Node values are unique integers, and 1 <= node value <= number of nodes
No multiple edges (connecting any pair of nodes in one direction) or self loops (edges connecting a node with itself) in the input graph
Description of the text format of the test cases

You might need this for debugging your solution on IK UpLevel platform.

Input and output file each contain a list or directed edges representing a directed graph.

The input example
Example is represented by

{
"edges": [
[1, 2],
[2, 3],
[3, 1]
]
}

Output is represented by

[
[2, 1],
[3, 2],
[1, 3]
]
"""

"""
Time compexity: dfs is O(V+E) 
Space complexity: 
"""


# For your reference:


class GraphNode:
    def __init__(self, value):
        self.value = value
        self.neighbors = []


def create_transpose(node):
    """
    Args:
     node(GraphNode_int32)
    Returns:
     GraphNode_int32
    """
    # Write your code here.
    
    visited = {}  # {int: int}
    
    def dfs(node):
        visited[node.value] = 1
        
        # IMP: create a SET from list, because when ngb values are removed and appended, 
        # elements change their index value and skip the neighbors when running loop.
        ngbs = {s for s in node.neighbors}
        
        for ngb in ngbs:
            node.neighbors.remove(ngb)
            if ngb.value not in visited:
                dfs(ngb)
            ngb.neighbors.append(node)
    
    dfs(node)
    return node