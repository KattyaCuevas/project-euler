num = 100
sum_1 = reduce(lambda a, b: a + b ** 2, range(1, num + 1))
sum_2 = reduce(lambda a, b: a + b, range(1, num + 1)) ** 2
print sum_2 - sum_1
