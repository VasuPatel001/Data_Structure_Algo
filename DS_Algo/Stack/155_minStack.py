"""
Leetcode 155: Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function. 

Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
minStack.getMin(); // return -3

Constraints:
-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.
"""

"""
Time Complexity: O(N)
Space Complexity:
    Input: O(1) since we are pushing and poping an indivdiual number
    Auxillary: O(N) we create self.min and self.stack
    Output: O(1)
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.size = 0
        self.min = []

    def push(self, val: int) -> None:
        if self.size == 0:
            self.min.append(val)
        else:  # self.min has atleast one element
            self.min.append(min(val, self.min[-1]))
        self.stack.append(val)
        self.size += 1

    def pop(self) -> None:
        self.min.pop()
        self.stack.pop()
        self.size -= 1

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()