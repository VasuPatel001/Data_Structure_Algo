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

A = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(A)

print('Sorted Array in Ascending Order:')
print(A)
