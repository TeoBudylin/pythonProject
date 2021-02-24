class Matrix:
    def __init__(self, array_of_array):
        self.matrix = array_of_array

    def __str__(self):
        string = ""
        for line in self.matrix:
            string += (f"{str(line)}\n")
        return string

    def __add__(self, other):
        result = []
        for i in range(0, len(self.matrix)):
            result.append([])
            for j in range(0, len(self.matrix[0])):
              result[i].append(self.matrix[i][j] + other.matrix[i][j])
        matrix_sum = Matrix(result)
        return matrix_sum


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

matrix_2 = Matrix([[10, 11, 12], [13, 14, 15], [16, 17, 18]])

print(matrix_1)
print(matrix_2)

print(matrix_1 + matrix_2)


