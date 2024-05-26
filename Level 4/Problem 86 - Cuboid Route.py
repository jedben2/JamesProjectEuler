# Problem 86 - Cuboid Route

# Clever me

from tqdm import tqdm
import gmpy2
from common import gcd


def numintegersols(M):
    count = 0
    for t in trips:
        if t[1] <= M and t[0] <= 2 * M:
            for a in range(1, M + 1):
                if t[0] - a <= t[1] and t[0] - a >= a:
                    count += 1
    return count


trips = []
for a in tqdm(range(1, 4000)):
    for b in range(1, 4000):
        if gmpy2.is_square(a ** 2 + b ** 2):
            trips.append([a, b])

vals = [0] * 2001
M1 = 0
M2 = 2000
M = round((M1 + M2) / 2)
target = 1000000

while not (vals[M - 1] < target and vals[M] > target):
    vals[M] = numintegersols(M)
    if vals[M] > target:
        M2 = M
    else:
        M1 = M
    M = round((M1 + M2) / 2)
print(M)
