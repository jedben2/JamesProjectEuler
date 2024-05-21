# Problem 67 - Maximum Path Sum II

from common import maxtrianglesum

with open("0067_triangle.txt", "r") as f:
    triangle_temp = f.readlines()
    for i in range(len(triangle_temp)):
        triangle_temp[i] = triangle_temp[i].strip()
triangle = [[int(line[3 * i:3 * i + 2]) for i in range(index + 1)] for index, line in enumerate(triangle_temp)]

print(maxtrianglesum(triangle))
