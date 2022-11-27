#!/usr/bin/env python3

import pandas as pd

"""
In the main function load a data set of municipal information
from the src folder (originally from Statistics Finland). Use
the function pd.read_csv(), and note that the separator is a
tabulator.

Print the shape of the DataFrame (number of rows and columns)
and the column names in the following format:

Shape: r,c
Columns:
col1 
col2
...
"""

def main():
    data_frame = pd.read_csv("src/municipal.tsv", sep="\t")

    rows, columns = data_frame.shape

    print(f"Shape: {rows}, {columns}")
    print("Columns:")
    for i in data_frame:
        print(i)

if __name__ == "__main__":
    main()
