"""
Find All Well-formed Brackets
Given a positive integer n, return ALL strings of length 2 * n with well-formed round brackets.

Example
{
"n": 3
}
Output:
[
"((()))",
"(()())",
"(())()",
"()(())",
"()()()"
]
Any array containing these five strings in any order is a correct output.

Notes
Order of strings in the returned array is insignificant, e.g. for n = 2 both ["(())", "()()"] and ["()()", "(())"] will be accepted.
Constraints:

1 <= n <= 12
Only use round brackets. '(' and ')'
"""

"""
Method 1: increasing n from 0 to n
"""
def helper(nleft: int, nright: int, n: int, slate: list[str], result: list[str]):
    # back tracking
    if nleft < nright or nleft > n or nright > n:
        return
    
    # leaf node worker
    if nleft == nright == n:
        result.append(''.join(slate))
        return
    
    # internal node worker
    # '('
    slate.append('(')
    helper(nleft+1, nright, n, slate, result)
    slate.pop()
    
    # '('
    slate.append(')')
    helper(nleft, nright+1, n, slate, result)
    slate.pop()
    

def find_all_well_formed_brackets(n):
    """
    Args:
     n(int32)
    Returns:
     list_str
    """
    # Write your code here.
    result = []
    helper(0, 0, n, [], result)
    return result


"""
Method 2: Decreasing nleft, nright from n to 0
"""

def helper(nleft, nright, slate: list[str], result: list[str]):
    # back tracking
    if nleft > nright or nleft < 0 or nright < 0:
        return
    
    # leaf node worker
    if nleft == nright == 0:
        result.append(''.join(slate))
        return
    
    # internal node worker
    # adding '('
    slate.append('(')
    helper(nleft-1, nright, slate, result)
    slate.pop()
    
    # adding ')'
    slate.append(')')
    helper(nleft, nright-1, slate, result)
    slate.pop()
    

def find_all_well_formed_brackets(n):
    """
    Args:
     n(int32)
    Returns:
     list_str
    """
    # Write your code here.
    result = []
    helper(n, n, [], result)
    return result
