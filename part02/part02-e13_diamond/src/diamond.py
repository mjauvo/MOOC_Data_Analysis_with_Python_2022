#!/usr/bin/env python3

import numpy as np

# Returns a two dimensional integer array where the 1s form
# a diamond shape. Rest of the numbers are 0. The function
# gets a parameter n that tells the length of a side of the
# diamond.
def diamond(n):
    eye = np.eye(n, dtype = int)

    left_up = np.fliplr(eye)
    left_down = eye[1:n,:]

    left_side = np.concatenate((left_up, left_down), axis=0)
    right_side = np.fliplr(left_side)[:,1:n]

    diamond = np.concatenate((left_side, right_side), axis=1)

    return diamond

def main():
    side_length = 4
    print(diamond(side_length))

if __name__ == "__main__":
    main()
