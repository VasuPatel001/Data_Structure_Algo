# Quick select in Python
import random


def helper(A: list[int], start: int, end: int, index: int) -> int:
    if start >= end:
        return

    # random pivot_idx selection
    pivot_idx = random.randint(start, end)
    A[start], A[pivot_idx] = A[pivot_idx], A[start]

    # Lomuto's partition routine
    smaller = start
    for bigger in (start+1, end+1):
        if A[bigger] < A[start]:
            smaller += 1
            A[smaller], A[bigger] = A[bigger], A[smaller]
    A[start], A[smaller] = A[smaller], A[start]

    # recurse either on left or right depending on 'index' value
    if index == smaller:
        return A[index]
    elif index < smaller:
        helper(A, start, smaller-1, index)
    else:  # index > smaller:
        helper(A, smaller+1, end, index)


def quickSelect(nums: list[int], k: int) -> int:
    """Quick Select function

    Parameters
    ----------
    nums : list[int]
        array of nums
    k : int
        kth largest element to be extracted from sorted array
        k belongs to [1, len(nums)]

    Returns
    -------
    int
        kth largest element to be extracted from sorted array 
    """
    return helper(nums, 0, len(nums)-1, len(nums)-k)
