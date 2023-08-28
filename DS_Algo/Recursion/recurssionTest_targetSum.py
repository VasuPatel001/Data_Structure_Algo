"""
Possible To Achieve Target Sum
Given a set of integers and a target value k, find whether there is a non-empty subset that sums up to k.

Example One
{
"arr": [2, 4, 8],
"k": 6
}
Output:
1
Because 2 + 4 = 6.

Example Two
{
"arr": [2, 4, 6],
"k": 5
}
Output:
0
Because no subset of numbers from the input sums up to 5.

Notes
Constraints:

1 <= size of the input array <= 18
-1012 <= elements of the array, k <= 1012
"""


def helper(arr: list[int], target: int, cur_idx: int, so_far: int, slate: list[int]):
    """
    Method used: exclusion/inclusion
    Uniqueness: use return include or exclude to return True as soon as one True condition is found

    Time Complexity: O(2^n * n), because 2^n # of leaf nodes in worst case and 'n' because internal node make slate
    Space Complexity: O(n), because auxillary slate is O(n) and call stack is also max O(n).
    """
    if so_far == target and len(slate) > 0:  # IMP: len(slate) > 0 is MUST because question asks for "NON-EMPTY" subsets
        return True
    
    if cur_idx == len(arr):
        if so_far != target:  # IMP: this condition is written in separate line from preceding because line 22 is independent of line 21.
            return False  
        return False  # this return is also required, if not written then it will go internal node worker and would return index out of bounds error
    
    # internal node worker
    # NOTE: here we use return helper(include) OR helper(exclude)
    # because we want to return True ASAP and not necessarily traverse entire tree
    return helper(arr, target, cur_idx + 1, so_far + arr[cur_idx], slate + [arr[cur_idx]]) or helper(arr, target, cur_idx + 1, so_far, slate)


def check_if_sum_possible(arr, k):
    """
    Args:
     arr(list_int64)
     k(int64)
    Returns:
     bool
    """
    # Write your code here.
    return helper(arr, k, 0, 0, [])
