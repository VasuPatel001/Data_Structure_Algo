"""
Leetcode 232: Implement Queue using Stacks

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:
void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.

Notes:
You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

Example 1:
Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false 

Constraints:
1 <= x <= 9
At most 100 calls will be made to push, pop, peek, and empty.
All the calls to pop and peek are valid.

Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.
"""
from collections import deque


class MyQueue:
    def __init__(self):
        # enqueue and dequeue are both stacks
        self.enqueue = deque()
        self.dequeue = deque()
        self.size = 0

    def push(self, x: int) -> None:
        self.enqueue.append(x)
        self.size += 1

    def pop(self) -> int:
        # queue is Empty
        if self.size == 0:
            return None

        # queue is NOT Empty
        self.size -= 1
        # dequeue is not empty
        if len(self.dequeue) > 0:    
            return self.dequeue.pop()
        # transfer elements from enqueue to dequeue
        while len(self.enqueue) > 0:
            self.dequeue.append(self.enqueue.pop())
        return self.dequeue.pop()

    def peek(self) -> int:
        # queue is Empty
        if self.size == 0:
            return None

        # queue is NOT Empty
        if len(self.dequeue) > 0:
            return self.dequeue[-1]
        while len(self.enqueue) > 0:
            self.dequeue.append(self.enqueue.pop())
        return self.dequeue[-1]

    def empty(self) -> bool:
        return self.size == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()