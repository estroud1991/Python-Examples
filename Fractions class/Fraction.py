__author__ = 'tompkinsj'


class Fraction:

    def __init__(self, top, bottom=1):
        """ Constructor for MixedFraction.
        Initializes num and den after reducing top / bottom by their gcd.
        :param top: numerator
        :param bottom: denominator
        """
        g = self.gcd(top, bottom)
        self.num = top // g
        self.den = bottom // g

    @staticmethod
    def gcd(m, n):
        """ Euclid's Division Algorithm to find the greatest common denominator (gcd)
        of two integers.
        <http://people.uncw.edu/tompkinsj/133/proofs/quotientRemainderTheorem.htm>
        :param m: an int
        :param n: an int
        :return: the greatest common denominator of m and n
        """
        while m % n != 0:
            m, n = n, m % n
        return n

    def __str__(self):
        """ String representation of this fraction.
        :return: 'num / den'
        """
        return '{}/{}'.format(str(self.num), str(self.den))

    def __add__(self, other):
        """ Adds this fraction to the input parameter (also a Fraction or FixedFraction
        (possibly a MixedFraction). For the MixedFraction case,
        Fraction is moved to second operand so
        MixedFraction handles the addition (arithmetic promotion is required).
        :param other a Fraction, FixedFraction, or MixedFraction
        :return Fraction(n, d)
        """
        n = self.num * other.den + self.den * other.num
        d = self.den * other.den
        return Fraction(n, d)

    def __pow__(self, exp):
        """ Multiplies this fraction by itself exp times.
        :param exp: the exponent to be applied
        :return: Fraction(n, d) after exponentiation
        """
        n = self.num ** exp
        d = self.den ** exp
        return Fraction(n, d)
