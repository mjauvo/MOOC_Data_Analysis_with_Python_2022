#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

"""
In function commute() do the following:
- Use the function bicycle_timeseries() to get the bicycle data. Restrict to
  August 2017, group by the weekday, aggregate by summing. Set the Weekday
  column to numbers from one to seven. Then set the column Weekday as the (row)
  index. Return the resulting DataFrame from the function.

In the main() function
- plot the DataFrame. Xticklabels should be the weekdays. Don't forget to call
  show() function!
- If you want the xticklabels to be ['Mon', 'Tue', 'Wed', 'Thu', 'Fr', 'Sat', 'Sun']
  instead of numbers (1,..,7), then it may get a bit messy. There seems to be a
  problem with non-numeric x values. You could try the following after plotting,
  but you don't have to:

  weekdays="x mon tue wed thu fri sat sun".title().split()
  plt.gca().set_xticklabels(weekdays)
"""

def split_date(df):
    timestamps = df["Päivämäärä"].str.split(expand = True)
    timestamps.dropna(how = "all", inplace = True)

    timestamps.columns = ["Weekday", "Day", "Month", "Year", "Hour"]

    # Hours
    timestamps["Hour"] = timestamps["Hour"].str.split(":", expand = True)[0]

    # Weekdays
    timestamps["Weekday"] = timestamps["Weekday"].map({
        "ma" : 1,
        "ti" : 2,
        "ke" : 3,
        "to" : 4,
        "pe" : 5,
        "la" : 6,
        "su" : 7
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
    cycling_data = cycling_data.drop(columns=["Hour", "Day", "Month", "Year"])
    cycling_data = cycling_data.set_index("Päivämäärä")

    return cycling_data

def commute():
    cycling_df = bicycle_timeseries()
    cycling_2017_august = cycling_df["2017-08-01" : "2017-08-31"]
    cycling_2017_august.set_index("Weekday", inplace = True)

    cycling_2017_august_grouped_sum = cycling_2017_august.groupby("Weekday").sum()

    return cycling_2017_august_grouped_sum
    
def main():
    commute_data = commute()
    plt.plot(commute_data)
    weekdays="x mon tue wed thu fri sat sun".title().split()
    plt.gca().set_xticklabels(weekdays)
    plt.title("Commute (2017 August)")
    plt.show()

if __name__ == "__main__":
    main()
