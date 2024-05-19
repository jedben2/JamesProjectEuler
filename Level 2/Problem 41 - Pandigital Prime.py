# Problem 41 - Pandigital Prime

from common import primes, permlist

pandigital8 = [int(i) for i in permlist(list(range(1, 8)))]
pandigitalprimes = set(pandigital8).intersection(set(primes))
print(max(pandigitalprimes))