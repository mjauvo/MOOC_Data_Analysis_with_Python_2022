#!/usr/bin/env python3

import pandas as pd

"""
Merge the processed cycling data set (from the previous exercise) and
weather data set along the columns year, month, and day. Note that the
names of these columns might be different in the two tables:
- use the left_on and right_on parameters.
- then drop useless columns 'm', 'd', 'Time', and 'Time zone'.
 
Write function cycling_weather() that reads the data sets and returns
the resulting DataFrame.
"""
 
def split_date(df):
    timestamps = df["Päivämäärä"].str.split(expand = True)
    timestamps.dropna(inplace = True)
 
    timestamps.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
 
    timestamps["Hour"] = timestamps["Hour"].str.split(":", expand = True)[0]
 
    timestamps["Weekday"] = timestamps["Weekday"].map({
        "ma" : "Mon",
        "ti" : "Tue",
        "ke" : "Wed",
        "to" : "Thu",
        "pe" : "Fri",
        "la" : "Sat",
        "su" : "Sun"
    })
 
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
 
def cycling_weather():
    cycling_df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep = ";")
    weather_df = pd.read_csv("src/kumpula-weather-2017.csv", sep = ",")
 
    timestamps = split_date(cycling_df)
 
    cycling_df = pd.concat([timestamps, cycling_df], axis = 1)
    cycling_df.dropna(axis = 0, how = "all", inplace = True)
    cycling_df.dropna(axis = 1, how = "all", inplace = True)
 
    cycling_df.drop("Päivämäärä", axis = 1, inplace = True)
 
    cycling_weather_df = pd.merge(cycling_df, weather_df, left_on = ["Year", "Month", "Day"], right_on = ["Year", "m", "d"])
    cycling_weather_df.drop(columns=["m", "d", "Time", "Time zone"], axis = 1, inplace = True)
 
    return cycling_weather_df
 
def main():
    data_frame = cycling_weather()
    print("Shape:", data_frame.shape)
    print("Column names:\n", data_frame.columns)
    print(data_frame.head())
 
if __name__ == "__main__":
    main()
 