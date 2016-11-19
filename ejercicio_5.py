num = 20
def is_primo(n):
    for x in xrange(2, n / 2 + 1):
        if n % x == 0:
            return False
    return True

primos = [x for x in xrange(2, num + 1) if is_primo(x)]
print primos

i = 0
while i < len(primos):
    n = primos[i]
    while primos[i] * n <= num:
        primos[i] = primos[i] * n
    i += 1

print primos
print reduce(lambda a, b: a * b, primos)
