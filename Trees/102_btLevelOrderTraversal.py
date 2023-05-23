"""
Leetcode 102: Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/description/

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""

"""
Pseudo Code:

List<List<Integer>> function getLevelOrder(TreeNode root) {

    List<List<Integer>> result = new List()

    if(root is null) return result

    Queue<TreeNode> nodeQueue = new Queue()

    nodeQueue.add(root)

   while(nodeQueue is not empty){

        // count number of items in the queue
        int count = nodeQueue.size()
        List temp = new List()

        for(int i=0; i<count; i++){

           TreeNode node = nodeQueue.remove()

           // add to the output
            temp.add(node.val)

           // add children to queue
           if(node.left is not null) nodeQueue.add(node.left)
           if(node.right is not null) nodeQueue.add(node.right)
        }
        result.add(temp)
   }
    return result
    
}
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Time Complexity: O(N) because we make a one time pass over each nodes of the binary tree to create a list of size N (i.e. input binary tree size) 
Space Complexity: O(N) because we use output array 'result' 
"""

import queue  # Python3 queue data structure


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        result = []  # List[List[int]]
        if root == None: return result
        
        # initialize queue (FIFO) with root node in it
        q = queue.Queue(maxsize=0)  # maxsize <= 0 will help us create queue of infinite size
        q.put(root)
        while not q.empty():
            count = q.qsize()
            temp = []
            # looping over the counts helps create List[List] that is required for the output
            for i in range(count):
                node = q.get() # get method extracts and return the first element in queue
                temp.append(node.val)

                # check for left, right nodes; if present add it to queue
                if node.left is not None: q.put(node.left)
                if node.right is not None: q.put(node.right)
            
            # append i_th layer traversal to result list
            result.append(temp)
        return result
