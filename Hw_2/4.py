# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки
# необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

str = input("Введите строку: ")

splited_str = str.split()

i = 1
for el in splited_str:
    print(f"{i}: {el[:10]}")
    i+=1