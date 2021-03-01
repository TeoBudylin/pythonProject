class Worker:
    def __init__(self, name, surname, position , wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def fullname(self):
        return f"{self.name} {self.surname}"

    def total_income(self):
        return sum(self._income.values())

ivanov = Position(name="Ivan", surname="Ivanov", position="engineer", wage=100000, bonus= 50000)

print(f"Полное имя - {ivanov.fullname()}")

print(f"полный доход с учетом премии - {ivanov.total_income()} рублей")