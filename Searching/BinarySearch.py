# Recursive Way
def binarySearch(a, l, r, key):
    """
    :param a : input array
    :param l : left index of array 
    :param r : right index of array
    :param key: Search element
    """
    if l <= r:

        mid = (l + r) // 2

        if key == a[mid]:
            return mid

        elif key < a[mid]:
            return binarySearch(a, l, mid - 1, key)

        else:
            return binarySearch(a, mid + 1, r, key)

    else:
        return -1
        # return l # if u want to know the position where key has to be placed


a = [1, 3, 5, 7, 9, 10]

print(binarySearch(a, 0, 5, 9))
print(binarySearch(a, 0, 5, 18))


# Iterative Way

def binarySearch1(a, l, r, key):
    """
    :param a : input array
    :param l : left index of array 
    :param r : right index of array
    :param key: Search element
    """
    while l <= r:

        mid = (l + r) // 2

        if a[mid] == key:
            return mid

        elif key < a[mid]:
            r = mid - 1

        else:
            l = mid + 1

    return -1
    # return l # if u want to know the position where key has to be placed


a = [1, 3, 5, 7, 9, 10]

print(binarySearch1(a, 0, 5, 2))
print(binarySearch1(a, 0, 5, 10))
