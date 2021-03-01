class Warehouse:
    def __init__(self,adress, capacity):
        self.adress = adress
        self.capacity = capacity
        self.equipment_list = []


    def adding_equirement(self, what, qty):
        if qty.isdigit():
            self.equipment_list.append({qty:what})
        else:
            print('Ошибка - введеное количество не является числом')

class OfficeEquipment:
    def __init__(self,name, mass, price):
        self.name = name
        self.mass = mass
        self.price = price

    def __str__(self):
        return self.name

class Printer(OfficeEquipment):
    def __init__(self, name, mass, price, is_color):
        OfficeEquipment.__init__(self, name, mass, price)
        self.is_color = is_color

class Computer(OfficeEquipment):
    def __init__(self, name, mass, price, performance):
        OfficeEquipment.__init__(self, name, mass, price)
        self.performance = performance


warehouse1 = Warehouse("Moscow", 12)

printer1 = Printer(name = 'HW', is_color=True, mass = 4, price = 200)

warehouse1.adding_equirement(printer1, qty = '4')

print(warehouse1.equipment_list)


