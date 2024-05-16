from common import permlist
from tqdm import tqdm

pandigitals = permlist([i for i in range(1, 10)])

nums = []
for num in tqdm(pandigitals):
    if eval(f"{num[:1]} * {num[1:5]} == {num[5:]}") or eval(f"{num[:2]} * {num[2:5]} == {num[5:]}"):
        nums.append(int(num[5:]))
print(sum(set(nums)))
