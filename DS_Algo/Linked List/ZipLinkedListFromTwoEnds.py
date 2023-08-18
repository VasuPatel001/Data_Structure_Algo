"""
IK Problem:

Zip Linked List From Two Ends
Given a linked list, zip it from its two ends in place, using constant extra space. The nodes in the resulting zipped linked list should go in this order: first, last, second, second last, and so on.

Follow up:
Implement functions to zip two linked lists and to unzip such that unzip(zip(L1, L2)) returns L1 and L2.

Example One
{"head": [1, 2, 3, 4, 5, 6]}
Output:
[1, 6, 2, 5, 3, 4]

Example Two
{"head": [1, 2, 3, 4, 5]}
Output:
[1, 5, 2, 4, 3]

Notes
The function has one parameter: head of the given linked list.
Return the head of zipped linked list.

Constraints:
0 <= number of nodes <= 100000
-2 * 109 <= node value <= 2 * 109
"""


#For your reference:
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def print_list(head):
    curr = head
    while curr:
        print(curr.value)
        curr = curr.next


def reverse_linked_list(head):
    prev = None
    curr = head
    while curr:
        ahead = curr.next
        curr.next = prev
        prev = curr
        curr = ahead
    return prev


def zip_given_linked_list(head):
    """
    Args:
     head(LinkedListNode_int32)
    Returns:
     LinkedListNode_int32
    """
    """
    Time Complexity: O(n)
    Auxiliary Space Used: O(1)
    Space Complexity: O(n)
    """
    # Write your code here.
    if head is None:
        return None

    # using slow, fast pointer, obtain the pointer of middle element
    # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
    # then slow should stop at 3.
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    """
    Separate linked lists from the middle.
    list1: 1 -> 2 -> 3 -> NULL
    list2: 4 -> 5 -> 6 -> NULL
    """
    list1 = head
    list2 = slow.next

    """
    Till now:
    1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL
    With list1 pointing to 1, list2 pointing to 4 and slow pointing to 3.

    Now break main linked list into two parts.
    So do 3->next = NULL.
    """
    slow.next = None

    # reverse the linked list from slow.next
    """
    list2: 4 -> 5 -> 6 -> NULL
    it becomes,
    list2: 6 -> 5 -> 4 -> None
    """
    list2 = reverse_linked_list(list2)

    """
    Merge list1 and list2.
    list1: 1 -> 2 -> 3 -> NULL
    list2: 6 -> 5 -> 4 -> NULL
    merged: 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> NULL
    """
    # print_list(list1)
    # print_list(list2)
    # we declare next1, next2 as two next pointers for
    next1 = None
    next2 = None
    while list2:
        next1 = list1.next
        next2 = list2.next
        list1.next = list2
        list2.next = next1
        list1 = next1
        list2 = next2
    return head
