import numpy as np
import pickle
from tqdm import tqdm
import copy


# Fibonacci numbers

def fib(n):
    phi = (1 + np.sqrt(5)) / 2
    return int((np.power(phi, n) - np.power(-1 / phi, n)) / np.sqrt(5))


# Prime numbers, factorisation, gcd, and lcm

with open("primes.txt", "rb") as f:
    primes = pickle.load(f)


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


def gcd(l):
    maxprime = max(l)
    numpows = np.array([primepowerfact(i, maxprime) for i in l])
    g = 1
    for i, p in enumerate(primes):
        try:
            g *= p ** np.min(numpows[:, i])
        except:
            return g


def lcm(l):
    maxprime = max(l)
    numpows = np.array([primepowerfact(i, maxprime) for i in l])
    g = 1
    for i, p in enumerate(primes):
        try:
            g *= p ** np.max(numpows[:, i])
        except:
            return g


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
    with open("primes.txt", "rb") as f:
        primes_temp = pickle.load(f)
    for k in tqdm(range(primes_temp[-1] + 2, primes_temp[-1] + 1 + 2 * n, 2)):
        if isprime(k):
            primes_temp.append(k)
    with open("primes.txt", "wb") as f:
        pickle.dump(primes_temp, f)
    primes = copy.copy(primes_temp)


def init_primes():
    global primes
    with open("primes.txt", "wb") as f:
        pickle.dump([2, 3, 5, 7, 11], f)
    with open("primes.txt", "rb") as f:
        primes = pickle.load(f)


# Palindromes

def ispalindrome(n):
    N = str(n)
    for i in range(len(N) // 2):
        if not N[i] == N[-1 - i]:
            return False
    return True


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


# Collatz algorithm (array)

def collatz(n):
    if n == 1:
        return [1]
    elif n % 2 == 0:
        return [n] + collatz(n // 2)
    else:
        return [n] + collatz(3 * n + 1)


# Permutations

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


# Digits

def digitlen(n):
    return len(str(n))


if __name__ == "__main__":
    pass
