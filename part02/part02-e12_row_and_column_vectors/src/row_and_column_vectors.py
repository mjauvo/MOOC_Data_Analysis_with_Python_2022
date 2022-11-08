#!/usr/bin/env python3

import numpy as np

"""
Create function get_row_vectors that returns a list
of rows from the input array of shape (n,m), but this
time the rows must have shape (1,m). Similarly, create
function get_columns_vectors that returns a list of columns
(each having shape (n,1)) of the input matrix .
"""

def get_row_vectors(a):
    row_vectors = []

    for vector in a:
        reshaped = vector.reshape(1, -1)
        row_vectors.append(reshaped)

    return row_vectors

def get_column_vectors(a):
    column_vectors = []

    for vector in a.T:
        reshaped = vector.reshape(-1, 1)
        column_vectors.append(reshaped)

    return column_vectors

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Row vectors:", get_row_vectors(a))
    print("Column vectors:", get_column_vectors(a))

if __name__ == "__main__":
    main()
