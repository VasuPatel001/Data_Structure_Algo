"""
Leetcode 206: Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # interview-kickstart solution
        if head is None:
            return None
        if head.next is None:
            return head
        middlep = head.next
        behindp = head
        behindp.next = None
        while middlep is not None:
            forwardp = middlep.next
            middlep.next = behindp
            behindp = middlep
            middlep = forwardp
        head = behindp
        return head

        ##########################################
        # Similar method
        ##########################################
        prev = None
        cur = head
        # print(cur.val, cur.next)
        while (cur is not None):
            forward = cur.next
            cur.next = prev
            prev = cur
            cur = forward
        return prev