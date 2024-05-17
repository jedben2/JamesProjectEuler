from common import primefactors, tqdm

nums = [i for i in range(2, 1000000)]
k = 4
for i in tqdm(range(0, len(nums))):
    if all(len(set(primefactors(nums[j]))) == k for j in range(i, i+k)):
        print(nums[i:i+k])
        break