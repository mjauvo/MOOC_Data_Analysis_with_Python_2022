#!/usr/bin/env python3

import numpy as np

# Gets a two dimensional array a of shape (n,2*m) as a parameter
# (the input array has 2*m columns) and returns a a matrix with
# those rows from the input that have the sum of the first m
# elements larger than the sum of the last m elements on the row.
def first_half_second_half(a):
    first_half, second_half = np.split(a, 2, axis=1)
    first_half_sum = np.sum(first_half, axis=1)
    second_half_sum = np.sum(second_half, axis=1)

    result = first_half_sum > second_half_sum

    return a[result]

def main():
    rows = 4
    columns = 2*rows
    range = 20

    array_2D = np.random.randint(range, size=(rows,columns))

    print("\n2D array:")
    print(array_2D)
    print("\nResult array:")
    print(first_half_second_half(array_2D))

if __name__ == "__main__":
    main()
