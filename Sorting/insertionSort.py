# Insertion Sort - Shifting Elements

def insertion_sort(A):
    # 0 index is the start of the sorted side while 1 is unsorted
    # i = 0 sorted side
    # j = 1 unsorted side
    for j in range(1, len(A)):
        key = A[j] # 2, 4, 6
        i = j - 1  # 0, 1, 2
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]  # Assigns the larger value to right
            i -= 1  # decreases index to find the index in which the key is greater than an element on the sorted side (will be inserted there next)
        A[i + 1] = key  # moves the key into the correct slot of the sorted side
    return A


A = [5, 2, 4, 6, 1, 3]
print(insertion_sort(A))