"""
IK question: https://uplevel.interviewkickstart.com/resource/rc-codingproblem-484810-924784-63-375-4910715

Longest Substring With Balanced Parentheses
Given a string brackets that only contains characters '(' and ')', find the length of the longest substring that has "balanced parentheses".

Example One
{"brackets": "((((())(((()"}
Output:
4
Because "(())" is the longest substring with balanced parentheses.

Example Two
{"balanced": "()()()"}
Output:
6
The entire string "()()()" has parentheses balanced.

Notes
A string is defined as having balanced parentheses if and only if it has an equal number of '(' and ')' and its every prefix has at least as many '('s as ')'s.

Constraints:
1 <= length of brackets <= 105
"""


def find_max_length_of_matching_parentheses(brackets):
    """
    Args:
     brackets(str)
    Returns:
     int32
    """
    # Write your code here.
    open = 0
    close = 0
    longest = 0

    # forward pass
    for i in range(len(brackets)):
        if brackets[i] == '(':
            open += 1
        else: # ')'
            close += 1
            if close > open:
                open = close = 0
            elif open == close:
                longest = max(longest, open * 2)

    # backward pass
    open = 0
    close = 0
    for i in range(len(brackets)-1, -1, -1):
        if brackets[i] == '(':
            open += 1
            if open > close:
                open = close = 0
            elif open == close:
                longest = max(longest, open * 2)
        else:
            close += 1

    return longest
