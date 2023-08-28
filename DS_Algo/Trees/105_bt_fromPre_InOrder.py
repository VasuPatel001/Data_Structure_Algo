"""
Leetcode 105: Contstruct Binary Tree from Preorder and Inorder Traversal
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]

Constraints:
1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
"""

"""
Pseudocode:

TreeNode function arrayToBT(int[] preorder, int[] inorder) {

    Map<Integer, Integer> ioMap = new Map()

    for(int i = 0; i< inorder.length; i++){
        ioMap.put(inorder[i], i)
    }

    TreeNode function btHelper(int[] preorder,  int pos, int poe,
                                int[] inorder, int ios, int ioe){

        if(pos > poe) return null

        int rootIdx = ioMap.get(preorder[pos]) // O(1)
        int count = rootIdx - ios

        TreeNode root = new TreeNode(preorder[pos])

        // preorder
        
        root.left = btHelper(preorder, pos+1, pos + count,
                             inorder, ios, rootIdx-1)

        // inorder

        root.right = btHelper(preorder, pos+count+1, poe,
                            inorder, rootIdx+1, ioe)

        // post order
        
        return root
    }
    return btHelper(preorder, 0, preorder.length-1,
                    inorder, 0, inorder.length-1)
    
}
"""

"""
Time Complexity: O(N) because we cover N nodes of the trees
Space Complexity: O(N) because we form result list of length equal to total number of nodes;
call stack for well balanced tree would be O(logN) and worst case call stack space would be O(N).
"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def helper(self, preorder, pos, poe,
                     inorder, ios, ioe):
        """
        preorder: List[int]
        pos: int
        poe: int
        inorder: List[int]
        ios: int
        ioe: int
        """
        # back tracking
        if pos > poe: return None

        # internal node worker
        root_idx = self.in_num_idx[preorder[pos]]
        count = root_idx - ios
        root = TreeNode(preorder[pos])

        root.left = self.helper(preorder, pos+1, pos+count,
                                inorder, ios, root_idx-1)
        root.right = self.helper(preorder, pos+count+1, poe,
                                 inorder, root_idx+1, ioe)
        return root

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.in_num_idx = {}
        for idx, num in enumerate(inorder):
            self.in_num_idx[num] = idx
        root = self.helper(preorder, 0, len(preorder)-1,
                           inorder, 0, len(inorder)-1)
        return root
