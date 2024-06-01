# Problem 99 - Largest Exponential

import numpy as np

with open("0099_base_exp.txt", "r") as f:
    nums = [[int(i) for i in l.strip().split(",")] for l in f.readlines()]

maxline = 0
for line in range(1, len(nums)):
    base1 = nums[line][0]
    exp1 = nums[line][1]
    base2 = nums[maxline][0]
    exp2 = nums[maxline][1]
    if exp1 * np.log(base1) > exp2 * np.log(base2):
        maxline = line
print(maxline)