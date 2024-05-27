# Problem 90 - Cube Digit Pairs

from itertools import product
from tqdm import tqdm

squares = ["{:02d}".format(i ** 2) for i in range(1, 10)]

alldice = []
nums = [str(i) for i in range(0, 10)]
for a, b, c, d, e, f in tqdm(product(nums, repeat=6)):
    dice = sorted([a, b, c, d, e, f])
    if len(set(dice)) == 6 and dice not in alldice:
        alldice.append(dice)


def goodpair(a, b):
    used = [0] * 9
    for i in a:
        for j in b:
            if i + j in squares:
                used[squares.index(i + j)] = 1
            elif i + j == '06':
                used[2] = 1
            elif i + j == '19':
                used[3] = 1
            elif i + j == '39':
                used[5] = 1
            elif i + j == '46':
                used[6] = 1
            elif i + j == '94':
                used[7] = 1

            if all(u == 1 for u in used):
                return True
    for j in a:
        for i in b:
            if i + j in squares:
                used[squares.index(i + j)] = 1
            elif i + j == '06':
                used[2] = 1
            elif i + j == '19':
                used[3] = 1
            elif i + j == '39':
                used[5] = 1
            elif i + j == '46':
                used[6] = 1
            elif i + j == '94':
                used[7] = 1

            if all(u == 1 for u in used):
                return True
    return False


def isdistinct(a, b):
    return sorted(a) != sorted(b)


pairs = []
for a in tqdm(alldice):
    for b in alldice[alldice.index(a):]:
        if isdistinct(a, b):
            if goodpair(a, b):
                pairs.append([a, b])

print(len(pairs))
