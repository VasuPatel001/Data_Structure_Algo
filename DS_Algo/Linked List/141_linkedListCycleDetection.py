"""
Leetcode 141: Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Constraints:
The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        n = total # of nodes in linked list
        lambda = # of nodes in cycle/loop, where lambda <= n

        Time Complexity:
            O(n+lambda) = O(n)
        Space Complexity:
            O(1) since we use only two pointers
        """

        """
        Note: This problem can be solved using the concept of directed graph
        cycle detection using DFS back edge detection (departure[ngb] == -1) approach.
        But that approach used O(N) space to store visited, parent, departure times.

        However, this problem asks us to detect cycle using O(1) space, hence we have to 
        use the approach of hare and tortoise having O(1) space and time slight greater than O(N), but still it would be called O(N).
        """
        if head is None:
            return False
        hare = head
        tortoise = head
        while hare.next and hare.next.next:
            hare = hare.next.next
            tortoise = tortoise.next
            if hare == tortoise:
                return True
        return False

        """
        Method 2: IK's another instructor method
        """
        if head is None:
            return False
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
