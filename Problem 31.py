# know 1x£2 is a way
from tqdm import tqdm

count = 1
for b in range(0, 3):
    for c in range(0, 5 - 2 * b):
        for d in tqdm(range(0, 11 - 2 * c)):
            for e in range(0, 21 - 2 * d):
                for f in range(0, 41 - 2 * e):
                    for g in range(0, 101 - 2 * f):
                        for h in range(0, 201 - 2 * g):
                            if b * 100 + c * 50 + d * 20 + e * 10 + f * 5 + g * 2 + h * 1 == 200:
                                count += 1
print(count)