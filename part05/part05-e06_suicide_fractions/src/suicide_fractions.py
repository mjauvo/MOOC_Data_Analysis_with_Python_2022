#!/usr/bin/env python3

import pandas as pd

"""
Load the suicide data set from src folder. This data was originally downloaded
from Kaggle. Kaggle contains lots of interesting open data sets.

Write function suicide_fractions() that loads the data set and returns a Series
that has the country as the (row) index and as the column the mean fraction of
suicides per population in that country. In other words, the value is the average
of suicide fractions. The information about year, sex and age is not used.
"""

def suicide_fractions():
    suicide_df = pd.read_csv("src/who_suicide_statistics.csv", sep=",")
    suicide_df.drop(columns = ["year", "sex", "age"])
    suicide_df["fraction"] = suicide_df["suicides_no"] / suicide_df["population"]

    suicide_grouped_avg = suicide_df.groupby("country").mean()

    return suicide_grouped_avg["fraction"]

def main():
    suicides_fractions = suicide_fractions()
    print(suicides_fractions)

if __name__ == "__main__":
    main()
