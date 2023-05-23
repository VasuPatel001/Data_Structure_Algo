"""
Leetcode 103: Binary Tree Zigzag Level Order Traversal
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
"""

"""
Pseudocode

List<List<Integer>> function getzigZagLevelOrder(TreeNode root) {

    List<List<Integer>> result = new List()
    boolean leftToRight = true

    if(root is null) return result

    Queue<TreeNode> nodeQueue = new Queue()

    nodeQueue.add(root)

   while(nodeQueue is not empty){

        // count number of items in the queue
        int count = nodeQueue.size()
        int[] temp = new int[count]

        for(int i=0; i<count; i++){

           TreeNode node = nodeQueue.remove()

           int idx = i
        if(not leftToRight) idx = count-1 - i
           // add to the output
            temp[idx]= node.val

           // add children to queue
           if(node.left is not null) nodeQueue.add(node.left)
           if(node.right is not null) nodeQueue.add(node.right)
        }
       // if(not leftToRight) temp.reverse() // O(n)?

        result.add(temp)
        leftToRight = not leftToRight
   }
    return result
    
}
"""

"""
Time Complexity: O(N) because we make a one time pass over each nodes of the binary tree to create a list of size N (i.e. input binary tree size) 
Space Complexity: O(N) because we use output array 'result' 
"""

# Definition for a binary tree node.
import queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        result = []
        if root == None: return result
        q = queue.Queue(maxsize=0)
        q.put(root)
        level = 0
        while not q.empty():  # IMP: Use q.empty() mehtod only and NOT use while q: because it is giving TLE error
            count = q.qsize()
            temp = [0] * count
            for i in range(count):
                node = q.get()
                idx = i
                if level % 2: # odd
                    idx = count - i - 1  # this method of reversing the alternating list is approprirate as opposed to list.reverse() method
                temp[idx] = node.val

                # check for left, right node
                if node.left is not None: q.put(node.left)
                if node.right is not None: q.put(node.right)
                
            result.append(temp)
            level += 1
        return result