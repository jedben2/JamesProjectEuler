# Champernowne's Constant

champerdown = ''.join([str(i) for i in range(1, 1000000)])

prod = 1
for i in range(0, 7):
    prod *= int(champerdown[10 ** i - 1])
print(prod)