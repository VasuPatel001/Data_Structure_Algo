"""
IK Problem: https://uplevel.interviewkickstart.com/resource/rc-codingproblem-484810-924784-63-379-4910715

Given a linked list and an integer k, swap k-th (1-indexed) node from the beginning, with k-th node from the end.
Note that you have to swap the actual nodes, not just their values.

Example
{"head": [1, 2, 3, 4, 7, 0],
"k": 2}
Output:

[1, 7, 3, 4, 2, 0]

Notes
The function has two parameters: head of the given linked list and k.
Return the head of the linked list after swapping k-th nodes of given linked list.
Constraints:
1 <= number of nodes in the given list <= 100000
-2 * 109 <= node value <= 2 * 109
1 <= k <= number of nodes
Try to access nodes of the given list as little as possible
"""


# For your reference:
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def swap_nodes(head, k):
    """
    Args:
     head(LinkedListNode_int32)
     k(int32)
    Returns:
     LinkedListNode_int32
    """
    # Write your code here.
    if not head:
        return head

    prv1 = None
    ptr1 = head

    while k > 1:
        prv1 = ptr1
        ptr1 = ptr1.next
        k -= 1

    temp = ptr1
    prv2 = None
    ptr2 = head

    while temp and temp.next:
        temp = temp.next
        prv2 = ptr2
        ptr2 = ptr2.next

    if prv1:
        prv1.next = ptr2
    else:
        head = ptr2

    if prv2:
        prv2.next = ptr1
    else:
        head = ptr1

    temp = ptr1.next
    ptr1.next = ptr2.next
    ptr2.next = temp
    return head
