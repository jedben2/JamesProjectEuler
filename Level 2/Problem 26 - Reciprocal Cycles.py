# Reciprocal Cycles

from common import primes

# we look for "full reptend primes" i.e. (10^p-1 - 1) / p = a cyclic number
# credit to https://en.wikipedia.org/wiki/Cyclic_number

def cyclicnumber(p):
    t = 0
    r = 1
    n = 0
    while True:
        t += 1
        x = r * 10
        d = int(t / p)
        r = x % p
        n = n * 10 + d
        if t > p / 2:
            return p
        elif r == 1:
            return 0

cyclicnums = [cyclicnumber(p) for p in primes if p < 1000]
print(max(cyclicnums))