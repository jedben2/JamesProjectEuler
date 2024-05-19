# Problem 65 - Convergents of e

from common import gcd, digitsum


def convergente(n):   # returns numerator and denominator of the nth convergent of e
    e = [2] + [2 * (i + 1) // 3 if (i + 1) / 3 % 1 == 0 else 1 for i in range(1, n)]
    a = e[-1]
    b = 1
    for d in e[-2:0:-1]:
        g = gcd(b, b * d + a)
        a, b = b // g, (b * d + a) // g
    return a + 2 * b, b


print(digitsum(convergente(100)[0]))
