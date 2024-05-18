# Permuted Multiples

# The repeating digits of 1/7 (142857) have this property. I kinda just remembered that fact :P
# Here is some (inefficient) code anyway.

from common import permlist, tqdm

for i in tqdm(range(100000, 150000)):
    perm = permlist(list(str(i)))
    if all(str(j * i) in perm for j in range(1, 7)):
        print(i)
        break