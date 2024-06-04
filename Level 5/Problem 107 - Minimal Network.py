# Problem 107 - Minimal Network

# https://en.wikipedia.org/wiki/Bor%C5%AFvka%27s_algorithm#Example and Minimal Spanning Trees

import numpy as np
from itertools import product

with open("0107_network.txt", "r") as f:
    network = np.array([[int(i) for i in line.strip().replace('-', '0').split(",")] for line in f.readlines()])


# network = np.array([[0, 16, 12, 21, 0, 0, 0],
#                     [16, 0, 0, 17, 20, 0, 0],
#                     [12, 0, 0, 28, 0, 31, 0],
#                     [21, 17, 28, 0, 18, 19, 23],
#                     [0, 20, 0, 18, 0, 0, 11],
#                     [0, 0, 31, 19, 0, 0, 27],
#                     [0, 0, 0, 23, 11, 27, 0]])


def preference(e1, e2):
    return e2 == 0 or e1 <= e2


def finditem(i, l):
    for j in range(len(l)):
        if i in l[j]:
            return j
    return None


def findconnectedcomponents(F):
    connectedcomps = []
    for i in range(F.shape[0]):
        if all(i not in comp for comp in connectedcomps):
            component = [i]
            newcomps = None
            while newcomps != []:
                newcomps = []
                for j in component:
                    edges = F[:, j]
                    for k in range(len(edges)):
                        if edges[k] != 0 and k not in component and k not in newcomps:
                            newcomps.append(k)
                component += newcomps

            connectedcomps.append(component)
    return connectedcomps


def minimaltree(network):
    minimalnetwork = np.full(network.shape, 0)
    running = True
    while running:
        connectedcomponents = findconnectedcomponents(minimalnetwork + minimalnetwork.transpose())
        cheapestedges = [[0]] * len(connectedcomponents)
        for i, j in product(range(network.shape[0]), repeat=2):
            if network[i, j] != 0 and len(set(connectedcomponents[finditem(i, connectedcomponents)]).intersection(
                    set(connectedcomponents[finditem(j, connectedcomponents)]))) == 0:
                weight = network[i, j]
                edgesi = cheapestedges[finditem(i, connectedcomponents)][0]
                if preference(weight, edgesi):
                    cheapestedges[finditem(i, connectedcomponents)] = [weight, i, j]
                edgesj = cheapestedges[finditem(j, connectedcomponents)][0]
                if preference(weight, edgesj):
                    cheapestedges[finditem(j, connectedcomponents)] = [weight, i, j]
        if cheapestedges == [[0]] * len(connectedcomponents):
            running = False
        else:
            for edge in cheapestedges:
                if edge != [0]:
                    minimalnetwork[edge[1], edge[2]] = edge[0]
    return minimalnetwork + minimalnetwork.transpose()


print(np.sum(np.concatenate(network)) // 2 - np.sum(np.concatenate(minimaltree(network))) // 2)
