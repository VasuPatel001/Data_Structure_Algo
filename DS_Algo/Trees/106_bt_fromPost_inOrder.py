"""
Leetcode 106: Construct Binary Tree from Inorder and Postorder Traversal

Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: inorder = [-1], postorder = [-1]
Output: [-1]

Constraints:
1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        # build an hash table for in-order
        io_map = {}
        for i, num in enumerate(inorder):
            io_map[num] = i

        def helper(inorder, ios, ioe, 
                   postorder, pos, poe):
            nonlocal io_map
            if pos > poe: return 

            # root will be posorder's poe
            root_idx = io_map[postorder[poe]]
            root = TreeNode(inorder[root_idx])

            count = root_idx - ios

            root.left = helper(inorder, ios, root_idx-1,
                               postorder, pos, pos + count - 1)
            root.right = helper(inorder, root_idx+1, ioe,
                                postorder, pos + count, poe - 1)

            return root

        return helper(inorder, 0, len(inorder)-1,
                      postorder, 0, len(postorder)-1)
