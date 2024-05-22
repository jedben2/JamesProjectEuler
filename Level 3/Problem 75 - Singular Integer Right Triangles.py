# Problem 75 - Singular Integer Right Triangles

# Due to duplicates, the count is doubled :/

from common import np, gmpy2, gcd
from tqdm import tqdm


counter = [0 for _ in range(1500001)]
for n in tqdm(range(1, 1500)):
    for m in range(n + 1, 1500):
        if gcd(m, n) == 1:
            if n % 2 == 1 and m % 2 == 1:
                epsilon = 0.5
            else:
                epsilon = 1
            trip = [epsilon * 2 * m * n, epsilon * (m ** 2 - n ** 2), epsilon * (m ** 2 + n ** 2)]
            perimeter = int(sum(trip))
            k = 1
            while k * perimeter <= 1500000:
                counter[perimeter * k] += 1
                k += 1

print(sum([1 for c in counter if  c == 2]))
