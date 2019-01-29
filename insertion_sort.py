# Insertion Sort


A = [3, 2, 5, 1, 4]

# O(n^2)


def insertion_sort(A):
    for i in range(1, len(A)):
        insert = A[i]  # element to insert
        j = i - 1
        print("Scan ", i, ": ", A)
        # and operator: both A and B have to be True
        # or operator: either A or B has to be True
        while j >= 0 and A[j] > insert:
            # shift to the right
            A[j+1] = A[j]
            j = j - 1
        # get the position of an element
        # in the sorted portion that's smaller
        # than the number to "insert"
        A[j+1] = insert


insertion_sort(A)
print(A)
