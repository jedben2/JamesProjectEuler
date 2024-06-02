# Problem 106 - Special Subset Sums Meta-testing

from itertools import combinations


def numtests(n):
    count = 0
    A = [i for i in range(1, n + 1)]
    for l in range(2, n // 2 + 1):
        combs = list(combinations(A, l))
        for c1 in combs:
            combs2 = list(combinations(list(set(A).difference(set(c1))), l))
            for c2 in combs2:
                if not all(sorted(c1)[i] < sorted(c2)[i] for i in range(l)) and not all(
                        sorted(c2)[i] < sorted(c1)[i] for i in range(l)):
                    count += 1
    return count // 2


print(numtests(12))
