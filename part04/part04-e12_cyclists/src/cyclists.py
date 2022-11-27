#!/usr/bin/env python3

import pandas as pd

"""
Write function cyclists() that does the following.

Load the Helsinki bicycle data set from the 'src' folder.
The dataset contains the number of cyclists passing by
measuring points per hour. The data is gathered over about
four years, and there are 20 measuring points around Helsinki.
The dataset contains some empty rows at the end. Get rid of
these. Also, get rid of columns that contain only missing
values. Return the cleaned dataset.
"""

def cyclists():
    data_frame = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    cleaned_dataset = data_frame.dropna(axis=0, how="all")
    cleaned_dataset = cleaned_dataset.dropna(axis=1, how="all")
    
    return cleaned_dataset

def main():
    print(cyclists())
    
if __name__ == "__main__":
    main()
