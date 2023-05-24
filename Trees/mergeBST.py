"""
IK UpLevel: Merge Two BSTs
Solved: https://uplevel.interviewkickstart.com/resource/submissions/rc-codingproblem-484794-910229-51-321

Given two Binary Search Trees (BSTs), merge them into a single height-balanced BST.

Notes
A node with value equal to the value of the root node can be inserted either in the left or right subtree.
A binary tree is called height-balanced if for each node the following property is satisfied:
The difference in the heights of its left and right subtrees differ by at most 1.

Constraints:
1 <= number of nodes in the given BSTs <= 104
-109 <= node value <= 109
"""


"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""

"""
Time Complexity:
O(node_count1 + node_count2).
In-order traversal of the first BST: O(node_count1).
In-order traversal of the second BST: O(node_count2).
Merging inorder1 and inorder2: O(node_count1 + node_count2).
Building a height-balanced BST: O(node_count1 + node_count2) (In each recursive call, we will build the node with value equal to inorder[mid] and initiate the processes to build its left and right subtrees. Building a tree node takes constant time, and we build node_count1 + node_count2 nodes in total).

Auxiliary Space Used
O(node_count1 + node_count2).
For storing the in-order traversal of both the BSTs: O(node_count1 + node_count2).
To merge the in-order traversals: O(node_count1 + node_count2).

Space Complexity
O(node_count1 + node_count2).

Space used for input: O(node_count1 + node_count2).
Auxiliary space used: O(node_count1 + node_count2).
Space used for output: O(node_count1 + node_count2).
So, total space complexity: O(node_count1 + node_count2).
"""

def createBST(arr: list[int], start: int, end: int):
    if start > end: return
    
    mid = start + (end-start) // 2
    
    root = BinaryTreeNode(arr[mid])
    
    root.left = createBST(arr, start, mid-1)
    root.right = createBST(arr, mid+1, end)
    
    return root


def mergeSort(arr1, arr2):
    i, j = 0, 0
    result = []
    while (i < len(arr1) and j < len(arr2)):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            result.append(arr2[j])
            j += 1
    
    while i < len(arr1):
        result.append(arr1[i])
        i += 1
    while j < len(arr2):
        result.append(arr2[j])
        j += 1
    return result


def inorder(root, result):
    if root.left is not None:
        inorder(root.left, result)
    
    # inorder
    result.append(root.value)
    
    if root.right is not None:
        inorder(root.right, result)

def merge_two_binary_search_trees(root1, root2):
    """
    Args:
     root1(BinaryTreeNode_int32)
     root2(BinaryTreeNode_int32)
    Returns:
     BinaryTreeNode_int32
    """
    # Write your code here.
    
    # create in-order traversal for root1, root2
    list1 = []
    list2 = []
    inorder(root1, list1)
    inorder(root2, list2)
    
    # merge list1, list2 using merge sort algo
    result = mergeSort(list1, list2)
    
    # create balanced bst using merged sorted array
    return createBST(result, 0, len(result) - 1)