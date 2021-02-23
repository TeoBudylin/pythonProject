class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def asphalt_mass(self, m_mass):
        return m_mass * self.__length * self.__width

road1 = Road(length = 2000, width = 10)

print(f"Необходимая масса асфальта - {road1.asphalt_mass(40)} кг")
