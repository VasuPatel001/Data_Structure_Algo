"""
Leetcode 222: Count Complete Tree Nodes

Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

Example 1:
Input: root = [1,2,3,4,5,6]
Output: 6

Example 2:
Input: root = []
Output: 0

Example 3:
Input: root = [1]
Output: 1

Constraints:
The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        ## RC ##
        ## APPROACH : RECURSION ##
        ## TIME COMPLEXICITY : LOG N * LOG N ##
        
        ## LOGIC ##
        # If left sub tree height equals right sub tree height then,
        #       a. left sub tree is perfect binary tree
        #       b. right sub tree is complete binary tree
        # If left sub tree height greater than right sub tree height then,
        #       a. left sub tree is complete binary tree
        #       b. right sub tree is perfect binary tree
        if root is None: return 0

        def leftDepth(leftnode):
            ld = 0
            while leftnode:
                ld += 1
                leftnode = leftnode.left
            return ld
        
        def rightDepth(rightnode):
            rd = 0
            while rightnode:
                rd += 1
                rightnode = rightnode.right
            return rd
        
        ld = leftDepth(root.left)
        rd = rightDepth(root.right)
        
        if ld == rd:
            return pow(2, ld + 1) - 1
        
        else: 
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
        ########################################################################
        # # O(N) solution
        if root is None: return 0
        count = 0

        def helper(node):
            nonlocal count
            count += 1

            # leaf node
            if node.left is None and node.right is None:
                return
            
            # internal node worker
            if node.left is not None: helper(node.left)
            if node.right is not None: helper(node.right)
        
        helper(root)
        return count