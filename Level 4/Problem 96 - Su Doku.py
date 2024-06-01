# Problem 96 - Su Doku

import numpy as np
import copy
from tqdm import tqdm

grids = []
with open("p096_sudoku.txt", "r") as f:
    file = f.readlines()
    for i in range(0, 50):
        grid = np.array([[int(i) for i in list(line.strip())] for line in file[10 * i + 1: 10 * i + 10]])
        grids.append(grid)


def valid(grid):
    for row in grid:
        count = [0] * 9
        for i in row:
            if i != 0:
                count[i - 1] += 1
        if any(count[i] > 1 for i in range(9)):
            return False
    for col in grid.transpose():
        count = [0] * 9
        for i in col:
            if i != 0:
                count[i - 1] += 1
        if any(count[i] > 1 for i in range(9)):
            return False
    for i in range(3):
        for j in range(3):
            box = grid[3 * i: 3 * i + 3, 3 * j: 3 * j + 3]
            boxvals = [l[k] for k in range(3) for l in box]
            count = [0] * 9
            for k in boxvals:
                if k != 0:
                    count[k - 1] += 1
            if any(count[k] > 1 for k in range(9)):
                return False
    return True


def solve(grid):
    solvedgrid = copy.copy(grid)
    # Deduction
    solved = False
    while not solved:
        rebegin = False
        for i in range(9):
            for j in range(9):
                if solvedgrid[i, j] == 0:
                    rowvals = [k for k in solvedgrid[i] if k != 0]
                    colvals = [k for k in solvedgrid[:, j] if k != 0]
                    box = solvedgrid[3 * (i // 3): 3 * (i // 3) + 3, 3 * (j // 3): 3 * (j // 3) + 3]
                    boxvals = [l[k] for k in range(3) for l in box if l[k] != 0]
                    vacant = set(range(1, 10)).difference(set(rowvals).union(set(colvals).union(set(boxvals))))
                    if len(vacant) == 1:
                        solvedgrid[i, j] = list(vacant)[0]
                        rebegin = True
                        break
            if rebegin:
                break
        if all([solvedgrid[i, j] != 0 for i in range(9) for j in range(9)]):
            return solvedgrid
        if rebegin == False:
            break

    # Backtracking method
    i = 0
    j = 0
    backtrackgrid = copy.copy(solvedgrid)
    reverse = False
    while not solved:
        if solvedgrid[i, j] == 0:
            backtrackgrid[i, j] += 1
            if backtrackgrid[i, j] > 9:
                reverse = True
                backtrackgrid[i, j] = 0
                j -= 1
                if j < 0:
                    i -= 1
                    j = 8
                if i < 0:
                    return "fail"
            elif not valid(backtrackgrid):
                continue
            else:
                reverse = False
                j += 1
                if j == 9:
                    j = 0
                    i += 1
                if i == 9:
                    return backtrackgrid
        elif reverse == True:
            j -= 1
            if j < 0:
                i -= 1
                j = 8
            if i < 0:
                return "fail"
        else:
            j += 1
            if j == 9:
                j = 0
                i += 1
            if i == 9:
                return backtrackgrid

    return backtrackgrid


s = 0
for grid in tqdm(grids):
    solvedgrid = solve(grid)
    s += 100 * solvedgrid[0, 0] + 10 * solvedgrid[0, 1] + solvedgrid[0, 2]
print(s)
