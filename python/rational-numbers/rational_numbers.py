import math


class Rational:
    def __init__(self, numer, denom):
        self._numer = numer
        self._denom = denom
        self._reduce_and_standardize()

    def __eq__(self, other):
        return (
            isinstance(other, Rational)
            and self._numer == other._numer
            and self._denom == other._denom
        )

    def __repr__(self):
        return f"{self._numer}/{self._denom}"

    def __add__(self, other):
        return Rational(
            self._numer * other._denom + self._denom * other._numer,
            self._denom * other._denom,
        )

    def __sub__(self, other):
        return Rational(
            self._numer * other._denom - self._denom * other._numer,
            self._denom * other._denom,
        )

    def __mul__(self, other):
        return Rational(self._numer * other._numer, self._denom * other._denom)

    def __truediv__(self, other):
        return Rational(self._numer * other._denom, other._numer * self._denom)

    def __abs__(self):
        return Rational(abs(self._numer), abs(self._denom))

    def __pow__(self, power):
        if isinstance(power, int) or (isinstance(power, float) and power.is_integer):
            if power >= 0:
                return Rational(self._numer**power, self._denom**power)
            return Rational(self._denom ** abs(power), self._numer ** abs(power))
        return self._numer**power / self._denom**power

    def __rpow__(self, base):
        return (base**self._numer) ** (1 / self._denom)

    def __hash__(self):
        return hash((self._numer, self._denom))

    def _reduce_and_standardize(self):
        gcd = math.gcd(self._numer, self._denom)
        self._numer //= gcd
        self._denom //= gcd
        if self._denom < 0:
            self._denom *= -1
            self._numer *= -1
