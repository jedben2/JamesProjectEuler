# Problem 39 - Integer Right Triangles

from tqdm import tqdm
import numpy as np

numsols = []
for p in tqdm(range(1, 1001)):
    sols = 0
    for a in range(1, p // 2):
        for b in range(a, p // 2):
            c = np.sqrt(a ** 2 + b ** 2)
            if c % 1 == 0 and a + b + c == p:
                sols += 1
    numsols.append(sols)
print(numsols.index(max(numsols)) + 1)
