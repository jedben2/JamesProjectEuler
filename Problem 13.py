import numpy as np

with open("p13nums.txt", "r") as f:
    nums_temp = f.readlines()
nums = np.array([int(line.strip()) for line in nums_temp])
print(str(sum(nums))[:10])