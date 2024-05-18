# Quadratic Primes

from common import primes
from tqdm import tqdm

# note that b has to be prime (n = 0 case).
# also a = p - b - 1 (n = 1 case => 1 + a + b = p for some prime p)
# can cut down on runtime because n is going to have to be larger than 80 (is an example in the problem).

def quadraticprime(a, b):
    n = 0
    while True:
        p = n ** 2 + a * n + b
        if p in primes:
            n += 1
        else:
            return n


maxcoeffs = [0, 0, 0]
for b in tqdm([p for p in primes if p < 1000]):
    for p in [p for p in primes if p < 1000]:
        a = p - b - 1
        n = quadraticprime(a, b)
        if n > maxcoeffs[2]:
            maxcoeffs = [a, b, n]
print(maxcoeffs)
print(maxcoeffs[0] * maxcoeffs[1])
