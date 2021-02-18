sum = 0

with open("5.txt", "w+") as f:
    f.write(input("Введите числа, разделенные пробелами: "))
    f.seek(0)
    str = f.readline()
    words = str.split()
    for word in words:
        sum += int(word)

print(f"сумма = {sum}")