#!/usr/bin/env python3

import pandas as pd

"""
Write function subsetting_with_loc() that in one go takes
the subset of municipalities from Akaa to Äänekoski and
restricts it to columns:

- "Population"
- "Share of Swedish-speakers of the population, %"
- "Share of foreign citizens of the population, %".

The function should return this content as a DataFrame.
Use the attribute loc.
"""

def subsetting_with_loc():
    data_frame = pd.read_csv("src/municipal.tsv", sep="\t", index_col=0)
    municipalities_subset = data_frame.loc["Akaa":"Äänekoski", ["Population", "Share of Swedish-speakers of the population, %", "Share of foreign citizens of the population, %"]]

    return municipalities_subset

def main():
    subset = subsetting_with_loc()
    print(subset)

if __name__ == "__main__":
    main()
