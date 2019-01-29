# Selection Sort
"""
 In Pseudocode,
    For each i from 0 to len(A) - 1
        Find the min element
        Swap the min element with A[i]
"""

A = [5, 3, 4, 1, 2]


def selection_sort(A):
    for i in range(len(A)):  # (0, 1, ..., len(A)-1)
        min_index = i
        print("Scan ", i, ": ", A)
        for j in range(i+1, len(A)):
            if A[min_index] > A[j]:
                min_index = j
        # swap
        A[i], A[min_index] = A[min_index], A[i]


selection_sort(A)
print(A)
