def quicksort(a):
    if len(a) == 0 or len(a) == 1:
        return a

    mid = a[len(a) // 2]

    left = [x for x in a if x < mid]
    middle = [x for x in a if x == mid]
    right = [x for x in a if x > mid] 

    return quicksort(left) + middle + quicksort(right)

print(quicksort([4,6,1,0,7,3]))