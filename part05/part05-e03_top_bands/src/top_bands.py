#!/usr/bin/env python3

import pandas as pd

"""
Merge the DataFrames UK top40 and the bands DataFrame that are stored in
the src folder. Do all this in the parameterless function top_bands(),
which should return the merged DataFrame. Use the left_on and right_on
parameters to merge. Test your function from the main() function.
"""

def top_bands():
    top_40_df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep = "\t")
    bands_df = pd.read_csv("src/bands.tsv", sep = "\t")

    bands_df["Band"] = bands_df["Band"].str.upper()

    top_40_bands_df = pd.merge(top_40_df, bands_df, left_on = "Artist", right_on = "Band")

    return top_40_bands_df

def main():
    data_frame = top_bands()
    print("Shape:", data_frame.shape)
    print("Column names:\n", data_frame.columns)
    print(data_frame.head())

if __name__ == "__main__":
    main()
