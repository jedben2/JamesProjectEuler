# Problem 70 - Totient Permutation

# Since we want the minimal ratio, makes sense to look around the larger end of the inteval since limsup(n/phi(n)) = 1
# (yes this did run for 30 mins. this problem was a pain but it gave me an excuse to revise for an exam instead of doing this)

from common import eulerphi, ispermutation, tqdm, isprime

print("start")

minval = [12, 1]
for n in tqdm(range(8 * 10 ** 6, 10 ** 7)):
    if isprime(n):
        continue
    k = eulerphi(n)
    if ispermutation(n, k) and n * minval[1] < k * minval[0]:
        minval = [n, k]
        print(minval, n / k)
print(minval[0])
