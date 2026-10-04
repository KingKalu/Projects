def divide(a):
    if len(a) == 0 or len(a) == 1:
        return a

    mid = len(a) // 2
    left = divide(a[:mid])
    right = divide(a[mid:])

    i=0
    j=0
    sortedlist = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sortedlist.append(left[i])
            i += 1
        else:
            sortedlist.append(right[j])
            j += 1

    return sortedlist + left[i:] + right[j:]
print(divide([4,6,1,0,7,3]))



