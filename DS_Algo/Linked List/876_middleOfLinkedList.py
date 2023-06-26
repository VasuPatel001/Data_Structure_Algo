"""
Leetcode 876: Middle of the Linked List

Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the SECOND/RIGHT middle node. 

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

Constraints:
The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ################################################################
        # Preferred Method: Useful for broad range of problems including divide and conquer on linked list.
        # IK Method: slow(tortoise) pointer moves @1x speed and ends at left/first
        # middle (for even length of linked list), then move tortoise to right/second
        # middle node manually.

        # Note: IK's method of ending tortoise at left/first middle is helpful
        # for implementing DIVIDE and CONQUER on singly linked list.
        ################################################################
        hare = head
        tortoise = head

        # IMP: Below while loop checks for hare.next BEFORE checking for hare.next.next 
        # because, hare.next.next may return Error if hare.next did not exist and 
        # we directly checked for hare.next.next
        while hare.next is not None and hare.next.next is not None:
            hare = hare.next.next
            tortoise = tortoise.next
        if hare.next is not None:
            tortoise = tortoise.next
        return tortoise

        ################################################################
        # Fast implementation using Slow(1x speed) and Fast(2x speed) pointers
        # Note: This method CANNOT be used for DIVIDE & CONQUER on singly linked list
        ################################################################
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

        ################################################################
        # Naive implemenation of calculating the length of linked list and finding middle node
        ################################################################
        curr = head
        total_nodes = 0
        while (curr is not None):
            total_nodes += 1
            curr = curr.next
        middle_node = (total_nodes // 2) + 1
        result = head
        i = 1
        while (i < middle_node):
            result = result.next
            i += 1
        return result
