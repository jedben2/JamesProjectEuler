# Problem 77 - Prime Summations

# Euler Transform: https://mathworld.wolfram.com/EulerTransform.html

from common import isprime, factors

a_n = [0] + [int(isprime(i)) for i in range(1, 100)]

c_n = [0] + [sum([d * a_n[d] for d in factors(n)]) for n in range(1, 100)]

b_n = [0]
for n in range(1, 100):
    b_n += [(c_n[n] + sum([c_n[k] * b_n[n - k] for k in range(1, n)])) // n]

print(b_n.index([b for b in b_n if b > 5000][0]))
