# Problem 51 - Prime Digit Replacements

from common import replacedigits, primescapped, tqdm, isprime

primes100k = [p for p in sorted(list(primescapped(200000))) if p > 1000]

done = False
for p in tqdm(primes100k):
    length = len(str(p))
    for i in range(2, 2 ** length, 2):
        pattern = [int(j) for j in list(format(i, f'#0{length + 2}b')[2:])]
        replacedprime = [p2 for p2 in replacedigits(pattern, str(p)) if isprime(int(p2))]
        if not all(len(str(int(j))) == len(replacedprime[-1]) for j in replacedprime):
            continue
        elif len(replacedprime) > 7:
            print(replacedprime)
            done = True
            break
    if done:
        break
