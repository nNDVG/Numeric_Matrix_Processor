class Matrix:

    def __init__(self):
        self.size_1 = []
        self.matrix_1 = []
        self.size_2 = []
        self.matrix_2 = []

    def main(self):
        print(f'1. Add matrices\n'
              f'2. Multiply matrix by a constant\n'
              f'3. Multiply matrices\n'
              f'4. Transpose matrix\n'
              f'5. Calculate a determinant\n'
              f'6. Inverse matrix\n'
              f'0. Exit')
        act = int(input('Your choice:'))
        self.check_act(act)

    def check_act(self, act):
        if act == 1:
            self.create_conditions(act)
            self.show(self.add_matrices())
        elif act == 2:
            self.create_conditions(act)
            number = float(input('Enter constant:'))
            self.show(self.multi_num(number))
        elif act == 3:
            self.create_conditions(act)
            self.show(self.multi_matrix())
        elif act == 4:
            self.show(self.transpose())
        elif act == 5:
            self.create_conditions(act)
            self.show(self.get_deternminant())
        elif act == 6:
            self.create_conditions(act)
            self.show(self.get_inverse())
        else:
            exit()
        return self.main()

    def create_conditions(self, act):
        if act == 1 or act == 3:
            self.size_1 = [int(x) for x in input('Enter size of first matrix:').split()]
            print('Enter first matrix:')
            self.matrix_1 = [[float(i) for i in input().split()] for x in range(self.size_1[0])]
            self.size_2 = [int(x) for x in input('Enter size of second  matrix:').split()]
            print('Enter second matrix:')
            self.matrix_2 = [[float(i) for i in input().split()] for x in range(self.size_2[0])]
        else:
            self.size_1 = [int(x) for x in input('Enter size of matrix:').split()]
            print('Enter matrix:')
            self.matrix_1 = [[float(i) for i in input().split()] for x in range(self.size_1[0])]

    def add_matrices(self):
        if self.size_1[0] == self.size_2[0] and self.size_1[1] == self.size_2[1]:
            sum_matrix = []
            for i in range(self.size_1[0]):
                sum_row = list(map(lambda x, y: x + y, self.matrix_1[i], self.matrix_2[i]))
                sum_matrix.append(sum_row)
            return sum_matrix
        else:
            print('The operation cannot be performed.\n')
            return self.main()

    def multi_num(self, number):
        matrix = []
        for row in self.matrix_1:
            new_row = list(map(lambda x: x * number, row))
            matrix.append(new_row)
        return matrix

    def multi_matrix(self):
        if self.size_1[1] == self.size_2[0]:
            result = [[sum(a * b for a, b in zip(A_row, B_col))
                       for B_col in zip(*self.matrix_2)]
                      for A_row in self.matrix_1]
            return result
        else:
            print('The operation cannot be performed.\n')
            return self.main()

    def transpose(self):
        print(f'1. Main diagonal\n'
              f'2. Side diagonal\n'
              f'3. Vertical line\n'
              f'4. Horizontal line')
        act = int(input('Your choice:'))
        self.create_conditions(4)
        if act == 1:
            return [[self.matrix_1[i][j]for i in range(self.size_1[0])] for j in range(self.size_1[1])]
        if act == 2:
            return [[self.matrix_1[i][j]for i in range(self.size_1[0] - 1, -1, -1)] for j in range(self.size_1[1] - 1, -1, -1)]
        if act == 3:
            return [el[::-1] for el in self.matrix_1]
        if act == 4:
            return [el for el in self.matrix_1[::-1]]

    @staticmethod
    def get_minor(matrix, i, j):
        return [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]

    def get_deternminant(self, passed_matrix=None):
        if passed_matrix is None:
            matrix = self.matrix_1
        else:
            matrix = passed_matrix
        if len(matrix) == 1:
            return matrix[0][0]
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        determinant = 0
        for c in range(len(matrix)):
            determinant += ((-1) ** c) * matrix[0][c] * self.get_deternminant(self.get_minor(matrix, 0, c))
        return determinant

    def get_inverse(self):
        if self.size_1[0] <= 2:
            print("This matrix doesn't have an inverse.\n")
            return self.main()
        determinant = self.get_deternminant()
        if len(self.matrix_1) == 2:
            return [[self.matrix_1[1][1] / determinant, -1 * self.matrix_1[0][1] / determinant],
                    [-1 * self.matrix_1[1][0] / determinant, self.matrix_1[0][0] / determinant]]
        cofactors = []
        for r in range(len(self.matrix_1)):
            cofactorRow = []
            for c in range(len(self.matrix_1)):
                minor = self.get_minor(self.matrix_1, r, c)
                cofactorRow.append(((-1) ** (r + c)) * self.get_deternminant(minor))
            cofactors.append(cofactorRow)
        cofactors = [[cofactors[i][j]for i in range(len(cofactors))] for j in range(len(cofactors[0]))]
        for r in range(len(cofactors)):
            for c in range(len(cofactors)):
                if cofactors[r][c] != 0:
                    cofactors[r][c] = round(cofactors[r][c] / determinant, 4)
                else: cofactors[r][c] = 0
        return cofactors

    @staticmethod
    def show(obj):
        print('The result is:')
        if isinstance(obj, list):
            for x in obj:
                print(*x)
        else:
            print(obj)
        print('')

if __name__ == '__main__':
  m = Matrix()
  m.main()
