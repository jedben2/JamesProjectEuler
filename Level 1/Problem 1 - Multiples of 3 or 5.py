# Multiples of 3 or 5

s = sum([a for a in range(1000) if (a % 3 == 0 or a % 5 == 0)])
print(s)
