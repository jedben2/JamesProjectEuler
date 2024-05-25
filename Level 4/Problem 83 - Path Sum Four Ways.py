# Problem 83 - Path Sum Four Ways

# https://en.wikipedia.org/wiki/Dijkstra's_algorithm

import numpy as np

with open("0083_matrix.txt", "r") as f:
    m = np.array([[int(i) for i in line.strip().split(',')] for line in f.readlines()])

# m = np.array([[131, 673, 234, 103, 18],
#               [201, 96, 342, 965, 150],
#               [630, 803, 746, 422, 111],
#               [537, 699, 497, 121, 956],
#               [805, 732, 524, 37, 331]])

unvisited = np.zeros(m.shape)  # 0 = unvisited, 1 = visited
distances = np.full(m.shape, 10 ** 6)  # 10 ** 6 = infinity
distances[0, 0] = 0

while not (unvisited == 1).all():
    unused_dists = [distances[i, j] for i in range(m.shape[0]) for j in range(m.shape[0]) if unvisited[i, j] == 0]
    mindist = min(unused_dists)
    coords = [(i, j) for i in range(m.shape[0]) for j in range(m.shape[0]) if unvisited[i, j] == 0]
    i, j = coords[unused_dists.index(mindist)]
    if unvisited[i, j] == 0 and distances[i, j] == mindist:
        neighbours_paths = [(i + x, j + y) for x in [-1, 0, 1] for y in [-1, 0, 1] if
                            0 <= i + x and 0 <= j + y and i + x < m.shape[0] and j + y < m.shape[
                                0] and x != y and x != -y]
        for neighbour in neighbours_paths:
            if unvisited[neighbour] == 0:
                newdist = distances[i, j] + m[neighbour]
                if distances[neighbour] > newdist:
                    distances[neighbour] = newdist
        unvisited[i, j] = 1

print(distances[-1, -1] + m[0, 0])
