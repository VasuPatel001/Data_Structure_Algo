"""
199. Binary Tree Right Side View
https://leetcode.com/problems/binary-tree-right-side-view/description/

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""

"""
Pseudocode:

List<Integer> function getRightSideView(TreeNode root) {

    List<Integer> result = new List()

    if(root is null) return result

    Queue<TreeNode> nodeQueue = new Queue()

    nodeQueue.add(root)

   while(nodeQueue is not empty){

        // count number of items in the queue
        int count = nodeQueue.size()
        int temp = 0

        for(int i=0; i<count; i++){

           TreeNode node = nodeQueue.remove()

           // add to the output
           temp = node.val

           // add children to queue
           if(node.left is not null) nodeQueue.add(node.left)
           if(node.right is not null) nodeQueue.add(node.right)
        }
        result.add(temp)
   }
    return result
    
}
"""

"""
Time Complexity: O(N) because we make a one time pass over each nodes of the binary tree to create a list of size N (i.e. input binary tree size) 
Space Complexity: O(N) because we use output array 'result' 
"""
import queue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if root is None: return []

        result = []
        q = deque()
        q.append(root)

        while q:
            count = len(q)
            for i in range(count):
                node = q.popleft()
                last_val = node.val  # we can keep on updating/create new last_val variable

                # check for left, right to append to queue
                if node.left is not None: q.append(node.left)
                if node.right is not None: q.append(node.right)

            result.append(last_val)

        return result
