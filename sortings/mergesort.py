def divide(a):
    mid = len(a) // 2
    left = divide(a[:mid])
    right = divide(a[mid:])



