from itertools import product
from tqdm import tqdm
from fractions import Fraction


nums = []
for a, b in tqdm(product([i for i in range(1,10)], repeat=2)):
    if a != b and a / b < 1:
        for c in range(1, 10):
            if int(str(a)+str(c)) * b == int(str(b) + str(c)) * a or int(str(c)+str(a)) * b == int(str(b) + str(c)) * a or int(str(a)+str(c)) * b == int(str(c) + str(b)) * a or int(str(c)+str(a)) * b == int(str(c) + str(a)) * a:
                nums.append(a/b)

print(nums)     # [0.25, 0.2, 0.4, 0.5] then the product is 1/100
