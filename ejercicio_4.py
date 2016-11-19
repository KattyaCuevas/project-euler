largest = 0
for x in xrange(999,100,-1):
    for y in xrange(999,100,-1):
        r = x * y
        if str(r) == str(r)[::-1] and largest < r:
            largest = r

print largest
