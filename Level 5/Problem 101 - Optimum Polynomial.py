# Problem 101 - Optimum Polynomial

# Numbers decided to not be integers so we split it up

def u(n):
    return sum((-n) ** k for k in range(11))


def OP(k, n):
    pnum = 0
    pdenom = 1
    vals = [u(i) for i in range(1, k + 1)]
    for i in range(1, k + 1):
        prodnum, proddenom = 1, 1
        for j in range(1, k + 1):
            if i != j:
                prodnum *= (n - j)
                proddenom *= (i - j)
        prodnum *= vals[i - 1]
        pnum = prodnum * pdenom + pnum * proddenom
        pdenom *= proddenom

    return pnum, pdenom


print(sum([OP(k, k + 1)[0] // OP(k, k + 1)[1] for k in range(1, 11)]))
