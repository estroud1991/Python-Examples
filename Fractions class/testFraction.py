from Fraction import Fraction
from MixedFraction import MixedFraction
__author__ = 'tompkinsj'


def main():
    fractList = []
    fractFile = open('Fractions.dat','r')
    for eachLine in fractFile:
        top, bottom = eachLine.split('/')
        fractList +=  fract
    f0 = Fraction(2)
    f1 = Fraction(1, 3)
    f2 = MixedFraction(12, 3)
    print(f0, '+', f1, '+', f2, '=', f0 + f1 + f2)
    f3 = f1 ** 3
    print('({})**3 = {}'.format(f1, f3))
    print('({})**3 = {}'.format(f2, f2**3))


if __name__ == '__main__':
    main()
