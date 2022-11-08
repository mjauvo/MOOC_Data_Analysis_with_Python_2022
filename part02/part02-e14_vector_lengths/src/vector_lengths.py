#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

# Gets a two dimensional array of shape (n,m) as a parameter.
# Each row in this array corresponds to a vector. Returns an
# array of shape (n,), that has the length of each vector in
# the input. The length is defined by the usual Euclidean
# norm.
def vector_lengths(a):
    a_squared = np.square(a)
    a_summed = np.sum(a_squared, axis=1)
    vector_lengths = np.sqrt(a_summed)

    return vector_lengths

def main():
    rand_array = np.random.randint(12, size=(3,7))
    print(vector_lengths(rand_array))

if __name__ == "__main__":
    main()
