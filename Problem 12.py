from common import sum1, factors

n = 1
while len(factors(sum1(n))) < 501:
    n += 1
print(sum1(n))

