from common import pentagonalnum, solvepentagonal
from tqdm import tqdm

pentagonals = [pentagonalnum(i) for i in range(1, 10000)]

pairs = []
for Pi in tqdm(pentagonals):
    for Pj in pentagonals:
        if solvepentagonal(Pi + Pj) % 1 == 0 and solvepentagonal(np.abs(Pj - Pi)) % 1 == 0:
            pairs.append((Pi, Pj))
print(pairs)
