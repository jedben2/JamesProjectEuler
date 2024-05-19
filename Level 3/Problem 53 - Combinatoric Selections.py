# Problem 53 - Combinatoric Selections

# If nCr > 10^6, then nC(n-r) > 10^6 as are all the values in between, of which there are a total of n - 2r + 1.

from math import comb
from tqdm import tqdm

numvals = 0
for n in tqdm(range(23, 101)):
    for r in range(0, n // 2):
        if comb(n, r) > 1000000:
            numvals += n - 2 * r + 1
            break
print(numvals)