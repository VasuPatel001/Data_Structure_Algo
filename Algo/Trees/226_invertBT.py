"""
Leetcode 226: Invert Binary Tree

Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None: return None
        prev = None
        answer = None
        
        def helper(node):
            nonlocal prev
            nonlocal answer
            if prev is None: 
                answer = node
            prev = node

            # preorder
            temp = node.left
            node.left = node.right
            node.right = temp

            # internal node worker
            if node.left is not None: helper(node.left)
            if node.right is not None: helper(node.right)

        helper(root)
        return answer