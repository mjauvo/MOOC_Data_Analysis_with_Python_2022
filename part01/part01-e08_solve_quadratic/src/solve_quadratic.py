#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    "This function returns both solutions of a generic quadratic as a pair."
    radicand = b**2 - (4*a*c)
    divisor = 2*a

    if radicand < 0:
        print("Can't take the square root of a negative number! ", radicand)
        return None
    else:
        dividend1 = (-1)*b + math.sqrt(radicand)
        dividend2 = (-1)*b - math.sqrt(radicand)

        x1 = dividend1 / divisor
        x2 = dividend2 / divisor

    return (x1, x2)

def main():
    print(solve_quadratic(1, -3, 2))

if __name__ == "__main__":
    main()
