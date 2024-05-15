def fibdigitlen(n):
    phi = (1 + np.sqrt(5)) / 2
    return n * np.log10(phi) - 0.5 * np.log10(5) + 1


i = 1
while fibdigitlen(i) < 1000:
    i += 1
print(i)
