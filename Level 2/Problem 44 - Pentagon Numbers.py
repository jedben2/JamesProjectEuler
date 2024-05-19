# Problem 44 - Pentagon Numbers

from common import pnumber, solvepnumber, np
from tqdm import tqdm

pentagonals = [pnumber(5, i) for i in range(1, 10000)]

pairs = []
for Pi in tqdm(pentagonals):
    for Pj in pentagonals:
        if solvepnumber(5, Pi + Pj) % 1 == 0 and solvepnumber(5, np.abs(Pj - Pi)) % 1 == 0:
            pairs.append((Pi, Pj))
print(pairs)
