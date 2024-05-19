# Problem 45 - Triangular, Pentagonal, and Hexagonal

from common import pnumber, solvepnumber

nums = []
i = 2
while len(nums) < 2:
    Ti = pnumber(3, i)
    if (solvepnumber(6, Ti) + solvepnumber(5, Ti)) % 1 == 0:
        nums.append(Ti)
    i += 1
print(nums)