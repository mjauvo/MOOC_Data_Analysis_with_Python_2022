#!/usr/bin/env python3

import pandas as pd

"""
Write function average_temperature() that reads the weather data
set and returns the average temperature in July.

Print the result in the main function in the following form:

Average temperature in July: xx.x
"""

def average_temperature():
    JULY = 7
    data_frame = pd.read_csv("src/kumpula-weather-2017.csv")
    data_july = data_frame[data_frame["m"] == JULY]
    temperature_july = data_july["Air temperature (degC)"]
    average_temperature_july = temperature_july.mean()

    return average_temperature_july

def main():
    average_temperature_july = average_temperature()
    print(f"Average temperature in July: {average_temperature_july:.1f}")

if __name__ == "__main__":
    main()
