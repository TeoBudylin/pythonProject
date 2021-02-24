# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна,
# лето, осень). Напишите решения через list и через dict.

month_num = int(input("Введите номер месяца: "))

if (month_num > 12) or (month_num < 1):
    print("неправильный номер месяца")
    exit()

my_list = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "cентябрь", "октябрь", "нояборь", "декабрь"]


print(f"Месяц номер {month_num} - это {my_list[month_num - 1]}")


my_dict = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", \
           10:"October", 11:"November", 12:"December"}


# print(my_dict)

print(f"Month #{month_num} is {my_dict[month_num]}")