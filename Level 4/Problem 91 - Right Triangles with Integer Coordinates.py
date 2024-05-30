# Problem 91 - Right Triangles with Integer Coordinates

from itertools import product

N = 50
count = 2 * N ** 2
for x1, y1 in product(range(1, N + 1), repeat=2):
    for x2 in range(0, N + 1):
        q = y1 ** 2 + x1 ** 2 - x1 * x2
        if q % y1 == 0 and q // y1 <= N and 0 <= q // y1:
            count += 1
print(count)
