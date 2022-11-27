#!/usr/bin/env python3

"""
Load again the municipal information DataFrame. The rows
of the DataFrame correspond to various geographical areas
of Finland. The first row is about Finland as a whole, then
rows from Akaa to Äänekoski are municipalities of Finland in
alphabetical order. After that some larger regions are listed.

Write function municipalities_of_finland() that returns a
DataFrame containing only rows about municipalities. Give an
appropriate argument for pd.read_csv so that it interprets the
column about region name as the (row) index. This way you can
index the DataFrame with the names of the regions.
"""

import pandas as pd

def municipalities_of_finland():
    data_frame = pd.read_csv("src/municipal.tsv", sep="\t", index_col="Region 2018")
    municipalities = data_frame["Akaa":"Äänekoski"]

    return municipalities
    
def main():
    municipalities = municipalities_of_finland()
    print(municipalities)
    
if __name__ == "__main__":
    main()
