# Problem 76 - Counting Summations

# https://en.wikipedia.org/wiki/Partition_function_(number_theory) is very useful

import math
from common import pnumber, solvepnumber

numways = [1, 1] + [0] * 100

for i in range(2, 102):
    ks = [k for k in range(-100, 100) if (-1 * math.sqrt(24*i+1) + 1) / 6 <= k and (math.sqrt(24*i+1) + 1) / 6 >= k]
    for k in ks:
        if k != 0:
            try:
                numways[i] += int((-1) ** (k + 1) * numways[i - pnumber(5, k)])
            except:
                pass
print(numways[100] - 1)