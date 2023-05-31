"""
Leetcode 94: Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""

"""
Time Complexity: O(N) because we cover N nodes of the trees
Space Complexity: O(N) because we form result list of length equal to total number of nodes;
call stack for well balanced tree would be O(logN) and worst case call stack space would be O(N).
"""



# For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    # ##########################
    # # In-order Recursive solution
    # if root is None: return []
    
    # result = []
    
    # def helper(node):
    
    #     # leaf node worker
    #     if node.left == None and node.right == None:
    #         return
        
    #     # internal node worker
    #     if node.left != None: helper(node.left)
    
    #     # in-order work
    #     result.append(node.value)
    #     if node.right != None: helper(node.right)

    #     return
    
    # helper(root)
    
    # return result
    
    ##########################
    # In-order Iterative solution
    if root is None: return []
    result = []
    stack = [(root, None)]
    while len(stack) > 0:
        node, zone = stack[-1]
        
        if zone == None:
            stack[-1] = node, "arrival"
            # Pre-order work
            ##########################
            if node.left != None:
                stack.append((node.left, None))
                
        if zone == "arrival":
            stack[-1] = node, "interim"
            # In-order work
            result.append(node.value)
            if node.right != None:
                stack.append((node.right, None))
        
        if zone == "interim":
            stack[-1] = node, "departure"
            # Post-order work
            ##########################
            stack.pop()
    return result