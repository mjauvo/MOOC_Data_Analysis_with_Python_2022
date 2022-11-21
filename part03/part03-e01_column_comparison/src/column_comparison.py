#!/usr/bin/env python3

import numpy as np

# Gets a two dimensional array a as parameter and returns
# a new array containing those rows from the input that
# have the value in the second column larger than in the
# second last column. 
def column_comparison(a):
    result = a[:,1] > a[:,-2]
    return a[result]
    
def main():
    """
    array_2D = np.array([[8, 9, 3, 8, 8],
                         [0, 5, 3, 9, 9],
                         [5, 7, 6, 0, 4],
                         [7, 8, 1, 6, 2],
                         [2, 1, 3, 5, 8]])
    """

    rows = 6
    columns = 6
    range = 12

    array_2D = np.random.randint(range, size=(rows, columns))
    print(column_comparison(array_2D))

if __name__ == "__main__":
    main()
