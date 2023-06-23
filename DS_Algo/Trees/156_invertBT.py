"""
Leetcode 156: Invert Binary Tree Upside Down
Implemented in upLevel: https://uplevel.interviewkickstart.com/resource/submissions/rc-codingproblem-484794-910229-51-322

Upside Down
Given a binary tree where every node has either 0 or 2 children and every right node is a leaf node, flip it upside down turning it into a binary tree where all left nodes are leafs.

Notes
Return the root of the output tree.

Constraints:
0 <= number of nodes <= 100000
1 <= node value <= 100000
"""


"""
Time Complexity
O(N) as we are traversing every node once.

Auxiliary Space Used
O(N) because of the stack memory used by recursion.

Space Complexity
O(N) because of the input and output size.
"""

# For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def flip_upside_down(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     BinaryTreeNode_int32
    """
    # Write your code here.
    if root is None: return None
    result = [None]
    
    def dfs(node: BinaryTreeNode, parent: BinaryTreeNode, rightSibling: BinaryTreeNode):
        # pre-order work
        oldleft = node.left
        oldright = node.right
        # updating pointers
        node.right = parent
        node.left = rightSibling
        
        # leaf node left worker
        if oldleft == None and oldright == None:
            result[0] = node
        
        # internal node worker "ONLY PASS LEFT"
        if oldleft is not None:
            dfs(oldleft, node, oldright)
        
    
    dfs(root, None, None)
    return result[0]
