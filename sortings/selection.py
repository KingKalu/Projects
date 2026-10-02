def selection(a):
    for i in range(len(a)):
        lowest = i
        for j in range(i+1,len(a)):
            if a[j] < a[lowest]:
                lowest = j
        a[i],a[lowest] = a[lowest],a[i]
    return a
print(selection([9,5,6,2,1]))
        
    
