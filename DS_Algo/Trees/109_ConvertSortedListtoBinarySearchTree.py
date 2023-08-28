"""
Leetcode 109: Convert Sorted List to Binary Search Tree

Given the head of a singly linked list where elements are sorted in ascending order, convert it to a 
height-balanced binary search tree.

Example 1:
Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.

Example 2:
Input: head = []
Output: []

Constraints:
The number of nodes in head is in the range [0, 2 * 104].
-105 <= Node.val <= 105
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head is None: return None
        inorder = []
        curr = head
        while curr is not None:
            inorder.append(curr.val)
            curr = curr.next

        def helper(inorder, start, end):
            if start > end: return

            mid = start + (end - start) // 2
            root = TreeNode(inorder[mid])
            root.left = helper(inorder, start, mid-1)
            root.right = helper(inorder, mid+1, end)

            return root

        return helper(inorder, 0, len(inorder)-1)
