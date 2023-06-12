#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA

"""
# Part 1.

Write function explained_variance() which reads the tab separated file "data.tsv".
The data contains 10 features. Then fit PCA to the data. The function should return
two lists (or 1D arrays). The first list should contain the variances of all the
features. The second list should consist of the explained variances returned by the
PCA.

In the main function print these values in the following form:

    The variances are: ?.??? ?.??? ...
    The explained variances after PCA are: ?.??? ?.??? ...

Print the values with three decimal precision and separate the values by a space.

# Part 2.

Plot the cumulative explained variances. The y-axis should be the cumulative sum,
and the x-axis the number of terms in the cumulative sum.
"""

def explained_variance():
    data_frame = pd.read_csv('src/data.tsv', sep='\t')

    pca = PCA()
    pca.fit(data_frame)

    variances = data_frame.var(axis=0)
    explained_variances = pca.explained_variance_

    return variances, explained_variances
    
def main():
    v, ev = explained_variance()
    print(sum(v), sum(ev))

    v_as_string = " ".join([f"{x:.3f}" for x in v])
    ev_as_string = " ".join([f"{x:.3f}" for x in ev])

    print(f"The variances are: {v_as_string}")
    print(f"The explained variances after PCA are: {ev_as_string}")

    plt.plot(range(1, len(ev)+1), np.cumsum(ev))

    plt.xlabel("Number of terms in cumulative sum")
    plt.xticks([1, 2, 3])
    plt.ylabel("Cumulative sum")

    plt.show()

if __name__ == "__main__":
    main()
