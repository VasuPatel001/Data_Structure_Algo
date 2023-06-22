# Selection Sort
#  Brute force 

# IK
def selection_sort(A):
    for i in range(len(A)):
        min_idx = i
        for j in range(i+1, len(A)):
            if A[j] < A[min_idx]:
                min_idx = j
            A[i], A[min_idx] = A[min_idx], A[i]
    return A


A = [5, 3, 2, 4, 6]
print( selection_sort(A))