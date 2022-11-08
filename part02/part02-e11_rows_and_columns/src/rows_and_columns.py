#!/usr/bin/env python3
import numpy as np

"""
Write two functions, get_rows and get_columns, that get
a two dimensional array as parameter. They should return
the list of rows and columns of the array, respectively.
The rows and columns should be one dimensional arrays.
You may use the transpose operation, which flips rows to
columns, in your solution.
"""

def get_rows(a):
    rows = []
    i = 0

    while i < len(a):
        rows.append(a[i])
        i += 1

    return rows

def get_columns(a):
    columns = []
    j = 0

    while j < len(a.T):
        columns.append(a.T[j])
        j += 1

    return columns

def main():
    np.random.seed(0)
    a = np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))

if __name__ == "__main__":
    main()
