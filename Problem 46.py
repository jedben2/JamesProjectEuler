from common import isgoldbach, composites, tqdm

oddcomposites = set([2 * i + 1 for i in range(1, 100000)]).intersection(set(composites))

for n in tqdm(oddcomposites):
    if not isgoldbach(n):
        print(n)
        break
