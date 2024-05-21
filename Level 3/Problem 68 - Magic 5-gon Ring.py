# Problem 68 - Magic 5-gon Ring

from common import permlist_list, tqdm

def sortlines(lines):
    externalnodes = [line[0] for line in lines]
    while externalnodes[0] != min(externalnodes):
        externalnodes = list(externalnodes[1:]) + [externalnodes[0]]
    sortedlines = []
    for node in externalnodes:
        for line in lines:
            if line[0] == node:
                sortedlines.append(line)
                break
    return sortedlines

def magicngonsol(n):
    sols = set()
    perms = permlist_list([i for i in tqdm(range(1, 2 * n + 1))])
    for perm in tqdm(perms):
        # print(perm)
        lines = [[0] * 3 for _ in range(n)]
        lines[0][0] = int(perm[0])
        lines[0][1] = int(perm[1])
        lines[0][2] = int(perm[2])
        j = 3
        for i in range(1, n - 1):
            lines[i][0] = int(perm[j])
            lines[i][1] = lines[i - 1][2]
            lines[i][2] = int(perm[j + 1])
            j += 2
        lines[-1][0] = int(perm[-1])
        lines[-1][1] = lines[-2][2]
        lines[-1][2] = lines[0][1]
        # print(lines)
        for s in range(13, 30):
            if all([sum(line) == s for line in lines]):
                lineconcat = ""
                for line2 in sortlines(lines):
                    lineconcat += ''.join([str(i) for i in line2])
                # print(lineconcat)
                sols.add(lineconcat)
    return sols

print(max([s for s in magicngonsol(5) if len(s) == 16]))