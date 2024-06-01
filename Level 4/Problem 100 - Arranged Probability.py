# Problem 100 - Arranged Probability

# https://www.alpertron.com.ar/QUAD.HTM

Tmin = 10 ** 12
T = 21
b = 15
while T < Tmin:
    b, T = 3 * b + 2 * T - 2, 4 * b + 3 * T - 3
print(b)
