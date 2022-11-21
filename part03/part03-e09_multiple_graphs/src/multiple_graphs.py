#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

"""
Make your main function plot the following two graphs in
one axes. The first graphs has x coordinates 2,4,6,7 and
y coordinates 4,3,5,1. The second graph has x coordinates
1,2,3,4 and y coordinates 4,2,3,1.

Add also a title and some labels for x axis and y axis.
Note that in the non-interactive mode you have to call
plt.show() for the figure to show.
"""

def main():
    # Graph 1
    x1 = np.array([2,4,6,7])
    y1 = np.array([4,3,5,1])

    # Graph 2
    x2 = np.array([1,2,3,4])
    y2 = np.array([4,2,3,1])

    plt.plot(x1, y1)
    plt.plot(x2, y2)
    plt.title("Exercise 3.9: Multiple graphs") # Add a title to the figure
    plt.xlabel("X")                          # Give a label to the x-axis
    plt.ylabel("Y")                          # Give a label to the y-axis
    plt.show()                               # Tell matplotlib to output the figure.


if __name__ == "__main__":
    main()
