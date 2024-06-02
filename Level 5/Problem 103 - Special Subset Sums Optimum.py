# Problem 103 - Special Subset Sums Optimum


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


minsum = [0, 1000]
for a in tqdm(range(20, 50)):
    for b in range(a + 1, 20 + a):
        for c in range(b + 1, 20 + a):
            for d in range(c + 1, 20 + a):
                for e in range(d + 1, 20 + a):
                    for f in range(e + 1, 20 + a):
                        A = [20, a, b, c, d, e, f]
                        if isspecial(A):
                            if sum(A) < minsum[1]:
                                minsum = [A, sum(A)]
print(minsum)
