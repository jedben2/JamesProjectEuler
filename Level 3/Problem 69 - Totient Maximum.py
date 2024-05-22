# Problem 69 - Totient Maximum

from common import eulerphi, tqdm

maxval = [0, 0]
for n in tqdm(range(2, 1000001)):
    r = n / eulerphi(n)
    if r > maxval[1]:
        maxval = [n, r]
print(maxval)