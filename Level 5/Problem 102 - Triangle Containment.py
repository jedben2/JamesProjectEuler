# Problem 102 - Triangle Containment

from common import dist, areatriangle, np

triangles = []
with open("0102_triangles.txt", "r") as f:
    for line in f.readlines():
        points = [int(i) for i in line.strip().split(",")]
        triangles.append([[points[2 * i], points[2 * i + 1]] for i in range(3)])

count = 0
for t in triangles:
    area = areatriangle(t[0], t[1], t[2])
    a1 = areatriangle(t[0], t[1], [0, 0])
    a2 = areatriangle(t[0], t[2], [0, 0])
    a3 = areatriangle(t[2], t[1], [0, 0])
    if np.isclose(a1 + a2 + a3, area):
        count += 1
print(count)
