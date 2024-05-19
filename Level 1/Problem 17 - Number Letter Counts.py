# Problem 17 - Number Letter Counts

import num2words

count = 0
for i in range(1, 1001):
    count += len(list(num2words.num2words(i).replace(' ', '').replace('-',"")))
print(count)