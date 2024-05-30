# Problem 95 - Amicable Chains

from common import sumdiv, isprime, tqdm

longest = [0, 0]
for n in tqdm(range(1, 10 ** 6 + 1)):
    if isprime(n):
        continue
    k = n
    chain = [k]
    while True:
        k = sumdiv(k)
        if k > 10 ** 6 or isprime(k):
            break
        elif k in chain:
            if len(chain) > longest[1] and k == n:
                longest = [min(chain), len(chain)]
            break
        chain.append(k)
print(longest)
