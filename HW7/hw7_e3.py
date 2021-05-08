class Cell:
    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return self.cells + other.cells

    def __sub__(self, other):
        if other.cells < self.cells:
            return self.cells - other.cells
        else:
            print('Invalid result. Cells can\'t be zero or less!')
            return None

    def __mul__(self, other):
        return self.cells * other.cells

    def __truediv__(self, other):
        return self.cells // other.cells

    def make_order(self, row):
        lines = self.cells // row
        line, rest = '', ''
        print('Cells order: ')
        for i in range(self.cells % row):
            rest += '*'
        for i in range(row):
            line += '*'
        for i in range(lines):
            print(line)
        print(rest)


cell1 = Cell(15)
cell2 = Cell(4)
print(f"{cell1+cell2}")
print(f"{cell1-cell2}")
print(f"{cell2-cell1}")
print(f"{cell1*cell2}")
print(f"{cell1/cell2}")
cell1.make_order(6)
