#!/usr/bin/env python3

import pandas as pd

"""
Make function powers_of_series that takes a Series
and a positive integer k as parameters and returns
a DataFrame.

The resulting DataFrame should have the same index
as the input Series. The first column of the dataFrame
should be the input Series, the second column should
contain the Series raised to power of two. The third
column should contain the Series raised to the power
of three, and so on until (and including) power of k.
The columns should have indices from 1 to k.
"""

def powers_of_series(s, k):
    powers_dataframe = pd.DataFrame()

    for i in range(1, k+1):
        powers_dataframe[i] = s**i

    return powers_dataframe
    
def main():
    series = pd.Series([1,2,3,4], index=list("abcd"))
    print(powers_of_series(series, 4))
    
if __name__ == "__main__":
    main()
