#!/usr/bin/env python3

import pandas as pd
import numpy as np

"""
Write function last_week() that reads the Top 40 data set mentioned in the previous
exercise. The function should then try to reconstruct the Top 40 list of the previous
week based on that week's list. Try to do this as well as possible. You can fill the
values that are impossible to reconstruct by missing value symbols. Your solution
should work for a Top 40 list of any week. So don't rely on specific features of this
Top 40 list. The column 'WoC' means "Weeks on Chart", that is, on how many weeks this
song has been on the Top 40 list.
"""

def last_week():
    last_week_df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")

    last_week_df.replace(["New", "Re"], np.nan, inplace=True)
    last_week_df = last_week_df.astype({"LW": "float"})
    last_week_df["Peak Pos"].where(lambda x: (last_week_df["Peak Pos"] != last_week_df["Pos"]) | (last_week_df["Peak Pos"] == last_week_df["LW"]), np.nan, inplace=True)
    last_week_df["WoC"] -= 1
    last_week_df["Pos"] = last_week_df["LW"]
    last_week_df = last_week_df[last_week_df["Pos"].notna()]
    last_week_df["LW"] = np.nan
    last_week_df["Pos"] = last_week_df["Pos"].astype("int64")

    for i in range(1, 41):
        if i not in last_week_df["Pos"].values:
            last_week_df = last_week_df.append([{"Pos":i}])

    last_week_df.sort_values(by = "Pos", inplace = True)
    last_week_df.reset_index(drop = True, inplace = True)

    return last_week_df

def main():
    data_frame = last_week()
    print("Shape: {}, {}".format(*data_frame.shape))
    print("dtypes:", data_frame.dtypes)
    print(data_frame)

if __name__ == "__main__":
    main()
