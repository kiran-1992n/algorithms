def linearSearch(a,key):

    size = len(a)

    for x in range(0,size):
        if a[x] == key:
            return x
    return -1

# Driver Code
a = [8,6,5,7,2,3,1,13,16]

print(linearSearch(a,7))
print(linearSearch(a,20))