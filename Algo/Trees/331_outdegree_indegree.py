"""
Leetcode 331: Verify Preorder Serialization of a Binary Tree

One way to serialize a binary tree is to use preorder traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as '#'.
For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where '#' represents a null node.
Given a string of comma-separated values preorder, return true if it is a correct preorder traversal serialization of a binary tree.
It is guaranteed that each comma-separated value in the string must be either an integer or a character '#' representing null pointer.
You may assume that the input format is always valid.

For example, it could never contain two consecutive commas, such as "1,,3".
Note: You are not allowed to reconstruct the tree.

Example 1:
Input: preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
Output: true

Example 2:
Input: preorder = "1,#"
Output: false

Example 3:
Input: preorder = "9,#,#,1"
Output: false

Constraints:
1 <= preorder.length <= 104
preorder consist of integers in the range [0, 100] and '#' separated by commas ','.
"""

"""
Approach
an explicit stack, and instead just uses a single variable degree to keep track of the outDegree (children) - inDegree (parent). It also removes the need for the stack and nodes lists used in the previous solution, which results in less memory usage and faster execution time.

The time complexity of this solution is O(n), where n is the number of nodes in the binary tree. The space complexity is O(1), as we are only using a single variable to keep track of the degree.
"""


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # Initialize the outDegree (children) - inDegree (parent) to 1
        degree = 1

        # Iterate through the nodes in the preorder traversal
        for node in preorder.split(','):
            # Decrement the degree by 1 for each node
            degree -= 1

            # If the degree is negative, return False
            if degree < 0: return False

            # If the node is not a leaf node, increase the degree by 2 for each non-leaf node
            if node != '#': degree += 2

        # If the final degree is 0, the tree is valid, else invalid
        return degree == 0
