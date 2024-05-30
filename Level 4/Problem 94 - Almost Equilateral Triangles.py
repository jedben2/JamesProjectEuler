# Problem 94 - Almost Equilateral Triangles

from common import tqdm
from gmpy2 import is_square


def areaplus(a):
    return (3 * a + 1) * (a - 1)


def areaminus(a):
    return (3 * a - 1) * (a + 1)


summation = 0
for a in tqdm(range(3, 333333334, 2)):
    p = 3 * a + 1
    a1 = areaplus(a)
    a2 = areaminus(a)
    if is_square(a1) and p <= 10 ** 9:
        summation += p
    if is_square(a2) and a > 1 and p <= 10 ** 9 + 2:
        summation += p - 2
print(summation)
