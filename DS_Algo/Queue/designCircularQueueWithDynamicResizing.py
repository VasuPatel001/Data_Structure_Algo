class MyCircularQueue:
    def __init__(self, k: int):
        # initialize an array of size k
        self.q = [-1] * k
        self.start = -1
        self.end = -1
        self.size = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        # queue is Empty
        if self.size == 0:
            self.q[0] = value
            self.start = 0
            self.end = 0
            self.size = 1
        # queue is NOT Empty
        else:
            if self.size == self.k:
                self.increaseSize(2 * self.k)
            self.end = (self.end + 1) % self.k
            self.q[self.end] = value
            self.size += 1
        return True

    def increaseSize(self, newCapacity: int):
        new_Q = [-1] * (newCapacity)
        nextIdx = 0
        while self.start != self.end:
            new_Q[nextIdx] = self.q[self.start]
            self.start = (self.start + 1) % self.k
            nextIdx += 1
        new_Q[nextIdx] = self.q[self.end]
        self.start = 0
        self.end = self.k - 1
        self.q = new_Q
        self.k = newCapacity

    def deQueue(self) -> bool:
        # queue is Empty
        if self.size == 0:
            return False
        # queue is NOT Empty
        if self.size == 1:
            self.q[self.start] = -1
            self.start = -1
            self.end = -1
            self.size = 0
        else:
            self.q[self.start] = -1
            self.start = (self.start + 1) % self.k
            self.size -= 1
        if self.size == int(0.25 * self.k):
            self.reduceSize(int(0.5 * self.k))
        return True

    def reduceSize(self, newCapacity: int):
        new_Q = [-1] * (newCapacity)
        nextIdx = 0
        while self.start != self.end:
            new_Q[nextIdx] = self.q[self.start]
            self.start = (self.start + 1) % self.k
            nextIdx += 1
        new_Q[nextIdx] = self.q[self.end]
        self.start = 0
        self.end = nextIdx
        self.q = new_Q
        self.k = 2 * newCapacity

    def Front(self) -> int:
        if self.size == 0:
            return -1
        return self.q[self.start]

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        return self.q[self.end]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
