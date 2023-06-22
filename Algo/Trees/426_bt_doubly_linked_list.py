"""
Leetcode 426: Convert BST to Sorted doubly linked list

https://uplevel.interviewkickstart.com/resource/submissions/rc-codingproblem-484794-910229-51-319

  
Convert A Binary Tree Into A Circular Doubly Linked List
Given the root node of a binary tree, convert it into a circular doubly linked list in-place. The left and the right pointers in nodes are to be used as previous and next pointers, respectively, in the structure that you return.

Returned list should follow the in-order traversal order of the given tree.

The "root" node that you return should be the first node in the in-order traversal order. That "root" node should be connected with the last node in the in-order traversal as if "root" node goes after the last node and last node goes before the "root" node.

Example
Example input

Output:

Example output

Notes
Constraints:

1 <= number of nodes <= 105
-109 <= node value <= 109
Description of the text format of the test cases

You might need this for debugging your solution on IK UpLevel platform.

Input file contains the given tree in the usual binary tree format.

Output file lists node values of the returned data structure:

starting from the returned node,
following right pointers until we reach the last node in the list,
then following left pointers until we come back to the root node.
Example output

Example output
is represented by
[1, 2, 3, 4, 5, 4, 3, 2, 1]
If the returned data structure is not circular or otherwise incorrect, the output may contain the correct portion of it, and you will find an error message in the ERROR field.
"""

# For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def binary_tree_to_cdll(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     BinaryTreeNode_int32
    """
    # Write your code here.
    if root == None: return None
    
    # leaf node worker
    if root.left == None and root.right == None:
        root.left = root
        root.right = root
        return root
    
    # internal node worker
    head_left = binary_tree_to_cdll(root.left)
    head_right = binary_tree_to_cdll(root.right)
    
    # If the head_left is NULL, we have to add the current root node at the beginning of
    # the second circular doubly linked list.
    if head_left == None:
        tail2 = head_right.left
        root.right = head_right
        head_right.left = root
        tail2.right = root
        root.left = tail2
        return root
    
    # If the head_right is NULL, we have to add the current root node at the end of
    # the first circular doubly linked list.
    if head_right == None:
        tail1 = head_left.left
        tail1.right = root
        root.left = tail1
        head_left.left = root
        root.right = head_left
        return head_left
    
    # If both head_left and head_right are non-NULL, we have to join the first and the second
    # circular doubly linked list via the current root node.

    tail1 = head_left.left
    tail2 = head_right.left

    tail1.right = root
    root.left = tail1
    root.right = head_right
    head_right.left = root
    head_left.left = tail2
    tail2.right = head_left

    return head_left