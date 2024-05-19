# Problem 62 - Cubic Permutations

from common import ispermutation, tqdm

cubes = [i ** 3 for i in tqdm(range(465, 10000))]


def numpermcubes(n):
    count = []
    for i in cubes:
        if ispermutation(i, n):
            count.append(i)
    return count


for i in tqdm(cubes):
    if len(numpermcubes(i)) == 5:
        print(i)
        break
