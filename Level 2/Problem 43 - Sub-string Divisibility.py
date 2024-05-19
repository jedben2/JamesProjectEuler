# Problem 43 - Sub-string Divisibility

from common import primes, permlist
from tqdm import tqdm

pandigitals = permlist(list(range(0, 10)))

nums = []
for num in tqdm(pandigitals):
    s = 0
    for i in range(1, 8):
        if int(num[i:i + 3]) % primes[i - 1] == 0:
            s += 1
    if s == 7:
        nums.append(int(num))
print(sum(nums))
