# Problem 89 - Roman Numerals

# Deal with the if statements

def romantodec(numeral):
    l = list(numeral)
    n = 0
    i = 0
    while i < len(l):
        if l[i] == "M":
            n += 1000
            i += 1
        elif l[i] == "D":
            n += 500
            i += 1
        elif l[i] == "C":
            if i == len(l) - 1:
                n += 100
                i += 1
            elif l[i + 1] == "D":
                n += 400
                i += 2
            elif l[i + 1] == "M":
                n += 900
                i += 2
            else:
                n += 100
                i += 1
        elif l[i] == "L":
            n += 50
            i += 1
        elif l[i] == "X":
            if i == len(l) - 1:
                n += 10
                i += 1
            elif l[i + 1] == "L":
                n += 40
                i += 2
            elif l[i + 1] == "C":
                n += 90
                i += 2
            else:
                n += 10
                i += 1
        elif l[i] == "V":
            n += 5
            i += 1
        else:
            if i == len(l) - 1:
                n += 1
                i += 1
            elif l[i + 1] == "V":
                n += 4
                i += 2
            elif l[i + 1] == "X":
                n += 9
                i += 2
            else:
                n += 1
                i += 1
    return n


def dectoroman(n):
    numeral = ""
    if n >= 1000:
        numeral += "M" * (n // 1000)
        n -= 1000 * (n // 1000)
    if n >= 900:
        numeral += "CM"
        n -= 900
    if n >= 500:
        numeral += "D"
        n -= 500
    if n >= 400:
        numeral += "CD"
        n -= 400
    if n >= 100:
        numeral += "C" * (n // 100)
        n -= 100 * (n // 100)
    if n >= 90:
        numeral += "XC"
        n -= 90
    if n >= 50:
        numeral += "L"
        n -= 50
    if n >= 40:
        numeral += "XL"
        n -= 40
    if n >= 10:
        numeral += "X" * (n // 10)
        n -= 10 * (n // 10)
    if n >= 9:
        numeral += "IX"
        n -= 9
    if n >= 5:
        numeral += "V"
        n -= 5
    if n >= 4:
        numeral += "IV"
        n -= 4
    if n >= 1:
        numeral += "I" * n
        n -= n
    return numeral


with open("0089_roman.txt", "r") as f:
    numerals = [line.strip() for line in f.readlines()]

charssaved = 0
for numeral in numerals:
    charssaved += len(numeral) - len(dectoroman(romantodec(numeral)))
print(charssaved)
