# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().

my_list = []

while (True):
    new_el = input('Enter new element, for finish type finish: ')
    if new_el != "finish":
        my_list.append(new_el)
    else:
        break
zip
print(my_list)

i = 0
while (i < len(my_list) - 1):
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
    i += 2

print(my_list)