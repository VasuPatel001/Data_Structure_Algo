# Quick sort in Python
import random


class Solution(object):
    def quickSort(self, nums) -> list[int]:
        """
        Parameters
        ----------
        nums : List[int]
        :rtype: List[int]
        """
        def helper(A, start, end):
            if start >= end:
                return

            # random pivot choice
            pivot_idx = random.randint(start, end)
            A[pivot_idx], A[start] = A[start], A[pivot_idx]

            # partition function
            smaller = start
            for bigger in (start+1, end+1):
                if A[bigger] < A[start]:
                    smaller += 1
                    A[smaller], A[bigger] = A[bigger], A[smaller]
            A[start], A[smaller] = A[smaller], A[start]

            # recurse on left and right partitions
            helper(A, start, smaller - 1)
            helper(A, smaller + 1, end)

        helper(A, 0, len(nums) - 1)
        return nums

A = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(A)

print('Sorted Array in Ascending Order:')
print(A)


def quickSort(A: list[int]) -> list[int]:
    def qSortHelper(A: list[int], start: int, end: int):
        if start >= end:
            return

        # choose a random pivot and swap it with start idx
        pivot_idx = random.randint(start, end)
        A[pivot_idx], A[start] = A[start], A[pivot_idx]

        # lomuto's partitioning
        smaller = start
        for bigger in range(start+1, end+1):
            if A[bigger] < A[start]:
                smaller += 1
                A[smaller], A[bigger] = A[bigger], A[smaller]
        A[start], A[smaller] = A[smaller], A[start]

        # hoarse partioning
        smaller = start + 1
        bigger = end
        while smaller <= bigger:
            if A[smaller] <= A[start]:
                smaller += 1
            elif A[bigger] > A[start]:
                bigger -= 1
            else:  # both pointers have been stuck
                A[smaller], A[bigger] = A[bigger], A[smaller]
                smaller += 1
                bigger -= 1
        A[smaller], A[start] = A[start], A[smaller]

        # recurse on left and right portions
        qSortHelper(A, start, smaller-1)
        qSortHelper(A, smaller+1, end)

    qSortHelper(A, 0, len(A)-1)
    return A
