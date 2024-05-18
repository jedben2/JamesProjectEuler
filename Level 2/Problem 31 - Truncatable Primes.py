# Truncatable Primes

from common import primes, truncatenum

count = 0
nums = []
i = 4
while count < 11:
    if not any(even in str(primes[i])[1:] for even in ["2", "4", "6", "8", "0"]):
        if all(p in primes for p in truncatenum(primes[i])):
            count += 1
            nums.append(primes[i])
    i += 1
print(sum(nums))