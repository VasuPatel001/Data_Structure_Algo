"""
Leetcode 250: Count Univalue Subtrees

Given a binary tree, find the number of unival subtrees. An unival (single value) tree is a tree that has the same value in every node.

Example one

Output: 6
The input tree has a total of 6 nodes. Each node is a root of a subtree. All those 6 subtrees are unival trees.

Example two
Output:
5
The input tree has a total of 7 nodes, so there are 7 subtrees. Of those 7, all but two subtrees are unival. The two non-unival subtrees are:
The one rooted in the root node and
The one rooted in the root's right child.

Constraints:
0 <= number of nodes in the tree <= 105
-109 <= node value <= 109
"""

"""
int function getUnivalSubtrees(TreeNode root) {
    
    if(root is null) return 0

    int uvCount = 0

     boolean function isUnival(TreeNode node) {
        
        if(node.left is null and node.right is null){
            uvCount++
            return true
        }

        boolean leftIsUnival = true
        boolean rightIsUnival = true

        if(node.left is not null){
            leftIsUnival = isUnival(node.left)
                           and (node.val == node.left.val) 
        }

        if(node.right is not null){
            rightIsUnival = isUnival(node.right)
                            and (node.val == node.right.val)
        }

        if(leftIsUnival and rightIsUnival) uvCount++
        
        return (leftIsUnival and rightIsUnival)
      
     }
     isUnival(root)
     return uvCount

}
"""
# For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_single_value_trees(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     int32
    """
    # Write your code here.
    if root == None: return 0
    count = [0]
    
    def dfs(node):
        # pre-order intialization
        isLeftUnival = True
        isRightUnival = True
        
        # leaf node worker
        if node.left == None and node.right == None:
            count[0] += 1
            return True
        
        # internal node worker
        if node.left != None:
            isLeftUnival = dfs(node.left) and node.value == node.left.value
        
        if node.right != None:
            isRightUnival = dfs(node.right) and node.value == node.right.value
        
        if isLeftUnival and isRightUnival: count[0] += 1
        return isLeftUnival and isRightUnival
    
    dfs(root)
    return count[0]