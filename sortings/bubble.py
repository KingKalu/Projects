def bubble(a):
    for i in range(len(a)-1, 0,-1):
        for j in range(1,len(a)):
            if a[j-1] > a[j]:
                a[j],a[j-1]=a[j-1],a[j]
    return a
print(bubble([9,5,6,2,1]))
