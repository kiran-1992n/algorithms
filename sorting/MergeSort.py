def merge(A, B):
    m = len(A)
    n = len(B)
    c = []
    i = j = 0

    while i < m and j < n:
        if A[i] < B[j]:
            c.append(A[i])
            i += 1

        else:
            c.append(B[j])
            j += 1

    for x in range(i, m):
        c.append(A[x])

    for y in range(j, n):
        c.append(B[y])

    return c


def MergeSort(A):
    if len(A) == 1:
        return A

    mid = len(A) // 2

    L = MergeSort(A[:mid])
    R = MergeSort(A[mid:])

    return merge(L, R)


# Driver Code
A = [1, 2, 4, 3, 5, 6, 7, 8, 9, 10]
# A=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# A=[2, 4, 3, 7, 0, 5, 4, 8, 15, 18, 6]
print(MergeSort(A))
