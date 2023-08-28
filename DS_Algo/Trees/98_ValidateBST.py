"""
Leetcode 98: Validate Binary Search Tree

Is It A BST
Given a binary tree, check if it is a binary search tree (BST). A valid BST does not have to be complete or balanced.

Consider this definition of a BST:
All nodes values of left subtree are "less than or equal" to parent node value.
All nodes values of right subtree are "greater than or equal" to parent node value.
Both left subtree and right subtree must be BSTs.
NULL tree is a BST.
Single node trees (including leaf nodes of any tree) are BSTs.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:
0 <= number of nodes <= 100000
-109 <= values stored in the nodes <= 109
"""

# For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def is_bst(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     bool
    """
    # Write your code here.
    if root == None: return True
    answer = True
    
    def helper(node):
        """
        A node will determine if its a BST by looking at its left and right subtrees.
        The largest value in left subtree should be greater than root value.
        The smalles value in right subtree shouould be less than root value.
        So each node should return (smallest, largest, amibst) values in its substrees back to its parents
        """
        # pre-order work
        amibst = True
        smallest, largest = node.value, node.value

        # individual leaf node worker
        if node.left == None and node.right == None:
            return smallest, largest, amibst

        # internal node worker
        if node.left != None:
            s, l, b = helper(node.left)
            smallest = min(smallest, s)
            largest = max(largest, l)
            if not b or l > node.value:
                amibst = False

        if node.right != None:
            s, l, b = helper(node.right)
            smallest = min(smallest, s)
            largest = max(largest, l)
            if not b or s < node.value:
                amibst = False

        return smallest, largest, amibst

    s, l, answer = helper(root)
    return answer
