class Cell:
    def __init__(self, qt):
        self.qt = qt

    def __add__(self, other):
        return Cell(self.qt + other.qt)

    def __sub__(self, other):
        if self.qt > other.qt:
            return Cell(self.qt - other.qt)
        else:
            print("Ошибка")

    def __mul__(self, other):
        return Cell(self.qt * other.qt)

    def __truediv__(self, other):
        return Cell(round(self.qt / other.qt))

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.qt // rows)]) + '\n' + '*' * (self.qt % rows)

cell_1 = Cell(4)

cell_2 = Cell(3)

cell_3 = cell_1 + cell_2

cell_4 = cell_1 * cell_2

cell_5 = cell_1 - cell_2

cell_6 = cell_1 / cell_2

print(cell_4.make_order(5))