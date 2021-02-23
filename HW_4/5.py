from functools import reduce

my_list = [el for el in list(range(100, 1000)) if el % 2 == 0]

def mul(a, b):
    return a * b

print(reduce(mul, my_list))