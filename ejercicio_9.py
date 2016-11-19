suma = 1000
for a in xrange(1, suma):
    for b in xrange(a + 1, suma):
        for c in xrange(b + 1, suma):
            if a + b + c == suma and a ** 2 + b ** 2 == c ** 2:
                print a * b * c
                break
