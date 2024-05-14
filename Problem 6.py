def sum2(n):
    return n * (n + 1) * (2 * n + 1) / 6


def sum3(n):
    return (n * (n + 1) / 2) ** 2


print(sum3(100) - sum2(100))
