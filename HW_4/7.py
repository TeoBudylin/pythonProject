from itertools import count

def fact(n):
    f = 1
    if n == 0:
        return 1
    for i in range(1, n + 1):
        f *= i
    return f

def fact_gen():
    for el in count(1):
        yield fact(el)

generator = fact_gen()

num = 0
for i in generator:
    if num == 10:
        break
    else:
        num += 1
        print(i)