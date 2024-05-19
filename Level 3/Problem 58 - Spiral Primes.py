# Problem 58 - Spiral Primes

from common import isprime


def spiraldiagonalsprime(n):  # nth layer
    if n == 1:
        return 0
    else:
        s = (2 * n - 1) ** 2
        return sum([int(isprime(d)) for d in [s - 2 * n + 2, s - 4 * n + 4, s - 6 * n + 6]])


r = 1
n = 1
while r * 10 > (4 * n - 3):
    n += 1
    r += spiraldiagonalsprime(n)
print(2 * n - 1, r / (4 * n - 3))
