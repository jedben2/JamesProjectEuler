# Problem 66 - Diophantine Equation

# https://en.wikipedia.org/wiki/Pell's_equation

from common import tqdm, evalcontinuedfractionsqrt, periodcontinuedfractionsqrt
from gmpy2 import is_square

squares2 = [i ** 2 for i in range(32)]

maxsol = [0, 0]
for D in tqdm(range(1, 1001)):
    if is_square(D):
        pass
    else:
        period = periodcontinuedfractionsqrt(D)
        if period % 2 == 0:
            x = evalcontinuedfractionsqrt(D, period)[0]
        else:
            x = evalcontinuedfractionsqrt(D, 2 * period)[0]
        if x > maxsol[0]:
            maxsol = [x, D]
print(maxsol)