"""
Leetcode 113: Path Sum II

Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.
A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: []

Example 3:
Input: root = [1,2], targetSum = 0
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""

"""
Pseudocode:

List<List<Integer>> function getSumPaths(TreeNode root, int sum) {

    List<List<Integer>> result = new List()

    if(root is null) return result


    function pathSumHelper(TreeNode node, int sum, Stack<Integer> slate){

        // pre order
        sum = sum - node.val
        slate.push(node.val)
        
        if(node.left is null and node.right is null){
            if(sum == 0) {
                result.add(slate.copy())
            }
            slate.pop()
            return
        }
        
        if(node.left is not null) {
            pathSumHelper(node.left, sum, slate )
        }

        // in order

        if(node.right is not null) {
            pathSumHelper(node.right, sum, slate )            
        }

        // post order
        slate.pop()
    }

    pathSumHelper(root, sum, new Stack())
    return result

}
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self, node: TreeNode, remain: int, slate: list[int], result: list[list[int]]):
        # pre-order work
        remain = remain - node.val
        slate.append(node.val)

        # leaf node worker
        if node.left == None and node.right == None:
            if remain == 0:
                result.append(slate[:])
            # post-order slate cleaning work for leaf node worker
            slate.pop()
            return

        # internal node worker
        if node.left != None: self.helper(node.left, remain, slate, result)
        if node.right != None: self.helper(node.right, remain, slate, result)

        # post-order slate cleaning work
        slate.pop()

    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> list[list[int]]:
        if root == None: return []
        result = []
        self.helper(root, targetSum, [], result)
        return result