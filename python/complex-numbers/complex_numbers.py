import math


class ComplexNumber:
    def __init__(self, real, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__)
            and self.real == other.real
            and self.imaginary == other.imaginary
        )

    def __hash__(self) -> int:
        return hash((self.real, self.imaginary))

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(
                self.real + other.real, self.imaginary + other.imaginary
            )
        return self.__add__(ComplexNumber(other))

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(
                self.real * other.real - self.imaginary * other.imaginary,
                self.imaginary * other.real + self.real * other.imaginary,
            )
        return self.__mul__(ComplexNumber(other))

    def __rmul__(self, other):
        return self * other

    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(
                self.real - other.real, self.imaginary - other.imaginary
            )
        return self.__sub__(ComplexNumber(other))

    def __rsub__(self, other):
        return -self + other

    def __truediv__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(
                (self.real * other.real + self.imaginary * other.imaginary)
                / (other.real**2 + other.imaginary**2),
                (self.imaginary * other.real - self.real * other.imaginary)
                / (other.real**2 + other.imaginary**2),
            )
        return ComplexNumber(self.real / other, self.imaginary / other)

    def __rtruediv__(self, other):
        return (
            ComplexNumber(
                self.real / (self.real**2 + self.imaginary**2),
                -self.imaginary / (self.real**2 + self.imaginary**2),
            )
            * other
        )

    def __abs__(self):
        return math.sqrt(self.real**2 + self.imaginary**2)

    def __neg__(self):
        return ComplexNumber(-self.real, -self.imaginary)

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        return ComplexNumber(
            math.e**self.real * math.cos(self.imaginary),
            math.e**self.real * math.sin(self.imaginary),
        )
