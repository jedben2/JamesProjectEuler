# Problem 79 - Passcode Derivation

# From observing the placement of digits, 7 is the first, 0 is the last and the middle consists of [1,2,3,6,8,9].

from common import tqdm, permlist

perms = ['7' + p + '0' for p in permlist([1, 2, 3, 6, 8, 9])]

with open("0079_keylog.txt", "r") as f:
    keys = [line.strip() for line in f.readlines()]

for k in tqdm(keys):
    for p in perms:
        if not (p.index(k[0]) < p.index(k[1]) and p.index(k[1]) < p.index(k[2])):
            perms.remove(p)
print(min(list(perms)))
