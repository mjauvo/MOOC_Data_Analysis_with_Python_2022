#!/usr/bin/env python3

import pandas as pd

"""
Write function below_zero() that returns the number of days
when the temperature was below zero.

Print the result in the main function in the following form:

Number of days below zero: xx
"""

def below_zero():
    data_frame = pd.read_csv("src/kumpula-weather-2017.csv")
    data_below_zero = (data_frame["Air temperature (degC)"] < 0)
    days_below_zero = sum(data_below_zero)

    return days_below_zero

def main():
    days_below_zero = below_zero()
    print(f"Number of days below zero: {days_below_zero}")
    
if __name__ == "__main__":
    main()
