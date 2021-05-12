class ComplexNumbers:
    real: int
    imaginary: int

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        real: int
        imaginary: int
        real = self.real + other.real
        imaginary = self.imaginary + other.imaginary
        return real, imaginary

    def __mul__(self, other):
        result = ComplexNumbers(0, 0)
        result.real = (self.real * other.real) + (self.imaginary * -other.imaginary)
        result.imaginary = (self.real * other.imaginary) + (self.imaginary * other.real)
        return result

    def __str__(self):
        if self.imaginary == -1:
            return f"{self.real} -i"
        else:
            return f"{self.real} {self.imaginary}i"


a = ComplexNumbers(2, 3)
b = ComplexNumbers(-1, 1)
c = a * b
print(c)
