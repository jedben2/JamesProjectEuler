# Problem 35 - Circular Primes

from common import cyclennum, primescapped
from tqdm import tqdm

primes1m = primescapped(1000000)

nums = []
for p in tqdm(primes1m):
    if any(even in str(p) for even in ["2", "4", "6", "8", "0"]):
        continue
    else:
        cycled = cyclennum(p)
        if set(cycled).intersection(set(primes1m)) == set(cycled):
            nums.append(p)
print(len(nums) + 1)  # 2 is not included in the check
