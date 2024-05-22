# Problem 71 - Ordered Fractions

from tqdm import tqdm

fracs = [int(3 * d / 7) / d for d in tqdm(range(1, 10 ** 6 + 1))]
fracs = sorted(list(set(fracs)))
r = fracs[fracs.index(3 / 7) - 1]
for d in range(1, 10 ** 6 + 1):
    if r * d % 1 == 0:
        print(r * d)
