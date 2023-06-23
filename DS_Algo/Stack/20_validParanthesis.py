"""
Leetcode 20: Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        lifo_stack = []
        for ch in s:
            # append when opening bracker
            if ch == '(' or ch == '{' or ch == '[':
                lifo_stack.append(ch)

            else:
                # pop when matching closing bracket found
                if not lifo_stack:
                    return False
                if ch == ')' and lifo_stack[-1] == '(':
                    lifo_stack.pop()
                elif ch == '}' and lifo_stack[-1] == '{':
                    lifo_stack.pop()
                elif ch == ']' and lifo_stack[-1] == '[':
                    lifo_stack.pop()

                # return False when last bracket does not match well
                else:
                    return False
        return len(lifo_stack) == 0
