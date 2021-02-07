def my_div_func(a, b):
    """this function divides a by b """
    if b == 0:
        print("division by 0 is forbidden ")
        exit(1)
    return a / b

a = int(input("Введите делимое: "))
b = int(input("Введите делитель: "))

c = my_div_func(a, b)

print(f"{a} / {b} = {c}")