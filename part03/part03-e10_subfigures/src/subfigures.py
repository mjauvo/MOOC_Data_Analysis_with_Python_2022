#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

# Creates a figure that has two subfigures (two axes in
# matplotlib parlance). Gets a 2-dimensional array 'a'
# as a parameter.
# 
# In the left subfigure draws, using the plot() method,
# a graph whose x coordinates are in the first column of
# a and the y coordinates are in the second column of 'a'.
# 
# In the right subfigure draws, using the scatter() method,
# a set of points whose x coords are again in the first
# column of 'a' and whose y coordinates are in the second
# column of 'a'. Additionally, the points should get their
# color from the third column of a, and size of the point
# from the fourth column of a. For this, use the 'c' and
# 's' named parameters of scatter, respectively.
def subfigures(a):
    column_1 = a[:,0]
    column_2 = a[:,1]
    column_3 = a[:,2]
    column_4 = a[:,3]

    # Subfigure 1 (left)
    plt.subplot(1,2,1) 
    plt.plot(column_1, column_2)

    # Subfigure 2 (right)
    plt.subplot(1,2,2)
    plt.scatter(column_1, column_2, c = column_3, s = column_4)

    plt.show()

def main():
    array_2D = np.vstack(([1, 3, 1.0, 100],
                          [3, 1, 3.0, 300],
                          [2, 9, -3.0, 200],
                          [4, 6, -1.0, 400]))

    subfigures(array_2D)

if __name__ == "__main__":
    main()
