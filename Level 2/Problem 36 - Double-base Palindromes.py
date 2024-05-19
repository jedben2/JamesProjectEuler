# Problem 36 - Double-base Palindromes

from common import ispalindrome

nums = []
for i in range(1, 1000000):
    if ispalindrome(i) and ispalindrome(int(str(bin(i))[2:])):
        nums.append(i)
print(sum(nums))
