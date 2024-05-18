# Digit Fifth Powers

from common import digitpowersum
from tqdm import tqdm

nums = []
for i in tqdm(range(2, 1000000)):
    if digitpowersum(i, 5) == i:
        nums.append(i)
print(sum(nums))
