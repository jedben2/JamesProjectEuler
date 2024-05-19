# Problem 49 - Prime Permutations

from common import primes, tqdm, permlist

fourdigitprimes = list(set(primes).intersection(list(range(1500, 10000))))

done = False
for p in tqdm(fourdigitprimes):
    perms = [int(i) for i in permlist(list(str(p)))]
    for d in range(1000, 4000, 2):
        if all(p + (n - 1) * d in fourdigitprimes for n in range(1, 4)) and all(p + (n - 1) * d in perms for n in range(1, 4)):
            print(''.join([str(p + (n - 1) * d) for n in range(1, 4)]))
            done = True
            break
    if done:
        break