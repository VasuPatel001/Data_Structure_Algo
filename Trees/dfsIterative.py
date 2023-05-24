    """_summary_
    """



# For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def postorder_traversal(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    if root == None: return []
    
    result = []
    stack = [(root, None)]
    
    while len(stack) != 0:
        (node, zone) = stack[-1]
        
        if zone is None:
            stack[-1] = (node, "arrival")
            # Pre-Order work
            ################
            if node.left is not None:
                stack.append((node.left, None))
        
        elif zone == "arrival":
            stack[-1] = (node, "interim")
            # In-order work
            ################
            if node.right is not None:
                stack.append((node.right, None))
                
        elif zone == "interim":
            stack[-1] = (node, "departure")
            # Post-order work
            result.append(node.value)
            
            stack.pop()
    
    return result
