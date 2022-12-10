#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LinearRegression

"""
Read the tab separated file mystery_data.tsv.

Its first five columns define the features, and the last column
is the response. Use scikit-learn's LinearRegression to fit this
data.

Implement function mystery_data() that reads this file and learns
and returns the regression coefficients for the five features. You
don't have to fit the intercept. The main method should print output
in the following form:

Coefficient of X1 is ...
Coefficient of X2 is ...
Coefficient of X3 is ...
Coefficient of X4 is ...
Coefficient of X5 is ...

Which features you think are needed to explain the response Y?
"""

def mystery_data():
    data_frame = pd.read_csv("src/mystery_data.tsv", sep="\t")
    model = LinearRegression(fit_intercept = False)

    model.fit(data_frame.iloc[:,0:5], data_frame.iloc[:,5])
    coefficients = model.coef_

    return coefficients

def main():
    coefficients = mystery_data()

    # print the coefficients here
    print()
    for i, coefficient in enumerate(coefficients):
        print(f"Coefficient of X{i+1} is {coefficient}")
    print()
    
if __name__ == "__main__":
    main()
