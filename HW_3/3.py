def my_func(a, b, c):
    """my_func() принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов"""

    if (a <= b) and (a <= c):
        return b + c
    elif (b <= a and b <= c):
        return a + c
    else:
        return  b + c

print(my_func(3, 5, 8))

