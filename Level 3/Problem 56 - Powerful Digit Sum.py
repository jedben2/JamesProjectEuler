# Problem 56 - Powerful Digit Sum

from common import digitsum, tqdm

maxsum = 0
for a in tqdm(range(1, 100)):
    for b in range(1, 100):
        d = digitsum(a ** b)
        if d > maxsum:
            maxsum = d
print(maxsum)
