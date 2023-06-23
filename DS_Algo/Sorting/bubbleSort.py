# Bubble Sort - Optimized vs Unoptimized

def bubble_optimized(A):
    iterations = 0
    for i in range(len(A)):
        for j in range(len(A) - i - 1): # adding the "-i" bcuz right side of array is already sorted, don't check again
            iterations += 1
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A, iterations


def bubble_unoptimized(A):
    iterations = 0
    for i in A:
        for j in range(len(A)-1):
            iterations += 1
            if A[j] > A[j+1]:
                swap(A, j, j + 1)
    return A, iterations


def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


A = [9, 8, 7, 6, 5, 4, 3, 2, 1]
B = [9, 8, 7, 6, 5, 4, 3, 2, 1]

print(bubble_optimized(A))
print(bubble_unoptimized(B))