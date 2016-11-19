
num = 2000000
array = range(2, num + 1)
n = 2
x = 1
i = 1
while n < array[-1]:
    print 'n', n
    while i < len(array):
        if array[i] % n == 0:
            array.remove(array[i])
        else:
            i += 1
    n = array[x]
    x += 1
    i = x
# print array
print reduce(lambda a, b: a + b, array)
