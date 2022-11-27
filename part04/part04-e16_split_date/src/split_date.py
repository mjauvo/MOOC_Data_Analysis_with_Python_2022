#!/usr/bin/env python3

import pandas as pd
import numpy as np

"""
Read again the bicycle data set from src folder, and clean it as in the earlier exercise.
Then split the Päivämäärä column into a DataFrame with five columns with column names
Weekday, Day, Month, Year, and Hour. Note that you also need to to do some conversions.

To get Hours, drop the colon and minutes.

Convert field Weekday according the following rule:

ma -> Mon
ti -> Tue
ke -> Wed
to -> Thu
pe -> Fri
la -> Sat
su -> Sun

Convert the Month column according to the following mapping

tammi -> 1
helmi -> 2
maalis -> 3
huhti -> 4
touko -> 5
kesä -> 6
heinä -> 7
elo -> 8
syys -> 9
loka -> 10
marras -> 11
joulu -> 12

Create function split_date() that does the above and returns a DataFrame with five
columns. You may want to use the map method of Series objects.

So the first element in the 'Päivämäärä' column of the original data set should be
converted from "ke 1 tammi 2014 00:00" to "Wed 1 1 2014 0" . Test your solution from
the main function.
"""

def split_date():
    data_frame = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep = ";")

    timestamps = data_frame["Päivämäärä"].str.split(expand = True)
    timestamps.dropna(how = "all", inplace = True)

    timestamps.columns = ["Weekday", "Day", "Month", "Year", "Hour"]

    # Hours
    timestamps["Hour"] = timestamps["Hour"].str.split(":", expand = True)[0]

    # Weekdays
    timestamps["Weekday"] = timestamps["Weekday"].map({
        "ma" : "Mon",
        "ti" : "Tue",
        "ke" : "Wed",
        "to" : "Thu",
        "pe" : "Fri",
        "la" : "Sat",
        "su" : "Sun"
    })

    # Months
    timestamps["Month"] = timestamps["Month"].map({
        "tammi" : 1,
        "helmi" : 2,
        "maalis": 3,
        "huhti" : 4,
        "touko" : 5,
        "kesä"  : 6,
        "heinä" : 7,
        "elo"   : 8,
        "syys"  : 9,
        "loka"  : 10,
        "marras": 11,
        "joulu" : 12
    })

    timestamps = timestamps.astype({
        "Weekday" : object,
        "Day"     : int,
        "Month"   : int,
        "Year"    : int,
        "Hour"    : int
    })    

    return timestamps

def main():
    print(split_date())
       
if __name__ == "__main__":
    main()
