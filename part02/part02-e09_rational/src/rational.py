#!/usr/bin/env python3

"""
Create a class Rational whose instances are rational
numbers. A new rational number can be created with
the call to the class.

For example, the call r=Rational(1,4) creates a rational
number “one quarter”.

Make the instances support the following operations:
+ - * / < > == with their natural behaviour. Make the
rationals also printable so that from the printout we
can clearly see that they are rational numbers.
"""

class Rational(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}/{self.y}"

    def __add__(number1, number2):
        return Rational(number1.x * number2.y + number2.x*number1.y, number1.y*number2.y)

    def __sub__(number1, number2):
        return Rational(number1.x * number2.y - number2.x*number1.y, number1.y*number2.y)

    def __mul__(number1, number2):
        return Rational(number1.x*number2.x, number1.y*number2.y)

    def __truediv__(number1, number2):
        return Rational(number1.x*number2.y, number1.y*number2.x)

    def __lt__(number1, number2):
        return number1.x*number2.y < number2.x*number1.y

    def __gt__(number1, number2):
        return number1.x*number2.y > number2.x*number1.y

    def __eq__(number1, number2):
        return number1.x == number2.x and number1.y == number2.y

def main():
    r1 = Rational(1,4)
    r2 = Rational(2,3)

    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
