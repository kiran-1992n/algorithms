def bubbleSort(A):
    n = len(A)
    for i in range(n):
        count = 0
        for j in range(n - i - 1):

            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                count += 1

        # print(i,count)

        # Used to reduce the run time i.e when the array is
        # almost sorted with minor mistake no need to run it n**2
        # number of times

        if count == 0:
            break

    return A


# Driver Code
A = [1, 2, 4, 3, 5, 6, 7, 8, 9, 10]
# A=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# A=[2, 4, 3, 7, 0, 5, 4, 8, 15, 18, 6]
print(bubbleSort(A))
