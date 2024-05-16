from common import digitfactorialsum
from tqdm import tqdm

nums = []
for n in tqdm(range(3, 1000000)):
    if digitfactorialsum(n) == n:
        nums.append(n)
print(sum(nums))