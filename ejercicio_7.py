num = 10001
def is_primo(n):
    for x in xrange(2, n / 2 + 1):
        if n % x == 0:
            return False
    return True
primos = []
i = 1
while len(primos) < num:
    i += 1
    if is_primo(i):
        primos.append(i)

print primos[-1]
