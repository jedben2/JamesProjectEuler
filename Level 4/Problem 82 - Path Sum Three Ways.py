# Problem 82 - Path Sum Three Ways

import numpy as np

with open("0082_matrix.txt", "r") as f:
    m = np.array([[int(i) for i in line.strip().split(',')] for line in f.readlines()])

# m = np.array([[131, 673, 234, 103, 18],[201, 96, 342, 965, 150],[630, 803, 746, 422, 111],[537, 699, 497, 121, 956],[805, 732, 524, 37, 331]])

n, k = m.shape

s = [m[i][0] for i in range(k)]

for col in range(1, k):
    s[0] += m[0][col]

    for row in range(1, n):  # work down looking at sums behind and above
        s[row] = min(s[row], s[row - 1]) + m[row, col]
    for row in range(n - 2, -1, -1):  # work up looking at sums behind and below (make sure to remove the addition from previous)
        s[row] = min(s[row] - m[row, col], s[row + 1]) + m[row, col]

print(min(s))
