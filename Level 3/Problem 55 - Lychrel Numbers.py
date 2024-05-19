# Problem 55 - Lychrel Numbers
from common import islychrel, tqdm

count = 0
for n in tqdm(range(10000)):
    if not islychrel(n):
        count += 1
print(count)
