# Problem 88 - Product-sum Numbers

from more_itertools import set_partitions
from common import primefactors, tqdm


def productpartition(n):
    factors = primefactors(n)
    parts = [sorted([prod(p) for p in part]) for k in range(2, len(factors) + 1) for part in set_partitions(factors, k)]
    p2 = []
    for p in parts:
        if p not in p2:
            p2.append(p)
    return p2


def prod(l):
    a = 1
    for i in l:
        a *= i
    return a


def prodsumnum(n):
    return [n - sum(p) + len(p) for p in productpartition(n)]


ks = [prodsumnum(n) for n in tqdm(range(4, 16000))]
nums = []
for k in tqdm(range(2, 12001)):
    nums.append(min([i + 4 for i, n in enumerate(ks) if k in n]))
print(sum(set(nums)))
