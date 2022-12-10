#!/usr/bin/env python3

import pandas as pd

"""
Write function split_date_continues() that
- reads the bicycle data set
- cleans the data set of columns/rows that contain only
  missing values
- drops the 'Päivämäärä' column and replaces it with its
  splitted components as before

Use the concat() function to do this. The function should
return a DataFrame with 25 columns (first five related to
the date and then the rest 20 conserning the measument location.
"""

def split_date(df):
    timestamps = df["Päivämäärä"].str.split(expand = True)
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

def split_date_continues():
    data_frame = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep = ";")
    timestamps = split_date(data_frame)

    data_frame.drop("Päivämäärä", axis = 1, inplace = True)
    data_frame.dropna(axis = 0, how = "all", inplace = True)
    data_frame.dropna(axis = 1, how = "all", inplace = True)
    
    new_timestamps = pd.concat([timestamps, data_frame], axis = 1)

    return new_timestamps

def main():
    df = split_date_continues()
    print("Shape:", df.shape)
    print("Column names:\n", df.columns)
    print(df.head())


if __name__ == "__main__":
    main()
