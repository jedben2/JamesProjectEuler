# Problem 63 - Powerful Digit Counts

# if b^n has n digits, then 1 <= b <= 9 because 10^n has n+1 digits.

count = 0
for n in range(23):
    for i in range(1, 10):
        if len(str(i ** n)) == n:
            count += 1
print(count)
