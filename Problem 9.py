import numpy as np

prod = 1
for c in range(1000):
    for b in range(1000):
        if np.power(1000 - b - c, 2) + np.power(b, 2) == np.power(c, 2):
            print((1000 - b - c) * b * c)
            break
    else:
        continue
    break