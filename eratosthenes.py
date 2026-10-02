import time
def primeList(n):
    result = [2]
    for num in range(3, n+1):
        root = int(num **.5)
        is_prime = True
        for i in range(2, root + 2):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            result.append(num)
    return result


def Eratos(n):
    is_prime = [True] * n
    is_prime[0] = False
    
    for num in range(2, int(n**.5) + 1):
        if is_prime[num - 1]:
            for i in range(num * num, n + 1, num):
                is_prime[i - 1] = False
    
    return [idx for idx, num in enumerate(is_prime, start=1) if num]

use = 1000000
ErasStart = time.time()
prime = Eratos(use)
print(time.time()-ErasStart)
# PrimeStart = time.time()
# primeList(use)
# print(time.time()-PrimeStart)