goods = [ \
(1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}), \
(2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}), \
(3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."}) ]

print(goods)


while True:

    print("1 - Добавить новый товар")
    print("2 - Сформировать словарь (пока не реализовано)")
    print("3 - Просто вывести на экран всю базу товаров")
    print("0 - Выход из программы")

    action = int(input("ВВедите действие: "))

    if action == 0:
        exit()

    elif action == 1:
        print("Добавляем новый товар в базу")
        new_name = input("Введите название товара: ")
        new_cost = int(input("Введите цену"))
        new_qt = int(input("Введите количество"))
        new_units = input("Введите единицы измерения")
        new_index = 0 #TODO
        new_dict = {"название": new_name, "цена": new_cost, "количество": new_qt, "eд": new_units}
        new_tuple = (new_index, new_dict)

        goods.append(new_tuple)

    elif action == 2:
        print()
        #TODO

    elif action == 3:
        print(goods)

