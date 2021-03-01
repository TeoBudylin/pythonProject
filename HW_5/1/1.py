with open("text_1.txt", "w") as f:
    while True:
        new_str = input("Введите строку: ") + "\n"
        if new_str == "\n":
            break
        f.write(new_str)