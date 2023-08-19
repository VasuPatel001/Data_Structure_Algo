"""
IK Problem: https://uplevel.interviewkickstart.com/resource/rc-codingproblem-484810-924784-63-380-4910715

Reverse A Linked List In Groups Of K
Given a linked list, reverse every group of k nodes. If there is a remainder (a group of less than k nodes) in the end, reverse that last group, too.

Example One
{"head": [1, 2, 3, 4, 5, 6],
"k": 3}
Output:
[3, 2, 1, 6, 5, 4]
Input list consists of two whole groups of three. In the output list the first three and last three nodes are reversed.

Example Two
{"head": [1, 2, 3, 4, 5, 6, 7, 8],
"k": 3}
Output:
[3, 2, 1, 6, 5, 4, 8, 7]
There are two whole groups of three and one partial group (a remainder that consists of just two nodes). Each of the three groups is reversed in the output.

Notes
The function has two parameters: head of the given linked list and k.
Return the head of the linked list after reversing the groups of nodes in it.

Constraints:
1 <= number of nodes in the list <= 100000
-2 * 109 <= node value <= 2 * 109
1 <= k <= number of nodes
Cannot use more than constant extra space
"""


# For your reference:
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse_list(head):
    curr = head
    prev = None
    while curr:
        ahead = curr.next
        curr.next = prev
        prev = curr
        curr = ahead


def reverse_linked_list_in_groups_of_k(head, k):
    """
    Args:
     head(LinkedListNode_int32)
     k(int32)
    Returns:
     LinkedListNode_int32
    """
    """
    Input:
    list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> NULL
    k: 3
    Output:
    3 -> 2 -> 1 -> 6 -> 5 -> 4 -> 8 -> 7-> NULL
    Groups to be reversed are (1 -> 2 -> 3), (4 -> 5 -> 6) and (7 -> 8).

    We will call reverse_linked_list function when (start = 1 and stop = 3),
    (start = 4 and stop = 6) and (start = 7 and stop = 8).

    Asymptotic complexity in terms of length of given linked list `n`:
    * Time: O(n)
    * Auxiliary space: O(1)
    * Total space: O(n)
    """
    # Write your code here.
    # edge case
    if head is None:
        return None

    prev_of_start = None
    start = head
    stop = head
    count = 0

    while stop:
        count += 1

        # if we have covered k nodes in between start and stop (inclusive) or we are at the last node
        if count == k or stop.next is None:
            next_of_stop = stop.next

            # We want to reverse start to stop nodes,
            # set stop->next = NULL so we know where to stop.
            stop.next = None

            # reverse the linked list
            reverse_list(start)

            # update prev
            if prev_of_start is None:
                # Head will change when we are reversing the linked list first time.
                head = stop
            else:
                # We have reversed start to stop nodes, hence now stop will be next node of
                # prev_of_start.
                prev_of_start.next = stop

            # We have reversed start to stop nodes, hence next_of_stop will be next node of start.

            start.next = next_of_stop

            """
            In the above example, after we have reversed first k nodes list will be:
            3 -> 2 -> 1 -> 4 -> 5 -> 6 -> 7 -> 8 -> NULL,
            start will point to 1, next_of_stop will point to 4.

            Now we will set start and stop to point at 4.
            And prev_of_start should be previous of 4 that is 1.
            """
            prev_of_start = start
            start = next_of_stop
            stop = next_of_stop
            count = 0
        else:
            stop = stop.next
    return head
