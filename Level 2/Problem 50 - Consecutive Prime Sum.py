# Problem 50 - Consecutive Prime Sum

from common import primes, tqdm, primescapped

maxnum = 0
maxiter = 170
primes1m = primescapped(1000000)
for length in tqdm(range(21, 1000)):
    s = sum(primes[0:length])
    for start in range(0, 10):
        if s > 1000000:
            break
        elif s in primes1m:
            if s > maxnum:
                maxnum = s
        s += primes[start + length] - primes[start]
print(maxnum)