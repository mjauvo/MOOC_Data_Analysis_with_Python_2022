#!/usr/bin/env python3

import pandas as pd
import numpy as np

"""
Write function special_missing_values() that does the following:

Read the data set of the top 40 singles from the beginning of the year 1964
from the src folder. Return the rows whose singles' position dropped compared
to last week's position (column LW=Last Week).

To do this you first have to convert the special values "New" and "Re"
(Re-entry) to missing values (None).
"""

def special_missing_values():
    data_frame = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")

    singles = data_frame.replace(["Re", "New"], np.NaN)
    singles[["Pos", "LW"]] = singles[["Pos", "LW"]].astype("float")
    sunken_positions = singles[singles["Pos"] > singles["LW"]]

    return sunken_positions

def main():
    spec_missing_values = special_missing_values()
    print(spec_missing_values)

if __name__ == "__main__":
    main()
