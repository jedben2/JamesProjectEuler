# Problem 105 - Special Subset Sums Testing

from itertools import combinations, product
from tqdm import tqdm


def isspecial(A):
    for k in range(len(A), 1, -1):
        combs1 = list(combinations(A, k))
        combs2 = list(combinations(A, k - 1))
        if any(sum(c1) <= sum(c2) for c1, c2 in product(combs1, combs2)):
            return False
        if any(sum(c1) == sum(c2) for c1, c2 in product(combs2, repeat=2) if len(set(c1).intersection(set(c2))) == 0):
            return False
    return True


sets = []
with open("0105_sets.txt", "r") as f:
    for line in f.readlines():
        sets.append([int(i) for i in line.strip().split(",")])

specialsets = []
for A in tqdm(sets):
    if isspecial(A):
        specialsets.append(A)
print(sum(sum(A) for A in specialsets))
