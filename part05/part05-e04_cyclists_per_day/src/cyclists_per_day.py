#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
Read, clean and parse the bicycle data set as before. Group the rows by year,
month, and day. Get the sum for each group. Make function cyclists_per_day()
that does the above. The function should return a DataFrame. Make sure that
the columns Hour and Weekday are not included in the returned DataFrame.

In the main() function, using the function cyclists_per_day(), get the daily
counts. The index of the DataFrame now consists of tuples (Year, Month, Day).
Then restrict this data to August of year 2017, and plot this data. Don't
forget to call the plt.show() function of matplotlib. The x-axis should have
ticks from 1 to 31, and there should be a curve to each measuring station.

Can you spot the weekends?
"""

def split_date(df):
    data = df["Päivämäärä"].str.split(expand = True)
    data.dropna(inplace = True)

    data.columns = ["Weekday", "Day", "Month", "Year", "Hour"]

    # Hours
    data["Hour"] = data["Hour"].str.split(":", expand = True)[0]

    # Weekdays
    data["Weekday"] = data["Weekday"].map({
        "ma" : "Mon",
        "ti" : "Tue",
        "ke" : "Wed",
        "to" : "Thu",
        "pe" : "Fri",
        "la" : "Sat",
        "su" : "Sun"
    })

    # Months
    data["Month"] = data["Month"].map({
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

    data = data.astype({
        "Weekday" : object,
        "Day"     : int,
        "Month"   : int,
        "Year"    : int,
        "Hour"    : int
    })    

    return data

def cyclists_per_day():
    cycling_df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep = ";")
    cycling_df = cycling_df.dropna(axis=0, how="all")
    cycling_df = cycling_df.dropna(axis=1, how="all")

    cycling_dates = split_date(cycling_df)

    cycling_df = cycling_df.drop("Päivämäärä", axis=1)

    cycling = pd.concat([cycling_dates, cycling_df], axis=1)
    cycling = cycling.drop(["Hour", "Weekday"], axis=1)
    grouped_cycling = cycling.groupby(["Year", "Month", "Day"])

    return grouped_cycling.sum()
    
def main():
    data = cyclists_per_day()
    data_2017_august = data.loc[(2017, 8)]

    '''
    Graph demonstrates valleys, i.e. reduced cycling during weekends
    '''
    plt.plot(data_2017_august)
    plt.xticks(np.arange(0, 32, 1))
    plt.title('Cyclists per day (August 2017)')
    plt.xlabel('Day')
    plt.ylabel('Cyclists')
    plt.show()

if __name__ == "__main__":
    main()
