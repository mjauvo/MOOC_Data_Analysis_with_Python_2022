#!/usr/bin/env python3

import pandas as pd

"""
Write function growing_municipalities() that gets subset of
municipalities (a DataFrame) as a parameter and returns the
proportion of municipalities with increasing population in
that subset.

Test your function from the main function using some subset
of the municipalities. Print the proportion as percentages
using 1 decimal precision.

Example output:

Proportion of growing municipalities: 12.4%
"""

def growing_municipalities(df):
    growing_municipalities = df[df["Population change from the previous year, %"] > 0]
    proportion = growing_municipalities.shape[0] / df.shape[0]

    return proportion

def main():
    data_frame = pd.read_csv("src/municipal.tsv", sep="\t", index_col=0)
    municipalities = data_frame["Akaa":"Äänekoski"]
    
    proportion = growing_municipalities(municipalities)
    print(f"Proportion of growing municipalities: {proportion:.1f}%")

if __name__ == "__main__":
    main()
