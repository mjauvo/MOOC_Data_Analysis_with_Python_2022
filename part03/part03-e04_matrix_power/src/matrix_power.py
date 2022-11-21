#!/usr/bin/env python3

import numpy as np
from functools import reduce

# Gets a square matrix 'a' as first argument and a non-negative
# integer 'n' as second argument, and returns a matrix multiplied
# by itself n-1 times. For negative powers, a^(-1) is defined to
# be equal to the multiplicative inverse of a.
def matrix_power(a, n):
    if n < 0:
        a = np.linalg.inv(a)
        n = n * (-1)
    elif n == 0:
        return np.eye(len(a), dtype=int)

    l = [a for i in range(n)]
    result_matrix = reduce(lambda a, b: a@b, l)

    return result_matrix

def main():
    dim = 4
    power = 2

    square_matrix = np.random.randint(10, size=(dim, dim))

    result_matrix = matrix_power(square_matrix, power)
    print(result_matrix)

if __name__ == "__main__":
    main()
