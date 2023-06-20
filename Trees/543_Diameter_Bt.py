"""
Leetcode 543: Diameter of Binary Tree

Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.

Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1

Constraints:
The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
"""

"""
int function getMaxDiameter(TreeNode root) {

    int diameter = 0

    if(root is null) return  diameter

    int function diameterHelper(TreeNode node) {

        if(node.left is null and node.right is null) return 0
        
        int leftMax = 0
        int rightMax = 0

        if(node.left is not null){
            leftMax = diameterHelper(node.left) + 1
        }   

        if(node.right is not null){
            rightMax = diameterHelper(node.right) + 1
        }

        int myDiameter = leftMax + rightMax

        diameter = (myDiameter > diameter) ? myDiameter : diameter

        return (leftMax > rightMax) ? leftMax : rightMax

    }

    diameterHelper(root)
    return diameter
}
"""

"""
Time complexity: O(N) because we are plassing through each node at most once
Space Coplexity: O(N) because 
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self, node: TreeNode) -> int:
        # leaf node worker
        if node.left is None and node.right is None:
            return 0

        # pre-order work
        left_dia = 0
        right_dia = 0

        # internal node worker updates left_dia and right_dia
        if node.left is not None:
            left_dia = self.helper(node.left) + 1
        if node.right is not None:
            right_dia = self.helper(node.right) + 1

        # post order work
        myDia = left_dia + right_dia
        self.maxDiameter = max(self.maxDiameter, myDia)

        # return max of left, right dia to top level managers
        return max(left_dia, right_dia)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None: return 0
        self.maxDiameter = 0
        self.helper(root)
        return self.maxDiameter