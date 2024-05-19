import numpy as np
import pickle, copy, math
from tqdm import tqdm


# Fibonacci numbers

def fib(n):
    phi = (1 + np.sqrt(5)) / 2
    return int((np.power(phi, n) - np.power(-1 / phi, n)) / np.sqrt(5))


# Prime numbers, factorisation, gcd, and lcm

with open("..//primes.txt", "rb") as f:
    primes = pickle.load(f)


def generatecomposites():
    return list(set(range(1, max(primes))) - set(primes))


def factors(N):
    factors = []
    for n in range(1, int(np.sqrt(N)) + 1):
        if N % n == 0:
            factors += [n, int(N // n)]
    return sorted(list(set(factors)))


def primefactors(N):
    for p in primes:
        if N % p == 0:
            if p == N:
                return [p]
            return [p] + primefactors(N // p)


def countlist(l, n):
    count = 0
    for item in l:
        if item == n: count += 1
    return count


def primepowerfact(n, maxprime):
    l = primefactors(n)
    pows = []
    for p in primes:
        if p > maxprime:
            return pows
        pows += [countlist(l, p)]


def gcd(a, b):
    c = min(a, b)
    r = max(a, b) % c
    if r == 0:
        return c
    return gcd(c, r)


def lcm(a, b):
    return a * b // gcd(a, b)


def isprime(n):
    global primes
    for p in primes:
        if p <= int(np.ceil(np.sqrt(n))):
            if n % p == 0 and n > p:
                return False
        else:
            break
    return True


def generate_primes(n):
    global primes
    with open("..//primes.txt", "rb") as f:
        primes_temp = pickle.load(f)
    for k in tqdm(range(primes_temp[-1] + 2, primes_temp[-1] + 1 + 2 * n, 2)):
        if isprime(k):
            primes_temp.append(k)
    with open("..//primes.txt", "wb") as f:
        pickle.dump(primes_temp, f)
    primes = copy.copy(primes_temp)


def init_primes():
    global primes
    with open("..//primes.txt", "wb") as f:
        pickle.dump([2, 3, 5, 7, 11], f)
    with open("..//primes.txt", "rb") as f:
        primes = pickle.load(f)


def primescapped(n):
    primestemp = set(primes)
    capped = set([i for i in range(n + 1)])
    return list(primestemp.intersection(capped))


# Summations

def sum1(n):
    return n * (n + 1) / 2


def sum2(n):
    return n * (n + 1) * (2 * n + 1) / 6


def sum3(n):
    return (n * (n + 1) / 2) ** 2


def digitsum(n):
    return sum([int(i) for i in str(n)])


def maxtrianglesum(triangle):
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(i + 1):
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
    return triangle[0][0]


def sumdiv(n):
    return sum(factors(n)[:-1])


def spiralsum(n):  # n layers
    if n == 1:
        return 1
    else:
        return 4 * (2 * n - 1) ** 2 - 12 * (n - 1) + spiralsum(n - 1)


def digitpowersum(n, pow):
    digits = [int(d) ** pow for d in list(str(n))]
    return sum(digits)


def digitfactorialsum(n):
    return sum([math.factorial(int(d)) for d in str(n)])


def sumselfpowermodB(n, B):
    return sum([i ** i % B for i in range(1, n + 1)]) % B


# Collatz algorithm (array)

def collatz(n):
    if n == 1:
        return [1]
    elif n % 2 == 0:
        return [n] + collatz(n // 2)
    else:
        return [n] + collatz(3 * n + 1)


# Permutations and operations on moving digits

def permlist_list(l):
    perms = []
    if len(l) == 1:
        return [l]
    else:
        for item in l:
            l2 = copy.deepcopy(l)
            l2.remove(item)
            l3 = permlist_list(l2)
            for thing in l3:
                perms.append([item] + thing)
        return perms


def permlist(l):
    perms = permlist_list(l)
    perms2 = [''.join([str(i) for i in bit]) for bit in perms]
    sorted_perms = sorted([int(i) for i in perms2])
    formatted_perms = [format(i, f'0{len(l)}d') for i in sorted_perms]
    return formatted_perms


def cyclennum(n):
    perms = [n]
    for i in range(len(str(n)) - 1):
        perms.append(int(str(perms[-1])[-1] + str(perms[-1])[:-1]))
    return perms


def replacedigits(pattern, n):
    replacednums = []
    n = str(n)
    for d in range(0, 10):
        nreplaced = ""
        for i, place in enumerate(pattern):
            if place:
                nreplaced += str(d)
            else:
                nreplaced += n[i]
        replacednums.append(nreplaced)
    return replacednums


def concatenatenums(a, b):
    return int(str(a) + str(b))


def truncatenum(n):
    nstr = str(n)
    splits = []
    for i in range(len(nstr)):
        splits.append(int(nstr[i:]))
        splits.append(int(nstr[:i + 1]))
    return splits[:-1]


# Special numbers

def pythagtriple(m, n):
    return m ** 2 - n ** 2, 2 * m * n, m ** 2 + n ** 2


def pentagonalnum(n):
    return n * (3 * n - 1) // 2


def solvepentagonal(n):
    return (1 + np.sqrt(24 * n + 1)) / 6


def hexagonalnum(n):
    return n * (2 * n - 1)


def solvehexagonal(n):
    return (1 + np.sqrt(8 * n + 1)) / 4


def ispalindrome(n):
    N = str(n)
    if N == N[::-1]:
        return True
    return False


def isgoldbach(n):
    for s in [i ** 2 for i in range(1, int(np.sqrt(n / 1.5)))]:
        if n - 2 * s in primes:
            return True
    return False


def islychrel(n):
    for i in range(50):
        n += int(str(n)[::-1])
        if ispalindrome(n):
            return True
    return False


if __name__ == "__main__":
    pass
