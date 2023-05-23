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

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self, node: TreeNode, result: list[int]):
        # leaf node worker
        if node.left == None and node.right == None:
            # inorder work for leaf node worker
            result.append(node.val)
            return

        # internal node worker
        if node.left != None: self.helper(node.left, result)

        # in-order work
        result.append(node.val)

        # internal node worker
        if node.right != None: self.helper(node.right, result)

    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if root == None: return []
        result = []
        self.helper(root, result)
        return result