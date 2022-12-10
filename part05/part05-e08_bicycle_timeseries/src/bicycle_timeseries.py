#!/usr/bin/env python3

import pandas as pd

"""
Write function bicycle_timeseries() that
- reads the data set
- cleans it
- turns its 'Päivämäärä' column into (row) DatetimeIndex
  (that is, to row names) of that DataFrame
- returns the new DataFrame
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

def bicycle_timeseries():
    cycling_data = split_date_continues()
    cycling_data["Päivämäärä"] = pd.to_datetime(cycling_data[["Year", "Month", "Day", "Hour"]])
    cycling_data = cycling_data.drop(columns=["Hour", "Weekday", "Day", "Month", "Year"])
    cycling_data = cycling_data.set_index("Päivämäärä")

    return cycling_data

def main():
    bicycle_ts = bicycle_timeseries()
    print(bicycle_ts)

if __name__ == "__main__":
    main()
