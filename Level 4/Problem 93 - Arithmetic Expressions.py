# Problem 93 - Arithmetic Expressions

from itertools import product
from tqdm import tqdm

operations = ["+", "-", "/", "*"]
formats = ["a1b2c3d", "a1(b2c3d)", "a1b2(c3d)", "(a1b)2(c3d)", "a1(b2(c3d))", "a1(b2c)3d", "(a1b)2c3d"]


def operationsintegers(digits):
    evals = set()
    for a, b, c, d in product(digits, repeat=4):
        if len(set([a, b, c, d])) == 4:
            for o1, o2, o3 in product(operations, repeat=3):
                for f in formats:
                    expr = f.replace("1", o1).replace("2", o2).replace("3", o3).replace("a", a).replace("b", b).replace(
                        "c", c).replace("d", d)
                    try:
                        evals.add(eval(expr))
                    except:
                        pass
    ints = []
    for e in evals:
        if e % 1 == 0 and e > 0:
            ints.append(int(e))
    return sorted(ints)


longestchain = [0, 0]
for a in tqdm(range(1, 7)):
    for b in range(a, 8):
        for c in range(b, 9):
            for d in range(c, 10):
                if a != b and b != c and c != d:
                    l = operationsintegers([str(i) for i in [a, b, c, d]])
                    if 1 in l:
                        i = 1
                        while True:
                            if i + 1 in l:
                                i += 1
                            else:
                                if i > longestchain[1]:
                                    longestchain = [f"{a}{b}{c}{d}", i]
                                break
print(longestchain)
