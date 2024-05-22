# Problem 74 - Digit Factorial Chains

from common import digitfactorialsum, tqdm


def digitfactorialsumchain(n):
    chain = [n]
    i = 0
    while len(set(chain)) == len(chain):
        chain.append(digitfactorialsum(chain[i]))
        i += 1
    return chain[:-1]


count = 0
for i in tqdm(range(1, 10 ** 6)):
    if len(digitfactorialsumchain(i)) == 60:
        count += 1
print(count)
