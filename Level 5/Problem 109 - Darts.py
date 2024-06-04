# Problem 109 - Darts

def numfinishes(n):
    count = 0
    ways = []
    if n == 50 or (n <= 40 and n % 2 == 0 and n > 0):
        count += 1
        ways.append(f'D{n // 2}')
    for i in list(range(1, 21)) + [25]:
        k = n - i
        if k == 50 or (k <= 40 and k % 2 == 0 and k > 0):
            ways.append(f"S{i} D{k // 2}")
            count += 1
        if i != 25:
            k = n - 3 * i
            if k == 50 or (k <= 40 and k % 2 == 0 and k > 0):
                ways.append(f"T{i} D{k // 2}")
                count += 1
        k = n - 2 * i
        if k == 50 or (k <= 40 and k % 2 == 0 and k > 0):
            ways.append(f"D{i} D{k // 2}")
            count += 1
    for i in list(range(1, 21)) + [25]:
        for j in list(range(1, 21)) + [25]:
            k = n - i - j
            if k == 50 or (k <= 40 and k % 2 == 0 and k > 0):
                if f'S{min(i, j)} S{max(i, j)} D{k // 2}' not in ways:
                    count += 1
                    ways.append(f'S{i} S{j} D{k // 2}')
            if j != 25:
                k = n - i - 3 * j
                if k == 50 or (k <= 40 and k % 2 == 0 and k > 0):
                    if f'S{i} T{j} D{k // 2}' not in ways:
                        count += 1
                        ways.append(f'S{i} T{j} D{k // 2}')
            if j != 25 and i != 25:
                k = n - 3 * i - 3 * j
                if k == 50 or (k <= 40 and k % 2 == 0 and k > 0):
                    if f'T{min(i, j)} T{max(i, j)} D{k // 2}' not in ways:
                        count += 1
                        ways.append(f'T{i} T{j} D{k // 2}')
            k = n - i - 2 * j
            if k == 50 or (k <= 40 and k % 2 == 0 and k > 0):
                if f'S{i} D{j} D{k // 2}' not in ways:
                    count += 1
                    ways.append(f'S{i} D{j} D{k // 2}')
            k = n - 2 * i - 2 * j
            if k == 50 or (k <= 40 and k % 2 == 0 and k > 0):
                if f'D{min(i, j)} D{max(i, j)} D{k // 2}' not in ways:
                    count += 1
                    ways.append(f'D{min(i, j)} D{max(i, j)} D{k // 2}')
            if i != 25:
                k = n - 3 * i - 2 * j
                if k == 50 or (k <= 40 and k % 2 == 0 and k > 0):
                    if f'T{i} D{j} D{k // 2}' not in ways:
                        count += 1
                        ways.append(f'T{i} D{j} D{k // 2}')
    return count


print(sum(numfinishes(n) for n in range(1, 100)))
