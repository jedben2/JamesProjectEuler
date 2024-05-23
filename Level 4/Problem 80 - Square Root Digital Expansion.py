# Problem 80 - Square Root Digital Expansion

from decimal import *
from gmpy2 import is_square

getcontext().prec = 101

s = 0
for i in range(1, 101):
    if not is_square(i):
        s += sum([int(j) for j in str(Decimal(i).sqrt()).replace('.', '')[0:100]])
print(s - 1)
