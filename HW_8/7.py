class ComplexType:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"{self.a}+{self.b}i"

    def __add__(self, other):
        return ComplexType(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexType(self.a * other.a - self.b * other.b, self.b * other.a + self.a * other.b)




complex1 = ComplexType(2, 3)
complex2 = ComplexType(4, 5)

print(complex1 + complex2)

print(complex1 * complex2)