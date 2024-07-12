# Problem 111 - Primes with Runs


from more_itertools import distinct_permutations as idp
from itertools import product
from gmpy2 import is_prime


def ninerepeats(d):
    nums = []
    templates = [''.join(t) for t in idp("aaaaaaaaab")]
    for template in templates:
        prime = template.replace("a", str(d))
        for i in range(10):
            fittedprime = prime.replace("b", str(i))
            if is_prime(int(fittedprime)):
                nums.append(int(fittedprime))
    return set(nums)


def eightrepeats(d):
    templates = [''.join(t) for t in idp("aaaaaaaabc")]
    nums = []
    for template in templates:
        prime = template.replace("a", str(d))
        for i, j in product(range(10), repeat=2):
            if i != d and j != d:
                fittedprime = prime.replace("b", str(i)).replace("c", str(j))
                if is_prime(int(fittedprime)):
                    if fittedprime[0] == '0':
                        continue
                    else:
                        nums.append(int(fittedprime))

    return set(nums)


print(sum([sum(ninerepeats(d)) for d in [1, 3, 4, 5, 6, 7, 9]] + [sum(eightrepeats(d)) for d in [0, 2, 8]]))

# d = 1, 3, 4, 5, 6, 7, 9 are nine repeating
# d = 0, 2, 8 are eight repeating
