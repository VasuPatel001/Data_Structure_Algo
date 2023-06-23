"""
Leetcode 111: Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5

Constraints:
The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000
"""


# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        BFS-Iterative
        """
        if root is None:
            return 0

        level = 0
        q = deque([root])
        while q:
            level += 1
            numNodes = len(q)
            for _ in range(numNodes):
                node = q.popleft()
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                if node.left is None and node.right is None:
                    return level

        """
        ALTERNATIVE
        DFS-Recursive approach
        """
        if root is None: return 0

        def helper(node):
            # preorder initialization
            leftdepth = float('inf')
            rightdepth = float('inf')

            # leaf node worker
            if node.left is None and node.right is None:
                return 1

            if node.left is not None:
                leftdepth = helper(node.left) + 1

            if node.right is not None:
                rightdepth = helper(node.right) + 1

            # post-order work
            return min(leftdepth, rightdepth)

        return helper(root)
