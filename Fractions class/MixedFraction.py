from Fraction import Fraction
__author__ = 'tompkinsj'


class MixedFraction (Fraction):

    def __init__(self, top, bottom=1):
        """ Initializes num and den after reducing top / bottom
        by their gcd by invoking super.
        
        Adds fields whole and n, initialized to 0.
        If num > den, assigns the quotient to whole and the remainder to n.
        :param top: numerator
        :param bottom: denominator
        """
        super().__init__(top, bottom)
        self.whole = 0
        self.n = 0
        if self.num >= self.den:
            self.whole = self.num // self.den
            self.n = self.num % self.den

    def __str__(self):
        """ String representation of this fraction.

        Empty strings are used in place of 0.
        :return: whole num / den :: num / den :: whole
        """
        if self.whole == 0:
            return super().__str__()
        elif self.n == 0:
            return str(self.whole)
        return '{} {}/{}'.format(str(self.whole), str(self.n), str(self.den))

    def __add__(self, other):
        """ Adds this fraction to the input parameter (also a
        Fraction (possibly a MixedFraction).
        
        :param other Fraction or MixedFraction
        :return MixedFraction(n, d)
        """
        n = self.num * other.den + self.den * other.num
        d = self.den * other.den
        return MixedFraction(n, d)

    def __sub__(self, other):
        """ Subtracts the input parameter (also a
        Fraction (possibly a MixedFraction) from this fraction.
        
        :param other Fraction or MixedFraction
        :return MixedFraction(n, d)
        """
        n = self.num * other.den - self.den * other.num
        d = self.den * other.den
        return MixedFraction(n, d)

    def __pow__(self, exp):
        """ Multiplies this fraction by itself exp times.

        :param exp: the exponent to be applied
        :return: MixedFraction(n, d) after exponentiation
        """
        f = super().__pow__(exp)
        return MixedFraction(f.num, f.den)


def main():
    f0 = MixedFraction(18, 9)
    f1 = MixedFraction(12, 3)
    f2 = MixedFraction(4, 2)
    print(f0, '+', f1, '+', f2, '=', f0 + f1 + f2)
    f0 = MixedFraction(10, 9)
    f1 = MixedFraction(4, 3)
    f2 = MixedFraction(3, 2)
    print(f0, '+', f1, '+', f2, '=', f0 + f1 + f2)
    f3 = f1 ** 3
    print('({})**3 = {}'.format(f1, f3))
    print('({})**3 = {}'.format(f2, f2 ** 3))
    f5 = Fraction(2, 9)
    print(f1, '+', f5, '=', f1 + f5)

    print(f5, '+', f1, '+', f0, '=', f5 + f1 + f0)

    print(f0, '+', f1, '+', f5, '=', f0 + f1 + f5)


if __name__ == '__main__':
    main()
