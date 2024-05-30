# Problem 92 - Square Digit Chains

from common import digitpowersum, tqdm

count = 0
for n in tqdm(range(1, 10 ** 7)):
    s = n
    while s != 1:
        s = digitpowersum(s, 2)
        if s == 89:
            count += 1
            break
print(count)