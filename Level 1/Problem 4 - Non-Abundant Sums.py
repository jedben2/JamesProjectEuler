# Non-Abundant Sums

from common import sumdiv, sum1

abundant = [s for s in range(28124) if sumdiv(s) > s]
sums = [a + b for a in abundant for b in abundant]
sums_restrict = set([s for s in sums if s < 28124])
print(sum1(max(sums_restrict)) - sum(sums_restrict))
