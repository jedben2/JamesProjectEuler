# Problem 2 - Even Fibonacci Numbers

from common import fib

n = 0
s = 0
while fib(n) <= 4000000:
    if fib(n) % 2 == 0:
        s += fib(n)
    n += 1
print(s)
