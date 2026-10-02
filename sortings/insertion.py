def insertion(a):
    for i in range(len(a)):
        key = a[i]
        j = i
        while j > 0 and a[j-1] > key:
            a[j] = a[j-1]
            j -= 1
        a[j] = key 
    return a
print(insertion([9,5,6,2,1]))