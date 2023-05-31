"""
Leetcode 95. Unique Binary Search Trees II

Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

Example 1:
Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

Example 2:
Input: n = 1
Output: [[1]]

Constraints:
1 <= n <= 8
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> list[Optional[TreeNode]]:
        # using memoization to keep track of which start, end pairs have already been computed
        self.memo = {}

        def helper(start: int, end: int) -> List[TreeNode]:
            if start > end: return [None]

            # memoization
            if (start, end) in self.memo:
                return self.memo[(start, end)]

            result = []

            # choose root index
            for i in range(start, end + 1):
                leftSubtrees = helper(start, i-1)
                rightSubtrees = helper(i+1, end)

                for left in leftSubtrees:
                    for right in rightSubtrees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        result.append(root)
            self.memo[(start, end)] = result

            return result

        return helper(1, n)
