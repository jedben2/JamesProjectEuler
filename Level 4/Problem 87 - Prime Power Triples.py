# Problem 87 - Prime Power Triples

from common import primescapped, np, tqdm

maxnum = 50 * (10 ** 6)
count = 0
P1 = sorted(primescapped(int(np.sqrt(maxnum)) + 1))
P2 = sorted(primescapped(int(np.power(maxnum, 1/3)) + 1))
P3 = sorted(primescapped(int(np.power(maxnum, 1/4)) + 1))

count = []
for p1 in tqdm(P1):
    a = np.power(p1, 2)
    for p2 in P2:
        b = a + np.power(p2, 3)
        if b > maxnum:
            break
        for p3 in P3:
            c = b + np.power(p3, 4)
            if c <= maxnum:
                count.append(c)
            else:
                break
print(len(set(count)))