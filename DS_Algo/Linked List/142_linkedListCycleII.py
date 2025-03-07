"""
Leetcode 142: Linked List Cycle II

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

Constraints:
The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""
from typing import Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Concept: when tortoise and hare meet, 
            Tortoise travels (start + i) distance
            Hare travesl 2(start + i) distance
            at the point of intersection: difference in the distance travelled is equal
            to multiple of cycle length (lambda).

            When they meet, we start a third_pointer from the head and tortoise at
            same speed (1x), point where they both meet first is the 
            first point in the cycle.

        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        if head is None:
            return None
        hare = head
        tortoise = head
        while hare.next and hare.next.next:
            hare = hare.next.next
            tortoise = tortoise.next
            if hare == tortoise:  # cycle detected
                third_pointer = head
                count = 0
                while third_pointer != tortoise:
                    third_pointer = third_pointer.next
                    tortoise = tortoise.next
                    count += 1
                return tortoise
