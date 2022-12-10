#!/usr/bin/env python3

import pandas as pd

"""
Copy the function suicide_fractions() from the previous exercise. 

Implement function suicide_weather as described below. We use the dataset
of average temperature (over years 1961-1990) in different countries from
src/List_of_countries_by_average_yearly_temperature.html
(https://en.wikipedia.org/wiki/List_of_countries_by_average_yearly_temperature).
You can use the function pd.read_html() to get all the tables from a html page.
By default pd.read_html() does not know which row contains column headers and
which column contains row headers. Therefore, you have to give both index_col
and header parameters to read_html. Maku sure you use the country as the (row)
index for both of the DataFrames. What is the Spearman correlation between these
variables? Use the corr() method of Series object. Note the the two Series need
not be sorted as the indices of the rows (country names) are used to align them.

The return value of the function suicide_weather() is a tuple (suicide_rows,
temperature_rows, common_rows, spearman_correlation) The output from the main
function should be of the following form:

Suicide DataFrame has x rows
Temperature DataFrame has x rows
Common DataFrame has x rows
Spearman correlation: x.x
"""

def suicide_fractions():
    suicide_df = pd.read_csv("src/who_suicide_statistics.csv", sep=",")
    suicide_df.drop(columns = ["year", "sex", "age"])
    suicide_df["fraction"] = suicide_df["suicides_no"] / suicide_df["population"]

    suicide_grouped_avg = suicide_df.groupby("country").mean()

    return suicide_grouped_avg["fraction"]

def suicide_weather():
    temperature_data = pd.read_html("src/List_of_countries_by_average_yearly_temperature.html", index_col = "Country")[0]
    temperature_data.rename(columns={"Average yearly temperature (1961–1990, degrees Celsius)": "temp_avg"}, inplace = True)
    temperature_data["temp_avg"] = temperature_data["temp_avg"].str.replace("\u2212", "-").astype("float")

    suicide_fractions_data = suicide_fractions()
    suicide_weather_common = pd.merge(temperature_data, suicide_fractions_data, left_index = True, right_index = True)
    suicide_weather_correlation = suicide_weather_common["fraction"].corr(suicide_weather_common["temp_avg"], method = "spearman")

    return (len(suicide_fractions_data), len(temperature_data), len(suicide_weather_common), suicide_weather_correlation)

def main():
    suicide_rows, temperature_rows, common_rows, spearman_correlation = suicide_weather()

    print(f"Suicide DataFrame has {suicide_rows} rows")
    print(f"Temperature DataFrame has {temperature_rows} rows")
    print(f"Common DataFrame has {common_rows} rows")
    print(f"Spearman correlation: {spearman_correlation}")

if __name__ == "__main__":
    main()
