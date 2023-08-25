# 5/5/2023 - did in IK platform, took an hour
#  hardest part was understanding "arr[start:end+1] = aux"
#   trying to copy the aux array into the main arr without new assignment, 
#   I didn't think of use a range within the array although the video stated explicitly

def merge_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    helper(arr, 0, len(arr)-1)
    return arr


def helper(A, start, end):
    if (start >= end):
        return

    mid = start + (end - start) // 2

    # recurse on left and right halves
    helper(A, start, mid)
    helper(A, mid+1, end)

    # merge routine
    merge(A, start, mid, end)
    return


def merge(A, start, mid, end):
    i = start
    j = mid + 1
    aux = []
    while (i <= mid and j <= end):
        if A[i] <= A[j]:
            aux.append(A[i])
            i += 1
        else:
            aux.append(A[j])
            j += 1

    # Gather phase
    while i <= mid:
        aux.append(A[i])
        i += 1
    while j <= end:
        aux.append(A[j])
        j += 1
    A[start:end+1] = aux  # IMP part was understanding "arr[start:end+1] = aux"
    return


def mergeSort(A: list[int]) -> list[int]:
    def mSortHelper(A: list[int], start: int, end: int):
        if start >= end:
            return

        # compute mid idx
        mid = start + (end-start)//2
        mSortHelper(A, start, mid)
        mSortHelper(A, mid+1, end)

        # merge routine
        i = start
        j = mid + 1
        aux = []  # Aux space: O(N)
        # Merge from two halves
        while (i <= mid and j <= end):
            if A[i] <= A[j]:  # <= ensure stability
                aux.append(A[i])
                i += 1
            else:  # A[i] > A[j]
                aux.append(A[j])
                j += 1

        # Gather phase
        while i <= mid:
            aux.append(A[i])
            i += 1
        while j <= end:
            aux.append(A[j])
            j += 1

        A[start:end+1] = aux

    mSortHelper(A, 0, len(A)-1)
    return A
