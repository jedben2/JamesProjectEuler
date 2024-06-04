# Problem 110 - Diophantine Reciprocals II

from common import primes
from itertools import combinations_with_replacement


def numsols(n):
    N = n
    count = 1
    for p in primes:
        c = 0
        while N % p == 0:
            c += 1
            N = N // p
        count *= 2 * c + 1
    return count // 2 + 1


def d(l):
    p = 1
    for i in l:
        p *= 2 * i + 1
    return p // 2 + 1


N = 15
minnum = 10 ** 100
for exps in combinations_with_replacement(list(range(0, N))[::-1], r=N):
    prod = 1
    for i in range(N):
        prod *= primes[i] ** exps[i]
    if prod < minnum:
        if d(exps) >= 4000000:
            minnum = prod
            print(prod, d(exps), exps)
print(numsols(minnum), minnum)
