# Problem 14 - Longest Collatz Sequence

from common import collatz
from tqdm import tqdm

longest = [0, 0]
for i in tqdm(range(1, 1000000)):
    a = len(collatz(i))
    if a > longest[1]:
        longest = [i, a]
print(longest)