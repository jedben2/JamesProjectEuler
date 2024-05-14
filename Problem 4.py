from common import ispalindrome

threedigit = [n for n in range(100, 1000)]
prods = []
for a in threedigit:
    for b in threedigit:
        c = a * b
        if ispalindrome(c): prods += [c]
print(max(prods))
