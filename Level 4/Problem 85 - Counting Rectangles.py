# Problem 85 - Counting Rectangles

from numpy import abs


def numrectangles(m, n):
    count = 0
    for a in range(1, m + 1):
        for b in range(1, n + 1):
            count += (m - a + 1) * (n - b + 1)
    return count


done = False
for i in range(1, 1000):
    for j in range(1, i + 1):
        if abs(numrectangles(i, j) - 2000000) < 10:  # Pretty close
            print(i * j)
            done = True
            break
    if done:
        break
