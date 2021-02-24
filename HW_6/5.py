class Stationery :
    def __init__(self, title):
        self.title = title
    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки ручкой")

class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки карандашом")


pen = Pen("моя ручка")

pen.draw()

pencil = Pencil("мой карандаш")

pencil.draw()

