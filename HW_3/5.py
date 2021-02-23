sum = 0
finish = 0
while True:
    str = (input("Введите строку из чисел, разделенных пробелами, для завершения введите END: "))
    splited_str = str.split()
    for el in splited_str:
        if (el == "END"):
            finish = 1
            break
        sum += int(el)
    print(f"сумма = {sum}")
    if finish == 1:
        exit()