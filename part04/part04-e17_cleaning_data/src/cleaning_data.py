#!/usr/bin/env python3

import pandas as pd
import numpy as np

"""
The entries in the following table of US presidents are not uniformly formatted. Make
function cleaning_data() that reads the table from the tsv file 'src/presidents.tsv'
and returns the cleaned version of it. Note, you must do the edits programmatically
using the string edit methods, not by creating a new DataFrame by hand. The columns
should have dtypes object, integer, float, integer, object.
"""

# Clean columns: President + Vice President
def clean_column_name(name_string):
    if ', ' in name_string:
        last, first = name_string.split(", ")
        cleaned_name = f"{first} {last}".title()
        return cleaned_name
    return name_string.title()

# Clean column: Start
def clean_column_start(col_start):
    col_start = col_start.str.extract('(\d+)', expand=False)
    return col_start

# Clean column: Last
def clean_column_last(col_last):
    col_last = col_last.replace('-', np.nan)
    return col_last

# Clean column: Seasons
def clean_column_seasons(col_seasons):
    col_seasons = col_seasons.replace(["one", "two"], [1, 2])
    return col_seasons

def cleaning_data():
    data_frame = pd.read_csv("src/presidents.tsv", sep="\t")

    # Column 1: President
    data_frame['President'] = data_frame['President'].apply(clean_column_name)
    data_frame['President'] = data_frame['President'].astype(object)

    # Column 2: Start
    data_frame['Start'] = clean_column_start(data_frame['Start'])
    data_frame['Start'] = data_frame['Start'].astype(int)

    # Column 3: Last
    data_frame['Last'] = clean_column_last(data_frame['Last'])
    data_frame['Last'] = data_frame['Last'].astype(float)

    # Column 4: Seasons
    data_frame['Seasons'] = clean_column_seasons(data_frame['Seasons'])
    data_frame['Seasons'] = data_frame['Seasons'].astype(int)

    # Column 5: Vice-President
    data_frame['Vice-president'] = data_frame['Vice-president'].apply(clean_column_name)
    data_frame['Vice-president'] = data_frame['Vice-president'].astype(object)

    return data_frame

def main():
    cleaned_data = cleaning_data()
    print(cleaned_data)

if __name__ == "__main__":
    main()
