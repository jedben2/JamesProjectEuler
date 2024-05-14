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
            if gcd([p, n]) != 1:
                return False
        else:
            return True
    return True


def generate_primes(n):
    global primes
    with open("primes.txt", "rb") as f:
        primes_temp = pickle.load(f)
    for k in tqdm(range(primes_temp[-1] + 1, primes_temp[-1] + 1 + n)):
        if isprime(k):
            primes_temp.append(k)
    with open("primes.txt", "wb") as f:
        pickle.dump(primes_temp, f)
    primes = copy.copy(primes_temp)


def init_primes():
    global primes
    with open("primes.txt", "wb") as f:
        pickle.dump([2], f)
    with open("primes.txt", "rb") as f:
        primes = pickle.load(f)


# Palindromes

def ispalindrome(n):
    N = str(n)
    for i in range(len(N) // 2):
        if not N[i] == N[-1 - i]:
            return False
    return True


if __name__ == "__main__":
    pass
