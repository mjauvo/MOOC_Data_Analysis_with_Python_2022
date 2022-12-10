#!/usr/bin/env python3

import pandas as pd

"""
We use again the UK top 40 data set from the first week of 1964 in the 'src'
folder. Here we define "goodness" of a record company (Publisher) based on
the sum of the weeks on chart (WoC) of its singles. Return a DataFrame of the
singles by the best record company (a subset of rows of the original DataFrame).
Do this with function best_record_company().
"""

def best_record_company():
    top_40_df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep = "\t")

    publisher_groups = top_40_df.groupby("Publisher")
    publisher_woc = publisher_groups.sum()["WoC"]
    publisher_woc_sorted_desc = publisher_woc.sort_values(ascending = False)
    publisher_best = publisher_woc_sorted_desc.index[0]

    singles_by_the_best = top_40_df[top_40_df["Publisher"] == publisher_best]

    return singles_by_the_best

def main():
    best_record_company_data = best_record_company()
    print(best_record_company_data)
    

if __name__ == "__main__":
    main()
