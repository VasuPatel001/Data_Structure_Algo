"""
Leetcode 437: Path Sum III
https://leetcode.com/problems/path-sum-iii/description/

Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

Example 1:
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

Example 2:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3

Constraints:
The number of nodes in the tree is in the range [0, 1000].
-109 <= Node.val <= 109
-1000 <= targetSum <= 1000
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None: return 0

        result = [0]

        def helper(node: TreeNode, targetSum: int, slate: list[int]):
            # pre-order work
            slate.append(node.val)
            testSum = 0
            for i in range(len(slate) - 1, -1, -1):
                testSum += slate[i]
                if testSum == targetSum:
                    result[0] += 1

            # leaf node worker: no work needed

            # internal node worker
            if node.left != None: helper(node.left, targetSum, slate)
            if node.right != None: helper(node.right, targetSum, slate)

            # post order work of clearing slate
            slate.pop()

        helper(root, targetSum, [])
        return result[0]
