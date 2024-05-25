# Problem 81 - Path Sum Two Ways

# Similar to the triangle problems except i worked forward instead of backwards

import numpy as np

with open("0081_matrix.txt", "r") as f:
    m = np.array([[int(i) for i in line.strip().split(',')] for line in f.readlines()])

for i in range(1, 80):
    m[i, 0] += m[i - 1, 0]
    m[0, i] += m[0, i - 1]

for i in range(1, 80):
    for j in range(1, 80):
        m[i, j] += min(m[i - 1, j], m[i, j - 1])
print(m[-1, -1])
