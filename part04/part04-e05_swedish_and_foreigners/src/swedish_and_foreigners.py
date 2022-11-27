#!/usr/bin/env python3

import pandas as pd

"""
Write function swedish_and_foreigners() that

- Reads the municipalities data set
- Takes the subset about municipalities (like in previous exercise)
- Further take a subset of rows that have proportion of Swedish speaking
  people and proportion of foreigners both above 5 % level
- From this data set take only columns about population, the proportions
  of Swedish speaking people and foreigners, that is three columns.

The function should return this final DataFrame.

Do you see some kind of correlation between the columns about Swedish
speaking and foreign people? Do you see correlation between the columns
about the population and the proportion of Swedish speaking people in
this subset?
"""

def swedish_and_foreigners():
    data_frame = pd.read_csv("src/municipal.tsv", sep="\t", index_col=0)
    municipalities = data_frame["Akaa":"Äänekoski"]

    municipalities_subset = municipalities[(municipalities["Share of Swedish-speakers of the population, %"] > 5) & (municipalities["Share of foreign citizens of the population, %"] > 5)]
    municipalities_subset = municipalities_subset[["Population", "Share of Swedish-speakers of the population, %", "Share of foreign citizens of the population, %"]]

    return municipalities_subset

def main():
    SE_and_XX = swedish_and_foreigners()
    print(SE_and_XX)

if __name__ == "__main__":
    main()
