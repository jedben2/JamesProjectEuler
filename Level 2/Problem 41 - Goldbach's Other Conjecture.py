# Goldbach's Other Conjecture

from common import isgoldbach, tqdm, generatecomposites

oddcomposites = set([2 * i + 1 for i in range(1, 100000)]).intersection(set(generatecomposites()))

for n in tqdm(oddcomposites):
    if not isgoldbach(n):
        print(n)
        break
