"""
Leetcode 144: Binary Tree Preorder Traversal
Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]

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
Time Complextiy: O(N) because we cover exactly N input nodes in the trees
Space Complexity: O(N) because result list stores N input nodes
"""

# Definition for a binary tree node.



# For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    # ##########################
    # # Recursive solution
    if root is None: return []

    result = []

    def helper(node):
        # pre-order work
        result.append(node.value)

        # leaf node worker
        if node.left is None and node.right is None:
            return

        # internal node worker
        if node.left is not None: helper(node.left)
        if node.right is not None: helper(node.right)

        return

    helper(root)
    return result

    ##########################
    # Iterative solution
    if root is None: return []
    result = []
    stack = [(root, None)]
    while len(stack) > 0:
        node, zone = stack[-1]

        if zone == None:
            stack[-1] = node, "arrival"
            # Pre-order work
            result.append(node.value)
            # left node traversal
            if node.left != None:
                stack.append((node.left, None))

        if zone == "arrival":
            stack[-1] = node, "interim"
            # In-order work
            ##########################

            # right node traversal
            if node.right != None:
                stack.append((node.right, None))

        if zone == "interim":
            stack[-1] = node, "departure"
            # Post-order work
            ##########################

            # pop the last element in the stack
            stack.pop()
    return result
