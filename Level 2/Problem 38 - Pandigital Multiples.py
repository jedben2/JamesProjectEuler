# Problem 38 - Pandigital Multiples

from common import permlist
from tqdm import tqdm

pandigitals = permlist([i for i in range(1, 10)])

nums = []
for i in tqdm(range(1,10000)):
    prodstring = ""
    j = 1
    while len(prodstring) < 9:
        prodstring += str(i * j)
        j += 1
    if prodstring in pandigitals:
        nums.append(prodstring)

print(max(nums))