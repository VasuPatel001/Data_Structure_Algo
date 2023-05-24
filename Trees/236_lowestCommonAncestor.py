"""
Leetcode 236: Lowest Common Ancestor of a Binary Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
https://uplevel.interviewkickstart.com/resource/submissions/rc-codingproblem-484794-910229-51-320

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [1,2], p = 1, q = 2
Output: 1

Constraints:
The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
"""

"""
Time Complexity
O(N).

Pre-processing par array by walking the entire tree - that is O(N). Then calculate the path vectors - O(N) worst case. Then match the two paths starting from the root until they differ - also O(N) worst case.

Auxiliary Space Used
O(N).

Space Complexity
O(N).

The given tree, par array, the paths - they all are of O(N) size.
"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def lca(root, a, b):
    """
    Args:
     root(BinaryTreeNode_int32)
     a(BinaryTreeNode_int32)
     b(BinaryTreeNode_int32)
    Returns:
     int32
    """
    # Write your code here.
    lca = [None]
    
    def dfs(node):
        # pre-order intialization
        afound = False
        bfound = False
        
        if node == a:
            afound = True
            
        if node == b:            
            bfound = True
        
        # leaf node worker -> no work
        
        # internal node work
        if node.left != None:
            af, bf = dfs(node.left)
            afound = afound or af
            bfound = bfound or bf
        
        if node.right != None:
            af, bf = dfs(node.right)
            afound = afound or af
            bfound = bfound or bf
        
        # post - order decision of lca
        if afound and bfound and lca[0] == None:
            lca[0] = node.value
        
        return afound, bfound
    
    dfs(root)
    return lca[0]