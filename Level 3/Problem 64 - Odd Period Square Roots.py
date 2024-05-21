# Problem 64 - Odd Period Square Roots

# Had to deal with numbers in the form of [a,b,c] which represents (a sqrt(N) + b) / c due to errors with long decimals.

from common import continuedfractionsqrt, tqdm

nums = []
for N in tqdm(range(1, 10001)):
    if len(continuedfractionsqrt(N)) % 2 == 0:
        nums.append(N)
print(len(nums))
print(max(nums))
