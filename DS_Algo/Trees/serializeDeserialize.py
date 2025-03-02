"""
Write serialization & deserialization functions for a binary tree


"""

"""
3 ways to solve the problem:
    1. Pre/Post-Order AND IN-Order. No need to remember null children. You can't have duplicates
    2. Level order traversal + remember null children 
    3. Pre/Post-order traversal + remember null children - this method works with duplicate node values.
"""


class TreeNode:
    def __init__(self, val, right=None, left=None):
        self.val = val
        self.left = left
        self.right = right


# Method 3 Solution: MOST ROBUS and should be implemented in FAANG interview question
class Solution:
    def serialize(self, root):
        if not root:
            return ["#"]
        res = [str(root.val)]
        res.extend(self.serialize(root.left))
        res.extend(self.serialize(root.right))
        return res

    def deserializeHelper(self, data, i):
        if (i >= len(data)) or (data[i] == "#"):
            return None, i+1
        node = TreeNode(int(data[i]))
        node.left, i = self.deserializeHelper(data, i+1)
        node.right, i = self.deserializeHelper(data, i)
        return node, i

    def deserialize(self, data):
        root, v = self.deserializeHelper(data, 0)
        return root

# Method 1 Solution: BASIC method Pre/Post-Order AND IN-Order. No need to remember null children. You can't have duplicates


def serialize(root: TreeNode):
    """
    Time, Space: O(N)
    """
    preorder_lst = []
    inorder_lst = []

    def preorder(node: TreeNode):
        if not node:
            return
        preorder_lst.append(node.val)
        preorder(node.left)
        preorder(node.right)

    def inorder(node: TreeNode):
        if not node:
            return
        inorder(node.left)
        inorder_lst.append(node.val)
        inorder(node.right)

    preorder(root)
    inorder(root)

    return preorder_lst, inorder_lst


def deserialize(preorder_lst, inorder_lst):
    inorder_dict = {}
    for idx, num in enumerate(inorder_lst):
        inorder_dict[num] = idx

    def unpack(preorder_lst, pos, poe,
               inorder_lst, ios, ioe):
        if pos >= poe:
            return

        root_val = preorder_lst[pos] 
        root = TreeNode(root_val)
        inorder_idx = inorder_dict[root_val]

        length = inorder_idx - ios
        root.left = unpack(preorder_lst, pos+1, pos+length,
                           inorder_lst, ios, inorder_idx-1)
        root.right = unpack(preorder_lst, pos+length+1, poe,
                            inorder_lst, inorder_idx+1, ioe)
        return root

    return unpack(preorder_lst, 0, len(preorder_lst)-1,
                  inorder_lst, 0, len(inorder_lst)-1)
