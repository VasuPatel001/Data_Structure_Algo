"""
IK problem: https://uplevel.interviewkickstart.com/resource/rc-codingproblem-484810-924784-63-1603-4910715

Remove Nth Node From The End Of A List

Remove n-th node from the end of the given linked list. Return the head of the modified list.

Example One
{"n": 2,
"head": [0, 1, 10, 5, 7]}
Output:
[0, 1, 10, 7]

Example Two
{"n": 1,
"head": [7]}
Output:
[]

Notes
Constraints:
1 <= length of the list <= 105
1 <= n <= length of the list
-109 <= value in a list node <= 109
"""


# For your reference:
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


"""
iterative_two_pointer_solution.cpp
This solution solves the problem in a single pass.

Let left and right be two pointers. Initially, let left point to the head of the list and move the right ahead such that it points to the n-th node from the head.
Keep moving both pointers forward a step at a time, maintaining the distance of n nodes between them.
When right reaches the end of the list, left will point to the n-th node from the end. So we can delete the node to which left points.

Time Complexity: O(length of the list).
Auxiliary Space Used: O(1).
Space Complexity: O(length of the list).
"""


def remove_nth_node_from_end(n, head):
    """
    Args:
     n(int32)
     head(LinkedListNode_int32)
    Returns:
     LinkedListNode_int32
    """
    # Write your code here.
    if not head:
        return None
    prev = None
    curr = head
    right = head
    for _ in range(n - 1):
        if right.next:
            right = right.next

    while right.next:
        prev = curr
        curr = curr.next
        right = right.next

    if prev:
        prev.next = curr.next
    else:
        head = curr.next
    return head
