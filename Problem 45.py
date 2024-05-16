from common import sum1, solvepentagonal, solvehexagonal

nums = []
i = 2
while len(nums) < 2:
    Ti = sum1(i)
    if (solvehexagonal(Ti) + solvepentagonal(Ti)) % 1 == 0:
        nums.append(Ti)
    i += 1
print(nums)