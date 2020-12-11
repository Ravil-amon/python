class Cell:
    def __init__(self, cellcell):
        self.cellcell = int(cellcell)

    def __str__(self):
        return f'{self.cellcell}'

    def __add__(self, other):
        return Cell(self.cellcell + other.cellcell)

    def __sub__(self, other):
        return Cell(int(self.cellcell - other.cellcell))

    def __mul__(self, other):
        return Cell(int(self.cellcell * other.cellcell))

    def __truediv__(self, other):
        return Cell(int(self.cellcell // other.cellcell))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.cellcell / cells_in_row)):
            row += f'{"*" * cells_in_row}\\n'
        row += f'{"*" * (self.cellcell % cells_in_row)}'
        return row


cel1 = Cell(43)
cel2 = Cell(11)
print(cel1 + cel2)
print(cel1 - cel2)
print(cel1 * cel2)
print(cel1 / cel2)
print(cel1.make_order(5))
print(cel2.make_order(3))
