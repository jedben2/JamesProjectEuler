# Problem 57 - Square Root Convergents

from common import gcd, tqdm


def continuedfracsqrt2(a, b):
    g = gcd(2 * a + b, a)
    return (2 * a + b) // g, a // g


a = 2
b = 2
count = 0
for i in tqdm(range(1, 1001)):
    a, b = continuedfracsqrt2(a, b)
    if len(str(a - b)) > len(str(b)):
        count += 1
print(count)
