# Problem 112 - Bouncy Numbers

def isbouncy(n):
    digits = [int(i) for i in list(str(n))]
    return not (all(digits[i] <= digits[i + 1] for i in range(len(digits) - 1)) or all(
        digits[i - 1] >= digits[i] for i in range(1, len(digits))))


numbouncy = 0
n = 100
while numbouncy * 100 != 99 * n:
    n += 1
    if isbouncy(n):
        numbouncy += 1
print(n)