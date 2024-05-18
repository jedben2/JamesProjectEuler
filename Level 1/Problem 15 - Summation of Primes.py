# Summation of Primes

from common import primes

i = 0
s = 0
while primes[i] < 2000000:
    s += primes[i]
    i += 1
print(s)
