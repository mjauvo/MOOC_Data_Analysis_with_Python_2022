#!/usr/bin/env python3

import pandas as pd

"""
Write function snow_depth() that reads in the weather DataFrame from the
'src' folder and returns the maximum amount of snow in the year 2017.

Print the result in the main() function in the following form:

Max snow depth: xx.x
"""

def snow_depth():
    data_frame = pd.read_csv("src/kumpula-weather-2017.csv")
    snow_depth = data_frame["Snow depth (cm)"]
    max_snow_depth = snow_depth.max()

    return max_snow_depth

def main():
    max_snow_depth = snow_depth()
    print(f"Max snow depth: {max_snow_depth:.1f}")

if __name__ == "__main__":
    main()
