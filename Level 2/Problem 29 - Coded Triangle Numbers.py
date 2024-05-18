# Coded Triangle Numbers

from common import sum1
from string import ascii_uppercase

with open("0042_words.txt", "r") as f:
    words = f.read()[1:-1].split('","')

trianglenums = [sum1(i) for i in range(1, 100)]

count = 0
for word in words:
    s = 0
    for char in word:
        s += ascii_uppercase.index(char) + 1
    if s in trianglenums:
        count += 1
print(count)
