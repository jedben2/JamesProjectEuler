# Problem 21 - Amicable Numbers

from common import sumdiv

amicables = set()
for a in range(1, 10000):
    b = sumdiv(a)
    if sumdiv(b) == a and b < 10000 and a != b:
        amicables.add(a)
print(sum(amicables))
