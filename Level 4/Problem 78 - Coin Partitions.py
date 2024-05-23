# Problem 78 - Coin Partitions

import math
from common import pnumber, tqdm

N = 60000

numways = [1, 1] + [0] * (N - 1)

for i in tqdm(range(2, N + 1)):
    ks = [k for k in range(-N, N) if -2 * i - 24 <= 12 * k and 2 * i + 28 >= 12 * k]
    for k in ks:
        ik = i - pnumber(5, k)
        if k != 0 and ik >= 0:
            try:
                numways[i] += (-1) ** (k + 1) * numways[ik]

            except:
                pass
    numways[i] = numways[i] % 1000000

print(numways.index(0))