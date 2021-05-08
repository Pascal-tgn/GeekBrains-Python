import re


class Matrix:
    def __init__(self, *matrix):
        self.matrix = list(matrix)

    def __str__(self):
        str_matrix = str(self.matrix)
        str_matrix = re.sub('\[|\]]|]$|,', '', str_matrix)
        str_matrix = re.sub(']\s', '\n', str_matrix)
        return f"\n{str_matrix}\n"

    def __add__(self, other):
        result_matrix, result_row = [], []
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[x])):
                result_row.append(self.matrix[x][y] + other.matrix[x][y])
            result_matrix.append(result_row)
            result_row = []
        return Matrix(result_matrix)


matrix1 = Matrix([2, 6, 8],
                 [2, 7, 1],
                 [3, 5, 5])

matrix2 = Matrix([1, 1, 1],
                 [2, 2, 2],
                 [3, 3, 3])
matrix3 = matrix1 + matrix2
print(f"Matrix1: {matrix1}")
print(f"Matrix2: {matrix2}")
print(f"Sum of Matrix1 and Matrix2: {matrix3}")
