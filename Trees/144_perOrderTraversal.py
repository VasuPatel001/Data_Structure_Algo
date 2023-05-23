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


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self, node: TreeNode, result: list[int]):
        # pre-order work
        result.append(node.val)

        # leaf node worker
        if node.left == None and node.right == None:
            return

        # internal node worker
        if node.left != None: self.helper(node.left, result)
        if node.right != None: self.helper(node.right, result)

    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if root == None: return []
        result = []
        self.helper(root, result)
        return result