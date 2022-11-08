#!/usr/bin/env python3

import numpy as np
# import scipy.linalg

# Gets two arrays X and Y with same shape (n,m) as parameters.
# Each row in the arrays corresponds to a vector. Returns a
# vector of shape (n,) with the corresponding angles between
# vectors of X and Y in degrees.
def vector_angles(X, Y):
    numerator = np.sum(X*Y, axis=1)
    factor_X = np.sqrt(np.sum(X**2, axis=1))
    factor_Y = np.sqrt(np.sum(Y**2, axis=1))
    denominator = factor_X * factor_Y
    cosine = numerator/denominator

    prec_cosine = np.clip(cosine, -1.0, 1.0)
    inv_cosine = np.arccos(prec_cosine)
    angles_degrees = np.degrees(inv_cosine)

    return angles_degrees

def main():
    X = np.random.randint(12,24, (4,5))
    Y = np.random.randint(10,30, (4,5))
    print(vector_angles(X, Y))

if __name__ == "__main__":
    main()
