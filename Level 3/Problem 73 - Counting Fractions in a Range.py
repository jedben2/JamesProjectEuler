# Problem 73 - Counting Fractions in a Range

from tqdm import tqdm

fracs = []
for d in tqdm(range(1, 12000 + 1)):
    fracs += [n / d for n in range(d // 3, d // 2 + 1)]
fracs = sorted([r for r in list(set(fracs)) if 3 * r > 1 and 2 * r < 1])
# print(fracs)
print(len(fracs))
