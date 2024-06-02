# Problem 104 - Pandigital Fibonacci Ends

from common import ispermutation, np

phi = (1 + np.sqrt(5)) / 2
logphi = np.log10(phi)
log5 = 0.5 * np.log10(5)


# F_n = phi^n / sqrt5 for large n, so use this for the first 9 digits

def fibfirst9(n):
    return int(np.power(10, n * logphi + 8 - log5 - np.floor(n * logphi - log5)))


a, b = 1, 1
k = 3
while True:
    a, b = (a + b) % 10 ** 9, a
    if ispermutation(a, 123456789):
        if ispermutation(fibfirst9(k), 123456789):
            print(k)
            break
    k += 1
