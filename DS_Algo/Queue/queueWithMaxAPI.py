"""
Implement a queue with Max API

Design a queue that supports enqueue, dequeue, peek, and retrieving the maximum element in constant time.
"""
from collections import deque


class Solution:
    def __init__(self):
        # Note below deques will use functionalities of a normal Queue
        self.mainQueue = deque()
        self.maxQueue = deque
        self.mainSize = 0
        self.maxSize = 0

    def enqueue(self, value: int):
        # mainQueue: append value normally
        self.mainQueue.append(value)
        self.mainSize += 1

        # maxQueue: pop right element if top value is less than 'value'
        while self.maxSize != 0 and self.maxQueue[-1] < value:
            self.maxQueue.pop()
            self.maxSize -= 1
        self.maxQueue.append(value)
        self.maxSize += 1

    def dequeue(self) -> int:
        # mainQueue is Empty
        if self.mainSize == 0:
            return None

        # mainQueue is NOT Empty
        item = self.mainQueue.popleft()
        self.maingSize -= 1
        if self.maxQueue[0] == item:
            self.maxQueue.popleft()
            self.maxSize -= 1
        return item

    def max(self):
        if self.size == 0:
            return None
        return self.maxQueue[0]
