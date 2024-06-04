# Problem 108 - Diophantine Reciprocals I

primes = [2, 3, 5, 7, 11, 13, 15, 17, 19]


def numsols(n):
    N = n ** 2
    count = 1
    for p in primes:
        c = 0
        while N % p == 0:
            c += 1
            N = N // p
        count *= c + 1
    return count // 2 + 1


n = 2
while True:
    if numsols(n) >= 1000:
        print(n)
        break
    n += 1
