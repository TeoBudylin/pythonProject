def int_func(word):
    """this func receive word and return it with First Capital Letter"""
    return word.title()



my_str = input("Введите строку: ")
my_str = my_str.split()
title_str = ""
for el in my_str:
    title_str = title_str + " " + int_func(el)

print(title_str)