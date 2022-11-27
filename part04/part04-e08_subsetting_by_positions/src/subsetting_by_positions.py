#!/usr/bin/env python3

import pandas as pd

"""
Write function subsetting_by_positions that does the following:

Read the data set of the top forty singles from the beginning of the year 1964
from the src folder. Return the top 10 entries and only the columns Title and
Artist. Get these elements by their positions, that is, by using a single call
to the iloc attribute. The function should return these as a DataFrame.
"""

def subsetting_by_positions():
    data_frame = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t", index_col=0)
    top_10 = data_frame.iloc[:10, [1, 2]]

    return top_10

def main():
    subset = subsetting_by_positions()
    print(subset)

if __name__ == "__main__":
    main()
