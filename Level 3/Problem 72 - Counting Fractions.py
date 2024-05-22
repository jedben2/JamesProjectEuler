# Problem 72 - Counting Fractions

from common import eulerphi, tqdm

D = 10 ** 6 + 1

print(sum([eulerphi(i) for i in tqdm(range(2, D))]))