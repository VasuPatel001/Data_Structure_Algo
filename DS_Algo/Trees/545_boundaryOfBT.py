"""
Leetcode 545: Boundary of Binary Tree
"""

class TreeNode:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def boundaryBT(root: TreeNode):
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.val]

        # 1. create a left boundary
        # Walk down the leftmost path to collect the nodes in leftBoundary until you hit the leftmost leaf
        # Note: this is not the leftview of the tree
        leftBoundary = [root.val]
        if root.left is not None:
            curr = root.left  # starting point for the walk
            while curr is not None:
                leftBoundary.append(curr.val)
                if curr.left is not None:
                    curr = curr.left
                else:
                    curr.right
        leftBoundary.pop()

        # 2. create a right boundary
        # Walk down the rightmost path to collect the nodes in leftBoundary until you hit the rightmost leaf
        # Note: this is not the rightview of the tree
        rightBoundary = []
        if root.right is not None:
            curr = root.right
            while curr is not None:
                rightBoundary.append(curr.val)
                if curr.right is not None:
                    curr = curr.right
                else:
                    curr = curr.left
        rightBoundary.pop()
        rightBoundary.reverse()

        # 3. create a leaf boundary by collecting leaves
        leaves = []
        def dfs(node: TreeNode):
            # leaf node worker
            if node.left is None and node.right is None:
                leaves.append(node.val)

            # internal node worker
            if node.left is not None:
                dfs(node.left)
            if node.right is not None:
                dfs(node.right)

        dfs(root)

        # merging the result from leftBoundar, leaves and rightBounday
        output = []
        output.extend(leftBoundary)
        output.extend(leaves)
        output.extend(rightBoundary)

        return output
