"""
Leetcode 112: Path Sum

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3:
Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.

Constraints:
The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""

"""
Pseudocode:

-------------------------------------------------------------
Top Down Depth-First

Flow of information travels from ROOT to LEAF

// Handle an empty tree as a special edge case 
   (return empty result array)

// Create a recursive function to execute on every node.

// Function: topDownDFS ( node, information to be passed down)
   // Process information passed down (Pre-Order)

   // Base Case: If Leaf Node, then do something if necessary.

   // Recursive Case: (Not a leaf node)
   // If the node has a LEFT child:  topDownDFS(node.left, info)
   // If the node has a RIGHT child: topDownDFS(node.right, info) 

   // Likely returns nothing back to the parent

boolean function hasPathSum(TreeNode root, int sum) {

    if(root is null) return false
    
    boolean psFlag = false


    function pathSumHelper(TreeNode node, int sum){


        if(psFlag) return

        sum = sum - node.val

        if(node.left is null and node.right is null){
            if(sum == 0) psFlag = true
            return
        }

        if(node.left is not null) pathSumHelper(node.left, sum )
        if(node.right is not null) pathSumHelper(node.right, sum )
    }

    pathSumHelper(root, sum)
    return psFlag

}
"""

"""
Time Complexity: O(N) because at the worst case we would need to visit all nodes to check if the sum is found
Space Complexity: O(logN) for call stack size which is equal to the height of the tree.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self, node: Optional[TreeNode], remain: int) -> bool:
        if node == None: return 
        # pre-order work
        remain = remain - node.val
        
        # leaf node worker
        if node.left == None and node.right == None:
            if remain == 0:
                return True
            return False

        # internal node worker
        return self.helper(node.left, remain) or \
               self.helper(node.right, remain)  # Note: Importance of using return a or b when return type is bool and we can quit checking once we ecnounter True
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None: return False
        return self.helper(root, targetSum)