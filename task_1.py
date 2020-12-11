class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __str__(self, mtrx):
        self.mtrx = mtrx
        return str(''.join([''.join([str(k) for k in i]) for i in self.mtrx]))

    def __add__(self):
        self.mtrx = [[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]
        for i in range(len(self.list_1)):
            for k in range(len(self.list_2[i])):
                self.mtrx[i][k] = self.list_1[i][k] + self.list_2[i][k]
        return str('\n'.join(['\t'.join([str(k) for k in i]) for i in self.mtrx]))


my_matr = Matrix([[12, 21, 3],
                  [11, 42, 53],
                  [5, 64, 50]],
                 [[7, 66, 73],
                  [36, 24, 16],
                  [77, 22, 15]])

print(my_matr.__add__())
