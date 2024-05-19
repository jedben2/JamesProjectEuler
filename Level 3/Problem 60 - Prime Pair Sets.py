# Problem 60 - Prime Pair Sets

# Not very quick but the combination is quite early :p

from common import isprime, concatenatenums, primescapped, tqdm

primes100k = primescapped(10000)
primes100k.remove(2)
primes100k.remove(5)


def primepairs(p1, p2):
    if isprime(concatenatenums(p1, p2)) and isprime(concatenatenums(p2, p1)):
        return True
    return False


minsum = 100000
for p1 in primes100k:
    for p2 in tqdm([p for p in primes100k if p > p1]):
        if primepairs(p1, p2):
            for p3 in [p for p in primes100k if p > p2]:
                if primepairs(p3, p2) and primepairs(p3, p1):
                    for p4 in [p for p in primes100k if p > p3]:
                        if all([primepairs(p4, p) for p in [p1, p2, p3]]):
                            for p5 in [p for p in primes100k if p > p4]:
                                if sum([p1, p2, p3, p4, p5]) < minsum:
                                    if all([primepairs(p5, p) for p in [p1, p2, p3, p4]]):
                                        minsum = sum([p1, p2, p3, p4, p5])
                                        print([p1, p2, p3, p4, p5], minsum)