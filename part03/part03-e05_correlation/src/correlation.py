#!/usr/bin/env python3

import scipy.stats as sc
import numpy as np

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

# Loads the data and computes the Pearson correlation between
# the variables 'sepal length' and 'petal length', and returns
# a tuple whose first element is the correlation. 
def lengths():
    data = load()
    sepal_length  = data[:,0]
    petal_length  = data[:,2]

    pearson_corr, _ = sc.pearsonr(sepal_length, petal_length)
    return pearson_corr

# Loads the data and computes the correlations between all the
# variables, and returns an array of shape (4,4) containing the
# correlations.
def correlations():
    data = load()

    corrs = np.corrcoef(data, rowvar=False)
    return corrs

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
