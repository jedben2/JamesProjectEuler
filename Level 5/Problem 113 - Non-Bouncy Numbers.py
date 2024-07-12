# Problem 113 - Non-Bouncy Numbers

def isbouncy(n):
    digits = [int(i) for i in list(str(n))]
    return not (all(digits[i] <= digits[i + 1] for i in range(len(digits) - 1)) or all(
        digits[i - 1] >= digits[i] for i in range(1, len(digits))))

# needs thinking doing