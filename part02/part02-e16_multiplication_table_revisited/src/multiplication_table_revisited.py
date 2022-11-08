#!/usr/bin/env python3

import numpy as np

# Gets a positive integer n as parameter. Returns an array
# with shape (n,n). The element at index (i,j) is i*j.
def multiplication_table(n):
    A = np.arange(n)
    B = A.reshape(n,1)
    multiplication_table = A * B

    return multiplication_table

def main():
    dim = 4
    print(multiplication_table(dim))

if __name__ == "__main__":
    main()
