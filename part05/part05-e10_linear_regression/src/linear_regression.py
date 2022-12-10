#!/usr/bin/env python3

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

"""
Write a function fit_line() that gets one dimensional arrays x and y as parameters.
The function should return the tuple (slope, intercept) of the fitted line. Write
a main program that tests the fit_line function with some example arrays. The main
function should produce output in the following form:

Slope: 1.0
Intercept: 1.16666666667

Modify your main function to plot the fitted line using matplotlib, in addition to
the textual output. Plot also the original data points.
"""

def fit_line(x, y):
    model = LinearRegression(fit_intercept=True)
    model.fit(x[:,np.newaxis], y)

    slope = model.coef_[0]
    intercept = model.intercept_

    return (slope, intercept) 
    
def main():
    n = 20
    x = np.linspace(0, 10, n)
    y = x*2 + 1 + 1*np.random.randn(n)

    slope, intercept = fit_line(x, y)

    print(f"Slope: {slope}")
    print(f"Intercept: {intercept}")

    plt.plot(x, y, 'o')

    xfit = np.linspace(0, 10, 50)
    yfit = xfit*slope + intercept
    plt.plot(xfit, yfit, color="red")
    plt.show()
    
if __name__ == "__main__":
    main()
