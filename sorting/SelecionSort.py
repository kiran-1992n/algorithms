def selectionSort(A):
    n = len(A)

    for i in range(n):
        min_ind = i

        for j in range(i + 1, n):
            if A[j] < A[min_ind]:
                min_ind = j
        A[i], A[min_ind] = A[min_ind], A[i]

    return A


# Driver Code
A = [1, 2, 4, 3, 5, 6, 7, 8, 9, 10]
# A=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# A=[2, 4, 3, 7, 0, 5, 4, 8, 15, 18, 6]
print(selectionSort(A))
